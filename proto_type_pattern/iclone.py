from abc import ABC, abstractmethod


# Prototype Interface
class IClone(ABC):
    @abstractmethod
    def clone(self):
        pass
