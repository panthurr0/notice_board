from django.db import models

NULLABLE = {"blank": True, "null": True}


class Advertisement(models.Model):
    title = models.CharField(
        verbose_name="Название товара",
        max_length=70
    )
    author = models.ForeignKey(
        "users.User",
        verbose_name="Создатель объявления",
        on_delete=models.SET_NULL,
        **NULLABLE
    )
    price = models.IntegerField(
        verbose_name="Цена товара", **NULLABLE
    )
    description = models.TextField(
        verbose_name="Описание товара", **NULLABLE
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Review(models.Model):
    text = models.TextField(
        verbose_name="Текст отзыва", **NULLABLE
    )
    author = models.ForeignKey(
        "users.User",
        verbose_name="Автор отзыва",
        on_delete=models.SET_NULL,
        **NULLABLE
    )
    ad = models.ForeignKey(
        Advertisement,
        verbose_name="Объявление",
        on_delete=models.SET_NULL,
        **NULLABLE
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True
    )

    def __str__(self):
        return f"{self.author}: {self.text[:10]}..."

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
