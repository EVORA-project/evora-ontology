package None;

import java.util.List;
import lombok.*;



/* version: 1.0.8773 */


/**
  A group of products
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Bundle extends Product {

  private List<Product> productsOfTheBundle;

}