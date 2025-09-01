import threading
import time

# Function for the daemon thread
def background_task():
    while True:
        print("Daemon thread is running...")
        time.sleep(1)

# Create the thread
daemon_thread = threading.Thread(target=background_task)

# Set it as a daemon thread
daemon_thread.daemon = True  # or daemon_thread.setDaemon(True)

# Start the thread
daemon_thread.start()

# Main thread work
print("Main thread is running...")
time.sleep(3)
print("Main thread finished.")



import threading
import time

def log_messages():
    for i in range(10):
        print(f"Logging message {i}")
        time.sleep(1)

t = threading.Thread(target=log_messages)
t.daemon = True
t.start()

print("Main program doing work...")
time.sleep(3)
print("Main program finished.")



import threading
import time

def worker(name):
    while True:
        print(f"{name} working in background")
        time.sleep(2)

# Create multiple daemon threads
t1 = threading.Thread(target=worker, args=("Thread-1",))
t2 = threading.Thread(target=worker, args=("Thread-2",))

t1.daemon = True
t2.daemon = True

t1.start()
t2.start()

print("Main thread doing something...")
time.sleep(5)
print("Main thread finished.")



import threading
import time

def normal_task():
    for i in range(5):
        print(f"Normal task running {i}")
        time.sleep(1)

def daemon_task():
    while True:
        print("Daemon task running...")
        time.sleep(1)

# Normal thread
normal = threading.Thread(target=normal_task)

# Daemon thread
daemon = threading.Thread(target=daemon_task)
daemon.daemon = True

# Start threads
normal.start()
daemon.start()

normal.join()  # Wait for normal thread to finish
print("Main thread finished, daemon thread stops automatically.")