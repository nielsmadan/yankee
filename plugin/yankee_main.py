import venom
import vim

from yankee import append_hello_world


venom.py_fn_to_vim_command("VenomHelloWorld", append_hello_world)

vim.map.nnoremap("<leader>vhw", ":VenomHelloWorld<CR>")
