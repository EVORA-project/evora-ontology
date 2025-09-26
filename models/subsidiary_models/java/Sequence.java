package None;

import java.util.List;
import lombok.*;



/* version: 1.0.9968 */


/**
  A nucleic acid or protein sequence information
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sequence extends Resource {

  private List<SequenceReference> sequenceReference;
  private String sequenceFasta;

}