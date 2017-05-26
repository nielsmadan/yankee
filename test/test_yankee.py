import unittest
from nose.tools import eq_

import vim_stub
import venom_stub

import yankee

class TestYankee(unittest.TestCase):
    # doesn't test anything useful at the moment, but at least runs.
    def test_get_lock_register(self):
        result = yankee.lock_paste_register()

        eq_(result, None)
