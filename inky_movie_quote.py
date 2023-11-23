import WIFI_CONFIG
from network_manager import NetworkManager
import time
import uasyncio
import ujson
from urllib import urequest
from picographics import PicoGraphics, DISPLAY_INKY_PACK

"""
Grab a quote from the imdb quote api
"""

graphics = PicoGraphics(DISPLAY_INKY_PACK)

WIDTH, HEIGHT = graphics.get_bounds()
# change the ip address to that of the computer running the api
ENDPOINT = 'http://192.168.0.119:8000/random_movie'
printed_connection_status = False

def status_handler(mode, status, ip):
    graphics.set_update_speed(2)
    graphics.set_pen(15)
    graphics.clear()
    graphics.set_pen(0)
    graphics.text("Network: {}".format(WIFI_CONFIG.SSID), 10, 10, scale=2)
    status_text = "Connecting..."
    if status is not None:
        if status:
            status_text = "Connection successful!"
        else:
            status_text = "Connection failed!"

    graphics.text(status_text, 10, 30, scale=2)
    graphics.text("IP: {}".format(ip), 10, 60, scale=2)
    graphics.update()

network_manager = NetworkManager(WIFI_CONFIG.COUNTRY, status_handler=status_handler)

while True:
    graphics.set_font("bitmap8")
    graphics.set_update_speed(1)
    
    if printed_connection_status == False:
        uasyncio.get_event_loop().run_until_complete(network_manager.client(WIFI_CONFIG.SSID, WIFI_CONFIG.PSK))
        printed_connection_status = True

    url = ENDPOINT
    print("Requesting URL: {}".format(url))
           
    response = urequest.urlopen(url)
    data = ujson.load(response)[0]
    response.close()
    
    while len(data['quote']) > 120:
        response = urequest.urlopen(url)
        data = ujson.load(response)[0]
        response.close()

    quote = data['quote']
    title = data['title']
    year = data['year']
    director = data['director']
    title_year = title + ' ' + year
    directed_by = 'Directed by ' + director

    print(quote)
    print(title)
    print(year)
    print(director)

    graphics.set_pen(15)
    graphics.clear()
    graphics.set_pen(0)

    graphics.text(quote, 10, 5, wordwrap=WIDTH - 20, scale=2)
    graphics.text(title_year, 10, 100, scale=1)
    graphics.text(directed_by, 10, 115, scale=1)

    graphics.update()

    # change this to adjust the time between requests
    time.sleep(600)