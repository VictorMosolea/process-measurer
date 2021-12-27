import java.time.Instant;
import java.time.temporal.ChronoField;
import java.time.temporal.ChronoUnit;

public class timing {
    public static int time_in_microsec(){
        Instant now = Instant.now().truncatedTo(ChronoUnit.MICROS);
        return  now.get(ChronoField.MICRO_OF_SECOND);
    }
}
