from django.db import models

# Create your models here.

# описываем поля модели(обьявление)

# заголовок
# Описание
# дата создания
# дата обновления
# Цена
# Уместен ли торг?

class Advertisement(models.Model):
    # поле для загаловка
    title = models.CharField('заголовок', max_length=130)
    # описание
    description = models.TextField('описание')
    # цена
    price = models.DecimalField('цена', max_digits=14, decimal_places=2)
    # торг
    auction = models.BooleanField('торг', help_text='отметьте если торг уместен')
    # дата создания
    created_at = models.DateTimeField(auto_now_add=True)
    # дата обновления
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        db_table = 'advertisements'

    def __str__(self): 
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'