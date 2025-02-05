package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8498 */


/**
  Digital document or record stored in a specific format that contains data or information
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class File extends Resource {

  private String name;
  private String description;
  private String contentURL;
  private String format;
  private License license;

}