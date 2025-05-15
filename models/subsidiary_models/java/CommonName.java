package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8702 */


/**
  Vernacular name that is the name used in everyday language to refer to an organism or group of organisms. This name is typically easier to remember and pronounce compared to the scientific name
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CommonName extends Term {

  private List<AlternateName> alternateName;
  private List<String> sourceOfInformation;

}