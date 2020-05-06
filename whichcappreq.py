import requests


class WeatherRequests:
    def __init__(self):
        self.url = "https://www.metaweather.com/api/"

    def search_city_name(self, name):
        """
        Searches for a list of cities matching the given name

        :param name: Name to search for
        :return: A list of cities containing the matching name
        
        """
        try:
            tmp = self.url
            tmp += 'location/search/'
            payload = {'query': name}
            response = requests.get(tmp, params=payload)
            weather = response.json()

            return weather

        except ValueError:
            return None

    def get_weather(self, woeid):
        """
        Returns weather information of the city matching given woeid

        :param woeid: Where on earth id
        :return: A list of weather information about the matching woeid
        """
        tmp = self.url
        tmp += 'location/'
        tmp += str(woeid)
        response = requests.get(tmp)
        weather = response.json()

        return weather
