from django.shortcuts import render
from .models import *
from django.views.generic import View

# Create your views here.
class BaseView(View):
    views = {}

class HomeView(BaseView):
    def get(self, request):
        self.views['products'] = Product.objects.all()
        self.views['reviews'] = Review.objects.all()
#         self.views['sliders'] = Slider.objects.all()

        return render(request,'index.html',self.views)
      

  





