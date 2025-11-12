package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10727 */


/**
  A structured representation of data about the classification and naming of biological organisms into groups according to shared characteristics.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Taxonomy extends Catalogue {

  private List<Taxon> taxon;
  private DataProvider taxonDataProvider;
  private DataProvider versionDataProvider;
  private List<TaxonomicRank> rank;
  private DataProvider rankDataProvider;

}