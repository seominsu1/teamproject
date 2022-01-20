from django.shortcuts import render, redirect

# Create your views here.
from restaurant.forms import BoardForm


def register(request):
    if request.method == 'GET' :
        boardForm = BoardForm()
        return render(request, 'register.html', {'boardForm':boardForm})
    elif request.method == 'POST':
        boardForm = BoardForm(request.POST)
        if boardForm.is_valid():
            board = boardForm.save(commit=False)
            board.save()
            return redirect('/register')

