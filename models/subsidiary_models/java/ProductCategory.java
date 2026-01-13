package None;

import java.util.List;
import lombok.*;



/* version: 1.0.10834 */


/**
  A term used to classify a group of products that share common characteristics or functions, which helps in their organization.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProductCategory extends Term {

  private ProductCategory parentCategory;

}