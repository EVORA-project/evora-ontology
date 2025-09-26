package None;

import java.util.List;
import lombok.*;



/* version: 1.0.9975 */


/**
  An intangible offering characterized by an activity, performance, or facilitation carried out by a provider to fulfill a user’s need
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Service extends ProductOrService {

  private String modelSpecies;
  private String modelType;

}