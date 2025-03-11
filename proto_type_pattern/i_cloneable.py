from abc import ABC, abstractmethod


# Prototype Interface
class ICloneable(ABC):
    @abstractmethod
    def clone(self):
        pass
