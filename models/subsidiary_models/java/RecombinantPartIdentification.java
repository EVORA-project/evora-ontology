package None;

import java.util.List;
import lombok.*;



/* version: 1.0.7894 */


/**
  Identification of a recombinant part
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RecombinantPartIdentification  {

  private String partIdentification;
  private List<Sequence> sequence;

}