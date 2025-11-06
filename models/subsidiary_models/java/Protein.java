package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10170 */


/**
  A protein as a derived product from a pathogen
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Protein extends Product {

  private BiologicalMaterialOrigin biologicalMaterialOrigin;
  private List<Sequence> sequence;
  private List<PdbReference> relatedPdb;
  private List<SpecialFeature> specialFeature;
  private List<TagSequence> tagSequence;
  private List<String> domain;
  private List<String> expressedAs;
  private List<String> inclusionBodiesType;
  private List<String> expressionSystem;
  private List<String> functionalCharacterization;
  private List<String> functionalAndTechnicalDescription;
  private List<String> proteinPurification;
  private List<String> tagStatusOfTheSolubilizedProtein;
  private List<String> typeOfFunctionalCharacterization;

}