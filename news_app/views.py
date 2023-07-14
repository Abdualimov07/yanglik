from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from .models import News, Category, Comment
from django.shortcuts import get_object_or_404
from .forms import ContactForm, CommentForm
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q
from hitcount.views import HitCountDetailView, HitCountMixin
from hitcount.utils import get_hitcount_model
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
# from django.contrib.auth.mixins import LoginRequiredMixin
from news_project.custom_permissions import OnlyLoggedSuperUser
from django.contrib.auth.decorators import login_required, user_passes_test
from hitcount.models import HitCount
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def news_list(request):
    # news_list = News.objects.filter(status=News.Status.Published)
    news_list = News.objects.all()
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html", context=context)




def news_detail(request, id):
    news = get_object_or_404(News, id=id, status = News.Status.Published)
    comments = news.comments.filter(active=True)
    new_comment = None
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = news
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
            
        
    
    
    context = {}
    # hitcount logikasi 
    hit_count = get_hitcount_model().objects.get_for_object(news)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk':hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)

    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits    

    

    context = {
        'news': news,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }

    return render(request, "news/news_detail.html", context=context)


    
 



def HomePageView(request):
    news_list = News.objects.order_by('-publish_time')[:5]
    categories = Category.objects.all()
    local_news = News.objects.all().filter(category__name="Mahalliy").order_by('-publish_time')[1:6]
    last_local_news = News.objects.all().filter(category__name="Mahalliy").order_by('-publish_time')[:2]
    header_last_news = News.objects.all().order_by('-publish_time')[:5]
    technology_news = News.objects.all().filter(category__name="Texnologiya").order_by('-publish_time')[1:6]
    foreign_news = News.objects.all().filter(category__name="Xorij").order_by('-publish_time')[1:6]
    sport_news = News.objects.all().filter(category__name="Sport").order_by('-publish_time')[1:6]
    last_foreign_news = News.objects.all().filter(category__name="Xorij").order_by('-publish_time')[:1]
    last_technology_news = News.objects.all().filter(category__name="Texnologiya").order_by('-publish_time')[:1]
    last_sport_news = News.objects.all().filter(category__name="Sport").order_by('-publish_time')[:1]
    popular_news = News.objects.order_by('-views')[:5]

    context = {
        'news_list': news_list,
        'categories': categories,
        'local_news': local_news,
        'foreign_news': foreign_news,
        'technology_news': technology_news,
        'sport_news': sport_news,
        'last_local_news': last_local_news,
        'last_foreign_news': last_foreign_news,
        'last_technology_news': last_technology_news,
        'last_sport_news': last_sport_news, 
        'header_last_news': header_last_news,
        'popular_news': popular_news,
            
    }

    

    return render(request, 'news/index.html', context=context)

def ContactView(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return render(request, 'news/successfuly_contact.html')
    
    context = {
        'form': form
    }
    return render(request, 'news/contact.html', context=context)





def error_404_view(request, exception):
    return render(request, 'news/404.html', status=404)





def SinglePageView(request):
    return render(request, 'news/single_page.html')

class SearchResultList(ListView):
    model = News
    template_name = 'news/search_result.html'
    context_object_name = 'barcha_yangiliklar'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(
            Q(title__icontains = query) | Q(body__icontains=query)
        )


class LocalNewsView(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_yangiliklar'

    def get_queryset(self):
        news = super().get_queryset().filter(category__name='Mahalliy')
        return news
     
class ForiegnNewsView(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij_yangiliklar'    

    def get_queryset(self):
        news = super().get_queryset().filter(category__name='Xorij')
        return news

class TechnologyNewsView(ListView):
    model = News
    template_name = 'news/texnology.html'
    context_object_name = 'texnologiya_yangiliklar'  

    def get_queryset(self):
        news = super().get_queryset().filter(category__name='Texnologiya')
        return news

class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_yangiliklar'    

    def get_queryset(self):
        news = super().get_queryset().filter(category__name='Sport')
        return news
    

class NewsCreateView(OnlyLoggedSuperUser, CreateView):
    model = News
    template_name = 'news/news_create.html'
    fields = ('title', 'slug', 'body', 'image','category', 'status')
    login_url = "login"

class NewsEditView(OnlyLoggedSuperUser, UpdateView):
    model = News
    template_name = 'news/news_edit.html'
    fields = ('title',  'body', 'image', 'status')

    def get_success_url(self):
        return reverse('news_detail_page', kwargs={'id': self.object.id})

class NewsDeleteView(OnlyLoggedSuperUser, DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('home_page')  





@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    admin_users = User.objects.filter(is_superuser=True)
    context = {
        'admin_users': admin_users,
    }
    return render(request, 'pages/admin_page.html', context)





