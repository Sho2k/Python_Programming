"""Program 58: Multithreading"""

import threading
import time

def print_task(task_name):
    for step in range(1, 4):
        print(f"{task_name}: step {step}")
        time.sleep(0.2)

first_thread = threading.Thread(target=print_task, args=("Task A",))
second_thread = threading.Thread(target=print_task, args=("Task B",))

first_thread.start()
second_thread.start()

first_thread.join()
second_thread.join()

print("Both tasks completed.")
