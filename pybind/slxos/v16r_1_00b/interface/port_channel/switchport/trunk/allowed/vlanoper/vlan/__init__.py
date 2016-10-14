
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/switchport/trunk/allowed/vlanoper/vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__add_','__remove_',)

  _yang_name = 'vlan'

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
    self.__add_ = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-vlan-range', is_config=True)
    self.__remove_ = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-vlan-range', is_config=True)

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
      return [u'interface', u'port-channel', u'switchport', u'trunk', u'allowed', u'vlanoper', u'vlan']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'interface', u'Port-channel', u'switchport', u'trunk', u'allowed', u'vlanoper', u'vlan']

  def _get_add_(self):
    """
    Getter method for add_, mapped from YANG variable /interface/port_channel/switchport/trunk/allowed/vlanoper/vlan/add (ui32-vlan-range)
    """
    return self.__add_
      
  def _set_add_(self, v, load=False):
    """
    Setter method for add_, mapped from YANG variable /interface/port_channel/switchport/trunk/allowed/vlanoper/vlan/add (ui32-vlan-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_add_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_add_() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-vlan-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """add_ must be of a type compatible with ui32-vlan-range""",
          'defined-type': "brocade-interface:ui32-vlan-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-vlan-range', is_config=True)""",
        })

    self.__add_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_add_(self):
    self.__add_ = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-vlan-range', is_config=True)


  def _get_remove_(self):
    """
    Getter method for remove_, mapped from YANG variable /interface/port_channel/switchport/trunk/allowed/vlanoper/vlan/remove (ui32-vlan-range)
    """
    return self.__remove_
      
  def _set_remove_(self, v, load=False):
    """
    Setter method for remove_, mapped from YANG variable /interface/port_channel/switchport/trunk/allowed/vlanoper/vlan/remove (ui32-vlan-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remove_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remove_() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-vlan-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remove_ must be of a type compatible with ui32-vlan-range""",
          'defined-type': "brocade-interface:ui32-vlan-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-vlan-range', is_config=True)""",
        })

    self.__remove_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remove_(self):
    self.__remove_ = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(4090)))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-vlan-range', is_config=True)

  add_ = __builtin__.property(_get_add_, _set_add_)
  remove_ = __builtin__.property(_get_remove_, _set_remove_)


  _pyangbind_elements = {'add_': add_, 'remove_': remove_, }


