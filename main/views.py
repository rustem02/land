from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.core.mail import EmailMultiAlternatives


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

from django.db.models.fields import BooleanField
def render_table(instans):
    l = []

    for each in instans._meta.fields:
        val = getattr(instans, each.name)
        if type(each) == BooleanField:
            if getattr(instans, each.name):
                val = 'Да'
            else:
                val = "Нет"
        l.append({'n': each.verbose_name, 'v': val})

    return l

from django.contrib.auth import login, logout, authenticate
def svod(request):

    qs = Questionaire.objects.all().order_by('id')

    context = {'l': []}

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=request.POST['login'].lower(),
                                password=request.POST['password'])
            if not user is None:
                login(request, user)



    if not request.user.is_authenticated:
        context['login_form'] = LoginForm()
    else:
        context['has_access'] = True

    context['fields'] = qs.model._meta.fields

    for item in qs:
        d = []
        for field in context['fields']:
            val = getattr(item, field.name)
            print(type(val))
            if type(val) == bool:
                if val:
                    val = 'Да'
                else:
                    val = 'Нет'

            d.append(val)
        context['l'].append(d)

    return render(request, 'main/svod.html', context=context)


def form(request):
    fm = QuestionareForm()
    if request.method == 'POST':
        fm = QuestionareForm(request.POST)

        if fm.is_valid():
            fm.save()

            subject, from_email, to = 'Новая заявка на дилерство', 'dealer@prst.ru',['pribka@mail.ru','skripkin-1@yandex.ru']
            text_content = 'Новая заявка на дилерство'
            cnt = render_table(fm.instance)
            html_content = render(request, 'main/formemail.html', context={'cnt': cnt}).content.decode('utf8')
            email = EmailMultiAlternatives(subject, text_content, from_email, to, )
            email.attach_alternative(html_content, 'text/html')
            email.send()



        else:
            subject, from_email, to = 'Ошибка в заявке на дилерство', 'dealer@prst.ru', 'pribka@mail.ru'
            text_content = 'Ошибка в заявке на дилерство'

            html_content = render(request, 'main/formemail.html', context={'fm': fm}).content.decode('utf8')
            email = EmailMultiAlternatives(subject, text_content, from_email, [to], )
            email.attach_alternative(html_content, 'text/html')
            email.send()

        return render(request, 'main/form_complete.html')

    return render(request, 'main/form.html', context={'fm': fm})


def example(request):
    if request.method == 'POST':

        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()

            # return HttpResponseRedirect('/POST/')


    else:
        form = ProfileForm()

    return render(request, 'main/example.html', {'form': form})
