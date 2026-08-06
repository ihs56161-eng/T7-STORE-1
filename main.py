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
        # زر الشراء الموجه لموقعك في رمز
        self.add_item(Button(
            label="الشراء عبر موقعنا في رمز", 
            url="https://t77.rmz.gg/", 
            emoji="<:emoji_25:1534663685224792125>", 
            style=discord.ButtonStyle.link
        ))

@bot.command()
@commands.has_permissions(administrator=True)
async def restock(ctx):
    embed = discord.Embed(
        description=(
            "تم تجديد المخزون 📦\n\n"
            "حسابات 1m-1.7m <a:emoji_18:1534616315254407273>\n\n"
            "السعر: بـ22.99﷼ فقط <a:emoji_16:1534616263601426442>\n\n"
            "🎯 | مواصفات الحساب\n"
            "🎣 | لفل الصيد +70\n\n"
            "طرق الدفع :<a:emoji_15:1534564974436024432>\n\n"
            "-<:emoji_21:1534624121009213590> -<:emoji_23:1534643150134579220>  -<:emoji_5:1526260857904824492> -<:emoji_23:1534637381334994974> -\n\n"
            "يسعدنا اختياركم لي متجرنا <a:emoji_22:1534632890388971551>\n\n"
            "الكمية المتوفرة: [كميه قليله جدا ] <:emoji_19:1534616462298185849>"
        ),
        color=0x9B59B6
    )
    
    # تعيين الصورة البانر
    embed.set_image(url="https://cdn.discordapp.com/attachments/1534664004151283983/1534664957881352364/file_00000000f198820a9c47e7ecb7c02189.png")

    view = RestockButtonView()
    
    # إرسال المنشن مع الإيمبد
    await ctx.send(content="@everyone", embed=embed, view=view)
    
    try:
        await ctx.message.delete()
    except:
        pass

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} - Restock Bot is ready!")

keep_alive()

# سحب التوكن من متغيرات البيئة
TOKEN = os.environ.get("TOKEN")
bot.run(TOKEN)
