
To convert the Markdown file (`README.md`) to HTML, you can use a Markdown-to-HTML converter tool or an online converter. Here's an example of the HTML version of the `README.md` content:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Telegram Quote Bot</title>
</head>
<body>
    <h1>Telegram Quote Bot</h1>

    <p>This is a Telegram bot that retrieves quotes from Wikiquote and provides additional functionality such as inline query support.</p>

    <h2>Features</h2>
    <ul>
        <li>Retrieve quotes by searching for the name of the person who said the quote.</li>
        <li>Get the quote of the day.</li>
        <li>Inline query support to generate formatted versions of the query text (uppercase, bold, and italic).</li>
    </ul>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li><code>python-telegram-bot</code> library</li>
        <li><code>wikiquote</code> library</li>
        <li><code>googletrans</code> library</li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/yourusername/telegram-quote-bot.git</code></pre>
        </li>
        <li>Install the required dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Obtain a bot token from BotFather on Telegram.</li>
        <li>Create a <code>config.py</code> file and define the bot token:
            <pre><code>BOT_TOKEN = "YOUR_BOT_TOKEN"</code></pre>
        </li>
        <li>Run the bot:
            <pre><code>python main.py</code></pre>
        </li>
    </ol>

    <h2>Usage</h2>
    <ul>
        <li>Start the bot by sending the <code>/start</code> command.</li>
        <li>Use the <code>/help</code> command to get information about how to use the bot.</li>
        <li>Send a message starting with <code>quote</code> followed by the name of the person to retrieve a quote from Wikiquote. For example, <code>quote Ataturk</code>.</li>
        <li>Use the <code>daily</code> command to get the quote of the day.</li>
        <li>Inline queries are supported. Type <code>@your_bot_username</code> followed by your query to generate formatted versions of the query text.</li>
    </ul>

    <h2>Contributing</h2>
    <p>Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.</p>

    <h2>License</h2>
    <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
</body>
</html>
