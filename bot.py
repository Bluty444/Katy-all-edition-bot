from telethon.tl.types import ChannelParticipantsAdmins
from telethon import TelegramClient, events
import re

bot = TelegramClient('bot', 12345, '0123456789abcdef0123456789abcdef').start(
    bot_token='12345:0123456789abcdef0123456789abcdef')


@bot.on(events.NewMessage)
async def Main(event):

    text = re.split(r' ', event.text.lower())

    if text[0] == "/start":

        await event.respond("Hello, I can help you to get list of all people or only admins in your chat")
        raise events.StopPropagation

    elif text[0] == "@all":

        chat = await event.get_chat()
        sender_id = event.sender_id

        if sender_id == chat.id:

            await event.reply("This command allowed only in the groups")

        else:

            users = await bot.get_participants(chat)
            usr_list = []
            num = 0

            for user in users:
                if num == 100:
                    break

                elif user.first_name is not None:
                    usr_list.append(
                        f"[{user.first_name}](tg://user?id={user.id})")
                    num += 1

            await event.respond(' '.join(usr_list))
            raise events.StopPropagation

    elif text[0] == "@admins":

        chat = await event.get_chat()
        sender_id = event.sender_id

        if sender_id == chat.id:

            await event.reply("This command allowed only in the groups")

        else:

            admins = await bot.get_participants(chat, filter=ChannelParticipantsAdmins)
            adm_list = []

            for admin in admins:

                if user.first_name is not None:
                    adm_list.append(
                        f"[{admin.first_name}](tg://user?id={admin.id})")

            await event.respond(' '.join(adm_list))
            raise events.StopPropagation

if __name__ == '__main__':
    bot.run_until_disconnected()
