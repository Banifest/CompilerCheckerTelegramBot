from dataclasses import dataclass
from typing import Tuple


@dataclass
class Feature:
    featureName: str
    reference: str
    version: str
    compilerSupport: Tuple[str]
