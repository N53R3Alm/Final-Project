import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_puppy_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('puppy')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_puppy_image_url()
    await ctx.send(image_url)

organic = ['sisa makanan', 'bahan kimia', 'daun', 'kulit pisang','sayur']
anorganic = ['kaca', 'plastik', 'stereofoam','ban', 'karet']

#FUNGSI PILIH SAMPAH
@bot.command()
#membuat fungsi pilah sampah
async def pilih_sampah(ctx):
    await ctx.send("Masukkan jenis sampah yang ingin kamu ketahui: ")
    msg = await bot.wait_for("message")

#PERUBAHAN IKLIM
@bot.command('climate changes')
#apa yang ingin dicari
async def perubahan_iklim(ctx):
     await ctx.send("Apa yang ingin dicari?")
     msg = await bot.wait_for("")
#solusi pencegahan perubahan iklim
async def solusi(ctx):
     await ctx.send("Berikut adalah cara - cara yang bisa kamu gunakan untuk mencegah perubahan iklim:")
     msg = await bot.wait_for("")
#pengertian perubahan iklim
async def pengertian(ctx):
     await ctx send("Perubahan iklim adalah suatu perubahan pada kondisi bumi yang tidak sesuai dengan yang seharusnya")
#akibat perubahan iklim
async def akibat(ctx):
     await ctx.send("Akibat dari perubahan iklim adalah sebagai berikut:")
     msg = await bot.wait_for("")
#contoh perubahan iklim
async def contoh(ctx):
     await ctx send("Contoh dari perubahan iklim adalah kemarau yang mengakibatkan pemanasan global, hujan deras yang mengakibatkan banjir dan lain - lain")
#penyebab pencegahan perubahan iklim
async def penyebab(ctx):
     await ctx.send("Penyebab perubahan iklim adalah sebagai berikut:")
     msg = await bot.wait_for("")









bot.run("MTE5NjgwNTQ0NDA4NjI3MjA0MA.Ghatul.O6mc0bHef3MXLSRgDUUgMqfuvGBLDWquwG-oEs")
