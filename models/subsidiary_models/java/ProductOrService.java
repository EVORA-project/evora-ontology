package None;

import java.util.List;
import lombok.*;



/* version: 1.0.9888 */


/**
  An offering provided by a provider, which may be tangible (a product) or intangible (a service)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class ProductOrService extends Dataset {

  private String accessPointUrl;
  private String refSku;
  private String unitDefinition;
  private ProductCategory category;
  private List<ProductCategory> additionalCategory;
  private BigDecimal unitCost;
  private String unitCostCurrency;
  private String unitCostNote;
  private String qualityGrading;
  private List<PathogenIdentification> pathogenIdentification;
  private List<Doi> doi;
  private RiskGroup riskGroup;
  private String biosafetyRestrictions;
  private boolean canBeUsedToProduceGmo;
  private Provider provider;
  private List<Collection> collection;
  private List<Keyword> keywords;
  private String availability;
  private List<Document> complementaryDocument;
  private String technicalRecommendation;
  private List<Image> productPicture;
  private List<ExternalRelatedReference> externalRelatedReference;
  private List<Certification> certification;
  private String internalReference;
  private String note;
  private ContactPoint contactPoint;

}