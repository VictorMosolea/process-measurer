#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <pthread.h>
#include <sys/time.h>
#include <unistd.h>

uint64_t COUNTER;
pthread_mutex_t LOCK;
pthread_mutex_t START;
pthread_cond_t CONDITION;

void *thread_func(void * unused){
    // wait till we may fire away
    pthread_mutex_lock(&START);
    pthread_mutex_unlock(&START);

    pthread_mutex_lock(&LOCK);

    // if not first thread, then signal the second
    if (COUNTER > 0) 
        pthread_cond_signal(&CONDITION);
    
    while(1){
        COUNTER++;
        pthread_cond_wait(&CONDITION, &LOCK);
        pthread_cond_signal(&CONDITION);
    }
}

int main(int argc,char ** argv){
    int64_t start;
    pthread_t t1, t2;
    uint64_t start_time, end_time;

    pthread_mutex_init(&LOCK, NULL);
    pthread_mutex_init(&START, NULL);   
    pthread_cond_init(&CONDITION, NULL);

    pthread_mutex_lock(&START);

    COUNTER = 0;

    pthread_create(&t1, NULL, thread_func, NULL);
    pthread_create(&t2, NULL, thread_func, NULL);

    pthread_detach(t1);
    pthread_detach(t2);

    // get start time and fire away
    pthread_mutex_unlock(&START);

    // Wait for about a second
    sleep(1);

    // Stop both threads
    pthread_mutex_lock(&LOCK);


    printf("Number of thread switches in about one second was %lu\n", COUNTER);
    return 0;
}