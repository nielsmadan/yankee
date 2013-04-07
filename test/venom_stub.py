import sys
import types

if 'venom' not in sys.modules:
    _venom_stub = types.ModuleType('Dummy Vim Module', "Dummy")
    sys.modules['venom'] = _venom_stub

    import venom
    venom.get_current_line = lambda *args, **kwargs: None
    venom.nnoremap = lambda *args, **kwargs: None
    venom.vnoremap = lambda *args, **kwargs: None
    venom.py_fn_to_vim_command = lambda *args, **kwargs: None
