from django.http import JsonResponse
from .tasks import test_task

def test_celery(request):
    """Тестовая вьюха для запуска задачи Celery"""
    result = test_task.delay()
    return JsonResponse({
        'status': 'Task submitted',
        'task_id': result.id
    })