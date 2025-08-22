# Using threading.Thread() with a target function

import threading
import time

def worker():
    print("Thread started")
    time.sleep(2)
    print("Thread finished")

# Create thread
t = threading.Thread(target=worker)

# Start thread
t.start()

# Wait for thread to complete
t.join()

print("Main program finished")


# Using threading.Thread() with arguments
import threading

def greet(name):
    print(f"Hello, {name}!")

# Create thread with arguments
t = threading.Thread(target=greet, args=("Phani",))
t.start()
t.join()


# By Extending the Thread class
import threading

class MyThread(threading.Thread):
    def run(self):
        print("Thread is running")

# Create object of MyThread
t = MyThread()
t.start()
t.join()


# Using Daemon Threads
# Daemon threads run in the background and terminate when the main program exits.
import threading
import time

def background_task():
    while True:
        print("Running in background...")
        time.sleep(1)

t = threading.Thread(target=background_task, daemon=True)
t.start()

time.sleep(3)
print("Main program ends")