from django.test import TestCase

from articles.utils import slugify_instance_title

from .models import Article
from django.utils.text import slugify
# Create your tests here.

class ArticleTestCase(TestCase):
    def setUp(self):
        self.number_Of_Count = 5
        for i in range(self.number_Of_Count):
            Article.objects.create(title='Article Test Case',
            content="Article Content Test")

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(),self.number_Of_Count)
    
    def test_unique_same_slug(self):
        qs = Article.objects.exclude(slug__iexact="article-test-case")
        #obj = Article.objects.all().order_by("id").last()
        #title = obj.title
        for obj in qs:
            title = obj.title
            slug = obj.slug
            slugified = slugify(title)
            self.assertNotEqual(slug,slugified)

    def test_same_slug(self):
        qs = Article.objects.exclude(slug__iexact="article-test-case")
        obj = Article.objects.all().order_by("id").last()
        title = obj.title
        slug = obj.slug
        slugified = slugify(title)
        self.assertNotEqual(slug,slugified)

    def test_slugify_instance_title(self):
        obj = Article.objects.all().last()
        new_slugs = []
        for i in range(0, 5):
            instance = slugify_instance_title(obj, save=False)
            new_slugs.append(instance.slug)
        unique_slugs = list(set(new_slugs))
        self.assertEqual(len(new_slugs),len(unique_slugs))

    def test_slugify_instance_test_redux(self):
        slug_list = Article.objects.all().values_list('slug', flat=True)
        unique_slug_list = list(set(slug_list))
        self.assertEqual(len(slug_list),len(unique_slug_list))

    def test_article_search(self):
        qs = Article.objects.search(query="meta")
        self.assertEqual(qs.count(), self.number_Of_Count)

        qs = Article.objects.search(query="Blueprint")
        self.assertEqual(qs.count(), self.number_Of_Count)

        qs = Article.objects.search(query="UE4")
        self.assertEqual(qs.count(), self.number_Of_Count)


