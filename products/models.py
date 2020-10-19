from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.CharField(max_length=1000, verbose_name="Описание")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_date = models.DateTimeField(verbose_name="Дата добавления", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Категории"
        verbose_name = "Категория"


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", null=True, blank=True,
                                 on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255, verbose_name="Название")
    price = models.FloatField(verbose_name="Цена", null=True, blank=True)
    count = models.IntegerField(verbose_name="Кол-во на складе")
    created_date = models.DateTimeField(verbose_name="Дата добавления", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Товары"
        verbose_name = "Товар"


# python manage.py makemigrations products
# python manage.py migrate
