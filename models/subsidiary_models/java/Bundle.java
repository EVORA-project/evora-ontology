package None;

import java.util.List;
import lombok.*;



/* version: 1.0.9808 */


/**
  A grouping of products and/or services intentionally combined into a single offering, typically to provide added value, convenience, or specific experimental utility
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Bundle extends Product {

  private List<Product> itemsOfTheBundle;

}