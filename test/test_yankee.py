import unittest
from nose.tools import eq_

import vim_stub
import venom_stub

import yankee

class TestGreeting(unittest.TestCase):
    def test_get_greeting(self):
        result = yankee.greetings._get_greeting()

        eq_(result, "Hello World")
