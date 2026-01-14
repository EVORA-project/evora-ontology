package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10888 */


/**
  Subclass of File representing visual content such as pictures, diagrams, or illustrations.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Image extends File {

  private String altText;

}