package None;

import java.util.List;
import lombok.*;



/* version: 1.0.9149 */


/**
  An hybridoma that provides antibodies that can be related to a pathogen
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Hybridoma extends Antibody {

  private String hybridomaDescription;

}