package None;

import java.util.List;
import lombok.*;



/* version: 1.0.11042 */


/**
  A protein as a derived product from a pathogen.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Protein extends Product {

  private BiologicalMaterialOrigin biologicalMaterialOrigin;
  private List<Sequence> sequence;
  private List<PdbReference> relatedPdb;
  private List<SpecialFeature> specialFeature;
  private TagSequence tagSequence;
  private String domain;
  private String expressedAs;
  private String inclusionBodiesType;
  private String expressionSystem;
  private String functionalCharacterization;
  private String functionalAndTechnicalDescription;
  private String proteinPurification;
  private String tagStatusOfTheSolubilizedProtein;
  private List<String> typeOfFunctionalCharacterization;

}