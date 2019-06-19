from django.contrib.syndication.views import Feed
from .models import Post

class AllPostsRssFeed(Feed):
    title = "Django"
    link = "/"
    description = "Django"
    def items(self):
        return Post.objects.all()
    def item_little(self, item):
        return '[%s] %s' % (item.category, item.little)
    def item_description(self, item):
        return item.body