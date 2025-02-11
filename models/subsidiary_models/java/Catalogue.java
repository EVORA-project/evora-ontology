package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8498 */


/**
  A curated collection of metadata about resources
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Catalogue extends Dataset {

  private String name;
  private String description;

}