package None;

import java.util.List;
import lombok.*;



/* version: 1.0.7785 */


/**
  A product or a service
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class ProductOrService extends NamedDataset {

  private String accessPointURL;
  private String refSKU;
  private String unitDefinition;
  private ProductCategory category;
  private List<ProductCategory> additionalCategory;
  private String unitCost;
  private String qualityGrading;
  private List<PathogenIdentification> pathogenIdentification;
  private List<DOI> relatedDOI;
  private RiskGroup riskGroup;
  private String biosafetyRestrictions;
  private boolean canItBeUsedToProduceGMO;
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