import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Modal
from datetime import datetime

from src.agendar_eventos import criar_evento

class AgendaModal(Modal):
        def __init__(self):
            super().__init__(title="Agendar Evento no Google Calendar")

        titulo = discord.ui.TextInput(
            label="Título do Evento", 
            placeholder="Ex.: Reunião de equipe", 
            required=True)
        
        inicio = discord.ui.TextInput(
            label="Data e Hora", 
            placeholder="Ex.: 2024-12-20T16:00 ou 2024-12-20", 
            required=True)
        
        termino = discord.ui.TextInput(
            label="Data e Hora de Término", 
            placeholder="Ex.: 2024-12-20T17:15 ou 2024-12-20", 
            required=True)

        
        descricao = discord.ui.TextInput(
            label="Descrição (Opcional)", 
            placeholder="Ex.: Discussão sobre metas", 
            required=False)
        
        local = discord.ui.TextInput(
            label="Local (Opcional)", 
            placeholder="Ex.: Escritório ou Zoom", 
            required=False)

        async def on_submit(self, interaction: discord.Interaction):

            try:
                # Verifica se é um evento de dia inteiro
                if "T" not in self.inicio.value and "T" not in self.termino.value:
                    start_datetime = datetime.fromisoformat(self.inicio.value)
                    end_datetime = datetime.fromisoformat(self.termino.value)
                    all_day = True
                else:
                    start_datetime = datetime.fromisoformat(self.inicio.value)
                    end_datetime = datetime.fromisoformat(self.termino.value)
                    all_day = False

                # Cria o evento
                link = criar_evento(
                    start_datetime, end_datetime, 
                    self.titulo.value, self.descricao.value, 
                    self.local.value, all_day
                )

                if link:
                    await interaction.response.send_message(
                        f"🎉 **Evento criado com sucesso!**\n\n"
                        f"**Nome do Evento**: {self.titulo.value}\n"
                        f"**Horário**: {'Dia inteiro' if all_day else f'{start_datetime} - {end_datetime}'}\n"
                        f"**Local**: {self.local.value or 'Não especificado'}\n"
                        f"**Descrição**: {self.descricao.value or 'Sem descrição'}\n\n"
                        f"[🔗 Clique aqui para visualizar no Google Calendar]({link})",
                        ephemeral=True,
                    )
                else:
                    await interaction.response.send_message(
                        f"❌ Ocorreu um erro ao criar o evento.\n"
                        f"Verifique as permissões ou importe o arquivo 'credencials.json' no comando slash '/up_credenciais'!",
                        ephemeral=True,
                    )
            except ValueError:
                await interaction.response.send_message(
                    "❌ **Formato de data/hora inválido.**\n"
                    "Para eventos de dia inteiro, use AAAA-MM-DD.\n"
                    "Para eventos com horário, use AAAA-MM-DDTHH:MM.",
                    ephemeral=True,
                )
            except Exception as e:
                await interaction.response.send_message(
                    f"❌ **Erro inesperado:** {e}", ephemeral=True
                )



class CriarEvento(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

# name="agendar", description="Abrir modal para agendar um evento no Google Calendar."
    @app_commands.command(name="agendar", description="Abrir modal para agendar um evento no Google Calendar.")
    async def agendar_evento(self, interaction: discord.Interaction):
        await interaction.response.send_modal(AgendaModal())
    
    

async def setup(bot):
    await bot.add_cog(CriarEvento(bot))