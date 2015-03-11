import sys

class log:

    @classmethod
    def info(cls, message=""):
        print("message: %s" % (message))

    @classmethod
    def fail(cls, actual="", expect=""):
        content = "actual: '%s' \nexpect: '%s'" % (actual, expect)
        raise AssertionError(content)

    @classmethod
    def error(cls, message=""):
        raise RuntimeError("message: %s" % (message))
