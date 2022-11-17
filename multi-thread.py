import threading
import time


def task(i):
    print(f"Task {i} starts for {i + 1} second(s)")
    time.sleep(i + 1)
    print(f"Task {i} ends")


T = []
print(dir(T))  # affiche les caractéristiques de T

for i in range(100):
    T.append(threading.Thread(target=task, args=[i]))

for i in range(len(T)):
    T[i].start()

for i in range(len(T)):
    T[i].join()

"""Ce programme ferme chaque tâche après que 
 toutes les tâches aient fini d'être exécuté"""
