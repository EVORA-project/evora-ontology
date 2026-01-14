package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10923 */


/**
  Vernacular name that is the name used in everyday language to refer to something like an organism or group of organisms. This name is typically easier to remember and pronounce compared to the scientific or technical name.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CommonName extends Term {

  private List<AlternateName> alternateName;
  private List<String> sourceOfInformation;

}