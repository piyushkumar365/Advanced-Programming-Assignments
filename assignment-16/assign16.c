#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];
int count = 0;

pthread_mutex_t mutex;
sem_t empty, full;

// Producer function
void *producer(void *arg)
{
    int item;

    for(int i = 1; i <= 10; i++)
    {
        item = i;

        sem_wait(&empty); // wait if buffer full

        pthread_mutex_lock(&mutex);

        buffer[count] = item;
        count++;

        printf("Producer produced item %d\n", item);

        pthread_mutex_unlock(&mutex);

        sem_post(&full); // signal consumer

        sleep(1);
    }

    pthread_exit(NULL);
}

// Consumer function
void *consumer(void *arg)
{
    int item;

    for(int i = 1; i <= 10; i++)
    {
        sem_wait(&full); // wait if buffer empty

        pthread_mutex_lock(&mutex);

        count--;
        item = buffer[count];

        printf("Consumer consumed item %d\n", item);

        pthread_mutex_unlock(&mutex);

        sem_post(&empty); // signal producer

        sleep(1);
    }

    pthread_exit(NULL);
}

int main()
{
    pthread_t p1, c1;

    // Initialize mutex
    pthread_mutex_init(&mutex, NULL);

    // Initialize semaphores
    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);

    // Create threads
    pthread_create(&p1, NULL, producer, NULL);
    pthread_create(&c1, NULL, consumer, NULL);

    // Wait for threads
    pthread_join(p1, NULL);
    pthread_join(c1, NULL);

    // Destroy mutex and semaphores
    pthread_mutex_destroy(&mutex);
    sem_destroy(&empty);
    sem_destroy(&full);

    return 0;
}