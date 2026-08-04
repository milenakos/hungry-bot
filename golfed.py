async def on_message(s):
 if s.channel.id!=1129788329295097857 or s.author.bot:return
 for x in (n:=[x for x in s.content.lower().split()if x in w]):
  if sum(x in y for y in m)>2:return m.clear() or await s.channel.send("eats the "+x)
 m[:]=m[-9:]+[n]
((b:=__import__("discord").Client(intents=__import__("discord").Intents(message_content=True,messages=True,guilds=True))),(w:={x.strip()for x in open("nouns.txt")}),(m:=[]),lambda:(b.event(on_message),b.run("token")))[-1]()
