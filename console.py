#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {"BaseModel"}

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval("{}()".format(args[0]))
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """ Prints the string representation of an instance,
        based on the class name and id"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in models.storage.all().keys():
                    print("** no instance found **")

                else:
                    print(models.storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")

        cls_name = args[0]
        obj_id = args[1]

        if cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")

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
        if len(args) <= 1:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for key, obj in objs.items():
                    if key.startswith(args[0]):
                        obj_list.append(str(obj))
                print(obj_list)
        else:
            for obj in objs.values():
                obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        cls_name = args[0]
        obj_id = args[1]

        if cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(cls_name, obj_id)
        objs = models.storage.all()
        if key not in objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")

            attr_name = args[2]
            attr_value = args[3]

            instance = objs[key]

            attr_value = BaseModel.deserialize_type(attr_value)
            setattr(instance, attr_name, attr_value)
            instance.save()

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
