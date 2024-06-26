from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        message = data['message']
        response_data = {
            'message': f'Echo: {message}'
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=400)
