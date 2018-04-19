"""This file contains custom simple implementation of python3.6 interpreter"""

import types
import dis
import sys
import os.path


class VirtualMachine:

    class CodeBlock:

        def __init__(self, instruction):
            self.name = None
            self.constant_table = []
            self.num_instructions = instruction.arg / 2
            self.instructions = []



    def __init__(self):
        if __name__ == "__main__":
            self.builtins = globals()["__builtins__"].__dict__
        else:
            self.builtins = globals()["__builtins__"]
        self.globals = globals()
        self.locals = {}
        self.stack = []

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
        return result

    def get_step_by_argval(self, argval):
        step = argval // 2 - 1
        return step

    def run_code(self, code):
        if isinstance(code, types.CodeType):
            code_obj = code
        elif isinstance(code, str):
            code_obj = compile(code, '<test>', 'exec')
        else:
            raise TypeError

        instructions = list(dis.get_instructions(code_obj))
        step = 0
        while step < len(instructions):
            instruction = instructions[step]

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

            elif instruction.opname == "CALL_FUNCTION_EX":
                if instruction.arg == 0:
                    kwargs = {}
                    args = self.stack.pop()
                elif instruction.arg == 1:
                    kwargs = self.stack.pop()
                    args = self.stack.pop()
                else:
                    raise Exception("Unknown instruction.arg in CALL_FUNCTION_EX")
                func = self.stack.pop()
                retval = func(*args, **kwargs)
                self.stack.append(retval)

            elif instruction.opname == "RETURN_VALUE":
                pass
                # TODO
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
            elif instruction.opname.startswith("BUILD_"):
                count = instruction.arg
                if instruction.opname.endswith(("_LIST", "_TUPLE", "_SET")):
                    result = []
                    for _ in range(count):
                        result.insert(0, self.stack.pop())
                    if instruction.opname == "BUILD_LIST":
                        self.stack.append(result)
                    elif instruction.opname == "BUILD_TUPLE":
                        self.stack.append(tuple(result))
                    elif instruction.opname == "BUILD_SET":
                        self.stack.append(set(result))
                    else:
                        raise Exception("Unknown type of container")
                # elif instruction.opname == "BUILD_MAP":
                #     result = {}
                #     for _ in range(count):
                #         key = self.stack.pop()
                #         value = self.stack.pop()
                #         result[key] = value
                #     self.stack.append(result)
                elif instruction.opname == "BUILD_CONST_KEY_MAP":
                    items = []
                    keys = self.stack.pop()
                    for key in reversed(keys):
                        value = self.stack.pop()
                        items.insert(0, (key, value))
                    result = dict(items)
                    self.stack.append(result)
                elif instruction.opname == "BUILD_SLICE":
                    arg1 = self.stack.pop()
                    arg2 = self.stack.pop()
                    if instruction.arg == 2:
                        self.stack.append(slice(arg2, arg1))
                    elif instruction.arg == 3:
                        arg3 = self.stack.pop()
                        self.stack.append(slice(arg3, arg2, arg1))
                    else:
                        raise  Exception("Unknown instruction.arg in BUILD_SLICE")
                else:
                    raise Exception("Unknown type of container")

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

            elif instruction.opname == "GET_ITER":
                arg = self.stack.pop()
                result = iter(arg)
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

            #  Operations with jumps (logical, for, etc)
            elif instruction.opname == "JUMP_IF_TRUE_OR_POP":
                top = self.stack.pop()
                if top:
                    step = self.get_step_by_argval(instruction.argval)
                    self.stack.append(top)

            elif instruction.opname == "JUMP_IF_FALSE_OR_POP":
                top = self.stack.pop()
                if not top:
                    step = self.get_step_by_argval(instruction.argval)
                    self.stack.append(top)

            elif instruction.opname == "POP_JUMP_IF_TRUE":
                top = self.stack.pop()
                if top:
                    step = self.get_step_by_argval(instruction.argval)

            elif instruction.opname == "POP_JUMP_IF_FALSE":
                top = self.stack.pop()
                if not top:
                    step = self.get_step_by_argval(instruction.argval)

            elif instruction.opname == "JUMP_FORWARD":
                step = self.get_step_by_argval(instruction.argval)

            elif instruction.opname == "JUMP_ABSOLUTE":
                step = self.get_step_by_argval(instruction.argval)

            elif instruction.opname == "FOR_ITER":
                top = self.stack[-1]
                try:
                    elem = top.__next__()
                    self.stack.append(elem)
                except StopIteration:
                    self.stack.pop()
                    step = self.get_step_by_argval(instruction.argval)

            elif instruction.opname == "SETUP_LOOP":
                pass
                # TODO

            elif instruction.opname == "POP_BLOCK":
                pass
                # TODO

            else:
                raise Exception("Unsupported instruction")

            step += 1

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
