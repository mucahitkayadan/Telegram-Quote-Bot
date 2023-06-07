from uuid import uuid4
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.utils.helpers import escape_markdown

def inlinequery(bot, update):
    """
    Handles the inline queries and generates three options for the user to choose from: uppercase, bold, and italic.

    Args:
        bot (telegram.Bot): The bot instance.
        update (telegram.Update): The update object containing the inline query.

    Returns:
        None
    """
    query = bot.InlineQuery().query
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Caps",
            input_message_content=InputTextMessageContent(query.upper())
        ),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Bold",
            input_message_content=InputTextMessageContent(
                "*{}*".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN
            )
        ),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Italic",
            input_message_content=InputTextMessageContent(
                "_{}_".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN
            )
        )
    ]

    update.inline_query.answer(results)
