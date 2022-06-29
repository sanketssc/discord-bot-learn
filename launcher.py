import hikari

bot = hikari.GatewayBot(token="OTg2ODc2MzYzNjIzNTI2NDAw.G9lk5m.9ZrKvsf1ZT8QiSSdMTNLNBvAi2Eh0jB2vifsrM")

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