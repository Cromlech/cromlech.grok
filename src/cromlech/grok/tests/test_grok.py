# -*- coding: utf-8 -*-

from cStringIO import StringIO
from crom import monkey, implicit
from zope.configuration.xmlconfig import xmlconfig


snippet = StringIO('''
<configure
    xmlns="http://namespaces.zope.org/zope"
    xmlns:grok="http://namespaces.zope.org/grok">

  <include package="cromlech.grok" file="meta.zcml" />
  <grok:grok package="cromlech.grok.tests.fixtures.component" />
  
</configure>
''')


def setup_function(method):
    monkey.incompat()
    implicit.initialize()


def teardown_function(method):
    monkey.revert_incompat()
    implicit.clear()


def test_component():
    from .fixtures import component as module

    xmlconfig(snippet)
 
    # we should now be able to adapt things
    source = module.Source()
    adapted = module.ITarget(source)
    assert module.ITarget.providedBy(adapted)
    assert isinstance(adapted, module.Adapter)
    assert adapted.context is source
