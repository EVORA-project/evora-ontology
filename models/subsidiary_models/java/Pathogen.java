package None;

import java.util.List;
import lombok.*;



/* version: 1.0.9149 */


/**
  Biological entity that causes disease in its host, which is typically an infectious microorganism or agent, such as a virus, bacterium, protozoan, prion, viroid, or fungus
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Pathogen extends Product {

  private BiologicalMaterialOrigin biologicalMaterialOrigin;
  private List<GeographicalOrigin> suspectedEpidemiologicalOrigin;
  private List<IsolationHost> isolationHost;
  private List<ProductionCellLine> productionCellLine;
  private List<PropagationHost> propagationHost;
  private List<TransmissionMethod> transmissionMethod;
  private List<Sequence> sequence;
  private String cultivability;
  private String clinicalInformation;
  private String identificationTechnique;
  private String infectivity;
  private String infectivityTest;
  private String isolationTechnique;
  private String isolationConditions;
  private String letterOfAuthority;
  private String passage;
  private String genomeSequencing;
  private String titer;

}