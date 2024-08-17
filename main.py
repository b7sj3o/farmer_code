import multiprocessing
import subprocess


def run_bot():
    subprocess.run(["python", "bot/main.py"])


def run_backend():
    subprocess.run(["python", "backend/main.py"])


def run_frontend():
    subprocess.run(["python", "frontend/main.py"])


if __name__ == "__main__":
    bot_process = multiprocessing.Process(target=run_bot)
    backend_process = multiprocessing.Process(target=run_backend)
    frontend_process = multiprocessing.Process(target=run_frontend)

    bot_process.start()
    backend_process.start()
    frontend_process.start()

    bot_process.join()
    backend_process.join()
    frontend_process.join()