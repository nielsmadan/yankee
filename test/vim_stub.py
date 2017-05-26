import sys
import types

import flexmock

if 'vim' not in sys.modules:
    _vim_stub = types.ModuleType('Dummy Vim Module', "Dummy")
    sys.modules['vim'] = _vim_stub

    import vim
    vim.command = lambda *args, **kwargs: None
    vim.eval = lambda *args, **kwargs: None

    class _dummy_opt(object):
        filetype = None

    vim.opt = _dummy_opt

    class _dummy_map(object):
        @staticmethod
        def nnoremap(*args, **kwargs):
            return None

        @staticmethod
        def vnoremap(*args, **kwargs):
            return None

    vim.map = _dummy_map

    class _dummy_g(object):
        def __contains__(self, name):
            return False

    vim.g = _dummy_g()

    class _dummy_current(object):
        def __init__(self):
            self.buffer = ''

    vim.current = _dummy_current()

    class _dummy_registers(object):
        @staticmethod
        def copy(_, __):
            pass

    vim.registers = _dummy_registers
