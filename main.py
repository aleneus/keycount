"""Counter of key pressed."""
import pyxhook
import os


def main():
    """Entry point."""

    hook_man = pyxhook.HookManager()
    hook_man.KeyDown = Handler().on_key_press
    hook_man.start()


class Handler:
    """Handler."""

    def __init__(self):
        self.__cnt = Counters()
        self.__clear_command = 'clear'
        self.__print()

    def on_key_press(self, event):
        """Update counters and output current values."""
        self.__update_counters(event)
        self.__print()

    def __update_counters(self, event):
        self.__cnt.total += 1

        if is_symbol(event.Key):
            self.__cnt.symbols += 1

        if is_navi(event.Key):
            self.__cnt.navi += 1

    def __print(self):
        self.__clear_console()

        sm_pc = self.__cnt.sm_pc()
        nv_pc = self.__cnt.nv_pc()
        oth_pc = round(100 - sm_pc - nv_pc, 2)

        print(f"     total: {self.__cnt.total}")
        print(f"   symbols: {self.__cnt.symbols} {sm_pc}%")
        print(f"navigation: {self.__cnt.navi} {nv_pc}%")
        print(f"     other: {self.__cnt.other()} {oth_pc}%")

    def __clear_console(self):
        os.system(self.__clear_command)


def is_navi(key):
    return key in [
        'Up', 'Down', 'Left', 'Right', 'Home', 'End', 'Page_Up', 'Page_Down'
    ]


def is_symbol(key):
    if key.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return True

    if key in "`1234567890":
        return True

    if key in [
            'grave',
            'asciitilde',
            'exclam',
            'at',
            'numbersign',
            'dollar',
            'percent',
            'asciicircum',
            'ampersand',
            'asterisk',
            'parenleft',
            'parenright',
            'minus',
            'underscore',
            'equal',
            'plus',
            'comma',
            'less',
            'period',
            'greater',
            'slash',
            'question',
            'backslash',
            'bar',
            'bracketleft',
            'braceleft',
            'bracketright',
            'braceright',
            'apostrophe',
            'quotedbl',
    ]:
        return True

    if key in ["Return", "space"]:
        return True

    return False


class Counters:
    """Counters of different keys."""

    def __init__(self):
        self.total = 0
        self.symbols = 0
        self.navi = 0

    def other(self):
        res = self.total
        res -= self.symbols
        res -= self.navi

        return res

    def sm_pc(self):
        if self.total == 0:
            return 0

        return round(100 * self.symbols / self.total, 2)

    def nv_pc(self):
        if self.total == 0:
            return 0

        return round(100 * self.navi / self.total, 2)


if __name__ == '__main__':
    main()
