from django.db import models
from django.contrib import admin


# Posts

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)
    parent = models.ForeignKey('self', null=True, related_name='replies')

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))


### Admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]

admin.site.register(Comment, CommentAdmin)

# class Thread(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Comment(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
