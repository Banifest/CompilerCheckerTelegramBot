from src.bot.bot_dispatcher import BotDispatcher
from src.helper.config.config import Config
from src.helper.config.config_processor import ConfigProcessor

if __name__ == "__main__":
    # Config parse
    config_processor: ConfigProcessor = ConfigProcessor()
    config_processor.parse_config(file_path="..\\")
    config: Config = config_processor.config

    # Setup and run bot
    bot_dispatcher = BotDispatcher(api_token=config.botSetting.APIToken)
    bot_dispatcher.start()
else:
    raise ImportError("Module cannot be imported")
