from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Author(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def _str_(self):
		return self.user.username

class Post(models.Model):
	title = models.CharField(max_length=200)
	test = models.TextField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	created_date = models.DateTimeField(auto_now_add=True)
	published_date = models.DateTimeField(auto_now_add=True)

	def _str_(self):
		return self.title


		