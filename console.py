#!/usr/bin/python3
"""console module"""
import cmd
import json
from datetime import datetime
import sys
import json


class HBNBCommand(cmd.Cmd):
    """ Class Definition class HBNBCommand(cmd.Cmd):"""
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

    def do_create(self, arg):
        if arg:
            if arg != "BaseModel":
                print(" ** class doesn't exist ** ")
            else:
                instance_name = 'data.json'
                with open(instance_name, "w") as json_file:
                    json.dump(arg, json_file)
                    print(id_name)
        else:
            print(" **class name missing** ")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
