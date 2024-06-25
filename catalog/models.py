from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.CharField(
        max_length=100, verbose_name="Описание", help_text="Введите описаание продукта"
    )
    photo = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Вставте изображение продукта",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за покупку"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )
    # manufactured_at = models.DateTimeField(auto_now=True, verbose_name="Дата производства продукта")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]

    def __str__(self):
        return f"{self.name}, {self.description}, {self.price}"


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Введите категорию"
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описаание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}, {self.description}"


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Продукт",
    )
    version_number = models.CharField(max_length=50, verbose_name="Номер версии")
    version_name = models.CharField(max_length=150, verbose_name="Название версии")
    is_current = models.BooleanField(
        default=False, verbose_name="Признак текущей версия"
    )

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продукта"
        ordering = ["product"]

    def __str__(self):
        return f"{self.product.name} - {self.version_name} ({self.version_number})"
