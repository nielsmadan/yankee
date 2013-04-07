import nose
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "plugin"))

nose.main(argv=sys.argv + ["-w", "./test"])
