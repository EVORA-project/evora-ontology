package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8305 */


/**
  Word or phrase from a specialized area of knowledge
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Term extends Dataset {

  private String name;
  private String description;
  private int weight;
  private Vocabulary inVocabulary;

}