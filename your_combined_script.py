import os
import multiprocessing
from subprocess import Popen

def run_flask():
    os.system('gunicorn app:app')

def run_tg_bot():
    os.system('python tg.py')

if __name__ == "__main__":
    flask_process = multiprocessing.Process(target=run_flask)
    tg_process = multiprocessing.Process(target=run_tg_bot)

    flask_process.start()
    tg_process.start()

    flask_process.join()
    tg_process.join()
