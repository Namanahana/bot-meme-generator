import discord
from discord.ext import commands
import os

from config import TOKEN, PREFIX
from ai import generate_image
from meme import make_meme

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot login sebagai {bot.user}")

@bot.command()
async def meme(ctx, *, args=None):
    try:
        await ctx.send("🧠 Lagi mikir meme...")

        if not args:
            await ctx.send("❌ Format: !meme prompt | teks atas | teks bawah")
            return

        parts = [p.strip() for p in args.split("|")]
        prompt = parts[0]
        top_text = parts[1] if len(parts) > 1 else ""
        bottom_text = parts[2] if len(parts) > 2 else ""

        image_path = generate_image(prompt)
        meme_path = make_meme(image_path, top_text, bottom_text)

        await ctx.send(file=discord.File(meme_path))

    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

bot.run(TOKEN)
