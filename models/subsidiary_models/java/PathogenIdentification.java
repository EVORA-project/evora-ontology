package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8369 */


/**
  A collection of distinguishing information that enables the differentiation of a pathogen from another
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PathogenIdentification extends Dataset {

  private Taxon taxon;
  private CommonName pathogenName;
  private String pathogenType;
  private List<String> hostType;
  private String subspecies;
  private String strain;
  private String isolate;
  private String genotype;
  private String serotype;
  private Variant variant;

}