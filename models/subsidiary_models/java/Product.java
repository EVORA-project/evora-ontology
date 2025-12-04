package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10806 */


/**
  A tangible, physical item made available by a provider for use, consumption, or ownership transfer.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Product extends ProductOrService {

  private IataClassification iataClassification;
  private String shippingConditions;
  private MaterialSafetyDataSheet materialSafetyDataSheet;
  private Originator originator;
  private String storageConditions;
  private boolean thirdPartyDistributionConsent;
  private String usageRestrictions;
  private String preparationTechnique;

}