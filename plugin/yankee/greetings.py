import vim

def append_hello_world():
    vim.current.buffer.append(_get_greeting())

def _get_greeting():
    return "Hello World"
