from django.shortcuts import render
from .models import Cards
# Create your views here.
def index(request):
    card_1 = Cards()
    card_1.title = "dkasjdlkjalskjdlajsdlkajsdlka"
    card_1.img = "1.jpg"
    card_1.text="Dasdaskjdklasjdlkajskldjaskljdklsajkldjaskl dksajdklasjdlkasjlkdjaslk dklas jdklasj dklasjkldj askldjas"
    return render(request,"index.html",{"card_1":card_1})