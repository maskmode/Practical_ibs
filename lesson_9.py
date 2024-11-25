import threading
import time

def countdown(thread_name):
    print(f"Поток {thread_name} начал выполнение")
    for i in range(10, 0, -1):
        print(f"{thread_name}: {i}")
        time.sleep(1)
    print(f"Поток {thread_name} завершил выполнение")

thread1 = threading.Thread(target=countdown, args=("Поток-1",))
thread2 = threading.Thread(target=countdown, args=("Поток-2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Все потоки завершены")
