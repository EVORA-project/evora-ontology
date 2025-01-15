package None;

import java.util.List;
import lombok.*;



/* version: 1.0.7500 */


/**
  A service
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Service extends ProductOrService {

  private String modelSpecies;
  private String modelType;

}