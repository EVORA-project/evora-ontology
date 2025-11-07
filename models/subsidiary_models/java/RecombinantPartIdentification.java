package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10635 */


/**
  Identification of a recombinant part.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RecombinantPartIdentification extends Resource {

  private String partIdentification;
  private List<Sequence> sequence;

}