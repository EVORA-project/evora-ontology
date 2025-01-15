package None;

import java.util.List;
import lombok.*;



/* version: 1.0.7504 */


/**
  A scientific publication
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Publication extends Dataset {

  private String title;
  private String authors;
  private String abstract;
  private DOI relatedDOI;
  private Journal journal;

}