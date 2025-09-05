package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8966 */


/**
  An external API (Application Programming Interface) or Endpoint that permits to retrieve data from other sources
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DataProvider extends DataService {

  private License license;
  private String loginRequestMethod;
  private String loginUrl;
  private String loginTokenName;
  private String queryMethod;
  private String contentType;
  private Dataset providedEntityType;
  private int weight;

}