import venom
import vim

plugin_prefix = "<leader>%s" % (vim.g.yankee_prefix if "yankee_prefix" in vim.g else "y")

from yankee import lock_paste_register, unlock_paste_register, toggle_lock_register

venom.py_fn_to_vim_command("YankeeLockPasteRegister", lock_paste_register)
venom.py_fn_to_vim_command("YankeeUnlockPasteRegister", unlock_paste_register)
venom.py_fn_to_vim_command("YankeeToggleLockPasteRegister", toggle_lock_register)

vim.map.nnoremap(plugin_prefix + "l", ":YankeeLockPasteRegister<CR>")
vim.map.nnoremap(plugin_prefix + "u", ":YankeeUnlockPasteRegister<CR>")
vim.map.nnoremap(plugin_prefix + "t", ":YankeeToggleLockPasteRegister<CR>")
