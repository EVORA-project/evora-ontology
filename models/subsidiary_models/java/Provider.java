package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8773 */


/**
  A provider of products or services, as a specific organization
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Provider extends Organization {

  private List<RI> memberOfRI;

}