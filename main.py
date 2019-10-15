import logging
from typing import Final

from src.bot.bot_dispatcher import BotDispatcher
from src.dispatcher.parser import Parser
from src.helper.config.config import Config
from src.helper.config.config_processor import ConfigProcessor

Parser().parse()

if __name__ == "__main__":
    # Config parse
    config_processor: ConfigProcessor = ConfigProcessor()
    config_processor.parse_config(file_path="..\\")
    config: Final[Config] = config_processor.config

    # Setup and run bot
    bot_dispatcher = BotDispatcher(
        api_token=config.botSetting.apiToken,
        logging_level=logging.DEBUG
    )
    bot_dispatcher.start()
else:
    raise ImportError("Module cannot be imported")
