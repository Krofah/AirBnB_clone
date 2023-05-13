#!/usr/bin/python3
import cmd
import json
from datetime import datetime
import sys
""" Class Definition class HBNBCommand(cmd.Cmd):"""


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command  to exit the program"""
        return True

    def do_EOF(self, arg):
        """ EXit on EOF"""
        print("")
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
