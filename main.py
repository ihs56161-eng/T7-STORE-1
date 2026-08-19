@bot.command()
@commands.has_permissions(administrator=True)
async def restock(ctx):
    embed = discord.Embed(
        title="📦 | تم تجديد المخزون في T7 STORE",
        description=(
            "أهلاً بكم، تم توفير دفعة جديدة من الحسابات المميزة!\n\n"
            "─────────────────────────\n\n"
            "🎣 **حسابات الصيد**\n"
            "• صيد: **70+**\n"
            "• السعر: **12.99﷼** فقط <a:emoji_16:1534616263601426442>\n\n"
            "─────────────────────────\n\n"
            "💸 **حسابات المليون**\n"
            "• فلوس: **1m+**\n"
            "• زراعة: **45+** 👨‍🌾\n"
            "• تهكير: **85+** 💻\n"
            "• السعر: **9.99﷼** فقط <a:emoji_16:1534616263601426442>\n\n"
            "─────────────────────────\n\n"
            "طرق الدفع :<a:emoji_15:1534564974436024432>\n"
            "-<:emoji_21:1534624121009213590> -<:emoji_23:1534643150134579220> -<:emoji_5:1526260857904824492> -<:emoji_23:1534637381334994974> -\n\n"
            "يسعدنا اختياركم لمتجرنا <a:emoji_22:1534632890388971551>\n\n"
            "الكمية المتوفرة: [كمية محدودة] <:emoji_19:1534616462298185849>"
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
        
