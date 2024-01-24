import threading
import multiprocessing
import concurrent.futures

def print_numbers():
    for i in range(1, 6):
        print(i)


"""
Points to Note
Global Interpreter Lock (GIL): Python's GIL means that in CPython (the standard Python implementation), only one thread can execute Python bytecodes at a time. This makes threading beneficial mostly for I/O-bound tasks rather than CPU-bound tasks. For CPU-bound tasks, consider using multiprocessing or concurrent.futures.ProcessPoolExecutor for parallel execution.
Thread Safety: When using threads, be cautious about data sharing and synchronization. Shared data may require locking mechanisms (like threading.Lock) to prevent data corruption or inconsistency.
Daemon Threads: By default, Python waits for all non-daemon threads to complete before it exits. You can make a thread a daemon by setting thread.daemon = True before starting it. Python will not wait for daemon threads to complete before exiting.
Handling Exceptions: Exceptions in threads do not affect other threads. It's important to catch and handle exceptions within each thread.
"""
def thread_example():
    # Creating a thread
    thread = threading.Thread(target=print_numbers)

    # Starting the thread
    thread.start()

    # Waiting for the thread to complete
    thread.join()

    print("Thread finished execution")

def multiprocessing_example():
    # Create a process
    process = multiprocessing.Process(target=print_numbers)

    # Start the process
    process.start()

    # Wait for the process to complete
    process.join()

    print("Process finished execution")


"""
Points to Note
Overhead: Creating processes has more overhead than creating threads. It's beneficial for CPU-bound tasks but might be less efficient for I/O-bound tasks.
Data Sharing: Sharing data between processes is more complex than with threads, as each process has its own memory space. When necessary, you can use IPC (Inter-Process Communication) methods like queues or pipes.
Global State: Since each process has its own Python interpreter and memory space, changes made in the global state of one process do not affect the others.
"""
def concurrent_futures_example():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Submit the function to be executed in a separate process
        future = executor.submit(print_numbers)

        # Wait for the function to complete and get the result
        result = future.result()

    print("Concurrent Futures Process finished execution")

if __name__ == '__main__':
    thread_example()
    multiprocessing_example()
    concurrent_futures_example()