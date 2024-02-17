import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re

# Configuracion el prefijo de los comandos
bot = commands.Bot(command_prefix='>', description="This is a helper bot")


# Función para recomendar una película basada en el género
def recomendar_pelicula(genero): 
    if genero.lower() == 'comedia':
        return 'Pulp Fiction'
    elif genero.lower() == 'drama':
        return 'The Shawshank Redemption'
    elif genero.lower() == 'accion':
        return 'The Dark Knight'
    elif genero.lower() == 'aventura':
        return 'The Origen'
    elif genero.lower() == 'ciencia ficcion':
        return 'Matrix'
    elif genero.lower() == 'infantil':
        return 'Pinocho'
    else:
        return None


#comando para recomendar una película
@bot.command()
async def recomendacion(ctx, genero):
    # Intentar recomendar una película del género especificado
    pelicula_recomendada = recomendar_pelicula(genero)
    if pelicula_recomendada:
        await ctx.send(f"¡Aquí tienes una película de {genero.lower()} recomendada para ti: {pelicula_recomendada}!")
    else:
        await ctx.send("Lo siento, no tenemos recomendaciones para ese género, sin embargo puedes buscar algo relacionado en youtube")

#primer comando para jugar con ChatBot en caso no haber escogido aun pelicula
@bot.command()
async def ping(ctx):
    await ctx.send('pong jjsjsj, sigue juando o escoje ahora una pelicula :)')

#segundo comando para jugar con ChatBot en caso no haber escogido aun pelicula
@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne+numTwo)

#segundo comando para jugar con ChatBot en caso no haber escogido aun pelicula
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="App Recomendación Pelis :)", description="Aun no escogido una peli y sigo jugando jsjsjjs", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Servidor creado para: ", value="ver pelis")
    embed.add_field(name="Como me llamo? ", value="Chat_Bot")
    embed.add_field(name="que personaje me gusta? ", value="Pikachu")
    embed.add_field(name="Mi ID", value="2847488-56")
    embed.set_thumbnail(url="https://www.pngplay.com/wp-content/uploads/10/Pokemon-No-Background.png")
    await ctx.send(embed=embed)

#comando para buscar alguna pelicula por youtube en caso de no encontrar la deseada
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    
    # Enviar los resultados como un mensaje al canal de Discord
    if search_results:
        await ctx.send(f'Los resultados de la búsqueda en YouTube son: {", ".join(search_results)}')
    else:
        await ctx.send('No se encontraron resultados para la búsqueda.')

# Evento que se ejecuta cuando el bot se conecta
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="App de pelis :)", url="https://www.youtube.com/watch?v=hFithj8USDs"))
    print("My bot es Ready :)") 
    print(f'Conectado como {bot.user}')

# Token del bot de Discord
TOKEN = 'tu_token_aqui'

# Conecta el bot al servidor de Discord
bot.run("MTIwODExODU5NDI3ODUyMjk0MA.GKnLSn.ZNaOE4X69pFwrLU6lIEI1062VKnITEZj4E-hHE")


