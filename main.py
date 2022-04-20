"""Counter of key pressed."""
import pyxhook
import os


class Counter:
    """Counter."""

    def __init__(self):
        self.__total = 0
        self.__symbols = 0
        self.__navi = 0
        self.__clear_command = 'clear'

    def on_key_press(self, event):
        """Update counter and output current value."""
        if 'mouse' in str(event):
            return

        self.__total += 1

        if is_symbol(event_get_key(event)):
            self.__symbols += 1

        if is_navi(event_get_key(event)):
            self.__navi += 1

        self.__clear_output()
        self.__print_value()

    def __clear_output(self):
        os.system(self.__clear_command)

    def __print_value(self):
        other = self.__total - self.__symbols - self.__navi

        print(f"  total: {self.__total}")
        print(f"symbols: {self.__symbols}")
        print(f"   navi: {self.__navi}")
        print(f"  other: {other}")


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


def event_get_key(event):
    return event.Key


def main():
    """Entry point."""

    hook_man = pyxhook.HookManager()
    hook_man.KeyDown = Counter().on_key_press
    hook_man.start()


if __name__ == '__main__':
    main()
