import logging

from aiogram import Bot, Dispatcher, executor, types


class BotDispatcher:
    _loggingLevel: int
    _APIToken: str
    _bot: Bot
    _dp: Dispatcher

    def __init__(self, api_token: str, logging_level: int = logging.INFO):
        # Configure logging
        self._loggingLevel = logging_level
        logging.basicConfig(level=logging.INFO)

        # Initialize bot and dispatcher
        self._APIToken = api_token
        self._bot = Bot(token=api_token)
        self._dp = Dispatcher(self._bot)

        # Temp solution for testing telegram bot
        @self._dp.message_handler(regexp='^zamazan4ik$')
        async def zamazan(message: types.Message):
            await self._bot.send_message(message.chat.id, "щенок".format(message.text))

        @self._dp.message_handler()
        async def echo(message: types.Message):
            await self._bot.send_message(message.chat.id, message.text)

    def start(self):
        executor.start_polling(self._dp, skip_updates=True)

    def run(self):
        pass
