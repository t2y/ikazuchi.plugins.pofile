`ikazuchi.plugins.pofile <https://bitbucket.org/t2y/ikazuchi.plugins.pofile>`_
is plugin for `ikazuchi <https://bitbucket.org/t2y/ikazuchi>`_ to transalte
PO file with good reference.

`ikazuchi` is intended to work with other tools since it's a CUI tool.

See the project `documentation <http://t2y.bitbucket.org/ikazuchi/build/html/index.html>`_ for more detail.

Features
========

* Translate GNU gettext catalog named PO file with good reference from web API

Setup
=====

by easy_install
----------------

Make environment::

   $ easy_install ikazuchi.plugins.pofile

by buildout
-----------

Make environment::

   $ hg clone https://bitbucket.org/t2y/ikazuchi.plugins.pofile
   $ cd ikazuchi.plugins.pofile
   $ python bootstrap.py -d
   $ bin/buildout


Usage
=====

Translate PO file with ikazuchi command::

    $ ./bin/ikazuchi -p pofile examples/short_test.po 
    msgid:                   ikazuchi translation
    reference(Google):       [Actually, translated sentence]
    Input:

All command option are::

    $ ikazuchi -h
    usage: ikazuchi [-h] [-a API] [-d] [-e ENCODING] [-f LANG] [-l]
                    [-p PLUGIN [PLUGIN ...]] [-q] [-s SENTENCE [SENTENCE ...]]
                    [-t LANG] [--version]

    optional arguments:
      -h, --help            show this help message and exit
      -a API, --api API     APIs are ['google', 'microsoft']
      -d, --detect          detect language for target sentence
      -e ENCODING, --encoding ENCODING
                            input/output encoding
      -f LANG, --from LANG  original language
      -l, --languages       show supported languages
      -p PLUGIN [PLUGIN ...], --plugin PLUGIN [PLUGIN ...]
                            extend with plugin, show available plugins using
                            "help"
      -q, --quiet           not to show original sentence to stdout
      -s SENTENCE [SENTENCE ...], --sentences SENTENCE [SENTENCE ...]
                            target sentences
      -t LANG, --to LANG    target language to translate
      --version             show program's version number and exit


Requirements
============

* Python 2.6 or later
* ikazuchi 0.5.0 or later
* polib 0.5.5 or later
* setuptools or distriubte


License
=======

Apache License 2.0


History
=======

0.1.0 (2011-06-03)
------------------
* first release

