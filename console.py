#!/usr/bin/python3
"""
This module introduces a new class.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class introduces the entry point of the command 
    line interpreter.
    """

    prompt = "(hbnb)"

    def do_quit(self, args):
        """
        This command exits from the command interpreter.
        """

        return True

    def do_EOF(self, args):
        """
        This command exits the program using ctrl + D.
        """

        print()
        return True

    def emptyline(self):
        """
        command does nothing when an empty line is entered.
        """

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
