package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8687 */


/**
  Science of naming, defining and classifying organisms
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Taxonomy extends Catalogue {

  private List<Taxon> taxon;
  private DataProvider taxonDataProvider;
  private Version version;
  private DataProvider versionDataProvider;
  private List<TaxonomicRank> rank;
  private DataProvider rankDataProvider;

}