from rich.console import Console
from time import time
from time import sleep
 
console = Console()


def send_message(message):

    if isinstance(message, BaseMessage):
        console.print(message, style=message.get_style())
    else:
        print(str(message))


class BaseMessage:
    def __init__(self, message_data):
        self._message_data = message_data
        self._style_data = ""
    def get_data(self):
        return self._message_data
    def set_data(self, new_data):
        self._message_data = new_data

    def get_style(self):

        return self._style_data

    def set_style(self, style) :
        self._style_data = style

    def __str__(self) :
        return self._message_data

    def __len__(self):
        return len(str(self))

    def __eq__(self, other) :
        if isinstance(other, BaseMessage):
            if str(self) == str(other):
                return True
            else: return False
        return False

    def __add__(self, other):
        if isinstance(other, BaseMessage):
            totaldata = str(self) + str(other)
        elif isinstance(other, str):
            totaldata = str(self) + other
        else:
            raise TypeError("Cannot find BaseMessage to add ")

        newMessage = self.__class__(totaldata)
        newMessage.set_style(self.get_style())
        return newMessage







class LogMessage(BaseMessage):
    def __init__(self, message_data):
        super().__init__(message_data)
        self.set_style("bold yellow on blue")



class WarningMessage(LogMessage):
    def __init__(self, message_data: str):
        super().__init__(message_data)
        self.set_style("bold white on red")
        self._timestamp = int(time())

    def get_timestamp(self):

        return self._timestamp

    def set_timestamp(self, new_timestamp: int) :
        self._timestamp = new_timestamp

    def __str__(self) -> str:

        return f'[WARNING {self.get_timestamp()}] {self.get_data()}'


class Bluetooth(BaseMessage):
    def __init__(self, message_data):
        super().__init__(message_data)
        self.set_style("bold green on black")

    def __str__(self) -> str:

        return self.get_data()
class Dania_Zaki(BaseMessage):
    def __init__(self, message_data):
        super().__init__(message_data)
        self.set_style("bold white on purple")

    def __str__(self) -> str:
        return self.get_data()



if __name__ == '__main__':


    base_msg = BaseMessage("Hello world")
    log_msg = LogMessage("logged in")
    warn_msg = WarningMessage("Disk space running low")
    mb_msg = Bluetooth("bluetooth connected successfully")
    Apology_msg =Dania_Zaki("Sorry AUR for the late submission")

    print("Base message:")
    send_message(base_msg)

    print("\nLog message:")
    send_message(log_msg)
    print("\nwarning Message:")
    send_message(warn_msg)

    print("\nBluetooth message:")
    send_message(mb_msg)
    print("\nMY APOLOCHEESE 🙏:")
    send_message(Apology_msg)
    sleep(10)

