Producer-Consumer Application Using Threading and Multiprocessing

**1. Objective**

To develop a simple Producer-Consumer application using Python Threading, Multiprocessing, and Queue synchronization.

The program demonstrates how a Producer creates data and a Consumer receives the data concurrently.

**2. Input**

The program does not take input from the user.

The Producer automatically generates numbers from 1 to 5 and places them into a Queue.

**3. Output**

The program displays the values produced and consumed using:

Threading
Multiprocessing

Example:

THREADING
Produced: 1
Consumed: 1
Produced: 2
Consumed: 2
Produced: 3
Consumed: 3
Produced: 4
Consumed: 4
Produced: 5
Consumed: 5

MULTIPROCESSING
Produced: 1
Consumed: 1
Produced: 2
Consumed: 2
Produced: 3
Consumed: 3
Produced: 4
Consumed: 4
Produced: 5
Consumed: 5

Completed

The exact order of Produced and Consumed messages may vary because threads and processes execute concurrently.

**4. Algorithm**

Step 1

Import the required modules:

threading

multiprocessing

queue

Step 2

Create a producer() function.

The Producer generates numbers from 1 to 5 and inserts them into the Queue using put().

Step 3

After producing all values, the Producer inserts None into the Queue.

None acts as a termination signal to tell the Consumer that production is finished.

Step 4

Create a consumer() function.

The Consumer gets values from the Queue using get().

Step 5

If the Consumer receives None, it stops execution.

Otherwise, it prints the consumed value.

Step 6

Create two Threads:

Producer Thread
Consumer Thread

Start them using start() and wait for completion using join().

Step 7

Create two Processes:

Producer Process
Consumer Process

Start them and wait for completion.

Step 8

Display the completion message.

5. Important Terms Used
Thread

A thread is a small unit of execution inside a program.

threading.Thread(...)

It allows the Producer and Consumer to execute concurrently.

Multiprocessing

Multiprocessing creates separate processes to perform tasks concurrently.

multiprocessing.Process(...)

Unlike threads, processes have separate memory spaces.

Producer

The Producer creates data.

def producer(q):
    for i in range(1, 6):
        q.put(i)

Here, the Producer generates numbers from 1 to 5.

Consumer

The Consumer receives and processes the data.

def consumer(q):
    while True:
        x = q.get()

It continuously gets values from the Queue.

Queue

A Queue is a data structure used to store and exchange data between Producer and Consumer.

q = queue.Queue()

It follows FIFO (First In, First Out).

Example:

Put:     1 → 2 → 3

Get:     1 → 2 → 3

put()

put() adds an item to the Queue.

q.put(i)
get()

get() removes and returns an item from the Queue.

x = q.get()
None

None is used as a termination signal.

q.put(None)

When the Consumer receives None, it knows that the Producer has finished.

start()

Starts a Thread or Process.

t1.start()

p1.start()

join()

Makes the main program wait until the Thread or Process finishes.

t1.join()

p1.join()

Synchronization

Synchronization means controlling concurrent operations so that data is exchanged safely and correctly.

In this program, the Queue provides safe communication between the Producer and Consumer.

Concurrent Execution

Concurrent execution means multiple tasks can make progress during the same period.

Here:

Producer ──┐
           ├──> Queue
Consumer ──┘

The Producer and Consumer work concurrently.

**6. Time Complexity**

Let N be the number of items produced.

The Producer processes N items and the Consumer processes N items.

Therefore:

Time Complexity = O(N)

For this program, N = 5.

**7. Space Complexity**

The Queue stores produced items temporarily.

Therefore:

Space Complexity = O(N)

In the program, the Queue can contain the produced values before they are consumed.

Threads and Processes also require some additional system memory, but the algorithmic auxiliary space is O(N).

**8. Advantages**

Simple implementation of the Producer-Consumer problem.

Demonstrates Threading.

Demonstrates Multiprocessing.

Uses Queue for synchronization.

Shows concurrent execution.

No external libraries are required.
9. Result

The Producer-Consumer application was successfully implemented using Python Threading, Multiprocessing, and Queue synchronization.
