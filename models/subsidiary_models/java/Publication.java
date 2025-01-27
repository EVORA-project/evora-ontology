package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8373 */


/**
  A scientific publication
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Publication extends Resource {

  private String title;
  private String authors;
  private String abstract;
  private DOI relatedDOI;
  private Journal journal;

}