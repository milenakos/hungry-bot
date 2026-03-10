import discord

bot = discord.Client(intents=discord.Intents(message_content=True, messages=True, guilds=True))

with open("nouns.txt", 'r') as file:
    words = {line.strip() for line in file}

noun_memory = []

@bot.event
async def on_message(message):
    global noun_memory
    if message.channel.id != 1129788329295097857 or message.author.bot:
        return

    nouns_found = []
    for word in message.content.lower().replace("\n", " ").split(" "):
        if word in words:
            nouns_found.append(word)

    for noun in nouns_found:
        use_times = 0
        for things in noun_memory:
            if noun in things:
                use_times += 1
        if use_times > 2:
            await message.channel.send(f"eats the {noun}")
            noun_memory = []
            return

    noun_memory.append(nouns_found)
    noun_memory = noun_memory[-10:]

bot.run("token")
