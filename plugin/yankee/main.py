import vim

class Yankee(object):
    def __init__(self):
        self.register_locked = False

    def get_lock_register(self):
        return vim.g.yankee_lock_register if "yankee_lock_register" in vim.g else "o"

    def lock_paste_register(self):
        lock_register = self.get_lock_register()

        vim.registers.copy("\"", lock_register)

        self.map_paste_commands()

        self.register_locked = True

    def unlock_paste_register(self):
        self.unmap_paste_commands()
        self.register_locked = False

    def toggle_lock_register(self):
        if self.register_locked:
            self.unlock_paste_register()
        else:
            self.lock_paste_register()

    def map_paste_commands(self):
        vim.map.nnoremap("p", "\"%sp" % self.get_lock_register())
        vim.map.nnoremap("P", "\"%sP" % self.get_lock_register())

    def unmap_paste_commands(self):
        vim.map.nnoremap("p", "p")
        vim.map.nnoremap("P", "P")


yankee = Yankee()

lock_paste_register = yankee.lock_paste_register
unlock_paste_register = yankee.unlock_paste_register
toggle_lock_register = yankee.toggle_lock_register
