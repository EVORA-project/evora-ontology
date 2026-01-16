package None;

import java.util.List;
import lombok.*;



/* version: 1.1.4 */


/**
  List of other names for things.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AlternateName extends Term {

  private List<AlternateName> alternateName;
  private List<String> sourceOfInformation;

}