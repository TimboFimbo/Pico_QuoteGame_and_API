import WIFI_CONFIG
from network_manager import NetworkManager
import time
import uasyncio
import ujson
from urllib import urequest
from picographics import PicoGraphics, DISPLAY_INKY_PACK
from pimoroni import Button
import random

"""
Grab a random quote from the imdb quote api (see https://github.com/TimboFimbo/Pico_QuoteGame_and_API)
Guess the movie - You can get a clue about the movie, or see the answer
Change the update time to get new quotes faster (default 5 minutes)
"""

graphics = PicoGraphics(DISPLAY_INKY_PACK)
button_a = Button(12)
button_b = Button(13)
button_c = Button(14)

WIDTH, HEIGHT = graphics.get_bounds()
# change the ip address to that of the computer running the api
ENDPOINT = 'http://192.168.0.119:8000/random_movie'
# the number of seconds until the next quote is displayed
TIME_TO_UPDATE = 300

printed_connection_status = False
state = 'quote'
changed_state = True
ready_to_update = True
last_update_time = time.time()
answer_seen = False
last_clue = 100
current_clue = last_clue

def clear():
    graphics.set_pen(15)
    graphics.clear()

def status_handler(mode, status, ip):
    graphics.set_update_speed(2)
    clear()
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
    if ready_to_update == True:
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
        stars = data['stars']
        title_year = title + ' ' + year
        directed_by = 'Directed by ' + director

        print(quote)
        print(title)
        print(year)
        print(director)
        print(stars)
        
        ready_to_update = False
        last_update_time = time.time()
        changed_state = True
        state = 'quote'
        answer_seen = False
        
    if changed_state == True:
        changed_state  = False
        if state == 'quote':
            clear()
            graphics.set_pen(0)
            graphics.text('Which movie is this quote from?...', 60, 5, scale=1)
            graphics.text(quote, 10, 20, wordwrap=WIDTH - 20, scale=2)
            if answer_seen == False:
                graphics.text('Press A for the answer, or C for a clue', 50, 120, scale=1)
            else:
                graphics.text('Press A for the answer, or C for to continue', 45, 120, scale=1)
            graphics.update()
        if state == 'clue':
            clear()
            while current_clue == last_clue:
                current_clue = random.randrange(0, len(stars) + 1)
            last_clue = current_clue
            graphics.set_pen(0)
            graphics.text("Here's a clue for you...", 85, 5, scale=1)
            if current_clue == len(stars):
                graphics.text(directed_by, 15, 40, wordwrap=WIDTH - 20, scale=2)
            else:
                graphics.text("Featuring " + stars[current_clue], 15, 40, wordwrap=WIDTH - 20, scale=2)
            graphics.text('Press A for the answer, B to go back, or C for another clue', 10, 120, scale=1)
            graphics.update()
        if state == 'answer':
            clear()
            graphics.set_pen(0)
            graphics.text("Here's the answer...", 90, 5, scale=1)
            graphics.text(title_year, 15, 40, wordwrap=WIDTH - 20, scale=2)
            graphics.text('Press B to go back, or C to continue', 55, 120, scale=1)
            graphics.update()
            answer_seen = True
    
    # checks for button presses to change states, and updates quotes based on time
    if changed_state == False:
        if button_a.read():
            if state != 'answer':
                state = 'answer'
                changed_state = True
        if button_b.read():
            if state != 'quote':
                state = 'quote'
                changed_state = True
        if button_c.read():
            if answer_seen == False:
                state = 'clue'
                changed_state = True
            else:
                ready_to_update = True
        
        if time.time() - last_update_time > TIME_TO_UPDATE:
            ready_to_update = True
        
        time.sleep(0.1)