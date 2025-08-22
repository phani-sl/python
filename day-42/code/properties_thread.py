# Setting and Getting name
import threading

def task():
    print(f"Running thread: {threading.current_thread().name}")

t = threading.Thread(target=task, name="MyCustomThread")
t.start()
t.join()


# join()
import threading, time

def long_task():
    time.sleep(5)
    print("Task finished")

t = threading.Thread(target=long_task)
t.start()

t.join(timeout=2)  # wait only 2 seconds
print("Main program continues (didn’t wait full 5 sec)")