# your_app/views.py
import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .models import HealthData
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
@method_decorator(csrf_exempt, name='dispatch')
class PostHealthDataView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        temperature = data.get('temperature')
        bpm = data.get('bpm')
        try:
            latest_data = HealthData.objects.latest('timestamp')
            latest_data.temperature = temperature
            latest_data.bpm = bpm
            latest_data.timestamp = datetime.datetime.now()
            latest_data.save()
        except HealthData.DoesNotExist:
            HealthData.objects.create(temperature=temperature, bpm=bpm)
        return JsonResponse({'status': 'success'})

def get_latest_data(request):
    try:
        latest_health_data = HealthData.objects.latest('timestamp')
        data = {
            'temperature': latest_health_data.temperature,
            'bpm': latest_health_data.bpm,
            'timestamp': latest_health_data.timestamp.strftime('%Y-%m-%d %H:%M:%S'),  # Format timestamp as needed
        }
    except HealthData.DoesNotExist:
        data = {
            'temperature': '',
            'bpm': '',
            'timestamp': '',
        }

    return JsonResponse(data)

class DisplayDataView(LoginRequiredMixin,TemplateView):
    template_name = 'display_data.html'

    
