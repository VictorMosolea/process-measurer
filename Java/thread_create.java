class DummyThread implements Runnable {
    @Override
    public void run() {}
}
public class thread_create {
    public static void main(String[] args){
        int n = 100;
        int start_time, end_time;
        start_time = timing.time_in_microsec();
        for (int i = 0; i < n; i++){
           Thread t = new Thread(new DummyThread());
        }
        end_time = timing.time_in_microsec();

        System.out.println(end_time - start_time);
    }
}
