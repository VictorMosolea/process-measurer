import java.util.concurrent.Semaphore;

class ProducerConsumer {

    private Semaphore semProducer = new Semaphore(0);
    private Semaphore semConsumer = new Semaphore(1);
    public static int COUNTER = 0;
    void printEvenNum() {
        try {
            semProducer.acquire();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        COUNTER ++;
        semConsumer.release();
    }

    void printOddNum() {
        try {
            semConsumer.acquire();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        COUNTER ++;
        semProducer.release();

    }
}

class Producer implements Runnable {
    private ProducerConsumer sp;

    Producer(ProducerConsumer sp){
        this.sp = sp;
    }

    @Override
    public void run() {
        for (;;) {
            sp.printEvenNum();
        }
    }
}

class Consumer implements Runnable {
    private ProducerConsumer sp;

    Consumer(ProducerConsumer sp){
        this.sp = sp;
    }
    @Override
    public void run() {
        for (;;) {
            sp.printOddNum();
        }
    }
}

class thread_context {
    public static void main(String[] args) {
        ProducerConsumer sp = new ProducerConsumer();

        Thread producer = new Thread(new Consumer(sp),"producer");
        Thread consumer = new Thread(new Producer(sp),"consumer");

        producer.setDaemon(true);
        consumer.setDaemon(true);
        
        producer.start();
        consumer.start();
        try{
            Thread.sleep(1000);
        }catch(Exception e){

        }
        System.out.println(ProducerConsumer.COUNTER);
    }
}
