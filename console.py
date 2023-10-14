#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt ='(hbnb) '
    
    def do_quit(self, line):
        """exit the program"""
        return True

    def do_EOF(self, line):
        """exit with ctrl-D"""
        return True
    
    def emptyline(self):
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
