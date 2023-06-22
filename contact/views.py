from django.shortcuts import render, redirect
from profiles.models import Profile
from .forms import ContactForm


def contact(request):
    try:
        profile = Profile.objects.get(user_id=request.user.id)
    except:
        profile = None
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog-list')
    ctx = {
        'profile': profile,
        'form': form
    }
    return render(request, 'contact/contact.html', ctx)
