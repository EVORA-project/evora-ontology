package None;

import java.util.List;
import lombok.*;



/* version: 1.0.7504 */


/**
  A service
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Service extends ProductOrService {

  private String modelSpecies;
  private String modelType;

}