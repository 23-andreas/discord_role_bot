# Simple Discord Role Bot
# This work is based on Anson the Developers work here:
# https://www.youtube.com/watch?v=MgCJG8kkq50&t=892s

# prerequisites:
# pip3 install discord
# Setup a Discord App
# Bot TOKEN
# Message ID to react to (enable developer mode to show it in the RMB menu)
# 

import discord
             
MESSAGE_ID = 123456789123456789
BOT_TOKEN = 'ACBDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVW' 

client = discord.Client()

# helper function to reduce redundency
def get_emoji_and_set_role(payload):
    message_id = payload.message_id
    if message_id == MESSAGE_ID:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        
        # for roles and emoji to match up, we need to check the names for spaces,
        # as they are not allowed in emoji names

        # MT3 Fan
        if payload.emoji.name == 'MT3_Fan': # this corresponds to the emoji name
            role = discord.utils.get(guild.roles, name='MT3 Fan') # this corresponds to the role name
        # All the Keycaps
        elif payload.emoji.name == 'All_the_Keycaps':
            role = discord.utils.get(guild.roles, name='All the Keycaps')
        # Keyboard Addict
        elif payload.emoji.name == 'Keyboard_Addict':
            role = discord.utils.get(guild.roles, name='Keyboard Addict')    
        # add more if needed here
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

    return role

@client.event
async def on_ready():
        print("Bot is logged in.")

@client.event
async def on_raw_reaction_add(payload):

    role = get_emoji_and_set_role(payload)

    if role is not None:
        print(role.name)
        member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id) 
        # member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        if member is not None:
            await member.add_roles(role)
            print(f"Role '{role}' added to member '{member}'")
        else:
            print('WARNING: Member not found.')
    else:
        print('WARNING: Role not found.')


@client.event
async def on_raw_reaction_remove(payload):

    role = get_emoji_and_set_role(payload)

    if role is not None:
        print(role.name)
        member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id) 
        # member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        if member is not None:
            await member.remove_roles(role)
            print(f"Role '{role}' removed from member '{member}'")

        else:
            print('WARNING: Member not found.')
    else:
        print('WARNING: Role not found.')

client.run(BOT_TOKEN)
