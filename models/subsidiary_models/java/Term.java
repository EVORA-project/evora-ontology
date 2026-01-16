package None;

import java.util.List;
import lombok.*;



/* version: 1.1.4 */


/**
  Word or phrase from a specialized area of knowledge.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Term extends Resource {

  private String title;
  private String description;
  private Integer weight;
  private Vocabulary inVocabulary;

}