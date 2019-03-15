from django.test import TestCase
import datetime as dt
# Create your tests here.
from .models import Editor,Article,tags

class EditorTestClass(TestCase):

# Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))
# Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()


class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
    def test_get_photos_today(self):
        today_photos = Article.todays_photos()
        self.assertTrue(len(today_photos)>0)

    def test_get_photos_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        photos_by_date = Article.days_photos(date)
        self.assertTrue(len(photos_by_date) == 0)                
