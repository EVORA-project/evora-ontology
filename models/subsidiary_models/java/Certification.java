package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10834 */


/**
  Assurance given by an independent certification body that a product, service or system meets the requirements of a standard.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Certification extends Resource {

  private String title;
  private String description;
  private Image logo;
  private List<Document> certificationDocument;
  private String resourceUrl;

}