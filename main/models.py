from django.db import models


# Create your models here.



class Questionaire(models.Model):
    choices = ((True, 'Да'), (False, 'Нет'),)
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата записи')
    email = models.EmailField(blank=False,
                              verbose_name='Email заявителя')
    company_name = models.CharField(max_length=255,
                                    blank=False,
                                    verbose_name='Наименование компании')
    company_address = models.TextField(blank=False,
                                       verbose_name='Адрес компании')
    company_phone = models.CharField(max_length=255,
                                     blank=False,
                                     verbose_name='Телефон компании')
    company_email = models.EmailField(blank=False,
                                      verbose_name='Общий email компании')
    company_site = models.CharField(max_length=255,
                                    blank=True, default='',
                                    verbose_name='Сайт компании')
    company_contact = models.CharField(max_length=255, blank=False,
                                       verbose_name='Контактное лицо')
    company_contact_position = models.CharField(max_length=255, blank=False,
                                                verbose_name='Должность контактного лица')
    company_contact_phone = models.CharField(max_length=255, blank=False,
                                             verbose_name='Телефон контактного лица')
    company_destination = models.TextField(blank=False,
                                           verbose_name='Направление деятельности, краткое описание бизнеса Ассортимент товаров и услуг(продажи, инжиниринг, производство и др. , примерно в какой пропорции распределен оборот между видами деятельности)')
    company_percent = models.FloatField(default=0,
                                        blank=True,
                                        null=True,
                                        verbose_name='Какой процент от Вашего оборота (из 100%)')
    company_amount = models.FloatField(default=0,
                                       verbose_name='Какой оборот у Вашей компании за прошлый год?')

    company_targeting = models.TextField(blank=True, default='',
        verbose_name='Средства  для расширения рынка сбыта и привлечения новых заказчиков')

    company_partners = models.TextField(blank=False,
                                        verbose_name="С какими фирмами (поставщиками, брэндами) по частотному приводу, мотор-редукторам, датчикам сотрудничаете и как долго?")

    company_deploy = models.TextField(blank=True, default='',
        verbose_name="Есть ли собственные разработки (краткое описание)")
    company_personal = models.TextField(blank=False,
                                        verbose_name="Количество сотрудников \ из них продавцов \ из них инженеров в фирме ?")
    company_ceo_has_tech = models.BooleanField(  verbose_name='Имеет ли управляющий (директор) техническое образование?')
    company_has_filial = models.BooleanField(verbose_name='Есть ли у Вашего предприятия филиалы в других регионах РФ? ')
    company_regions = models.TextField(blank=True, default='',
        verbose_name="Регионы, где есть филиал")
    company_destination_activity = models.TextField(blank=False,
                                                    verbose_name="В каких отраслях промышленности Вы наиболее активны? ")

    company_different_services = models.TextField(blank=True, default='',
        verbose_name="Дополнительные сервисы компании")
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
    other_device_description = models.TextField(blank=True, default='',verbose_name='Описание иного оборудования')
    company_can_have_dealer_page = models.TextField(blank=False,
                                                    verbose_name="Готовы ли Вы освоить Личный кабинет дилера для самостоятельной работы с клиентом после заключения договора в течении 3-4 дней?")

