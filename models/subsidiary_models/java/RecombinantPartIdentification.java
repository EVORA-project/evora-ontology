package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8719 */


/**
  Identification of a recombinant part
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RecombinantPartIdentification extends Resource {

  private String partIdentification;
  private List<Sequence> sequence;

}