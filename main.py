import urllib.request

import locale

import lxml.etree as etree


def get_xml(url):
    response = urllib.request.urlopen(url)
    return response.read()


def num():
    num = ''

    while (
    not num.isdigit()):
        num = input("Введите количество норвежских крон для конвертации: ")
        if (not num.isdigit()):
            print('Программа может работать только с цифровыми значениями')
        else:
            print("Результаты конвертации:")

    num = int(num)
    return num


if __name__ == '__main__':
    xml = get_xml('http://www.cbr.ru/scripts/XML_daily.asp')
    xml_data = etree.fromstring(xml)

    huf = xml_data.xpath("/ValCurs/Valute[@ID='R01135']/Value")[0].text
    huf_nominal = xml_data.xpath("/ValCurs/Valute[@ID='R01135']/Nominal")[0].text
    nok = xml_data.xpath("/ValCurs/Valute[@ID='R01535']/Value")[0].text
    nok_nominal = xml_data.xpath("/ValCurs/Valute[@ID='R01535']/Nominal")[0].text

    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

    nok_rub = float(locale.atof(nok)) / float(locale.atof(nok_nominal))
    huf_rub = float(locale.atof(huf)) / float(locale.atof(huf_nominal))

    num = num()

    currency_nok = nok_rub * num
    currency_huf = currency_nok / huf_rub

    print("Норвежские кроны в рублях:", currency_nok)
    print("Рубли в венгерских форинтах:",currency_huf)