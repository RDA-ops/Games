
from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    """Модель игры. Хранит данные и JS-код."""
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    js_code = models.TextField(help_text="JavaScript код игры")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class HighScore(models.Model):
    """Модель для хранения рекордов."""
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='scores')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    score = models.IntegerField(default=0)
    achieved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return f"{self.user}: {self.score} in {self.game}"
