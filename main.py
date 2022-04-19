"""Counter of key pressed."""
import pyxhook
import os


class Counter:
    """Counter."""

    def __init__(self):
        self.__counter = 0
        self.__clear_command = 'clear'

    def on_key_press(self, event):
        """Update counter and output current value."""
        if 'mouse' in str(event):
            return

        self.__counter += 1
        self.__clear_output()
        self.__print_value()

    def __clear_output(self):
        os.system(self.__clear_command)

    def __print_value(self):
        print(f"keys total: {self.__counter}")


def main():
    """Entry point."""

    hook_man = pyxhook.HookManager()
    hook_man.KeyDown = Counter().on_key_press
    hook_man.start()


if __name__ == '__main__':
    main()
