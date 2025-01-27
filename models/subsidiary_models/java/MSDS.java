package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8373 */


/**
  A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MSDS extends Dataset {

  private ContactPoint msdsContact;
  private String physicalChemicalProperties;
  private String hazardsIdentification;
  private String firstAidMeasures;
  private String fireFightingMeasures;
  private String accidentalReleaseMeasures;
  private String handlingAndStorage;
  private String exposureControlsPersonalProtection;
  private String stabilityAndReactivity;
  private String toxicologicalInformation;
  private String ecologicalInformation;
  private String disposalConsiderations;
  private String transportInformation;
  private String regulatoryInformation;
  private String furtherInformation;

}