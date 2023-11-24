# Pico QuoteGame and API
Run an API that returns random movie quotes, and displays them on a Pico Inky Pack screen
Guess the movie - You can get a clue about the movie, or see the answer
Change the update time to get new quotes faster (default 5 minutes)

This package contains the following things:

- A web scraper that grabs quotes and info from an IMDB 'Top 1000 Movies' list. Note that this has already been run, and the output json file is included, but it could still be run again or adapted to grab quotes from other places
- A simple REST API that returns these quotes and info when requested
- An application for the Raspberry Pi Pico Inky Pack that makes requests to the API, displays the quotes at random, and displays clues or the answer

To use it all you will need the following:

- Something to run the API on (such as a Raspberry Pi or old PC)
- A Raspberry Pi Pico W (with headers)
- The Pimoroni Pico MicroPython firmware (https://github.com/pimoroni/pimoroni-pico/releases)
- A Pimoroni Pico Inky Pack (https://shop.pimoroni.com/products/pico-inky-pack?variant=40044626051155)

The API will also work without the Pico application (will still need the movie_list.json file), which could be useful if you want to use the random quotes in another application.

The API uses FastAPI and Uvicorn - check here (https://fastapi.tiangolo.com/) for instructions on how to set it up and get a basic API running, as well as how to connect to it from another computer.

The Inky Pack appliction was adapted from the Pimoroni 'quote of the day' example that you can find here (https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/examples/pico_inky). Check the instructions for how to get this example running, then the Pico quote app will be all set to go.

Before use, check the comments in the scripts and replace the IP address and movie list file location where noted.

Finally, this is just a test for now, as I'm currently a little hooked on the Pico and some of its add-ons. Now that this is working, I'm going to add more movies to the list and more clues to display for each. Oh, and the scraper currently can't handle films with multiple directors, so I'll fix that if it needs to be run again. For now, I just fixed the few incorrect movie details by hand.

EDIT: Okay, I think I'm just beginning to understand what everyone else has been accepting for a while - A.I. can be really useful for content generation. None of the code is machine-generated, but I got ChatGPT to produce a number of new movies for the list, in the same JSON format as the existing ones. I've included the prompt I used - ask it to continue with a specific genre, decade, director, actor, or any other detail you like to get more!