import requests

url = "https://www.metaweather.com/api/"


def search_city_name(name):
    """
    Searches for a list of cities matching the given name

    :param name: Name to search for
    :return: A list of cities containing the matching name

    """
    try:
        tmp = url
        tmp += 'location/search/'
        payload = {'query': name}
        response = requests.get(tmp, params=payload)
        weather = response.json()

        return weather

    except ValueError:
        return None


def get_weather(woeid):
    """
    Returns weather information of the city matching given woeid

    :param woeid: Where on earth id
    :return: A list of weather information about the matching woeid
    """
    tmp = url
    tmp += 'location/'
    tmp += str(woeid)
    response = requests.get(tmp)
    weather = response.json()

    return weather


def get_weather_abbr(woeid):
    """

    :param woeid: woeid of the location
    :return: Weather abbreviation of the woeid
    """
    tmp = get_weather(woeid)['consolidated_weather'][0]['weather_state_abbr']
    if tmp:
        return tmp
    return None
