# bot.py — Digital_Flapski, the reference "Kid".
# A Discord bot that answers when you @mention it, powered by your LOCAL Ollama model.
# Nothing here phones home except to Discord — the thinking happens on your own GPU.

import os
from pathlib import Path

import discord
from dotenv import load_dotenv
from ollama import AsyncClient

# --- secrets --------------------------------------------------------------
# load_dotenv reads the .env file sitting next to this script and puts its
# values into the environment. The token NEVER gets written into the code.
# Point it at THIS script's folder so it works no matter where it's launched from.
load_dotenv(Path(__file__).parent / ".env")
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise SystemExit(
        "No DISCORD_TOKEN found. Open the .env file next to bot.py and paste your bot "
        "token after 'DISCORD_TOKEN=' (Dev Portal -> your app -> Bot -> Reset Token)."
    )
MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

# --- the Kid's personality (a system prompt is a pre-pull buff) -----------
SYSTEM = (
    "You are Digital_Flapski, the digital familiar of the WoW guild 'Goats After Dark'. "
    "You are a sharp, dry, faintly grizzled old goat. Keep answers short and useful. "
    "Your guild are ex-hardcore raiders: no fluff, no corporate cheer, they can take it straight."
)

# --- Discord wiring -------------------------------------------------------
intents = discord.Intents.default()
intents.message_content = True   # THE gotcha. Off = the bot receives blank messages and looks broken.
discord_client = discord.Client(intents=intents)
oracle = AsyncClient()           # talks to your local Ollama server on http://localhost:11434

@discord_client.event
async def on_ready():
    print(f"Digital_Flapski is awake as {discord_client.user}. @mention me in a channel I can see.")

@discord_client.event
async def on_message(message: discord.Message):
    # 1. Ignore ourselves AND every other bot (e.g. GoatHerder) — stops bot-to-bot loops.
    if message.author.bot:
        return
    # 2. Only respond when actually @mentioned (keeps the Kid from spamming every channel).
    if discord_client.user not in message.mentions:
        return

    # 3. Strip the mention(s) so the model sees a clean question.
    prompt = message.content
    for tag in (f"<@{discord_client.user.id}>", f"<@!{discord_client.user.id}>"):
        prompt = prompt.replace(tag, "")
    prompt = prompt.strip() or "Introduce yourself to the guild in one line."

    # 4. Show the typing indicator while the model 'casts', then send the prompt to Ollama.
    async with message.channel.typing():
        reply = await oracle.chat(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": prompt},
            ],
        )

    # 5. Reply in-channel. Discord hard-caps a single message at 2000 characters.
    await message.reply(reply["message"]["content"][:2000])

discord_client.run(TOKEN)
