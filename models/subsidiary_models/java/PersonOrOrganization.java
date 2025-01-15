package None;

import java.util.List;
import lombok.*;



/* version: 1.0.7504 */


/**
  A person or an organization
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PersonOrOrganization extends Nameable {

  private String homePage;
  private ContactPoint contactPoint;
  private Image logo;

}