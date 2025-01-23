package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8305 */


/**
  A person or an organization
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PersonOrOrganization extends Dataset {

  private String name;
  private String description;
  private String homePage;
  private ContactPoint contactPoint;
  private Image logo;

}