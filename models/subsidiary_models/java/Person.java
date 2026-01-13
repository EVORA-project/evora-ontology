package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10825 */


/**
  An individual.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Person extends PersonOrOrganization {

  private String orcidId;

}