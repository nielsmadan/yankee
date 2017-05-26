yankee
======

Yankee is a minimal plugin to fix some of the annoyances around yanking and maybe more in the future.

Current features:

* locking default paste register (so that `p` will keep pasting the same thing, even if you delete/change/yank
  something else in between).

v1.0 features:

* easily paste from system clipboard

Planned features:

* keep track of changes and yanks.
* choose text to paste from list of deletes/changes/yanks.

Installation
------------

yankee depends on venom. Best way to install is with [vim-plug](https://github.com/junegunn/vim-plug):

 Plug 'nielsmadan/venom' | Plug 'nielsmadan/yankee'

Commands
--------

 <leader>yl - Lock the paste register (p will continue to paste the same thing even if you yank other text)
 <leader>yu - Unlock the paste register (p will paste whatever was last yanked again).
 <leader>yt - Toggle lock / unlock paste register.

Options
-------

Yankee works by storing the content of the default register into a named register, and then overwriting p/P commands to
paste from there (and undoing the mapping later). By default it will use the named 'o' register for this. This can be
overwritten using:

 let g:yankee_lock_register = "t"

All yankee commands start with '<leader>y'. If you'd like to use another prefix rather than 'y' you can overwrite this
using:

 let g:yankee_prefix = "q"

This would then change it to '<leader>q'.
