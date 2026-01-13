package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10825 */


/**
  Numeric code assigned to identify a particular historical version of a work (e.g. software or technical standards).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Version extends Resource {

  private String version;
  private String versionOf;
  private List<Resource> resource;

}