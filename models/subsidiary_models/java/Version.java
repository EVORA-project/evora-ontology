package None;

import java.util.List;
import lombok.*;



/* version: 1.0.7356 */


/**
  Numeric code assigned to identify a particular historical version of a work (e.g. software or technical standards)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Version extends Dataset {

  private String iD;
  private String versionOf;

}