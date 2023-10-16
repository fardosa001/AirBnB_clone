#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import models
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {"BaseModel", "User", "City", "State",
               "Amenity", "Place", "Review"}

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """ Prints the string representation of an instance,
        based on the class name and id"""

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objs = models.storage.all()
        name = "{}.{}".format(args[0], args[1])
        if name in objs:
            print(objs[name])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        elif len(args) == 1:
            print("** instance id missing **")
            return

        cls_name = args[0]
        obj_id = args[1]

        if cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        else:
            name = "{}.{}".format(cls_name, obj_id)
            objects = models.storage.all()
            if name in objects:
                del objects[name]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """ Prints all string representation of all instances,
        based or not on the class name."""
        args = line.split()
        objs = models.storage.all()
        obj_list = []
        if len(args) == 1:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for key, obj in objs.items():
                    if key.startswith(args[0]):
                        obj_list.append(obj.__str__())
                print(obj_list)
        else:
            for obj in objs.values():
                obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""

        args = tuple(line.split())
        if len(args) == 0:
            print("** class name missing **")
            return

        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        elif len(args) == 1:
            print("** instance id missing **")
            return

        elif len(args) < 3:
            print("** attribute name missing **")
            return

        elif len(args) < 4:
            print("** value missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objs = models.storage.all()
        if key not in objs:
            print("** no instance found **")
            return

        attr_name = args[2]
        attr_value = args[3]
        instance = objs[key]

        try:
            value = eval(attr_value)
        except Exception:
            value = attr_value
        setattr(instance, attr_name, value)
        models.storage.save()

    def do_quit(self, line):
        """exit the program"""
        return True

    def do_EOF(self, line):
        """exit with ctrl-D"""
        return True

    def emptyline(self):
        """no command executed"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
