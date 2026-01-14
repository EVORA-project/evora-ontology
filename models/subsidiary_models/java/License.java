package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10923 */


/**
  The legal terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class License extends Resource {

  private String title;
  private String description;
  private String resourceUrl;
  private String licensingOrAttribution;
  private Image logo;

}