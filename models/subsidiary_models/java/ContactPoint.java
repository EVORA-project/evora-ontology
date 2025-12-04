package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10787 */


/**
  Entity serving as focal point of information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ContactPoint extends Resource {

  private String name;
  private String description;
  private String email;
  private String telephone;
  private String streetAddress;
  private String addressLocality;
  private String addressRegion;
  private String postalCode;
  private Country addressCountry;
  private String orcidId;

}