import vim

def map_paste_commands():
    vim.map.nnoremap("p", "\"op")
    vim.map.nnoremap("P", "\"oP")

def unmap_paste_commands():
    vim.map.nnoremap("p", "p")
    vim.map.nnoremap("P", "P")

class Yankee(object):
    def __init__(self):
        self.register_locked = False

    def get_lock_register(self):
        return "o"

    def lock_paste_register(self):
        lock_register = self.get_lock_register()

        vim.registers.copy("\"", lock_register)

        map_paste_commands()

        self.register_locked = True

    def unlock_paste_register(self):
        unmap_paste_commands()
        self.register_locked = False

    def toggle_lock_register(self):
        if self.register_locked:
            self.unlock_paste_register()
        else:
            self.lock_paste_register()

yankee = Yankee()

lock_paste_register = yankee.lock_paste_register
unlock_paste_register = yankee.unlock_paste_register
toggle_lock_register = yankee.toggle_lock_register
