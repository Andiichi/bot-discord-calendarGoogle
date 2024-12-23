import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv(dotenv_path=".env")

# Configuração das intenções
permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True

# Instância do bot com prefixo `.`
bot = commands.Bot(command_prefix=".", intents=permissoes)

    
async def carregar_cogs():
    for arquivo in os.listdir('cogs'):
        if arquivo.endswith('.py'):
            await bot.load_extension(f'cogs.{arquivo[:-3]}')

@bot.event
async def on_ready():
    try:
        await carregar_cogs()
        await bot.tree.sync()
        print(f'>>> {bot.user} em execução!\n')
        # Exibe os comandos prefixados carregados
        print("Comandos prefixados carregados:", [command.name for command in bot.commands])
        # Exibe os comandos de barra carregados
        print("Slash commands carregados:", [command.name for command in await bot.tree.fetch_commands()])

    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")
    

# Rodar o bot
token = os.getenv('TOKEN_DISCORD')
bot.run(token)
  