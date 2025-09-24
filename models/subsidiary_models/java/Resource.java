package None;

import java.util.List;
import lombok.*;



/* version: 1.0.9891 */


/**
  Resource published or curated by a single agent
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Resource  {

  private List<String> keyword;
  private ZonedDateTime dateIssued;
  private ZonedDateTime dateModified;

}