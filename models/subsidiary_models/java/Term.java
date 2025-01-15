package None;

import java.util.List;
import lombok.*;



/* version: 1.0.7500 */


/**
  Word or phrase from a specialized area of knowledge
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Term extends NamedDataset {

  private int weight;
  private Vocabulary inVocabulary;

}