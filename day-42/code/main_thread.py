# without join()
import threading
import time

def worker():
    print("Child thread starting...")
    time.sleep(2)
    print("Child thread finished!")

t = threading.Thread(target=worker)
t.start()

print("Main thread finished!")   # Main thread doesn’t wait here


# with join()
import threading
import time

def worker():
    print("Child thread starting...")
    time.sleep(2)
    print("Child thread finished!")

t = threading.Thread(target=worker)
t.start()

t.join()   # Main thread waits for child
print("Main thread finished after child thread!")


# multiple child threads with join
import threading
import time

def worker(name, delay):
    print(f"Thread {name} starting...")
    time.sleep(delay)
    print(f"Thread {name} finished!")

# Create multiple threads
t1 = threading.Thread(target=worker, args=("A", 2))
t2 = threading.Thread(target=worker, args=("B", 3))

# Start threads
t1.start()
t2.start()

# Main thread waits for both
t1.join()
t2.join()

print("Main thread finished after all child threads!")