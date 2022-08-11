"""
Learning Corpus definition file. The corpus mistake types and learning items are defined here in a
DSL style, as well as the mistake type priorities.

The actual corpus initialization is done in the corpus.py file.
"""

from textwrap import dedent

from constants import T
from learningcorpus import (Example, LearningCorpus, MistakeType, ParametrizedResponse, Reference, ResourceResponse,
                            TextResponse)
from utils import mcq, mtc, mt, fbs, fitb, HighlightProblem, HighlightSolution


# HTML checked and unchecked boxes, used in generated output
CHECKED_BOX = "&#10003;"
UNCHECKED_BOX = "&#9744;"


corpus = LearningCorpus(mistakeTypeCategories=[
    class_mistakes := mtc(n="Class mistakes",
        mistakeTypes=[
            missing_class := mt(n="Missing class", stud=[], inst="cls", feedbacks=fbs({
                1: HighlightProblem(),  # Highlight entire sentence. Can infer this from level
                2: TextResponse(text="Make sure you have modeled all the classes in the problem description."),
                3: HighlightProblem(),
                4: ParametrizedResponse(text="Remember to add the ${inst_cls} class."),
                5: ResourceResponse(learningResources=[class_ref := Reference(content="Please review the "
                            "[Classes](https://mycourses2.mcgill.ca/) part of the Class Diagram lecture.")]),
            })),
        ],
        subcategories=[
            class_name_mistakes := mtc(n="Class name mistakes", mistakeTypes=[
                plural_class_name := mt(n="Plural class name", atomic=True, stud_inst="cls", feedbacks=fbs({
                    1: HighlightSolution(),
                    2: TextResponse(text="Remember that class names should be singular."),
                    3: ParametrizedResponse(text="${stud_cls} should be ${inst_cls}, using the singular."),
                    # markdown emojis ✔ and ❌, which can be transformed to LaTeX
                    4: ResourceResponse(learningResources=[correct_class_naming_example := Example(content=dedent("""\
                        Please note these examples of correct vs incorrect class naming:
                        :x: Examples to avoid | :heavy_check_mark: Good class names
                        --- | ---
                        pilot | Pilot
                        Airplanes | Airplane 
                        AirlineData | Airline"""))]),
                    5: ResourceResponse(learningResources=[class_ref := Reference(content="Please review the "
                            "[Classes](https://mycourses2.mcgill.ca/) part of the Class Diagram lecture.")]),
                })),
                software_engineering_term := mt(n="Software engineering term", atomic=True, stud_inst="cls",
                    feedbacks=fbs({
                        1: HighlightSolution(),
                        2: TextResponse(
                            text="Remember that a domain model should not contain software engineering terms."),
                        3: ParametrizedResponse(text="${stud_cls} contains a software engineering term (e.g., data, "
                            "database, table, record), which does not belong in a domain model."),
                        4: ResourceResponse(learningResources=[correct_class_naming_example]),
                        5: ResourceResponse(learningResources=[class_ref]),
                    })),
            ]),
        ]
    ),

    attribute_mistakes := mtc(n="Attribute mistakes",
        subcategories=[
            attribute_name_mistakes := mtc(n="Attribute name mistakes", mistakeTypes=[
                bad_attribute_name_spelling := mt(n="Bad attribute name spelling", stud_inst="attr", feedbacks=fbs({
                    1: HighlightSolution(),
                    2: TextResponse(text="Double check this attribute name."),
                    3: ParametrizedResponse(text="The ${stud_attr.cls}.${stud_attr} attribute is misspelled.[ Use the "
                                                 "same spelling as the problem description.]"),
                    4: ResourceResponse(learningResources=[attr_naming_quiz := mcq[
                        "Select all the correct attribute names from the list below.",
                           "needsReciept",
                        T: "numberOfItems",
                           "ID",
                           "numItems",
                           "Name",
                        T: "identifier",
                    ]]),
                    5: ResourceResponse(learningResources=[attribute_ref := Reference(
                    content="Please review the [Attribute](https://mycourses2.mcgill.ca/) and "
                        "[Noun Analysis](https://mycourses2.mcgill.ca/) parts of the Class Diagram lecture.")]),
                })),
            ]),
            attribute_in_wrong_class_mistakes := mtc(n="Attribute in wrong class mistakes", mistakeTypes=[
                attribute_misplaced := mt(n="Attribute misplaced", stud_inst="attr", feedbacks=fbs({
                    1: HighlightSolution(),
                    2: TextResponse(text="Can you think of a better place for this attribute?"),
                    3: ParametrizedResponse(text="The ${stud_attr} attribute does not belong in the ${stud_attr.cls} "
                                                 "class. Where else can we place it?"),
                    4: ParametrizedResponse(text="The ${stud_attr} attribute belongs in the ${inst_attr.cls} class."),
                    5: ResourceResponse(learningResources=[attribute_ref]),
                })),
            ]),
            extra_attribute_mistakes := mtc(n="Extra attribute mistakes", mistakeTypes=[
                plural_attribute := mt(n="Plural attribute", stud_inst="attr", feedbacks=fbs({
                    1: HighlightSolution(),
                    2: TextResponse(text="Double check this attribute name."),
                    3: ParametrizedResponse(text="The ${stud_attr.cls}.${stud_attr} attribute should be singular."),
                    # Create a list multiple choice quiz using the McqFactory. See its documentation for more details
                    4: ResourceResponse(learningResources=[attribute_quiz := mcq[
                        "Pick the classes which are modeled correctly with Umple.",  # prompt
                           "class Student { courses; }",
                           "class Folder { List<File> files; }",
                        T: "class Restaurant { 1 -- * Employee; }",  # correct (true) choice
                    ]]),
                    5: ResourceResponse(learningResources=[attribute_ref]),
                })),
            ]),
        ]
    ),

    relationship_mistakes := mtc(n="Relationship mistakes", subcategories=[
        missing_association_aggregation_mistakes := mtc(n="Missing association/aggregation mistakes", mistakeTypes=[
            missing_association := mt(n="Missing association", stud=[], inst="assoc", feedbacks=fbs({
                1: HighlightProblem(),
                2: TextResponse(text="How should this relationship be modeled?"),
                3: ParametrizedResponse(text="How would you capture the relationship between ${inst_assoc.end0.cls} "
                                             "and ${inst_assoc.end1.cls}?"),
                4: ResourceResponse(learningResources=[compos_aggreg_assoc_ref := Reference(content=dedent("""\
                    Please review the _Composition vs. Aggregation vs. Association_ section of 
                    the [UML Class Diagram lecture slides](https://mycourses2.mcgill.ca/) to 
                    better understand these relationships and where they are used.

                    ![composition vs aggregation vs association](images/composition_aggregation_association.png)""")
                )]),
            })),
            using_attr_instead_of_assoc := mt(
                n="Using attr instead of assoc", d="Using attribute instead of association",
                stud="attr", inst="assocend", feedbacks=fbs({
                    1: HighlightSolution(),
                    2: TextResponse(text="Remember that attributes are simple pieces of data."),
                    3: ParametrizedResponse(text="${stud_attr} should be its own class."),
                    4: ResourceResponse(learningResources=[mcq[
                        "Pick the class(es) modeled correctly in Umple.",
                           "class BankAccount { Client client; }",
                        T: "class BankAccount { * -- 1..2 Client clients; }; class Client {}",
                           "class BankAccount { 1..2 -- * Client clients; }; class Client {}",
                           "class Loan { libraryPatron; }"]]),
                    5: ResourceResponse(learningResources=[compos_aggreg_assoc_ref]),
                })),
        ]),
        multiplicity_mistakes := mtc(n="Multiplicity mistakes", mistakeTypes=[
            wrong_multiplicity := mt(n="Wrong multiplicity", stud_inst="assocend", feedbacks=fbs({
                1: HighlightSolution(),
                2: TextResponse(text="Double check this association."),
                3: TextResponse(text="The multiplicity for this association end is incorrect."),
                4: ParametrizedResponse(
                    text="How many ${stud_assocend.opposite.cls} instances does a ${stud_assocend.cls} have?"),
                5: ResourceResponse(learningResources=[multiplicities_quiz := mcq[
                    "Pick the association(s) with correct multiplicities:",
                       "1 EmployeeRole -- 1 Person;",
                    T: "* Episode -- 1 TvSeries;",
                       "* Bank -- 1 Client;",
                       "* Client -- 1 BankAccount;",
                    T: "0..2 Loan -- 1 Client;",
                       "* Person -- 1 EmployeeRole;",
                    T: "* EmployeeRole -- 1 Person;",
                    ]]),
                6: ResourceResponse(learningResources=[mult_ref := Reference(
                    content="Please review the [multiplicities](https://mycourses2.mcgill.ca/) part of the "
                            "Class Diagram lecture.")]),
            })),
        ]),
        role_name_mistakes := mtc(n="Role name mistakes", mistakeTypes=[
            missing_role_name := mt(n="Missing role name", stud_inst="assocend", feedbacks=fbs({
                1: HighlightSolution(),
                2: TextResponse(text="Can you model this relationship more precisely?"),
                3: ParametrizedResponse(text="The relationship between ${stud_assocend.cls} and "
                    "${stud_assocend.opposite.cls} is missing a role name."),
                4: ResourceResponse(learningResources=[role_name_ref := Reference(content=dedent("""\
                    Can you think of appropriate [role names](https://mycourses2.mcgill.ca/)
                    for this relationship? Role names help identify the role a class plays in a
                    relationship and are particularly important if there is more than one relationship
                    between the same two classes.

                    ![Role name](images/role_name.png)
                    """))]),
            })),
            wrong_role_name := mt(
                n="Wrong role name", d="Wrong role name but correct association", stud_inst="assocend", feedbacks=fbs({
                    1: HighlightSolution(),
                    2: TextResponse(text="Double check this role name."),
                    3: ParametrizedResponse(text="The ${stud_assocend} role name is not correct."),
                    4: ParametrizedResponse(
                        text="The ${stud_assocend} role name should be changed to ${inst_assocend}."),
                    5: ResourceResponse(learningResources=[role_name_ref]),
                })),
        ]),
        composition_mistakes := mtc(n="Composition mistakes", mistakeTypes=[
            incomplete_containment_tree := mt(n="Incomplete containment tree", stud="cls*", inst=[], feedbacks=fbs({
                1: HighlightSolution(),
                2: TextResponse(text="Please double-check the relationships of these classes."),
                3: ParametrizedResponse(
                    text="${stud_cls*} should be contained in the containment tree.[ Use composition for this.]"),
                4: ResourceResponse(learningResources=[containment_example := Example(content=dedent("""\
                        Observe the following domain model. Every single class except the root class is directly or
                        indirectly contained in the root class, `PISystem`.

                        ![PISystem](images/PISystem.png)"""))]),
                5: ResourceResponse(learningResources=[containment_quiz := mcq[dedent("""\
                        Which of the following compositions should be part of the containment tree for the following
                        model?

                        ![IRS](images/IRS.png)"""),
                        T: "1 IRS <@>- * StudentRole",
                        T: "1 IRS <@>- * Person",
                           "1 IRS <@>- * Game",
                        T: "1 IRS <@>- * League",
                           "1 IRS <@>- * RegularLeague",
                        ]]),
                6: ResourceResponse(learningResources=[compos_aggreg_assoc_ref]),
            })),
        ]),
        generalization_mistakes := mtc(n="Generalization mistakes", mistakeTypes=[
            missing_generalization := mt(n="Missing generalization", stud=[], inst=["sub_cls", "super_cls"],
                feedbacks=fbs({
                    1: HighlightProblem(),
                    2: TextResponse(text="What is the relationship between these classes?"),
                    3: ParametrizedResponse(text="A ${inst_sub_cls} is a ${inst_super_cls}. How should we model this?"),
                    4: ResourceResponse(learningResources=[inherit_hierarchy_quiz := fitb(
                        # First parameter is the prompt (learning resource main content)
                        "Place the following classes in an inheritance hierarchy: Vehicle, Wheel, LuxuryBus, "
                        "Airplane, Car, Driver, LandVehicle, Bus. Only use a term once.",
                        # Remaining parameters are the statements with blanks in {curly braces}
                        "SportsCar isA {Car}",
                        "{Wheel} isA VehiclePart",
                        "Truck isA {LandVehicle}",
                        "AmphibiousVehicle isA {Vehicle}",
                        "{LuxuryBus} isA BusVehicle",
                    )]),
                5: ResourceResponse(learningResources=[gen_ref := Reference(
                    content="Please review the [Generalization](https://mycourses2.mcgill.ca/) part of the Class "
                            "Diagram lecture.")]),
            })),
        ]),
    ]),

    design_pattern_mistakes := mtc(n="Design pattern mistakes", subcategories=[
        abstraction_occurrence_pattern_mistakes := mtc(n="Abstraction-Occurrence pattern mistakes", mistakeTypes=[
            missing_ao_pattern := mt(
                n="Missing AO pattern", d="Missing Abstraction-Occurrence pattern",
                stud=[], inst=["abs_cls", "occ_cls"], feedbacks=fbs({
                    1: HighlightProblem(),
                    2: TextResponse(
                        text="Think carefully about how to model the relationship between these concepts."),
                    3: ParametrizedResponse(
                        text="The concepts of ${inst_abs_cls} and ${inst_occ_cls} and the relationship between them "
                            "should be modeled with the Abstraction-Occurrence pattern."),
                    4: ResourceResponse(learningResources=[ao_ref := Reference(content=dedent("""\
                        The [Abstraction-Occurrence Pattern](https://mycourses2.mcgill.ca/) can be used to 
                        represent a set of related objects that share common information but also differ
                        from each other in an important way.

                        ![Abstraction-Occurrence Pattern](images/abstraction_occurrence.png)"""))]),
                })),
        ]),
    ]),
])


# mistake types by priority, from most to least important
mts_by_priority: list[MistakeType | str] = [
    "Mistakes in an existing class",
    plural_class_name,
    software_engineering_term,

    "Mistakes in an existing attribute",
    bad_attribute_name_spelling,
    plural_attribute,
    attribute_misplaced,

    "Mistakes in an existing relationship",
    using_attr_instead_of_assoc,
    wrong_multiplicity,
    wrong_role_name,
    incomplete_containment_tree,

    "Design pattern mistakes",
    # eg, Subclass should be full Player-Role pattern

    "Extra items",
    # ...

    "Missing items",
    missing_class,
    missing_generalization,
    missing_association,
    missing_role_name,

    "Missing/incomplete patterns",
    missing_ao_pattern,
]
