import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

VERIFY_TOKEN = "123"


@csrf_exempt
def webhook(request):
    print(request)
    if request.method == 'GET':
        token_sent = request.GET.get('hub.verify_token')
        if token_sent == VERIFY_TOKEN:
            return HttpResponse(request.GET.get('hub.challenge'))
        return HttpResponse('Invalid verification token', status=403)

    elif request.method == 'POST':
        print(request)
        try:
            data = json.loads(request.body.decode('utf-8'))
            # Processar os dados recebidos aqui
            print(data)
            return JsonResponse({'status': 'success'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)
