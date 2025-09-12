package None;

import java.util.List;
import lombok.*;



/* version: 1.0.9734 */


/**
  Conceptual entity that groups one or more populations of an organism or organisms, as seen by taxonomists, to form a unit
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Taxon extends Term {

  private List<Taxonomy> taxonomy;
  private Taxon parentTaxon;
  private TaxonomicRank rank;
  private List<Taxon> previouslyKnownAs;
  private List<Taxon> externalEquivalentTaxon;
  private String taxonomicId;
  private String taxonomicNodeId;

}