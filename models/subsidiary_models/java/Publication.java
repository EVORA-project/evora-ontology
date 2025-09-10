package None;

import java.util.List;
import lombok.*;



/* version: 1.0.9149 */


/**
  A scientific publication
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Publication extends Resource {

  private String title;
  private String authors;
  private String abstract;
  private Doi doi;
  private Journal journal;

}