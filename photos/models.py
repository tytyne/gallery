from django.db import models
import datetime as dt
# Create your models here.
   
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)


    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']   

class Location(models.Model):
    location_name= models.CharField(max_length =30,blank =True)
    location_slang = models.CharField(max_length =30)
    

    def __str__(self):
        return self.location_name
    class Meta:
        ordering = ['location_name']  

class Category(models.Model):
    category_name= models.CharField(max_length =30)
    category_slang = models.CharField(max_length = 10,blank =True)


    def __str__(self):
        return self.category_name
    class Meta:
        ordering = ['category_name']  



class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    location = models.ForeignKey(Editor)
    category= models.ForeignKey(Category,blank =True,null=True)
    editor = models.ManyToManyField(Location)
    pub_date = models.DateTimeField(auto_now_add=True)    
    article_image = models.ImageField(upload_to = 'articles/',blank=True)
    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        photos = cls.objects.filter(pub_date__date = today)
        return photos
    @classmethod
    def days_photos(cls,date):
        photos = cls.objects.filter(pub_date__date = date)
        return photos    
     

    @classmethod
    def save_image(self):
      self.save()  


    @classmethod
    def delete_image():
       photos.objects.filter(id=self.pk).delete()

  
    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__icontains=search_term)
        return photos
   
  
   
     
