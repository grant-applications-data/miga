package None;

import java.util.List;
import lombok.*;






/**
  Final score or score for a specific criterion, step, and/or reviewer.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ReviewScore  {

  private String reviewer;
  private Integer step;
  private String criterion;
  private float score;

}