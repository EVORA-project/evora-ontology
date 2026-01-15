package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10956 */


/**
  A reference that permits to retrieve the sequence information from a sequence provider.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SequenceReference extends Resource {

  private String accessionNumber;
  private String sequenceProvider;

}