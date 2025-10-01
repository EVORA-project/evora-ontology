package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10016 */


/**
  Information about the origin of the biological material, compulsory for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BiologicalMaterialOrigin extends Resource {

  private boolean recombinantMaterial;
  private boolean biologicalSourceType;
  private List<BiologicalPartOrigin> biologicalPartOrigin;

}