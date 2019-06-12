# coding=utf-8
import os
from typing import Optional

import jsonpickle

from src.helper.config.config import Config
from src.helper.pattern.singleton import Singleton


class ConfigProcessor(metaclass=Singleton):
    _config: Config

    __CURRENT_DIR: str = ".\\"
    __CONFIG_FILE_NAME: str = "config.json"
    __BOT_SETTING: str = "botSetting"

    def __init__(self):
        self._config = Config()

    def _create_standard_config(self, file_path: str):
        config_file = open(file_path, mode="w")
        config_file.write(jsonpickle.encode(self._config, unpicklable=False))
        config_file.close()

    @property
    def config(self) -> Config:
        return self._config

    def parse_config(self, file_path: Optional[str] = None):
        local_file_path: str = "{0}{1}".format(file_path or self.__CURRENT_DIR, self.__CONFIG_FILE_NAME)
        if os.path.exists(local_file_path):
            config_file = open(local_file_path)
            parsed_config = jsonpickle.decode(config_file.read())
            self._config.botSetting = Config.BotSetting(**parsed_config[ConfigProcessor.__BOT_SETTING])
            config_file.close()
        else:
            self._create_standard_config(file_path=local_file_path)
