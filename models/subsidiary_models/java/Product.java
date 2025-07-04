package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8773 */


/**
  A product
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Product extends ProductOrService {

  private IATAClassification hasIATAClassification;
  private String shippingConditions;
  private MSDS materialSafetyDataSheet;
  private Originator originator;
  private String storageConditions;
  private boolean thirdPartyDistributionConsent;
  private String usageRestrictions;

}