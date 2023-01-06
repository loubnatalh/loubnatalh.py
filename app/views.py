from django.http import HttpResponse
def home(request):
    return HttpResponse('bonjour à tous')

from django.shortcuts import render
from .models import dht
def dht11(request):
     tab = dht.objects.all()
     s = {'tab': tab}
     return render(request, 'tables.html', s)

     class EditorChartView(TemplateView):
         template_name = 'app/charts.html'
         def get_context_data(self, **kwargs):
             context = super().get_context_data(**kwargs)
             context["tab"] = Dht.objects.all()
             return context
