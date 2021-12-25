import java.time.Instant;
import java.time.temporal.ChronoField;
import java.time.temporal.ChronoUnit;

class DummyThread implements Runnable {
    @Override
    public void run() {}
}


public class thread_create {

    public static int time_in_microsec(){
        Instant now = Instant.now().truncatedTo(ChronoUnit.MICROS);
       return  now.get(ChronoField.MICRO_OF_SECOND);
    }
    public static void main(String[] args){
        int n = 100;
        int start_time, end_time;
        start_time = thread_create.time_in_microsec();
        for (int i = 0; i < n; i++){
           Thread t = new Thread(new DummyThread());
        }
        end_time = thread_create.time_in_microsec();

        System.out.println(end_time - start_time);
    }
}
