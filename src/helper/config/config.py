# coding=utf-8
from dataclasses import dataclass


@dataclass
class Config:
    @dataclass
    class BotSetting:
        APIToken: str = ""

    botSetting: BotSetting = BotSetting()
