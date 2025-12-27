import os
import threading
from flask import Flask

import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

# --- Mini serveur web pour Render ---
app = Flask(__name__)

@app.get("/")
def home():
    return "OK", 200

def run_web():
    port = int(os.getenv("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_web, daemon=True).start()
# --- Fin serveur web ---

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    try:
        await bot.tree.sync()
        print(f"Bot connecté : {bot.user}")
    except Exception as e:
        print(e)

@bot.tree.command(name="ping", description="Tester le bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong 🎈 Bot actif !")

bot.run(TOKEN)
