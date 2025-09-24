package None;

import java.util.List;
import lombok.*;



/* version: 1.0.9891 */


/**
  Information on the origin of a synthetic part that composes the biological material
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SyntheticPartOrigin extends BiologicalPartOrigin {

  private boolean modificationsFromTheReferenceSequences;
  private String descriptionOfModificationsMadeFromTheReferenceSequences;

}