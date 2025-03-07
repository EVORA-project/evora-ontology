package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8636 */


/**
  Information on the origin of a unitary, cohesive part that is part of, or constitutes the biological material. It can be multiple parts in case of a recombinant biological material
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class BiologicalPartOrigin extends Resource {

  private RecombinantPartIdentification recombinantPartIdentification;
  private boolean accessToPhysicalGeneticResource;

}