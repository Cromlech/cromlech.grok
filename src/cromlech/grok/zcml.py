# -*- coding: utf-8 -*-
"""Crom ZCML directives."""

from crom.config import grok
from zope.interface import Interface
from zope.configuration.fields import GlobalObject


class ICromDirective(Interface):
    """Grok a package or module."""

    package = GlobalObject(
        title=u"Package",
        description=u"The package or module to be analyzed by Crom.",
        required=False)


def cromDirective(_context, package):
    grok(package, _context)
