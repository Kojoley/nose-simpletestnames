from __future__ import unicode_literals

from nose.plugins import Plugin


class SimpleTestNames(Plugin):
    name = 'simpletestnames'
    enabled = True

    def configure(self, options, conf):
        self.current_directory = conf.workingDir

    def describeTest(self, test):
        addr = test.address()
        if addr is None:
            return None

        filename, _, func = addr
        if filename is None:
            return None

        path_prefix_len = len(self.current_directory) + 1

        assert len(filename) > path_prefix_len
        assert filename.lower().startswith(self.current_directory.lower())

        test_rel_path = filename[path_prefix_len:].replace('\\', '/')

        if func is None:
            return test_rel_path

        s = "%s::%s" % (test_rel_path, func.replace('.', '::'))
        if getattr(test.test, 'arg', None):
            s = "%s[%s]" % (s, '-'.join(map(str, test.test.arg)))

        return s