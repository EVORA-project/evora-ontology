package None;

import java.util.List;
import lombok.*;



/* version: 1.0.9137 */


/**
  A person or an organization
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PersonOrOrganization extends Resource {

  private String name;
  private String description;
  private String homePage;
  private ContactPoint contactPoint;
  private Image logo;

}