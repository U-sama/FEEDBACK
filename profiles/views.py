from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ProfileForm
from .models import UserProfile
# Create your views here.

class CreateProfileView(CreateView):
    model = UserProfile
    fields = "__all__"
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"

# def store_file(file):
#     with open(f"temp/{file.name}", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()

#         return render(request, "profiles/create_profile.html", {"form":form})

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)

#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES["user_file"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
        
#         return render(request, "profiles/create_profile.html", {"form":submitted_form})


class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profile.html"
    context_object_name = "profiles"

