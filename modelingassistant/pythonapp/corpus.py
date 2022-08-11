"""
Initializes and provides access to the Learning Corpus at runtime.
"""
# pylint: disable=invalid-name

from corpus_definition import (corpus as corpus_def, mts_by_priority as mts_by_priority_def,
    missing_generalization, incomplete_containment_tree, missing_ao_pattern, software_engineering_term,
    plural_class_name, missing_class, using_attr_instead_of_assoc, plural_attribute, bad_attribute_name_spelling,
    attribute_misplaced, missing_association, wrong_role_name, missing_role_name, wrong_multiplicity)
from constants import USE_CONTEXTUAL_CAPITALIZATION
from learningcorpus import LearningItem, MistakeType, ResourceResponse, ParametrizedResponse
from utils import _mtc_subcats, warn


WARN_ABOUT_MISTAKE_TYPES_WITHOUT_PARAM_RESP = False

CL = "Capital Letter"
UL = "Uppercase Letter"

corpus = corpus_def
mts_by_priority = [mt for mt in mts_by_priority_def if isinstance(mt, MistakeType)]

domain_modeling = LearningItem(name="DomainModeling", learningCorpus=corpus)

class_ = LearningItem(name="Class", learningCorpus=corpus, mistakeTypes=[
    software_engineering_term, plural_class_name, missing_class])
attribute = LearningItem(name="Attribute", learningCorpus=corpus, mistakeTypes=[
    plural_attribute, bad_attribute_name_spelling, attribute_misplaced])
association = LearningItem(name="Association", learningCorpus=corpus, mistakeTypes=[
    using_attr_instead_of_assoc, missing_association])
associationend = LearningItem(name="AssociationEnd", learningCorpus=corpus, mistakeTypes=[
    wrong_role_name, missing_role_name, wrong_multiplicity])
composition = LearningItem(name="Composition", learningCorpus=corpus, mistakeTypes=[incomplete_containment_tree])
generalization = LearningItem(name="Generalization", learningCorpus=corpus, mistakeTypes=[missing_generalization])
design_patterns = LearningItem(name="DesignPatterns", learningCorpus=corpus, mistakeTypes=[missing_ao_pattern])


for supercat, subcats in _mtc_subcats.items():
    for subcat in subcats:
        subcat.supercategory = supercat
        subcat.learningCorpus = corpus

for _mt in corpus.mistakeTypes():
    has_param_resp = False
    for feedback in _mt.feedbacks:
        feedback.learningCorpus = corpus
        if isinstance(feedback, ResourceResponse):
            for lr in feedback.learningResources:
                lr.learningCorpus = corpus
        if isinstance(feedback, ParametrizedResponse):
            has_param_resp = True
    if WARN_ABOUT_MISTAKE_TYPES_WITHOUT_PARAM_RESP and not has_param_resp:
        warn(f'Mistake type "{_mt.name}" has no parametrized response')


for i, _mt in enumerate(mts_by_priority, start=1):
    _mt.priority = i


def effectuate_contextual_capitalization(use_caps: bool = None):
    "Enable or disable contextual capitalization in the feedback texts."
    if use_caps is None:
        use_caps = USE_CONTEXTUAL_CAPITALIZATION
    for fb in corpus.feedbacks:
        if fb.text:
            if use_caps:
                fb.text = fb.text.replace(CL.lower(), CL).replace(UL.lower(), UL)
            else:
                fb.text = fb.text.replace(CL, CL.lower()).replace(UL, UL.lower())


effectuate_contextual_capitalization()
