package None;

import java.util.List;
import lombok.*;



/* version: 1.0.7785 */


/**
  Any entity that has a name and can have a textual description
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Nameable  {

  private String name;
  private String description;

}