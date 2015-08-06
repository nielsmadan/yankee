import venom
import vim

from yankee import lock_paste_register, unlock_paste_register

venom.py_fn_to_vim_command("YankeeLockPasteRegister", lock_paste_register)
venom.py_fn_to_vim_command("YankeeUnlockPasteRegister", unlock_paste_register)

vim.map.nnoremap("<leader>yl", ":YankeeLockPasteRegister<CR>")
vim.map.nnoremap("<leader>yu", ":YankeeUnlockPasteRegister<CR>")