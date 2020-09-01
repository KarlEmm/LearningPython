from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  content = models.TextField()
  date_added = models.DateTimeField(auto_now=True)

  def __str__(self):
    blogtitle = self.title.__str__()
    if len(blogtitle) > 50:
      return f"{blogtitle[:50]}..."
    else:
      return f"{blogtitle}"