package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10945 */


/**
  A syndromic grouping of pathogens, based on typical disease manifestation, clinical syndrome, or primary system affected. Examples include Respiratory viruses, Hemorrhagic viruses, and Gastroenteritis viruses. Clinical groups are not taxonomic categories but practical classifications used in medicine, epidemiology, and public health.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ClinicalGroup extends Term {

  private List<AlternateName> alternateName;
  private List<Taxon> taxon;

}