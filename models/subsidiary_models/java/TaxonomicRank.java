package None;

import java.util.List;
import lombok.*;



/* version: 1.2.0 */


/**
  The possible taxonomic ranks and their description.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TaxonomicRank extends Term {

  private List<Taxonomy> taxonomy;

}