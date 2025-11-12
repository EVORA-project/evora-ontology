package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10727 */


/**
  Nucleic acid related to a pathogen. It can be extracted or synthetic.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NucleicAcid extends Product {

  private BiologicalMaterialOrigin biologicalMaterialOrigin;
  private List<Data> genBankFileOfTheConstruct;
  private List<Sequence> sequence;
  private boolean clonedNucleicAcid;
  private ExpressionVector clonedIntoPlasmid;
  private List<PlasmidSelection> plasmidSelection;
  private TagSequence tagSequence;
  private String regionEncompassedInThisProduct;
  private boolean mutationObserved;
  private String observedMutations;
  private String identificationTechnique;
  private String sequencing;
  private String titer;
  private boolean sequenceChecked;

}