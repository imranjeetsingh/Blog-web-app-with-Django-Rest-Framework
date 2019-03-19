from urllib.parse import quote_plus

from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .forms import PostForm
from .models import Post
# Create your views here.

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request,"Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request,"Invalid data")
    context = {
        "form":form,
    }
    return render(request, "post_form.html",context)

def post_detail(request,slug=None):
    instance = get_object_or_404(Post,slug=slug)
    share_string = quote_plus(instance.content)
    context = {
        "instance":instance,
        "title" : "Detail",
        "share_string":share_string,
    }
    return render(request,"post_detail.html",context)

def post_list(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list,4)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    print(page)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    print(queryset)
    context = {
        "object_list": queryset,
        "title" : "Posts",
        "page_request_var":page_request_var,
    }
    return render(request,"post_list.html",context)

def post_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request,"successfully deleted the post")
    return redirect("posts:list")

def post_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None, request.FILES or None , instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.error(request,"suceessfully Updated data")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title":instance.title,
        "instance":instance,
        "form":form
    }
    return render(request,"post_form.html",context)