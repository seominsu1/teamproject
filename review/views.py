from django.db.models import Q
from django.shortcuts import render, redirect
from review.models import Review
from review.forms import ReviewForm

def register(request):
    if request.method == "GET":
        reviewForm = ReviewForm()
        return render(request, 'review/revw_register.html', {'reviewForm': reviewForm})
    elif request.method == "POST":
        reviewForm = ReviewForm(request.POST)
        if reviewForm.is_valid():
            review = reviewForm.save(commit=False)
            review.writer=request.user
            review.save()
            return redirect('/reviewRegister')

def posts(request):
    posts = Review.objects.all()
    return render(request, 'review/revw_list.html', {'posts': posts})

def read(request, bid):
    post = Review.objects.get(Q(id=bid))
    return render(request, 'review/revw_read.html', {'post': post})

def delete(request, bid):
    post = Review.objects.get(Q(id=bid))
    post.delete()
    return redirect('/reviewList')