package None;

import java.util.List;
import lombok.*;



/* version: 1.0.7894 */


/**
  The legal terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class License extends Nameable {

  private String resourceURL;
  private String licensingOrAttribution;
  private Image logo;

}