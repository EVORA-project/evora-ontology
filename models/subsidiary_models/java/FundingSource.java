package None;

import java.util.List;
import lombok.*;



/* version: 1.1.4 */


/**
  A program, grant, or project providing financial support for the access or use of a product or service, either fully or partially.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FundingSource extends Resource {

  private String title;
  private String description;
  private String fundingProgram;
  private String grantNumber;
  private Organization funder;
  private LocalDate fundingPeriodStart;
  private LocalDate fundingPeriodEnd;
  private String eligibilityCriteria;
  private Image logo;

}