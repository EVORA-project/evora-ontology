package None;

import java.util.List;
import lombok.*;



/* version: 1.0.7897 */


/**
  A reference that permits to retrieve an item from an external provider
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExternalRelatedReference extends Dataset {

  private String reference;
  private String referenceLabel;
  private String referenceProviderPrefix;
  private String referenceProviderName;

}