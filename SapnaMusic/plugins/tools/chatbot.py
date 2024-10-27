from SapnaMusic import app
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
    CallbackContext,
)

# Replace this with your actual bot token
BOT_TOKEN = "7642505679:AAFD-CVcvZRR_NDyOpnvYoNmMvzXqF30Bz4"

# Global variable to store chat state (enabled/disabled)
chatbot_enabled = {}


def get_chatbot_response(message):
    """Fetches a response from the chatbot API."""
    url = f"https://chatwithai.codesearch.workers.dev/?chat={message}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.json().get("message", "Sorry, I couldn't understand that.")


def handle_chatbot_response(update: Update, context: CallbackContext):
    """Handles responses from the chatbot and sends them back to the user."""
    chat_id = update.effective_chat.id

    # Only respond if chatbot is enabled in this group
    if chatbot_enabled.get(chat_id, False):
        if update.message.reply_to_message and update.message.reply_to_message.from_user.id == context.bot.id:
            message_text = update.message.text
            response = get_chatbot_response(message_text)
            update.message.reply_text(response)


def start(update: Update, context: CallbackContext):
    """Sends a welcome message."""
    update.message.reply_text("Hello! I'm a chatbot. Use /chatbot to manage my activation.")


def activate_chatbot(update: Update, context: CallbackContext):
    """Activates or deactivates the chatbot using inline buttons."""
    user = update.effective_user
    chat = update.effective_chat

    # Check if the user is an administrator
    if not chat.get_member(user.id).status in ("creator", "administrator"):
        update.message.reply_text("Only admins can manage the chatbot.")
        return

    chat_id = update.effective_chat.id
    current_state = chatbot_enabled.get(chat_id, False)

    keyboard = [
        [
            InlineKeyboardButton("Turn On" if not current_state else "Turn Off", callback_data=f"toggle_{chat_id}"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        f"Chatbot is currently {'**On**' if current_state else '**Off**'} in this group.",
        reply_markup=reply_markup,
        parse_mode="Markdown",
    )


def handle_button_press(update: Update, context: CallbackContext):
    """Handles the inline button press to toggle the chatbot state."""
    query = update.callback_query
    chat_id = int(query.data.split("_")[1])
    
    # Toggle the chatbot state
    chatbot_enabled[chat_id] = not chatbot_enabled.get(chat_id, False) 

    # Update the inline button text
    new_state = chatbot_enabled[chat_id]
    keyboard = [
        [
            InlineKeyboardButton("Turn On" if not new_state else "Turn Off", callback_data=f"toggle_{chat_id}"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=f"Chatbot is now {'**On**' if new_state else '**Off**'}.",
        reply_markup=reply_markup,
        parse_mode="Markdown",
    )


def main():
    """Starts the bot."""
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("chatbot", activate_chatbot))
    dp.add_handler(CallbackQueryHandler(handle_button_press))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_chatbot_response)) 

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
