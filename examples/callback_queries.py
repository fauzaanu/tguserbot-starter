from pyrogram import Client

app = Client("my_bot", bot_token="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11")


@app.on_callback_query()
async def answer(client, callback_query):
    await callback_query.answer(
        f"Button contains: '{callback_query.data}'",
        show_alert=True)


app.run()  # Automatically start() and idle()