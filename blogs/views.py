from django.shortcuts import render, redirect
from .models import BlogPost, Subscribers
from .serailizers import BlogPostSerializer
from django.http import JsonResponse
from django.contrib import messages


# Create your views here.
def index(request):
    blogs = BlogPost.objects.all()
    serializer = BlogPostSerializer(blogs, many=True)
    # return JsonResponse(serializer.data, safe=False)
    return render(request, 'index.html', {'blogs': blogs})


def blog_post(request):

    if request.method == "POST":
        if request.user.is_authenticated:
            experience = request.POST.get('experience')
            image = request.FILES.get('image')
            place = request.get('place')
            rating = request.get('rating')
            posted_by = request.user
            
            blog = BlogPost(experience=experience, image=image, place=place, rating=rating, posted_by=posted_by)
            blog.save()

            messages.success(request, 'Posted successfully!')
            return redirect('/')
        
        else:
            return redirect('login')
        
    else:
        return redirect('/')


def subscribe(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        if name and email:
            subscriber, _ = Subscribers.objects.update_or_create(name=name, email=email)
            subscriber.save()
            
            messages.success(request, 'Subscribed!')
        
        else:
            messages.success(request, 'Please fields all the fields!')
    
    return redirect('/')
    