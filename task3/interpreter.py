"""This file contains custom simple implementation of python3.6 interpreter"""

import types
import dis
import sys
import os.path


class VirtualMachine:

    def __init__(self):
        if __name__ == "__main__":
            self.builtins = globals()["__builtins__"].__dict__
        else:
            self.builtins = globals()["__builtins__"]
        self.globals = globals()
        self.locals = {}
        self.stack = []
        self.jump_to = None

    def find_instance_by_name(self, name):
        if name in self.locals:
            instance = self.locals[name]
            namespace = self.locals
        elif name in self.globals:
            instance = self.globals[name]
            namespace = self.globals
        elif name in self.builtins:
            instance = self.builtins[name]
            namespace = self.builtins
        else:
            raise NameError
        return instance, namespace

    def __str__(self):
        result = "Locals: " + str(self.locals)
        result += " |  stack: " + str(self.stack)
        result += " | jump_to: " + str(self.jump_to)
        return result

    def run_code(self, code):
        if isinstance(code, types.CodeType):
            code_obj = code
        elif isinstance(code, str):
            code_obj = compile(code, '<test>', 'exec')
        else:
            raise TypeError

        for instruction in dis.get_instructions(code_obj):
            if self.jump_to and self.jump_to != instruction.offset:
                continue
            else:
                self.jump_to = None

            if instruction.opname == "LOAD_CONST":
                self.stack.append(instruction.argval)

            elif instruction.opname == "LOAD_NAME":
                name = instruction.argval
                value, namespace = self.find_instance_by_name(name)
                self.stack.append(value)

            elif instruction.opname == "CALL_FUNCTION":
                args = []
                for _ in range(instruction.arg):
                    args.insert(0, self.stack.pop())
                func = self.stack.pop()
                retval = func(*args)
                self.stack.append(retval)

            elif instruction.opname == "CALL_FUNCTION_KW":
                args = []
                kwargs = {}
                key_words = self.stack.pop()
                for key_word in reversed(key_words):
                    kwargs[key_word] = self.stack.pop()
                for _ in range(instruction.arg - len(kwargs)):
                    args.insert(0, self.stack.pop())
                func = self.stack.pop()
                retval = func(*args, **kwargs)
                self.stack.append(retval)

            elif instruction.opname == "RETURN_VALUE":
                pass
                # self.stack.append(instruction.argval)

            elif instruction.opname == "POP_TOP":
                self.stack.pop()

            elif instruction.opname == "STORE_NAME":
                name = instruction.argval
                value = self.stack.pop()
                self.locals[name] = value

            elif instruction.opname == "DUP_TOP":
                value = self.stack[-1]
                self.stack.append(value)

            elif instruction.opname == "UNPACK_SEQUENCE":
                # count = instruction.arg
                values = self.stack.pop()
                for value in reversed(values):
                    self.stack.append(value)

            #  Build containers
            elif instruction.opname == "BUILD_TUPLE":
                count = instruction.arg
                result = []
                for _ in range(count):
                    result.insert(0, self.stack.pop())
                self.stack.append(tuple(result))

            elif instruction.opname == "BUILD_LIST":
                count = instruction.arg
                result = []
                for _ in range(count):
                    result.insert(0, self.stack.pop())
                self.stack.append(result)

            #  Comparison operators
            elif instruction.opname == "COMPARE_OP":
                arg2 = self.stack.pop()
                arg1 = self.stack.pop()
                if instruction.argval == '==':
                    result = arg1 == arg2
                elif instruction.argval == '!=':
                    result = arg1 != arg2
                elif instruction.argval == '>':
                    result = arg1 > arg2
                elif instruction.argval == '<':
                    result = arg1 < arg2
                elif instruction.argval == '>=':
                    result = arg1 >= arg2
                elif instruction.argval == '<=':
                    result = arg1 <= arg2
                elif instruction.argval == 'in':
                    result = arg1 in arg2
                elif instruction.argval == 'not in':
                    result = arg1 not in arg2
                elif instruction.argval == 'is':
                    result = arg1 is arg2
                elif instruction.argval == 'is not':
                    result = arg1 is not arg2
                else:
                    raise Exception("Unsupported comparison operator")
                self.stack.append(result)

            #  Unary operations
            elif instruction.opname.startswith("UNARY_"):
                arg = self.stack.pop()
                if instruction.opname == "UNARY_POSITIVE":
                    result = +arg
                elif instruction.opname == "UNARY_NEGATIVE":
                    result = -arg
                elif instruction.opname == "UNARY_NOT":
                    result = not arg
                elif instruction.opname == "UNARY_INVERT":
                    result = ~arg
                else:
                    raise Exception("Unsupported unary operator")
                self.stack.append(result)

            #  Binary and inplace operations
            elif instruction.opname.startswith(("BINARY_", "INPLACE_")):
                arg2 = self.stack.pop()
                arg1 = self.stack.pop()
                if instruction.opname.endswith("_ADD"):
                    result = arg1 + arg2
                elif instruction.opname.endswith("_SUBTRACT"):
                    result = arg1 - arg2
                elif instruction.opname.endswith("_MULTIPLY"):
                    result = arg1 * arg2
                elif instruction.opname.endswith("_POWER"):
                    result = arg1 ** arg2
                elif instruction.opname.endswith("_FLOOR_DIVIDE"):
                    result = arg1 // arg2
                elif instruction.opname.endswith("_TRUE_DIVIDE"):
                    result = arg1 / arg2
                elif instruction.opname.endswith("_MODULO"):
                    result = arg1 % arg2
                elif instruction.opname.endswith("_SUBSCR"):
                    result = arg1[arg2]
                elif instruction.opname.endswith("_LSHIFT"):
                    result = arg1 << arg2
                elif instruction.opname.endswith("_RSHIFT"):
                    result = arg1 >> arg2
                elif instruction.opname.endswith("_AND"):
                    result = arg1 & arg2
                elif instruction.opname.endswith("_XOR"):
                    result = arg1 ^ arg2
                elif instruction.opname.endswith("_OR"):
                    result = arg1 | arg2
                elif instruction.opname.endswith("_MATRIX_MULTIPLY"):
                    result = arg1 @ arg2
                else:
                    raise Exception("Unsupported binary (or inplace) operator")
                self.stack.append(result)

            #  Logical operations and cases
            elif instruction.opname == "JUMP_IF_TRUE_OR_POP":
                top = self.stack.pop()
                if top:
                    self.jump_to = instruction.argval
                    self.stack.append(top)

            elif instruction.opname == "JUMP_IF_FALSE_OR_POP":
                top = self.stack.pop()
                if not top:
                    self.jump_to = instruction.argval
                    self.stack.append(top)

            elif instruction.opname == "POP_JUMP_IF_TRUE":
                top = self.stack.pop()
                if top:
                    self.jump_to = instruction.argval

            elif instruction.opname == "POP_JUMP_IF_FALSE":
                top = self.stack.pop()
                if not top:
                    self.jump_to = instruction.argval

            elif instruction.opname == "JUMP_FORWARD":
                self.jump_to = instruction.argval



            else:
                raise Exception("Unsupported instruction")

        return None


if __name__ == "__main__":
    vm = VirtualMachine()
    print("Using custom VirtualMachine as python3.6 interpreter...")
    if len(sys.argv) != 2:
        print("Rule of using:\n$ python interpreter.py <file_to_execute.py>")
        exit()
    file_name = sys.argv[-1]
    if not os.path.isfile(file_name):
        print("Rule of using:\n$ python interpreter.py <file_to_execute.py>")
        print("Please, select an existing file to interpret")
        exit()
    with open(file_name, "r") as file:
        file_content = "".join(file.readlines())
    vm.run_code(file_content)
