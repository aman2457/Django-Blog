from django.core.exceptions import PermissionDenied
from .models import Post

def user_is_blog_post_user(function):
    def wrap(request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        if post.user == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap