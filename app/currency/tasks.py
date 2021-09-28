from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
import requests
from decimal import Decimal
from currency.models import Rate
from bs4 import BeautifulSoup
from currency import model_choices as mch


def round_currency(num):
    return Decimal(num).quantize(Decimal('.01'))


def add_rates(sale, buy, currency_type, source):
    last_rate = Rate.objects.filter(
            type=currency_type,
            source=source,
            ).order_by('created').last()

    if last_rate is None or last_rate.sale != sale or last_rate.buy != buy:
        Rate.objects.create(
            type=currency_type,
            sale=sale,
            buy=buy,
            source=source,
        )


@shared_task
def contactus_task(subject, body):
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [settings.SUPPORT_EMAIL],
        fail_silently=False,
    )


@shared_task
def parse_privatbank():

    privat_url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

    response = requests.get(privat_url)

    response.raise_for_status()

    source = 'privatbank'
    rates = response.json()
    currency_types = {
        'USD': mch.TYPE_USD,
        'EUR': mch.TYPE_EUR,
        'RUR': mch.TYPE_RUB,
    }

    for rate in rates:
        ct = rate['ccy']
        if ct in currency_types:
            currency_type = currency_types[ct]
            sale = round_currency(rate['sale'])
            buy = round_currency(rate['buy'])

            add_rates(sale, buy, currency_type, source)


@shared_task
def parse_monobank():

    monobank_url = 'https://api.monobank.ua/bank/currency'

    response = requests.get(monobank_url)

    response.raise_for_status()

    source = 'monobank'
    rates = response.json()
    currency_types = {
        840: mch.TYPE_USD,
        978: mch.TYPE_EUR,
        643: mch.TYPE_RUB,
    }

    for rate in rates:
        ct = rate['currencyCodeA']
        uah_type = rate['currencyCodeB']
        if ct in currency_types and uah_type == 980:
            sale = round_currency(rate['rateSell'])
            buy = round_currency(rate['rateBuy'])
            currency_type = currency_types[ct]

            add_rates(sale, buy, currency_type, source)


@shared_task
def parse_vkurse():

    vkurse_url = 'http://vkurse.dp.ua/course.json'

    response = requests.get(vkurse_url)

    response.raise_for_status()

    source = 'vkurse'
    rates = response.json()
    currency_types = {
        'Dollar': mch.TYPE_USD,
        'Euro': mch.TYPE_EUR,
        'Rub': mch.TYPE_RUB,
    }

    for rate in rates:
        if rate in currency_types:
            currency_type = currency_types[rate]
            price = rates[rate]
            sale = round_currency(price['sale'])
            buy = round_currency(price['buy'])

            add_rates(sale, buy, currency_type, source)


@shared_task
def parse_alfabank():

    alfabank_url = 'https://alfabank.ua/ru'

    response = requests.get(alfabank_url)

    response.raise_for_status()

    source = 'alfabank'
    soup = BeautifulSoup(response.text, 'html.parser')
    currency_types = {
        'USD': mch.TYPE_USD,
        'EUR': mch.TYPE_EUR,
        'RUB': mch.TYPE_RUB,
    }

    for currency_type in currency_types:
        sale = round_currency(soup.find('span', {'data-currency': f'{currency_type}_SALE'}).text.strip())
        buy = round_currency(soup.find('span', {'data-currency': f'{currency_type}_BUY'}).text.strip())

        add_rates(sale, buy, currency_type, source)


@shared_task
def parse_pivdennyi():
    pivdennyi_url = 'https://bank.com.ua/api/ru/v1/rest-ui/find-branch-course?date=1631739600'

    response = requests.get(pivdennyi_url)

    response.raise_for_status()

    source = 'pivdennyi'

    rates = response.json()
    currency_types = {
        'USD': mch.TYPE_USD,
        'EUR': mch.TYPE_EUR,
        'RUB': mch.TYPE_RUB,
    }

    for rate in rates:
        ct = rate[1]
        if ct in currency_types:
            currency_type = currency_types[ct]
            sale = round_currency(rate[3])
            buy = round_currency(rate[2])

            add_rates(sale, buy, currency_type, source)
