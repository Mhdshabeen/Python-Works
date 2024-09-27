
from abc import ABC,abstractmethod


class editor(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def debug(self):
        pass

class Vscode(editor):

    def open(self):
        print("Abstraction of open method")

    def execute(self):
        print("Abstraction method of execute")

    def debug(self):
        print("Abstraction of debug method")