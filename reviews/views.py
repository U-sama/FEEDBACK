from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import reviews

# Create your views here.

class ReviewView(CreateView):
    model = reviews
    template_name = "reviews/review.html"
    form_class = ReviewForm
    success_url = "/thank-you"


# class ReviewView(FormView):
#     template_name = "reviews/review.html"
#     form_class = ReviewForm
#     success_url = "/thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {"form":form})


#     def post(self,request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#         return render(request, "reviews/review.html", {"form":form})
    

class Thank_YouView(TemplateView):
    template_name = "reviews/Thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context
    
# class ReviewsListViews(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["reviews"] = reviews.objects.all()
#         return context

class ReviewsListViews(ListView):
    template_name = "reviews/review_list.html"
    model = reviews
    context_object_name = "reviews"

    #To make specific Query
    # def get_queryset(self):
    #     base_query =  super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data
    

# class ReviewDetailsView(View):
#     def get (self, request, slug):
#         review = get_object_or_404(reviews, id=slug)
#         return render(request, "reviews/review_details.html", {"review":review})
    
class ReviewDetailsView(DetailView):
    template_name = "reviews/review_details.html"
    model= reviews # We can access it throgh (object, modelName (lowered cased))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favourite_id = request.session.get["favourite_review"]
        context["is_favourite"] = favourite_id == str(loaded_review.id)
        return context
    

# class ReviewDetailsView(TemplateView):
#     template_name = "reviews/review_details.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         context["review"] = get_object_or_404(reviews, id=review_id)
#         return context
    

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favourite_review"] = review_id
        print()
        return HttpResponseRedirect(f"/reviews/{review_id}")
