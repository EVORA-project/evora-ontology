package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10956 */


/**
  The country as of ISO3166.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Country extends Term {

  private String alpha2Code;

}