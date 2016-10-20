
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-aaa - based on the path /rule/command/interface-fc-leaf/interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fibrechannel_leaf',)

  _yang_name = 'interface'
  _rest_name = 'interface'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
    else:
      self._path_helper = False

    extmethods = kwargs.pop("extmethods", None)
    if extmethods is False:
      self._extmethods = False
    elif extmethods is not None and isinstance(extmethods, dict):
      self._extmethods = extmethods
    elif hasattr(self, "_parent"):
      extmethods = getattr(self._parent, "_extmethods", None)
      self._extmethods = extmethods
    else:
      self._extmethods = False
    self.__fibrechannel_leaf = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="fibrechannel-leaf", rest_name="fibrechannel", parent=self, choice=(u'cmdlist', u'interface-s'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'fibrechannel'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='interface:interface-type', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'rule', u'command', u'interface-fc-leaf', u'interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rule', u'command', u'interface']

  def _get_fibrechannel_leaf(self):
    """
    Getter method for fibrechannel_leaf, mapped from YANG variable /rule/command/interface_fc_leaf/interface/fibrechannel_leaf (interface:interface-type)
    """
    return self.__fibrechannel_leaf
      
  def _set_fibrechannel_leaf(self, v, load=False):
    """
    Setter method for fibrechannel_leaf, mapped from YANG variable /rule/command/interface_fc_leaf/interface/fibrechannel_leaf (interface:interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fibrechannel_leaf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fibrechannel_leaf() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="fibrechannel-leaf", rest_name="fibrechannel", parent=self, choice=(u'cmdlist', u'interface-s'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'fibrechannel'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='interface:interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fibrechannel_leaf must be of a type compatible with interface:interface-type""",
          'defined-type': "interface:interface-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="fibrechannel-leaf", rest_name="fibrechannel", parent=self, choice=(u'cmdlist', u'interface-s'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'fibrechannel'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='interface:interface-type', is_config=True)""",
        })

    self.__fibrechannel_leaf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fibrechannel_leaf(self):
    self.__fibrechannel_leaf = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="fibrechannel-leaf", rest_name="fibrechannel", parent=self, choice=(u'cmdlist', u'interface-s'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'fibrechannel'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='interface:interface-type', is_config=True)

  fibrechannel_leaf = __builtin__.property(_get_fibrechannel_leaf, _set_fibrechannel_leaf)

  __choices__ = {u'cmdlist': {u'interface-s': [u'fibrechannel_leaf']}}
  _pyangbind_elements = {'fibrechannel_leaf': fibrechannel_leaf, }


