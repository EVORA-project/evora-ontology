package None;

import java.util.List;
import lombok.*;



/* version: 1.0.9149 */


/**
  A nucleic acid or protein sequence information
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sequence extends Resource {

  private List<SequenceReference> sequenceReference;
  private String sequenceFasta;

}