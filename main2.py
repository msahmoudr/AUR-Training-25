from time import time
from rich.console import Console

console = Console()


def send_Msg(msg):
    if isinstance(msg, BaseMsg):
        console.print(msg, style=msg.style)
    else:
        print(msg)


class BaseMsg:
    def __init__(self, data: str):
        self._data = data

    @property
    def style(self):
        return ''  # BaseMsg-specific: no special styling

    @property
    def data(self):
        return self._data

    def __str__(self):
        return self._data

    def __len__(self):
        return len(str(self))

    def __eq__(self, other):
        if isinstance(other, BaseMsg):
            return str(self) == str(other)
        return False

    def __add__(self, other):
        if isinstance(other, BaseMsg):
            new_data = str(self) + str(other)
        elif isinstance(other, str):
            new_data = str(self) + other
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'BaseMsg' and '{type(other).__name__}'")

        # Return new instance of the same class
        return self.__class__(new_data)


class LogMsg(BaseMsg):
    def __init__(self, data):
        super().__init__(data)
        self._timestamp = int(time())

    @property
    def style(self):
        return "on yellow"  # Yellow background

    def __str__(self):
        return f'[{self._timestamp}] {self._data}'


class WarnMsg(LogMsg):
    @property
    def style(self):
        return "white on red"  # White text on red background

    def __str__(self):
        return f'[WARN][{self._timestamp}] {self._data}'


# Test code
if __name__ == '__main__':
    m1 = BaseMsg('Normal message')
    m2 = LogMsg('Log message')
    m3 = WarnMsg('Warning message')

    send_Msg(m1)
    send_Msg(m2)
    send_Msg(m3)

    # Test addition operations
    m4 = m2 + " additional text"
    send_Msg(m4)

    m5 = m3 + m2  # Warning + Log
    send_Msg(m5)

    # Test equality
    print(f"Length of m2: {len(m2)}")
    print(f"m2 == m3: {m2 == m3}")