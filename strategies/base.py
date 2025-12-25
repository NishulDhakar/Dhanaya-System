from abc import ABC, abstractmethod
from typing import Dict
import pandas as pd


class Strategy(ABC):
    @abstractmethod
    def generate_signal(self, data: pd.DataFrame) -> Dict[str, str]:
        pass
