package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10623 */


/**
  Information on the origin of a natural part that composes the biological material.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NaturalPartOrigin extends BiologicalPartOrigin {

  private Country countryOfCollection;
  private IplcOrigin indigenousPeopleAndLocalCommunityOrigin;
  private ZonedDateTime collectionDate;
  private boolean beforeDate;
  private String permitIdentifierForAbs;

}