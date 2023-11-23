# Pico QuoteGame and API
Run an API that returns random movie quotes and info, and display them on a Pico Inky Pack screen

This package contains the following things:

- A web scraper that grabs quotes and info from an IMDB 'Top 1000 Movies' list. Note that this has already been run, and the output json file is inclded, but it could still be run again or adapted to grab quotes from other places
- A simple REST API that returns these quotes and info when requested
- An application for the Raspberry Pi Pico Inky Pack that makes requests to the API and displays the quotes and info at random

The API will work without the Pico application (will still need the movie_list.json file), which could be useful if you want to use the random quotes in another application.

To use it all together you will need the following:

- Something to run the API on (such as a Raspberry Pi or old PC)
- A Raspberry Pi Pico W (with headers)
- The Pimoroni Pico MicroPython firmware (https://github.com/pimoroni/pimoroni-pico/releases)
- A Pimoroni Pico Inky Pack (https://shop.pimoroni.com/products/pico-inky-pack?variant=40044626051155)

The API uses FastAPI and Uvicorn - check here (https://fastapi.tiangolo.com/) for instructions on how to set it up and get a basic API running, as well as how to connect to it from another computer.

The Inky Pack appliction was adapted from the Pimoroni 'quote of the day' example that you can find here (https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/examples/pico_inky). Check the instruction for how to get this example running, then this Pico quote app will be all set to go.

Before use, check the comments in the scripts and replce the IP address and movie list file location where noted.

Finally, this is just a test for now, as I'm currently a little hooked on the Pico and some of its add-ons. Now that this is working, I'm going to add support for the Inky Pack buttons, which will allow you to switch between an unknown quote, a clue about the movie, and the title of the movie. It's not much of a game, but could make for some fun movie trivia throughout the day. I'll keep updating this readme as more is added. Oh, and you'll sometimes find a review quote about the movie instead of a quote from the movie itself - I need to go through and get rid of those.
