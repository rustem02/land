from django.db import models
from uuid import uuid4


# Create your models here.



class ShortQuestionaire(models.Model):
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата записи')
    company_contact_phone = models.CharField(max_length=255,
                                             blank=False,
                                             verbose_name='Телефон')
    email = models.EmailField(blank=False,
                              verbose_name='Email заявителя')
    fio = models.CharField(max_length=255,
                           verbose_name='Фамилия Имя')
    inn = models.CharField(blank=False,
                           max_length=255,
                           verbose_name="ИНН")
    secret = models.UUIDField(default=uuid4,
                              # editable=False
                              )
    secret_used = models.BooleanField(default=False,
                                      verbose_name='Секретный код использован')


class Questionaire(models.Model):
    short_version = models.ForeignKey(ShortQuestionaire,
                                      on_delete=models.PROTECT,
                                      null=True,
                                      verbose_name='Начальная заявка')
    choices = ((True, 'Да'), (False, 'Нет'),)
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата записи')

    short_opisanie = models.TextField(blank=False,
                                       verbose_name="Краткое описание Вашего бизнеса")

    skolko_na_rynke = models.TextField(blank=False,
                                        verbose_name="Сколько лет на рынке\ из них на рынке автоматизации?")

    company_partners = models.TextField(blank=False,
                                        verbose_name="С какими фирмами (поставщиками, брэндами) по частотному приводу, мотор-редукторам, датчикам сотрудничаете и как долго?")

    company_personal = models.TextField(blank=False,
                                        verbose_name="Количество сотрудников \ из них продавцов \ из них инженеров в фирме ?")

    company_has_filial = models.BooleanField(verbose_name='Есть ли у Вашего предприятия филиалы в других регионах РФ? ')

    company_destination_activity = models.TextField(blank=False,
                                                    verbose_name="В каких отраслях промышленности Вы наиболее активны? ")


    prom_kipia = models.BooleanField(verbose_name='Промышленная автоматика и КИПиА, в т.ч.')
    non_contact = models.BooleanField(verbose_name='Бесконтактные датчики')
    optical = models.BooleanField(verbose_name='Оптические датчики')
    indikator = models.BooleanField(verbose_name='Управление и индикация')
    temperature = models.BooleanField(verbose_name='Датчики давления и температуры')
    ibp = models.BooleanField(verbose_name='Блоки питания')
    encoder = models.BooleanField(verbose_name='Энкодеры')
    converter = models.BooleanField(verbose_name='Частотные преобразователи')
    motor_reductor = models.BooleanField(verbose_name='Мотор-редукторы и электродвигатели')
    baumer = models.BooleanField(
        verbose_name='Датчики Baumer (Швейцария/Германия): оптические, лазерные, ультразвуковые, касания, индуктивные, емкостные')
    process_baumer = models.BooleanField(
        verbose_name='Датчики процессов для пищевых производств Baumer (уровня, давление, температуры, концентрации) в пищевом исполнении')
    cement_pesok_zerno = models.BooleanField(
        verbose_name='Датчики уровня сыпучих материалов (песок, цемент, зерно, комбикорм)')
    convair_security = models.BooleanField(
        verbose_name='Конвейерная безопасность (аварийный выключатель конвейера, датчик схода ленты, датчик препятствия, датчик затора, датчик перегруза)')
    light_indication = models.BooleanField(
        verbose_name='Светосигнальное оборудование (светосигнальные колонны и маячки)')
    other_device = models.BooleanField(verbose_name='Другое')
    other_device_description = models.TextField(blank=True, default='', verbose_name='Описание иного оборудования')

    # class Meta:
    #     model = ShortQuestionaire
    #     exclude = 'short_version'