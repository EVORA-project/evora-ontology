package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8369 */


/**
  A social entity established to meet needs or pursue specific goals
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Organization extends PersonOrOrganization {

  private AlternateName alternateName;
  private Country country;
  private String rORiD;

}