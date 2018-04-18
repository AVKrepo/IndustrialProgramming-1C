import io
import sys
from contextlib import redirect_stdout, redirect_stderr

import interpreter


def compare_outputs(code):
    vm = interpreter.VirtualMachine()
    vm_stdout = io.StringIO()
    vm_stderr = io.StringIO()
    with redirect_stdout(vm_stdout), redirect_stderr(vm_stderr):
        try:
            vm.run_code(code)
        except Exception:
            pass

    exec_stdout = io.StringIO()
    exec_stderr = io.StringIO()
    with redirect_stdout(exec_stdout), redirect_stderr(exec_stderr):
        try:
            exec(code)
        except Exception:
            pass

    if vm_stderr.getvalue() != exec_stderr.getvalue():
        print("Stderr is different:", file=sys.stderr)
        print("-----vm_stderr-----", file=sys.stderr)
        print(vm_stderr.getvalue(), file=sys.stderr)
        print("----exec_stderr----", file=sys.stderr)
        print(exec_stderr.getvalue(), file=sys.stderr)
        print(file=sys.stderr)

    if vm_stdout.getvalue() != exec_stdout.getvalue():
        print("Stdout is different:")
        print("-----vm_stdout-----")
        print(vm_stdout.getvalue())
        print("----exec_stdout----")
        print(exec_stdout.getvalue())
        print()

    assert vm_stderr.getvalue() == exec_stderr.getvalue()
    assert vm_stdout.getvalue() == exec_stdout.getvalue()

    print("End of compare_outputs")
    return True
