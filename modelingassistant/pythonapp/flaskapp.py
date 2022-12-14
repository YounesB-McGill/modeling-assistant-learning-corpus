#!/usr/bin/env python3

"""
REST API for modeling assistant.
"""

# pylint: disable=invalid-name

import json

from feedback import give_feedback_for_student_cdm
from flask import abort, Flask, Response, jsonify, request
from flask_cors import CORS
from modelingassistant_app import MODELING_ASSISTANT, SRSET
from stringserdes import str_to_modelingassistant


DEBUG_MODE = True
PORT = 8080

app = Flask(__name__)
CORS(app)  # TODO Make this more secure later


@app.route("/")
def root():
    "Root endpoint."
    return abort(403)  # return 403 Forbidden for now


@app.route("/helloworld/<name>")
def hello_world(name) -> Response:
    "Simple route used for testing the app."
    return jsonify({"hello": name})


@app.route("/feedback/<userName>", methods=["POST"])
def feedback(userName: str) -> Response:
    """
    Return feedback for the user's class diagram given its name.

    Body: {"classDiagram": <ClassDiagram in XMI format>}
    """
    print("Got POST REST call for feedback on this class diagram")
    cdm_xmi: str = json.loads(request.get_data())["classDiagram"]
    print(f"{'badClsName' in cdm_xmi = }")
    print(f"{'Airplane' in cdm_xmi = }")
    r = jsonify(give_feedback_for_student_cdm(userName, cdm_xmi))
    print(f"/feedback/{userName}: Returning this response: ", r.data.decode("utf-8"))
    return r
    #return jsonify(give_feedback_for_student_cdm(userName, cdm_xmi))


@app.route("/modelingassistant", methods=["GET", "POST"])
def modeling_assistant() -> Response:
    "Get or set the modeling assistant as an XMI string. This endpoint should be considered provisional."
    global MODELING_ASSISTANT  # pylint: disable=global-statement
    print(f"Received a /modelingassistant {request.method} request")
    if request.method == "GET":
        ma_str = SRSET.create_ma_str(MODELING_ASSISTANT.instance)
        r = jsonify({"modelingAssistantXmi": ma_str})
        print("GET /modelingassistant: Returning this response: \n", ma_str)
        return r
        # return jsonify({"modelingAssistantXmi": str_to_modelingassistant(MODELING_ASSISTANT.instance)})
    if request.method == "POST":
        print(f"Old MA id: {id(MODELING_ASSISTANT.instance)}")
        MODELING_ASSISTANT.instance = str_to_modelingassistant(json.loads(request.get_data())["modelingAssistantXmi"])
        print(f"New MA id: {id(MODELING_ASSISTANT.instance)}")
        r = jsonify({"success": True})
        print("/modelingassistant: Returning this response: ", r.data.decode("utf-8"))
        return r
        # return jsonify({"success": True})
    return abort(405)  # invalid method


if __name__ == "__main__":
    app.run(debug=DEBUG_MODE, port=PORT)
