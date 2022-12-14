"""
Helper module for easy serialization and deserialization of models and metamodels from files.
"""

from collections.abc import Iterable
import os

from pyecore.ecore import EObject
from pyecore.resources.resource import Resource, ResourceSet, URI

from classdiagram import ClassDiagram
from learningcorpus import LearningCorpus, LearningItem
from serdes import set_static_class_for
from stringserdes import SRSET
from constants import (CLASS_DIAGRAM_MM, DEFAULT_MODELING_ASSISTANT_PATH, LEARNING_CORPUS_MM, LEARNING_CORPUS_QUIZ_MM,
                       MODELING_ASSISTANT_MM)
from utils import warn
from modelingassistant import ModelingAssistant


def load_metamodels(*ecore_files: str) -> ResourceSet:
    """
    Return a ResourceSet loaded with the given metamodels from the ecore file paths.
    """
    rset = SRSET
    for ecore_file in ecore_files:
        mm_root = rset.get_resource(URI(ecore_file)).contents[0]
        rset.metamodel_registry[mm_root.nsURI] = mm_root  # ecore loaded in rset as a metamodel here
    return rset


def load_cdm(cdm_file: str, use_static_classes: bool = True) -> ClassDiagram:
    """
    Open a class diagram instance from the given file.
    """
    if not cdm_file.endswith(".cdm"):
        warn(f"Attempting to open {cdm_file} with unexpected extension as a *.cdm file.")
    rset = load_metamodels(CLASS_DIAGRAM_MM)
    resource = rset.get_resource(URI(cdm_file))
    class_diagram = resource.contents[0]
    if use_static_classes:
        class_diagram.__class__ = ClassDiagram
        for e in class_diagram.eAllContents():
            set_static_class_for(e)
    return class_diagram


def load_ma(ma_file: str, use_static_classes: bool = True) -> ModelingAssistant:
    """
    Open a modeling assistant instance from the given file.
    """
    if not ma_file.endswith(".modelingassistant"):
        warn(f"Attempting to open {ma_file} with unexpected extension as a *.modelingassistant file.")
    rset = load_metamodels(CLASS_DIAGRAM_MM, LEARNING_CORPUS_MM, MODELING_ASSISTANT_MM)
    resource = rset.get_resource(URI(ma_file))
    modeling_assistant: ModelingAssistant = resource.contents[0]
    if use_static_classes:
        modeling_assistant.__class__ = ModelingAssistant
        for e in modeling_assistant.eAllContents():
            set_static_class_for(e)
    return modeling_assistant


def load_default_ma(use_static_classes: bool = True) -> ModelingAssistant:
    """
    Open the default modeling assistant instance.
    """
    if not os.path.exists(DEFAULT_MODELING_ASSISTANT_PATH):
        save_to_file(DEFAULT_MODELING_ASSISTANT_PATH, ModelingAssistant())
    return load_ma(DEFAULT_MODELING_ASSISTANT_PATH, use_static_classes)


def load_lc(lc_file: str, use_static_classes: bool = True) -> LearningCorpus:
    """
    Open a learning corpus instance from the given file.
    """
    if not lc_file.endswith(".learningcorpus"):
        warn(f"Attempting to open {lc_file} with unexpected extension as a *.learningcorpus file.")
    rset = load_metamodels(LEARNING_CORPUS_MM)
    resource = rset.get_resource(URI(lc_file))
    learning_corpus = resource.contents[0]
    # use static autogenerated classes instead of the dynamic pyecore ones inferred from the metamodel
    if use_static_classes:
        learning_corpus.__class__ = LearningCorpus
        learning_corpus.learningItems.feature._eType = LearningItem  # pylint: disable=protected-access
        for e in learning_corpus.eAllContents():
            set_static_class_for(e)
    return learning_corpus


def save_to_files(items_by_filename: dict[str, EObject | list[EObject]]):
    """
    Save the given EObject items to their respective files.
    """
    uri_to_filename = {URI(fn): fn for fn in items_by_filename.keys()}
    filename_to_uri = {fn: uri for uri, fn in uri_to_filename.items()}
    rset = load_metamodels(CLASS_DIAGRAM_MM, LEARNING_CORPUS_MM, LEARNING_CORPUS_QUIZ_MM, MODELING_ASSISTANT_MM)
    resources = []
    for filename in items_by_filename.keys():
        resource: Resource = rset.create_resource(filename_to_uri[filename])
        resource.use_uuid = True
        resources.append(resource)
    for resource in resources:
        item = items = items_by_filename[uri_to_filename[resource.uri]]
        if isinstance(items, Iterable):
            resource.extend(items)
        else:
            resource.append(item)
    for resource in resources:
        resource.save()


def save_to_file(filename: str, item: EObject):
    """
    Save the given EObject item to the given file.
    """
    save_to_files({filename: item})
