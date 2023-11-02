 Telegram Quote Bot

Telegram Quote Bot
==================

This is a Telegram bot that retrieves quotes from Wikiquote and provides additional functionality such as inline query support.

Features
--------

*   Retrieve quotes by searching for the name of the person who said the quote.
*   Get the quote of the day.
*   Inline query support to generate formatted versions of the query text (uppercase, bold, and italic).

Requirements
------------

*   Python 3.x
*   `python-telegram-bot` library
*   `wikiquote` library
*   `googletrans` library

Installation
------------

1.  Clone the repository:

    git clone https://github.com/mucahitkayadan/telegram-quote-bot.git

2.  Install the required dependencies:

    pip install -r requirements.txt

3.  Obtain a bot token from BotFather on Telegram.
4.  Create a `config.py` file and define the bot token:

    BOT_TOKEN = "YOUR_BOT_TOKEN"

5.  Run the bot:

    python main.py

Usage
-----

*   Start the bot by sending the `/start` command.
*   Use the `/help` command to get information about how to use the bot.
*   Send a message starting with `quote` followed by the name of the person to retrieve a quote from Wikiquote. For example, `quote Ataturk`.
*   Use the `daily` command to get the quote of the day.
*   Inline queries are supported. Type `@your_bot_username` followed by your query to generate formatted versions of the query text.

Contributing
------------

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

License
-------

This project is licensed under the [MIT License](LICENSE).
