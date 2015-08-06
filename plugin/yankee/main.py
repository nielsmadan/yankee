import vim

def get_lock_register():
    return "o"

def lock_paste_register():
    lock_register = get_lock_register()

    vim.registers.copy("\"", lock_register)

    map_paste_commands()

def unlock_paste_register():
    unmap_paste_commands()

def map_paste_commands():
    vim.map.nnoremap("p", "\"op")
    vim.map.nnoremap("P", "\"oP")

def unmap_paste_commands():
    vim.map.nnoremap("p", "p")
    vim.map.nnoremap("P", "P")
