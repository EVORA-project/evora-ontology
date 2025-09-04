package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8940 */


/**
  A social entity established to meet needs or pursue specific goals
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Organization extends PersonOrOrganization {

  private List<AlternateName> alternateName;
  private Country country;
  private String rorId;

}