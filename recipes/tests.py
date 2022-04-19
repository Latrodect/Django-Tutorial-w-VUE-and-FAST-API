from unicodedata import name
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Recipe, RecipeIngredient
# Create your tests here.

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('root', password='171219Bercin.')
        
    def test_password(self):
        pwd = "171219Bercin."
        password_bool = self.user_a.check_password(pwd)
        self.assertTrue(password_bool)

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a =User.objects.create_user('root',password='171219Bercin.')
        self.recipe_a = Recipe.objects.create(
            name = "Grilled Chicken",
            user = self.user_a
        ) 
        self.recipe_b = Recipe.objects.create(
            name="Grilled Chicken Tacos",
            user=self.user_a
        )
        self.recipe_ingredient_a = RecipeIngredient.objects.create(
            recipe = self.recipe_a,
            name="Grilled Chicken",
            quantity="1/2",
            unit="poungs"

        )

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(),1)

    def test_user_recipe_reverse_count(self):
        user = self.user_a
        qs = user.recipe_set.all()
        self.assertEqual(qs.count(),2)

    def test_user_recipe_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)
        self.assertEqual(qs.count(),2)

    def test_recipe_ingredient_reverse_count(self):
        recipe = self.recipe_a
        qs = recipe.recipeingredient_set.all()
        self.assertEqual(qs.count(),1)

    def test_recipe_ingredient_forward_count(self):
        recipe = self.recipe_a
        qs = RecipeIngredient.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(),1)

    def test_user_two_level_relation(self):
        user = self.user_a
        qs = RecipeIngredient.objects.filter(recipe__user=user)
        self.assertEqual(qs.count(),1)

    def test_user_two_level_relation_reverse(self):
        user = self.user_a
        recipeingredient_ids = list(user.recipe_set.all()
        .values_list('recipeingredient__id', flat=True))
        qs = RecipeIngredient.objects.filter(id__in=recipeingredient_ids)
        self.assertEqual(qs.count(), 1)

    def test_user_two_level_relation_via_reverse(self):
        user = self.user_a
        ids = user.recipe_set.all().values_list("id", flat=True)
        qs = RecipeIngredient.objects.filter(id__in=ids)
        self.assertEqual(qs.count(), 1)