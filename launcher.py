import hikari

token = "OTg2ODc2MzYzNjI"  + "zNTI2NDAw.GClA_x.h1Jc" + "ZIdbjcevic4338cs" + "9KWYLYu4DGW4nWns6s"
bot = hikari.GatewayBot(token=token)

@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    # If a non-bot user sends a message "hk.ping", respond with "Pong!"
    # We check there is actually content first, if no message content exists,
    # we would get `None' here.
    if event.is_bot or not event.content:
        return

    if event.content.startswith("meeps"):
        await event.message.respond("Pong!")

bot.run()