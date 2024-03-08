from django.shortcuts import render
from .models import Coffee
from .forms import CoffeeForm

from datetime import datetime

# Create your views here.
def self_introduction(req):
    return render(
        req,
        'main.html',
        {
            'name' : '임동주',
            'age' : 32,
            'hobby' : 'Badminton',
            'prefer' : 'Dog and Cat',
            'MBTI' : 'ENTP'
        }
    )


def manage_coffee(req):
    coffee_list = Coffee.objects.all()

    if req.method == 'POST':
        form = CoffeeForm(req.POST)
        if form.is_valid():
            cof = form.save(commit=False)
            cof.create_date = datetime.now()
            cof.save()

    return render(
        req,
        'coffees.html',
        {
            'coffee_list' : coffee_list,
            'coffee_form' : form,
        }
    )