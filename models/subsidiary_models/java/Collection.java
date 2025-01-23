package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8305 */


/**
  Set of products and services with some common characteristics
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Collection extends Catalogue {

  private List<ProductOrService> collectionItem;
  private DataProvider collectionDataProvider;

}