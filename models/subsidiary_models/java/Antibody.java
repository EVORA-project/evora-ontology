package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10773 */


/**
  Protein that can bind to certain types of foreign bodies, such as pathogens.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Antibody extends Product {

  private String productionSystem;
  private boolean antibodyPurifiedByAffinity;
  private boolean specificityDocumented;
  private String antibodySpecificity;
  private String targetedAntigen;
  private List<SequenceReference> sequenceReference;
  private String antibodyType;
  private List<String> antibodyCharacterizationMethod;
  private String antibodyCharacterizationObservation;

}