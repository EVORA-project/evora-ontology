package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8773 */


/**
  A nucleic acid or protein sequence information
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sequence extends Resource {

  private List<SequenceReference> sequenceReference;
  private String sequenceFASTA;

}