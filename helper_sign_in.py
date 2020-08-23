import logging
import secrets

from telethon import TelegramClient
from telethon.errors.rpcerrorlist import (PhoneCodeInvalidError,
                                          SessionPasswordNeededError)

from alchemysession import AlchemySessionContainer


async def bleck_megick(event, config_jbo):
    if not event.is_private:
        return
    bot_me = await event.client.get_me()
    print(bot_me.stringify())
    if bot_me.username.lower() == config_jbo.TG_BOT_USER_NAME_BF_HER.lower() and int(event.chat_id) in config_jbo.SUDO_USERS:
        # force int for Type checks
        # 🤣🤣 validations
        async with event.client.conversation(event.chat_id) as conv:
            await conv.send_message(
                "welcome **master**\n"
                "please send me your Phone Number, to generate "
                "`HU_STRING_SESSION` \n"
                "Enter the Phone Number that you want to make awesome, "
                "powered by @UniBorg"
            )
            msg2 = await conv.get_response()
            logging.info(msg2.stringify())
            phone = msg2.message.strip()
            container = AlchemySessionContainer(config_jbo.DB_URI)
            session_id = str(secrets.randbelow(1000000))
            session = container.new_session(session_id)

            current_client = TelegramClient(
                session,
                api_id=config_jbo.APP_ID,
                api_hash=config_jbo.API_HASH,
                device_model="GNU/Linux nonUI",
                app_version="@UniBorg 2.0",
                lang_code="ml"
            )
            await current_client.connect()
            sent = await current_client.send_code_request(phone)
            logging.info(sent)
            if not sent:
                await conv.send_message(
                    "This number is not registered on Telegram. "
                    "Please check your #karma by reading https://t.me/c/1220993104/28753"
                )
                return

            await conv.send_message(
                "This number is registered on Telegram. "
                "Please input the verification code "
                "that you receive from [Telegram](tg://user?id=777000) "
                "seperated by space, "
                "else a `PhoneCodeInvalidError` would be raised."
            )
            msg4 = await conv.get_response()

            received_code = msg4.message.strip()
            received_tfa_code = None
            received_code = "".join(received_code.split(" "))

            try:
                await current_client.sign_in(
                    phone,
                    code=received_code,
                    password=received_tfa_code
                )
            except PhoneCodeInvalidError:
                await conv.send_message(
                    "Invalid Code Received. "
                    "Please re /start"
                )
                return
            except SessionPasswordNeededError:
                await conv.send_message(
                    "The entered Telegram Number is protected with 2FA. "
                    "Please enter your second factor authentication code.\n"
                    "__This message "
                    "will only be used for generating your string session, "
                    "and will never be used for any other purposes "
                    "than for which it is asked.__"
                    "\n\n"
                    "The code is available for review at "
                    "https://github.com/SpEcHiDe/UniBorg/raw/master/helper_sign_in.py"
                )
                msg6 = await conv.get_response()
                received_tfa_code = msg6.message.strip()
                await current_client.sign_in(password=received_tfa_code)

            # all done
            # Getting information about yourself
            current_client_me = await current_client.get_me()
            # "me" is an User object. You can pretty-print
            # any Telegram object with the "stringify" method:
            logging.info(current_client_me.stringify())

            string_session_messeg = await conv.send_message(
                f"{session_id}"
            )
            await string_session_messeg.reply(
                "now, "
                "please turn of the application "
                "and set the above variable to "
                "`HU_STRING_SESSION` variable, "
                "and restart application."
            )
    else:
        await event.reply("un authorized -_- user(s)")
