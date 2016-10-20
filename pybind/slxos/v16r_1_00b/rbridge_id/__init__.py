
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import interface_nodespecific
import ipv6
class rbridge_id(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rbridge_id','__swbd_number','__interface_nodespecific','__ipv6',)

  _yang_name = 'rbridge-id'
  _rest_name = 'rbridge-id'

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
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Internet Protocol (IPv6)', u'sort-priority': u'77', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='container', is_config=True)
    self.__rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rbridge-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='uint32', is_config=True)
    self.__interface_nodespecific = YANGDynClass(base=interface_nodespecific.interface_nodespecific, is_container='container', yang_name="interface-nodespecific", rest_name="interface-nodespecific", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'built-in-self-test', u'callpoint': u'interface_nodespecific'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='container', is_config=True)
    self.__swbd_number = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="swbd-number", rest_name="swbd-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display Node SWBD Number', u'cli-suppress-show-conf-path': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='int32', is_config=False)

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
      return [u'rbridge-id']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id']

  def _get_rbridge_id(self):
    """
    Getter method for rbridge_id, mapped from YANG variable /rbridge_id/rbridge_id (uint32)
    """
    return self.__rbridge_id
      
  def _set_rbridge_id(self, v, load=False):
    """
    Setter method for rbridge_id, mapped from YANG variable /rbridge_id/rbridge_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rbridge_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rbridge_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rbridge-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rbridge_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rbridge-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='uint32', is_config=True)""",
        })

    self.__rbridge_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rbridge_id(self):
    self.__rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rbridge-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='uint32', is_config=True)


  def _get_swbd_number(self):
    """
    Getter method for swbd_number, mapped from YANG variable /rbridge_id/swbd_number (int32)
    """
    return self.__swbd_number
      
  def _set_swbd_number(self, v, load=False):
    """
    Setter method for swbd_number, mapped from YANG variable /rbridge_id/swbd_number (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_swbd_number is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_swbd_number() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="swbd-number", rest_name="swbd-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display Node SWBD Number', u'cli-suppress-show-conf-path': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='int32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """swbd_number must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="swbd-number", rest_name="swbd-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display Node SWBD Number', u'cli-suppress-show-conf-path': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='int32', is_config=False)""",
        })

    self.__swbd_number = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_swbd_number(self):
    self.__swbd_number = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="swbd-number", rest_name="swbd-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display Node SWBD Number', u'cli-suppress-show-conf-path': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='int32', is_config=False)


  def _get_interface_nodespecific(self):
    """
    Getter method for interface_nodespecific, mapped from YANG variable /rbridge_id/interface_nodespecific (container)
    """
    return self.__interface_nodespecific
      
  def _set_interface_nodespecific(self, v, load=False):
    """
    Setter method for interface_nodespecific, mapped from YANG variable /rbridge_id/interface_nodespecific (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_nodespecific is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_nodespecific() directly.
    """
    try:
      t = YANGDynClass(v,base=interface_nodespecific.interface_nodespecific, is_container='container', yang_name="interface-nodespecific", rest_name="interface-nodespecific", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'built-in-self-test', u'callpoint': u'interface_nodespecific'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_nodespecific must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_nodespecific.interface_nodespecific, is_container='container', yang_name="interface-nodespecific", rest_name="interface-nodespecific", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'built-in-self-test', u'callpoint': u'interface_nodespecific'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='container', is_config=True)""",
        })

    self.__interface_nodespecific = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_nodespecific(self):
    self.__interface_nodespecific = YANGDynClass(base=interface_nodespecific.interface_nodespecific, is_container='container', yang_name="interface-nodespecific", rest_name="interface-nodespecific", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'built-in-self-test', u'callpoint': u'interface_nodespecific'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='container', is_config=True)


  def _get_ipv6(self):
    """
    Getter method for ipv6, mapped from YANG variable /rbridge_id/ipv6 (container)

    YANG Description: Internet Protoccol (IPv6). 
    """
    return self.__ipv6
      
  def _set_ipv6(self, v, load=False):
    """
    Setter method for ipv6, mapped from YANG variable /rbridge_id/ipv6 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6() directly.

    YANG Description: Internet Protoccol (IPv6). 
    """
    try:
      t = YANGDynClass(v,base=ipv6.ipv6, is_container='container', yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Internet Protocol (IPv6)', u'sort-priority': u'77', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6.ipv6, is_container='container', yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Internet Protocol (IPv6)', u'sort-priority': u'77', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='container', is_config=True)""",
        })

    self.__ipv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6(self):
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Internet Protocol (IPv6)', u'sort-priority': u'77', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='container', is_config=True)

  rbridge_id = __builtin__.property(_get_rbridge_id, _set_rbridge_id)
  swbd_number = __builtin__.property(_get_swbd_number)
  interface_nodespecific = __builtin__.property(_get_interface_nodespecific, _set_interface_nodespecific)
  ipv6 = __builtin__.property(_get_ipv6, _set_ipv6)


  _pyangbind_elements = {'rbridge_id': rbridge_id, 'swbd_number': swbd_number, 'interface_nodespecific': interface_nodespecific, 'ipv6': ipv6, }


