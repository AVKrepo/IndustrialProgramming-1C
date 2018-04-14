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
        self.consts = []
        self.names = []

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

    def run_code(self, code):
        if isinstance(code, types.CodeType):
            code_obj = code
        elif isinstance(code, str):
            code_obj = compile(code, '<test>', 'exec')
        else:
            raise TypeError

        for instruction in dis.get_instructions(code_obj):
            if instruction.opname == "LOAD_CONST":
                self.consts.append(instruction.argval)

            if instruction.opname == "LOAD_NAME":
                self.names.append(instruction.argval)

            if instruction.opname == "CALL_FUNCTION":
                func_name = self.names.pop()
                func, namespace = self.find_instance_by_name(func_name)
                args = []
                for _ in range(instruction.arg):
                    args.insert(0, self.consts.pop())
                retval = func(*args)
                self.consts.append(retval)

            if instruction.opname == "CALL_FUNCTION_KW":
                func_name = self.names.pop()
                func, namespace = self.find_instance_by_name(func_name)
                args = []
                kwargs = {}
                key_words = self.consts.pop()
                for key_word in reversed(key_words):
                    kwargs[key_word] = self.consts.pop()
                for _ in range(instruction.arg - len(kwargs)):
                    args.insert(0, self.consts.pop())
                retval = func(*args, **kwargs)
                self.consts.append(retval)

            if instruction.opname == "RETURN_VALUE":
                self.consts.append(instruction.argval)

            if instruction.opname == "POP_TOP":
                self.consts.pop()

        return None


if __name__ == "__main__":
    vm = VirtualMachine()
