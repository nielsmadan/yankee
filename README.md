yankee
======

**work in progress at the moment**

Yankee is yet another yank manager for vim. In terms of features and complexity it's somewhere between
[yankstack](https://github.com/maxbrunsfeld/vim-yankstack) and
[YankRing](http://www.vim.org/scripts/script.php?script_id=1234) (Goldilocks certified).

Features include:

* locking default paste register (so that `p` will keep pasting the same thing, even if you delete/change/yank
  something else in between).
* keep track of changes and yanks.
* choose text to paste from list of deletes/changes/yanks.

Installation
------------

yankee depends on venom. Best way to install is with [vim-plug](https://github.com/junegunn/vim-plug):

 Plug 'nielsmadan/venom' | Plug 'nielsmadan/yankee'

Options
-------

Yankee works by storing the content of the default register into a named register, and then overwriting p/P commands to
paste from there (and undoing the mapping later). By default it will use the named 'o' register for this. This can be
overwritten:

 let g:yankee_lock_register = "t"
