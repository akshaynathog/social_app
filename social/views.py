from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, ListView, DetailView,UpdateView,View
from django.contrib.auth.models import User
from social.forms import RegistrationForm, LoginForm, PostsForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from social.models import Posts, Comments,User_detail
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.db.models import Count

# Create your views here.


def signin_required(fn):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "You must Login")
            return redirect("signin")
        else:
            return fn(request, *args, **kwargs)
    return wrapper

decorators=[signin_required,never_cache]


class SignUpView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "rgister2.html"
    success_url = reverse_lazy("signin")

    def form_valid(self, form):
        messages.success(self.request, "User Created Successfully")
        return super().form_valid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name: str = "login2.html"

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user = authenticate(request, username=uname, password=pwd)
            if user:
                login(request, user)
                print("success")
                return redirect("home")
            else:
                print("Fail")
                return render(request, self.template_name, {"form": form})


@method_decorator(decorators, name="dispatch")
class IndexView(CreateView, ListView):
    template_name: str = "index.html"
    form_class = PostsForm
    model = Posts
    success_url = reverse_lazy("my-posts")
    context_object_name: str = "posts"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Question Created Successfully")
        return super().form_valid(form)

    def get_queryset(self):
        return Posts.objects.all().exclude(user=self.request.user).order_by('-created_date')



decorators
def signout(request, *args, **kwargs):
    logout(request)
    return redirect("signin")

@method_decorator(decorators, name="dispatch")
class MyPostsView(CreateView, ListView):
    template_name: str = "myposts.html"
    form_class = PostsForm
    model = Posts
    success_url = reverse_lazy("my-posts")
    context_object_name: str = "posts"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Question Created Successfully")
        return super().form_valid(form)

    def get_queryset(self):
        return Posts.objects.filter(user=self.request.user).order_by('-created_date')


# localhost:8000/posts/1/comments/add

decorators
def add_comment(request, *args, **kwargs):
    post_id = kwargs.get("id")
    post = Posts.objects.get(id=post_id)
    com = request.POST.get("comment")
    post.comments_set.create(comment=com, user=request.user)
    return redirect("home")

decorators
def upvote_view(request, *args, **kwargs):
    com_id = kwargs.get("id")
    com = Comments.objects.get(id=com_id)
    com.up_vote.add(request.user)
    return redirect("home")

@method_decorator(decorators, name="dispatch")
class PostDetailView(DetailView):
    model = Posts
    template_name: str = "post-detail.html"
    pk_url_kwarg: str = "id"
    context_object_name: str = "post"
    # form_class=AnswersForm

@method_decorator(decorators, name="dispatch")
class ProfiledetailView(ListView):
    model=User
    template_name: str="Profile-detail.html"
    pk_url_kwarg: str = "id"
    context_object_name: str = "ptof"






    


class PostEditView(UpdateView):
    model= Posts
    form_class=PostsForm
    template_name: str="post-update.html"
    pk_url_kwarg: str="id"
    success_url= reverse_lazy("my-posts")

    def form_valid(self, form):
        # messages.success(self.request,"Post Updated")
        return super().form_valid(form)



class PostDeleteView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        Posts.objects.filter(id=id).delete()
        messages.success(request, "Post has been Deleted")
        return redirect("my-posts")


class CommentDeleteView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        Comments.objects.filter(id=id).delete()
        messages.success(request, "Comments has been Deleted")
        return redirect("my-posts")



