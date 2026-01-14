package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10897 */


/**
  A subset of words or phrases specific to a particular subject or field.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Vocabulary extends Catalogue {

  private DataProvider termDataProvider;
  private List<Term> term;

}