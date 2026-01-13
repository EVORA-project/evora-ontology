package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10825 */


/**
  A collection of data, published or curated by a single agent, and available for access.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Dataset extends Resource {

  private String title;
  private String description;
  private String version;

}