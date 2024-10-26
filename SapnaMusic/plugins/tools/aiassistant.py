from pyrogram import Client, filters, enums
import requests
import urllib.parse
import asyncio
from pyrogram.types import Message
from SapnaMusic import app

def ask_query(query, model=None):
    default_model = 'gpt-4o'
    system_prompt = """You are a helpful assistant. Your name is Tanu, and your owner's name is Sachin, known as @V_VIP_OWNER """

    model = model or default_model

    if model == default_model:
        query = f"{system_prompt}\n\nUser: {query}"

    encoded_query = urllib.parse.quote(query)
    url = f"https://chatwithai.codesearch.workers.dev/?chat={encoded_query}&model={model}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("result", "No response found.")
    else:
        return f"Error fetching response from API. Status code: {response.status_code}"

async def send_typing_action(client: Client, chat_id: int, duration: int = 1):
    await client.send_chat_action(chat_id, enums.ChatAction.TYPING)
    await asyncio.sleep(duration)

def get_model_from_db(group_id):
    return 'claude-sonnet-3.5'

@app.on_message(filters.command("aii"))
async def handle_query(client, message):
    if len(message.command) < 2:
        await message.reply_text("<b>Please provide a query to ask.</b>")
        return

    user_query = message.text.split(maxsplit=1)[1]
    user_mention = message.from_user.mention
    await send_typing_action(client, message.chat.id, duration=2)
    response = ask_query(user_query)
    await message.reply_text(f"{user_mention}, <b>{response}</b>")

@app.on_message(filters.mentioned & filters.group)
async def handle_mention(client: Client, message: Message) -> None:
    group_id = message.chat.id

    user_text = None

    if message.reply_to_message and message.reply_to_message.text:
        user_text = message.reply_to_message.text.strip()
    elif len(message.text.split(" ", 1)) > 1:
        user_text = message.text.split(" ", 1)[1].strip()

    if user_text:
        model_name = get_model_from_db(group_id)

        await send_typing_action(client, group_id)

        api_response = ask_query(user_text, model_name)

        await message.reply(f"<b>{api_response}</b>")
    else:
        await message.reply("<b>Please ask a question after mentioning me</b>")
