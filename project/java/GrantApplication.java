package None;

import java.util.List;
import lombok.*;






/**
  A research grant application.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GrantApplication  {

  private String piAge;
  private String piGender;
  private Integer applicationYear;
  private String grantScheme;
  private String discipline;
  private List<ReviewScore> scores;
  private boolean success;

}