import discord  
from discord.ext import commands  
import os
import random
import requests

intents = discord.Intents.default()  
intents.message_content = True  
intents.members = True


# Botun prefiksi
bot = commands.Bot(command_prefix='$', intents=intents)

# Çevre dostu fikirler listesi
cevre = [
    "Tek kullanımlık plastik yerine tekrar kullanılabilir ürünler tercih edin.",
    "Enerji tasarrufu için kullanılmayan cihazları prizden çekin.",
    "Yerel çiftçilerden alışveriş yaparak karbon ayak izinizi azaltın.",
    "Toplu taşıma kullanın veya bisiklete binerek fosil yakıt tüketimini azaltın.",
    "Kağıt israfını önlemek için dijital notlar alın.",
    "Geri dönüştürülebilir atıkları doğru şekilde ayırın.",
    "Yanınızda bir su şişesi taşıyarak plastik şişe kullanımını azaltın.",
    "Bahçenizde kompost yaparak organik atıkları değerlendirin.",
    "Doğal temizlik malzemeleri kullanarak kimyasal kirliliği azaltın.",
    "Ağaç dikerek çevrenize katkıda bulunun."
]

# Botun hazır olduğunu bildiren olay
@bot.event
async def on_ready():
    print(f'\u26a1 {bot.user.name} botu aktif ve çalışıyor!')

# Çevre dostu fikirler komutu
@bot.command()
async def cevredostu(ctx):
    tip = random.choice(cevre)
    await ctx.send(f"\ud83c\udf3f {tip}")

# Kullanıcıdan gelen mesajlarda selam verme örneği
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "merhaba" in message.content.lower():
        await message.channel.send("Merhaba! \ud83d\ude04 Çevre dostu fikirler için `$cevredostu` komutunu kullanabilirsiniz.")

    await bot.process_commands(message)

# Botu başlatma
bot.run('Token var')
