from .models import Post, Tag
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q

class PostList(generic.ListView):

    template_name = "index.html"
    paginate_by = 3
    def get_queryset(self):
        #Situation 1 - A search query
        search_query = self.request.GET.get('search','')
        if search_query:
            return  Post.objects.filter(status=1).filter(title__icontains=query).order_by("-created_on")
        return Post.objects.filter(status=1).order_by("-created_on")



def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def list_posts_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)

    posts = Post.objects.filter(status=1, tags=tag)

    context = {
        "tag_name": tag.name,
        "post_list": posts
    }

    return render(request, "index.html", context)
