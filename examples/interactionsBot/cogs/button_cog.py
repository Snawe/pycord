import discord
from discord.ext import commands
from discord.ext.commands.context import Context

from discord.commands import slash_command

class ButtonView(discord.ui.View):
    def __init__(self):
        # making None is important if you want the button work after restart!
        super().__init__(timeout=None)

    #custom_id is required and should be unique for <commands.Bot.add_view>
    # attribute emoji can be used to include emojis which can be default str emoji or str(<:emojiName:int(ID)>)
    @discord.ui.button(style=discord.ButtonStyle.blurple,custom_id="counter:firstButton")
    async def leftButton(self,button,interaction):
        await interaction.response.edit_message("button was pressed!")

        
    """
    timeout is used if there is a timeout on the button interaction with is 180 by default
    
    the following example removes the button from the message rather than disabling them.
    async def on_timeout(self):
            for child in self.children:
                child.disabled = True
            await interaction.edit_original_message(view=None)
    """

class ButtonExample(commands.Cog):
    def __init__(self,client):
        self.client = client

    @slash_command(guild_ids=[...],name="slash_command_name",description="command description!")
    async def CommandName(self,ctx):
        navigator = ButtonView() # button View <discord.ui.View>
        await ctx.respond("press the button.",view=navigator) 

    # for error handling
    @CommandName.error
    async def CommandName_error(self, ctx:Context ,error):
        return await ctx.respond(error,ephemeral=True) # ephemeral makes "Only you can see this" message

def setup(client):
    client.add_cog(ButtonExample(client))
