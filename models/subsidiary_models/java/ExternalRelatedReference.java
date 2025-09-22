package None;

import java.util.List;
import lombok.*;



/* version: 1.0.9877 */


/**
  A reference that permits to retrieve an item from an external provider
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExternalRelatedReference extends Resource {

  private String reference;
  private String referenceLabel;
  private String referenceProviderPrefix;
  private String referenceProviderName;

}