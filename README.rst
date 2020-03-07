========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |travis| image:: https://api.travis-ci.org/rciorba/python-anglicize.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/rciorba/python-anglicize

.. |version| image:: https://img.shields.io/pypi/v/anglicize.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/anglicize

.. |wheel| image:: https://img.shields.io/pypi/wheel/anglicize.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/anglicize

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/anglicize.svg
    :alt: Supported versions
    :target: https://pypi.org/project/anglicize

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/anglicize.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/anglicize

.. |commits-since| image:: https://img.shields.io/github/commits-since/rciorba/python-anglicize/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/rciorba/python-anglicize/compare/v0.0.0...master

.. end-badges

A simple package to help sort non-English names.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install anglicize

You can also install the in-development version with::

    pip install https://github.com/rciorba/python-anglicize/archive/master.zip


Documentation
=============

This library provides one function, which takes a string and substitutes characters.

To use::

    # call the function directly:
    anglicize("Łukasz") == "Lukasz"

    # or use it to sort a list:
    sorted(["Luke", "Łukasz", "Zan"], key=anglicize) == ["Luke", "Łukasz", "Zan"]

    # there we go, that's much better than this:
    sorted(["Ana", "Łukasz", "Zack"]) == ["Ana"", "Zack", "Łukasz]

Rationale
=========

The purpose of this library is to help you sort non-English names writen in latin-based alphabets.

Different languages have wildly different rules for sorting, for example ``Å`` comes after ``Z`` in
Finnish but after ``A`` in Norwegian. The approach taken here is to treat visually similar letters
the same, so basically ``ÅÄĂÂ`` (and others) should all become ``A``.

Handling letters that have little similarity to A-Z
===================================================

The German ß is the main issue here. I chose to handle it like an S, mostly because it's different
enough from B (the most similar visually) and because it's well known as a version of S to most
Europeans.

Languages covered
=================

- Albanian
- Azerbaijani
- Bosnian
- Bulgarian transliteration
- Croatian
- Dutch
- Estonian
- Finnish
- French
- Gagauz
- German
- Hungarian
- Icelandic
- Latvian
- Lithuanian
- Luxembourgish
- Montenegrin
- Norwegian
- Polish
- Portuguese
- Romanian
- Serbian
- Spanish
- Swedish
- Tatar
- Turkish
- Turkmen


Contributing
============

Do you know a language written in a latin alphabet and want to check it's correctly handled? Have a
look in ``tests/test_anglicize.py``. If the language is there please check all "special" letters are
handled. This list has been mostly compiled off of Wikipedia, so I would not be surprised to hear about.

You can either make the changes and submit a PR or just create an issue mentioning
- language
- characters which need handling

Development
===========

To run tests for all python environments run::

    tox
