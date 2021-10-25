from django.db import models
from django import forms

# Create your models here.

class Guestbook(models.Model):
    message = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)

class GuestbookForm(forms.ModelForm):
    class Meta:
        model = Guestbook
        fields = '__all__'
        excludes = {'date'}
        labels = {
            'message':'ช่องแสดงความคิดเห็น'
        }
        widgets = {
            'message':forms.Textarea(attrs={'row':'3'})     
        }


class Post(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    author=models.TextField()
    category= models.TextField()

    def __str__(self):
        return self.name+"/"+self.author+"/"+self.category
