package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8369 */


/**
  A collection of operations that provides access to one or more datasets or data processing functions
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class DataService extends Resource {

  private String name;
  private String description;

}