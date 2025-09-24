package None;

import java.util.List;
import lombok.*;



/* version: 1.0.9907 */


/**
  The virus as a biological material
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Virus extends Pathogen {

  private List<VirusName> coInfectingViruses;
  private boolean contaminationWithCoInfectingViruses;
  private boolean mycoplasmicContent;

}