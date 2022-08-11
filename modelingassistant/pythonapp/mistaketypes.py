"""
This file contains all mistake types and categories.
It is generated automatically by the createcorpus.py script.
"""

from constants import LEARNING_CORPUS_PATH
from fileserdes import load_lc
from learningcorpus import MistakeTypeCategory, MistakeType

corpus = load_lc(LEARNING_CORPUS_PATH)

# Populate dictionaries
MISTAKE_TYPE_CATEGORIES_BY_NAME: dict[str, MistakeTypeCategory] = {c.name: c for c in corpus.mistakeTypeCategories}
MISTAKE_TYPES_BY_NAME: dict[str, MistakeType] = {mt.name: mt for mt in corpus.mistakeTypes()}

# Short-name references to the above dicts for greater code legibility
_MTCS = MISTAKE_TYPE_CATEGORIES_BY_NAME
_MTS = MISTAKE_TYPES_BY_NAME


# Mistake type categories
CLASS_MISTAKES: MistakeTypeCategory = _MTCS["Class mistakes"]
ATTRIBUTE_MISTAKES: MistakeTypeCategory = _MTCS["Attribute mistakes"]
RELATIONSHIP_MISTAKES: MistakeTypeCategory = _MTCS["Relationship mistakes"]
DESIGN_PATTERN_MISTAKES: MistakeTypeCategory = _MTCS["Design pattern mistakes"]
CLASS_NAME_MISTAKES: MistakeTypeCategory = _MTCS["Class name mistakes"]
ATTRIBUTE_NAME_MISTAKES: MistakeTypeCategory = _MTCS["Attribute name mistakes"]
ATTRIBUTE_IN_WRONG_CLASS_MISTAKES: MistakeTypeCategory = _MTCS["Attribute in wrong class mistakes"]
EXTRA_ATTRIBUTE_MISTAKES: MistakeTypeCategory = _MTCS["Extra attribute mistakes"]
MISSING_ASSOCIATION_AGGREGATION_MISTAKES: MistakeTypeCategory = _MTCS["Missing association/aggregation mistakes"]
MULTIPLICITY_MISTAKES: MistakeTypeCategory = _MTCS["Multiplicity mistakes"]
ROLE_NAME_MISTAKES: MistakeTypeCategory = _MTCS["Role name mistakes"]
COMPOSITION_MISTAKES: MistakeTypeCategory = _MTCS["Composition mistakes"]
GENERALIZATION_MISTAKES: MistakeTypeCategory = _MTCS["Generalization mistakes"]
ABSTRACTION_OCCURRENCE_PATTERN_MISTAKES: MistakeTypeCategory = _MTCS["Abstraction-Occurrence pattern mistakes"]

# Mistake types
MISSING_CLASS: MistakeType = _MTS["Missing class"]
PLURAL_CLASS_NAME: MistakeType = _MTS["Plural class name"]
SOFTWARE_ENGINEERING_TERM: MistakeType = _MTS["Software engineering term"]
BAD_ATTRIBUTE_NAME_SPELLING: MistakeType = _MTS["Bad attribute name spelling"]
ATTRIBUTE_MISPLACED: MistakeType = _MTS["Attribute misplaced"]
PLURAL_ATTRIBUTE: MistakeType = _MTS["Plural attribute"]
MISSING_ASSOCIATION: MistakeType = _MTS["Missing association"]
USING_ATTR_INSTEAD_OF_ASSOC: MistakeType = _MTS["Using attr instead of assoc"]
WRONG_MULTIPLICITY: MistakeType = _MTS["Wrong multiplicity"]
MISSING_ROLE_NAME: MistakeType = _MTS["Missing role name"]
WRONG_ROLE_NAME: MistakeType = _MTS["Wrong role name"]
INCOMPLETE_CONTAINMENT_TREE: MistakeType = _MTS["Incomplete containment tree"]
MISSING_GENERALIZATION: MistakeType = _MTS["Missing generalization"]
MISSING_AO_PATTERN: MistakeType = _MTS["Missing AO pattern"]
