#!/usr/bin/python3
import cmd
import json
from datetime import datetime
import sys
""" Class Definition class HBNBCommand(cmd.Cmd):"""
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command  to exit the program"""
        return True

    def do_EOF(self, arg):
        """ EXit on EOF"""
        print("")
        return True
    def emptyline(self, arg):
        """an empty line + ENTER shouldn’t execute anything"""
        pass
if __name__ == "__main__":
    HBNBCommand().cmdloop()
 
    def do_create(self):
        """Instance that saves it (to json file) and print the id . EX:$"""
        self.id = str(datetime.now().timestamps())
if len(sys.argv) < 3:
    print("** class name missing **")
else:
    class_name = sys.argv[2]
    try:
        if class_name not in globalS();
        print("** class doesn't exist **")
    else:
        model = BaseModel()
date = {"id",model.id}
save_filr = open("BaseModel.json","w")
json.dump(date ,save_file, indent = 6)
save_file.close()
print(model.id)
except KeyError:
    print
