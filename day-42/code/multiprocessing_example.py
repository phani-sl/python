import multiprocessing
import os

def worker():
    print(f"Worker process running with PID: {os.getpid()}")

if __name__ == "__main__":
    # Create a new process
    p = multiprocessing.Process(target=worker)
    p.start()   # Start the process
    p.join()    # Wait for process to finish

    print("Main process finished.")
