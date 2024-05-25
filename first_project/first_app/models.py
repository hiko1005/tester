from django.db import models

# Create your models here.

class Site(models.Model):
    label = models.CharField(max_length=255, null=False, verbose_name="Назва сайту")
    url = models.URLField(null=False, verbose_name="Посилання сайту")
    description = models.CharField(max_length=255, null=True, verbose_name="Опис сайту")
    expected_responce_code = models.CharField(max_length=200, null=True, verbose_name="Очікувана відповідь")
    expected_responce_code_pattern = models.CharField(max_length=200, null=True, verbose_name="Заготовка відповіді")
    cheking_active = models.BooleanField(default=True, verbose_name="Перевірка")
    inversive_condition = models.BooleanField(default=True, verbose_name="Інверсія умов")
    cron_schedule = models.CharField(max_length=255, default="* * * * *", verbose_name="Розклад перевірки", help_text="формат crontab")
    last_checked = models.DateTimeField(null=True)
    is_alive = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Сайт"
        verbose_name_plural = "Сайти"

class Contact(models.Model): 
    label = models.CharField(max_length=255, null=False, verbose_name="Назва контакту")
    contact_string = models.CharField(max_length=255, null=False, verbose_name="Контакт")
    is_active = models.BooleanField(default=True, verbose_name="Перевірка")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакти"


class MailingService(models.Model):

    TYPE_CHOICES = (
        ('EMAIL', 'e-mail'),
        # ('TELEGRAM', 'Telegram'),
        ('CUSTOM', 'Custom')
    )

    BODY_FORMAT = (
        ('JSON', 'JSON'),
        ('XML', 'XML'),
        ('PLAIN TEXT', 'PLAIN TEXT')
    )

    label = models.CharField(max_length=255, null=False, verbose_name="Назва сервісу")
    type = models.CharField(choices=TYPE_CHOICES, max_length=255, null=False, verbose_name="Тип сповіщення")
    token = models.CharField(max_length=255, null=False, verbose_name="Токен")
    message_pattern = models.TextField(null=False, verbose_name="Текст сповіщення")
    is_active = models.BooleanField(default=True, verbose_name="Перевірка")
    login = models.CharField(max_length=255, null=True, verbose_name="Логін")
    password = models.CharField(max_length=255, null=True, verbose_name="Пароль")
    headers = models.TextField(null=True, verbose_name="HTTP заголовки")
    api_url = models.CharField(max_length=255, null=True, verbose_name="Посилання АПІ")
    request_type = models.CharField(max_length=255, null=True, verbose_name="Тип запиту")
    body_pattern = models.TextField(null=True, verbose_name="Заготівка тіла запиту")
    body_format = models.CharField(max_length=255, null=False, verbose_name="Тип передачі тіла", default="JSON", choices = BODY_FORMAT)

    class Meta:
        verbose_name = "Сервіс розсилки"
        verbose_name_plural = "Сервіси розсилки"

class MailingList(models.Model):
    label = models.CharField(max_length=255, null=False, verbose_name="Назва")
    is_active = models.BooleanField(default=True, verbose_name="Перевірка")
    contacts = models.ManyToManyField("Contact", related_name="mailing_list", verbose_name="Контакти")
    mailing_services = models.ManyToManyField("MailingService", related_name="mailing_lists", verbose_name="Сервіси сповіщення")
    sites = models.ManyToManyField("Site", related_name="mailing_lists", verbose_name="Сайти")

    class Meta:
        verbose_name = "Список розсилки"
        verbose_name_plural = "Списки розсилки"
