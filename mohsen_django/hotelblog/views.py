from django.shortcuts import render
from .models import Cards
# Create your views here.
def index(request):
    card_1 = Cards()
    card_1.title = "dkasjdlkjalskjdlajsdlkajsdlka"
    card_1.img = "1.jpg"
    card_1.text="Dasdaskjdklasjdlkajskldjaskljdklsajkldjaskl dksajdklasjdlkasjlkdjaslk dklas jdklasj dklasjkldj askldjas"
    card_2 = Cards()
    card_2.title = "dasdadsad"
    card_2.img = "2.jpg"
    card_2.text="Dasdsadsajkdkjsahjk dasjkdhakjhdkjsah sadjhasdjsakjdhjka dajksdhaksdak"
    return render(request,"index.html",{"card_1":card_1,"card_2":card_2})