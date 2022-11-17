"""créer le téléchargement en parallèle de photos sur 3 codes différents avec thread,
 multiprocessing et pool de thread.
Calculer des statistiques sur les téléchargements, il faut donc répéter les téléchargements"""
import threading
import time
from threading import Thread

import requests
import concurrent.futures
import statistics

img_urls = [
    "https://cdn.pixabay.com/photo/2022/10/31/18/44/spider-web-7560535_960_720.jpg",
    "https://cdn.pixabay.com/photo/2022/10/25/13/28/hanoi-7545860_960_720.jpg"
]


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[9]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")


T = []

def method1():  # threading
   t1 = threading.Thread(target=download_image, args=[1])
   t1.start()

    t2 = threading.Thread(target=download_image, args=[2])
    t2.start()

def method2():  # pool thread
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)


def method3():  # multiprocessing
    for i in range(100):
        T.append(threading.Thread(target=download_image, args=[i]))

    for i in range(len(T)):
        T[i].start()

    for i in range(len(T)):
        T[i].join()
