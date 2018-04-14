"""This file contains custom simple implementation of python3.6 interpreter"""

import types
import dis


class VirtualMachine:

    def __init__(self):
        if __name__ == "__main__":
            self.builtins = globals()["__builtins__"].__dict__
        else:
            self.builtins = globals()["__builtins__"]
        self.globals = globals()
        self.locals = {}
        self.stack = []
        self.is_jump = False

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
        result += " | is_jump: " + str(self.is_jump)
        return result

    def run_code(self, code):
        if isinstance(code, types.CodeType):
            code_obj = code
        elif isinstance(code, str):
            code_obj = compile(code, '<test>', 'exec')
        else:
            raise TypeError

        for instruction in dis.get_instructions(code_obj):
            if self.is_jump:
                if instruction.is_jump_target:
                    self.is_jump = False
                else:
                    continue

            if instruction.opname == "LOAD_CONST":
                self.stack.append(instruction.argval)

            if instruction.opname == "LOAD_NAME":
                name = instruction.argval
                value, namespace = self.find_instance_by_name(name)
                self.stack.append(value)

            if instruction.opname == "CALL_FUNCTION":
                args = []
                for _ in range(instruction.arg):
                    args.insert(0, self.stack.pop())
                func = self.stack.pop()
                retval = func(*args)
                self.stack.append(retval)

            if instruction.opname == "CALL_FUNCTION_KW":
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

            if instruction.opname == "RETURN_VALUE":
                pass
                # self.stack.append(instruction.argval)

            if instruction.opname == "POP_TOP":
                self.stack.pop()

            if instruction.opname == "STORE_NAME":
                name = instruction.argval
                value = self.stack.pop()
                self.locals[name] = value

            if instruction.opname == "DUP_TOP":
                value = self.stack[-1]
                self.stack.append(value)

            if instruction.opname == "UNPACK_SEQUENCE":
                # count = instruction.arg
                values = self.stack.pop()
                for value in reversed(values):
                    self.stack.append(value)

            """Unary operations"""
            if instruction.opname.startswith("UNARY_"):
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
                    raise Exception()
                self.stack.append(result)

            """Binary operations"""
            if instruction.opname.startswith("BINARY_"):
                arg2 = self.stack.pop()
                arg1 = self.stack.pop()
                if instruction.opname == "BINARY_ADD":
                    result = arg1 + arg2
                elif instruction.opname == "BINARY_SUBTRACT":
                    result = arg1 - arg2
                elif instruction.opname == "BINARY_MULTIPLY":
                    result = arg1 * arg2
                elif instruction.opname == "BINARY_POWER":
                    result = arg1 ** arg2
                elif instruction.opname == "BINARY_FLOOR_DIVIDE":
                    result = arg1 // arg2
                elif instruction.opname == "BINARY_TRUE_DIVIDE":
                    result = arg1 / arg2
                elif instruction.opname == "BINARY_MODULO":
                    result = arg1 % arg2
                elif instruction.opname == "BINARY_SUBSCR":
                    result = arg1[arg2]
                elif instruction.opname == "BINARY_LSHIFT":
                    result = arg1 << arg2
                elif instruction.opname == "BINARY_RSHIFT":
                    result = arg1 >> arg2
                elif instruction.opname == "BINARY_AND":
                    result = arg1 & arg2
                elif instruction.opname == "BINARY_XOR":
                    result = arg1 ^ arg2
                elif instruction.opname == "BINARY_OR":
                    result = arg1 | arg2
                elif instruction.opname == "BINARY_MATRIX_MULTIPLY":
                    result = arg1 @ arg2
                else:
                    raise Exception()
                self.stack.append(result)

            """Logic operations"""
            if instruction.opname == "JUMP_IF_TRUE_OR_POP":
                top = self.stack.pop()
                if top:
                    self.is_jump = True
                    self.stack.append(top)

            if instruction.opname == "JUMP_IF_FALSE_OR_POP":
                top = self.stack.pop()
                if not top:
                    self.is_jump = True
                    self.stack.append(top)

            # if instruction.opname == "JUMP_IF_TRUE_OR_POP":

        return None


if __name__ == "__main__":
    vm = VirtualMachine()
    print(vm)
