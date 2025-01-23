package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8305 */


/**
  Identification of a recombinant part
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RecombinantPartIdentification extends Dataset {

  private String partIdentification;
  private List<Sequence> sequence;

}