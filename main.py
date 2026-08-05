import discord
from discord.ext import commands
from discord.ui import View, Button
from flask import Flask
from threading import Thread
import os

# سيرفر فلاسك عشان يظل البوت صاحي 24/7 مع UptimeRobot
app = Flask('')

@app.route('/')
def home():
    return "T7-STORE Restock Bot is online!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

# إعداد البوت
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class RestockButtonView(View):
    def __init__(self):
        super().__init__(timeout=None)
        # زر الشراء الموجه لموقعك
        self.add_item(Button(
            label="الشراء عبر موقعنا في سله", 
            url="https://t77.rmz.gg/", 
            emoji="<:emoji_59:1456744370190422302>", 
            style=discord.ButtonStyle.link
        ))

@bot.command()
@commands.has_permissions(administrator=True)
async def restock(ctx):
    embed = discord.Embed(
        description=(
            "تم تجديد المخزون 📦\n\n"
            "حسابات 600k-800k <a:by_noobot:1432240712480460930>\n"
            "حسابات آمن من حسابات المليون بي جوده عاليه <a:by_noobot:1449305780212858940>\n\n"
            "السعر 11.99<:by_noobot:1434271270278533241>\n\n"
            "🎯 | مواصفات الحساب\n"
            "📊 | لفل الحساب +60\n"
            "🌾 | زراعة +45\n"
            "📦 | صناديق +65\n"
            "🍳 | طبخ +70\n"
            "🏧 | صرافة +70\n\n"
            "طرق الدفع: <a:by_noobot:1453009231056732326>\n"
            "<:by_noobot:1453009492836094032> -<:by_noobot:1454766626489499669>  -<:by_noobot:1454766482218025135>- <:by_noobot:1453009386690842747> <:by_noobot:1454766716734144613>\n\n"
            "يسعدنا اختياركم لي متجرنا :<a:by_noobot:1456368116249526373>\n\n"
            "الكمية المتوفرة: [ 40 ] :stock:"
        ),
        color=0x9B59B6
    )

    view = RestockButtonView()
    # تم إزالة منشن everyone للتجربة فقط
    await ctx.send(embed=embed, view=view)
    
    try:
        await ctx.message.delete()
    except:
        pass

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} - Restock Bot is ready!")

keep_alive()

# سحب التوكن الخاص بالبوت من متغيرات البيئة في ريندر
TOKEN = os.environ.get("TOKEN")
bot.run(TOKEN)
