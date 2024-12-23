import discord
from discord import app_commands
from discord.ext import commands

from calendar_google.listar_eventos import listagem_calendar

class ListarEvento(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

   
    @app_commands.command(name="listar_agenda", description=f"Listar eventos no Google Calendar no mês atual.")
    async def listar_agenda(self, interaction: discord.Interaction):
        try:
            eventos = listagem_calendar()
            await interaction.response.send_message(eventos, ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(
                f"Erro ao listar eventos: {e}\n"
            f"Tente novamente ou verifique se tem o arquivo 'credencials.json' cadastrado",
            ephemeral=True)
    
    

async def setup(bot):
    await bot.add_cog(ListarEvento(bot))

