package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10142 */


/**
  A detection kit for specific pathogens
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DetectionKit extends Product {

  private List<File> standardOperatingProcedureFile;
  private boolean specificityDocumented;
  private String specificity;
  private String targetedRegion;

}