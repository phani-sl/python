# How to Start a Thread
# In Python, a thread is created using threading.Thread() and started with the start() method.
import threading

def worker():
    print("Thread is running...")

# Create a Thread
t = threading.Thread(target=worker)

# Start the Thread
t.start()

# Wait for thread to finish
t.join()


# How to Get the Thread Name
"""
Every thread has a name property (default: "Thread-1", "Thread-2", etc.).
We can:
Set a custom name while creating a thread → Thread(name="MyThread")
Get the current thread’s name → threading.current_thread().name
Get another thread’s name → t.name
"""
import threading

def worker():
    print(f"Current thread running: {threading.current_thread().name}")

# Create a Thread with a custom name
t = threading.Thread(target=worker, name="CustomWorkerThread")

t.start()
t.join()

# Get thread name from object
print("Thread object name:", t.name)