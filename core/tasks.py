from celery import shared_task
import time

@shared_task
def test_task():
    print("Задача Celery выполняется...")
    time.sleep(5)  # Имитация долгой работы
    print("Задача Celery завершена!")
    return "Success"