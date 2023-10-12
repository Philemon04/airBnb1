#!/usr/bin/python3

import cmd

from models.base_model import BaseModel
from models.engine import file_storage

classes = {"BaseModel": BaseModel}
class HBNBCommand(cmd.Cmd):
    prompt = '(hnhb)'

    def do_quit(self, arg):
        """Exits CLI

        @rtype: object
        """
        print()
        return True

    def do_eof(self, arg):
        """Exits CLI

        @rtype: object
        """
        return True
    def do_create(self, args):

        arg = args.split()

        if arg<=0:
            print('** class name missing **')

        if arg in classes:
            new_dict = arg[1:]
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
        instance.save()




if __name__ == '__main__':
    HBNBCommand().cmdloop()
