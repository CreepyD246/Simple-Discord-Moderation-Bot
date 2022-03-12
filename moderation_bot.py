# Importing modules/libraries
import discord

# Creating client instance - this will be used to interact with the Discord API (connection to Discord)
client = discord.Client()
key = "INSERT YOUR TOKEN HERE"

# These are all the words you want to block (the last 2 items are so the bot also deletes messages
# containing links) - You can add as many terms in here as you'd like.
block_words = ["curse_word_1", "curse_word_2", "http://", "https://"]

# The on_ready event happens when the bot comes online
@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}") # Printing the bot's name when it comes online

# The on_message event happens when a message gets sent on the server
@client.event
async def on_message(msg):

    # If the message wasn't sent by the bot
    if msg.author != client.user:

        # Going through each blocked word to check if it's in the message
        for text in block_words:
            # Checking if the message was sent by a moderator (because it would be nice if moderators
            # could share links in case it would be important for them to do so).
            if "Moderator" not in str(msg.author.roles) and text in str(msg.content.lower()):
                await msg.delete() # Deletes the message
                return # So that we don't continue going throuh the loop once we've already found
                       # a blocked word

        print("Not Deleting...") # This will be printed if the bot doesn't delete a message
        

client.run(key) # Running the bot
