package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  The virus as a biological material.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Virus extends Pathogen {

  private List<VirusName> coInfectingViruses;
  private String contaminationWithCoInfectingViruses;
  private String mycoplasmicContent;

}