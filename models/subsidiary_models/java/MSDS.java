package None;

import java.util.List;
import lombok.*;



/* version: 1.0.9137 */



@Data
@EqualsAndHashCode(callSuper=false)
public class MSDS  {

  private ContactPoint materialSafetyContact;
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