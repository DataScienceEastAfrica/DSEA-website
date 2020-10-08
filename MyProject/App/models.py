from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mdeditor.fields import MDTextField
from PIL import Image


class Post(models.Model):
	cover_image = models.FileField(upload_to='ArticlePics')
	title = models.CharField(max_length=100)
	content = MDTextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	# def save(self,*args, **kwargs):
	# 	super().save(*args,**kwargs)
	# 	image= Image.open(self.cover_image.path)
	# 	if image.width > 4000 or image.height > 100:
	# 		output_img = (4000, 100)
	# 		image.thumbnail(output_img)
	# 		image.save(self.cover_image.path)


		
		

    
 # for profile picture
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	image = models.ImageField(default = 'avartar.jpg', upload_to='ProfilePics')
	

	def __str__(self):
		return f"{self.user.username} profile"

	def save(self, *args,**kwargs):
		super().save(*args,**kwargs)
		img = Image.open(self.image.path)
		if img.width >300 or img.height >300:
			img_output = (300,300)
			img.thumbnail(img_output)
			img.save(self.image.path)
			

 # end of the profile Picture   
    
    

        

    
        




    
    
    
    
    
    

    
        

    
        
