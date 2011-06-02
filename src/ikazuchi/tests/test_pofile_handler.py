# -*- coding: utf-8 -*-

import tempfile
from nose.tools import *

# functions for test
from ikazuchi.plugins.pofile import *

class TestHandler(object):
    class Option(object):
        def __init__(self, pofile):
            self.api = "google"
            self.plugin["pofile", pofile]
            self.encoding = ["utf-8", "utf-8"]

    def setup(self):
        def make_po_file(path):
            f = tempfile.NamedTemporaryFile(dir=path)
            f.write('msgid "forest"\nmsgstr ""\nmsgid "book"\nmsgstr "hon"')
            f.flush()
            return f
        self.po_file = make_po_file(tempfile.tempdir)

    def teardown(self):
        self.po_file.close()

    def test_select_translation(self):
        data = [
            (["ref", "", "y"], "ref"),
            (["ref", "cur", "y"], "ref"),
            (["ref", "cur", ""], "cur"),
            (["ref", "", ""], ""),
            (["ref", "cur", "ent"], "ent"),
            (["ref", "", "ent"], "ent"),
        ]
        h = Handler(Option(self.po_file.name))
        for d in data:
            assert_equals(d[1], h._select_translation(*d[0]))

def test_markup_msgid_notranslate():
    from data.po.markup_notranslate import DATA_SET
    _fmt = u"{0}_{1} ({2} ...)"
    _func = u"test_markup_msgid_notranslate"
    for num, (data, expected) in enumerate(DATA_SET):
        name = _fmt.format(_func, num, str(data)[:10])
        _assert = lambda e, a: assert_equal(e, a)
        _assert.description = name
        yield _assert, expected, Handler.markup_msgid_notranslate(data)