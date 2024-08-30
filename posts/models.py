from django.db import models
from django.conf import settings

class Post(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  post_image = models.ImageField(null=True, blank=True, upload_to="images/")
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
        return self.title
      
  def is_bookmarked_by(self, user):
        return Bookmark.objects.filter(post=self, user=user).exists()
      
class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'post']