// package ...

import java.util.HashMap;
import java.util.Map;
import learningcorpus.LearningCorpus;
import learningcorpus.MistakeType;
import learningcorpus.MistakeTypeCategory;

/**
 * This class contains all mistake types and categories.
 * It is generated automatically by the createcorpus.py script.
 */
public class MistakeTypes {

  /** The path of the learning corpus instance with mistake types. */
  public static final String LEARNING_CORPUS_PATH =
      "../modelingassistant/learningcorpusinstances/default.learningcorpus";

  /** Map of mistake type categories by name. */
  public static final Map<String, MistakeTypeCategory> MISTAKE_TYPE_CATEGORIES_BY_NAME = new HashMap<>();

  /** Map of mistake types by name. */
  public static final Map<String, MistakeType> MISTAKE_TYPES_BY_NAME = new HashMap<>();

  // Short-name references to the above maps for greater code legibility
  private static final Map<String, MistakeTypeCategory> MTCS = MISTAKE_TYPE_CATEGORIES_BY_NAME;
  private static final Map<String, MistakeType> MTS = MISTAKE_TYPES_BY_NAME;

  static {
    var learningCorpus = LearningCorpus.fromFile(LEARNING_CORPUS_PATH);
    learningCorpus.getMistakeTypeCategories().forEach(mtc -> MISTAKE_TYPE_CATEGORIES_BY_NAME.put(mtc.getName(), mtc));
    learningCorpus.getMistakeTypes().forEach(mt -> MISTAKE_TYPES_BY_NAME.put(mt.getName(), mt));
  }

  // Mistake type categories

  /** The category for class mistakes. */
  public static final MistakeTypeCategory CLASS_MISTAKES = MTCS.get("Class mistakes");

  /** The category for attribute mistakes. */
  public static final MistakeTypeCategory ATTRIBUTE_MISTAKES = MTCS.get("Attribute mistakes");

  /** The category for relationship mistakes. */
  public static final MistakeTypeCategory RELATIONSHIP_MISTAKES = MTCS.get("Relationship mistakes");

  /** The category for design pattern mistakes. */
  public static final MistakeTypeCategory DESIGN_PATTERN_MISTAKES = MTCS.get("Design pattern mistakes");

  /** The category for class name mistakes. */
  public static final MistakeTypeCategory CLASS_NAME_MISTAKES = MTCS.get("Class name mistakes");

  /** The category for attribute name mistakes. */
  public static final MistakeTypeCategory ATTRIBUTE_NAME_MISTAKES = MTCS.get("Attribute name mistakes");

  /** The category for attribute in wrong class mistakes. */
  public static final MistakeTypeCategory ATTRIBUTE_IN_WRONG_CLASS_MISTAKES =
      MTCS.get("Attribute in wrong class mistakes");

  /** The category for extra attribute mistakes. */
  public static final MistakeTypeCategory EXTRA_ATTRIBUTE_MISTAKES = MTCS.get("Extra attribute mistakes");

  /** The category for missing association/aggregation mistakes. */
  public static final MistakeTypeCategory MISSING_ASSOCIATION_AGGREGATION_MISTAKES =
      MTCS.get("Missing association/aggregation mistakes");

  /** The category for multiplicity mistakes. */
  public static final MistakeTypeCategory MULTIPLICITY_MISTAKES = MTCS.get("Multiplicity mistakes");

  /** The category for role name mistakes. */
  public static final MistakeTypeCategory ROLE_NAME_MISTAKES = MTCS.get("Role name mistakes");

  /** The category for composition mistakes. */
  public static final MistakeTypeCategory COMPOSITION_MISTAKES = MTCS.get("Composition mistakes");

  /** The category for generalization mistakes. */
  public static final MistakeTypeCategory GENERALIZATION_MISTAKES = MTCS.get("Generalization mistakes");

  /** The category for abstraction-occurrence pattern mistakes. */
  public static final MistakeTypeCategory ABSTRACTION_OCCURRENCE_PATTERN_MISTAKES =
      MTCS.get("Abstraction-Occurrence pattern mistakes");


  // Mistake types

  /** The missing class mistake type. */
  public static final MistakeType MISSING_CLASS = MTS.get("Missing class");

  /** The plural class name mistake type. */
  public static final MistakeType PLURAL_CLASS_NAME = MTS.get("Plural class name");

  /** The software engineering term mistake type. */
  public static final MistakeType SOFTWARE_ENGINEERING_TERM = MTS.get("Software engineering term");

  /** The bad attribute name spelling mistake type. */
  public static final MistakeType BAD_ATTRIBUTE_NAME_SPELLING = MTS.get("Bad attribute name spelling");

  /** The attribute misplaced mistake type. */
  public static final MistakeType ATTRIBUTE_MISPLACED = MTS.get("Attribute misplaced");

  /** The plural attribute mistake type. */
  public static final MistakeType PLURAL_ATTRIBUTE = MTS.get("Plural attribute");

  /** The missing association mistake type. */
  public static final MistakeType MISSING_ASSOCIATION = MTS.get("Missing association");

  /** The using attribute instead of association mistake type. */
  public static final MistakeType USING_ATTR_INSTEAD_OF_ASSOC = MTS.get("Using attr instead of assoc");

  /** The wrong multiplicity mistake type. */
  public static final MistakeType WRONG_MULTIPLICITY = MTS.get("Wrong multiplicity");

  /** The missing role name mistake type. */
  public static final MistakeType MISSING_ROLE_NAME = MTS.get("Missing role name");

  /** The wrong role name but correct association mistake type. */
  public static final MistakeType WRONG_ROLE_NAME = MTS.get("Wrong role name");

  /** The incomplete containment tree mistake type. */
  public static final MistakeType INCOMPLETE_CONTAINMENT_TREE = MTS.get("Incomplete containment tree");

  /** The missing generalization mistake type. */
  public static final MistakeType MISSING_GENERALIZATION = MTS.get("Missing generalization");

  /** The missing abstraction-occurrence pattern mistake type. */
  public static final MistakeType MISSING_AO_PATTERN = MTS.get("Missing AO pattern");

}
