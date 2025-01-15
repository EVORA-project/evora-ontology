package None;

import java.util.List;
import lombok.*;



/* version: 1.0.7356 */


/**
  A reference that permits to retrieve the sequence information from a sequence provider
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SequenceReference extends Dataset {

  private String accessionNumber;
  private String sequenceProvider;

}