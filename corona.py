# coding:utf-8

try:
    from covid import Covid
except ModuleNotFoundError:
    import os
    os.system("python -m pip install covid")
    from covid import Covid
import datetime

def get_all_country(covid):
    list_country = covid.get_data()
    for country in list_country:
        date = datetime.datetime.fromtimestamp(country['last_update']/1000).isoformat(sep=" ")
        country['last_update'] = date
    return list_country


def get_country(covid):
    countries = covid.list_countries()
    return sorted(countries, key=lambda d: d["name"])


def get_stat_by_id(covid, id):
    country = covid.get_status_by_country_id(id)
    country['last_update'] = datetime.datetime.fromtimestamp(country['last_update']/1000).isoformat(sep=" ")
    return country


def get_stat_by_name(covid, name):
    country = covid.get_status_by_country_name(name)
    country['last_update'] = datetime.datetime.fromtimestamp(country['last_update']/1000).isoformat(sep=" ")
    return country


def run(commande='country'):
    covid = Covid()
    name = None
    try:
        commande = int(commande)
    except ValueError:
        pass
    if commande == 'country':
        country_list = get_country(covid)
        return country_list
    if isinstance(commande, int):
        result = get_stat_by_id(covid, commande)
        countries = get_country(covid)
        for country in countries:
            if int(country.get('id')) == commande:
                name = country.get('name')
    elif commande == 'all':
        result = get_all_country(covid)
        name = None
    else:
        result = get_stat_by_name(covid, commande)
        name = commande
    return result, name