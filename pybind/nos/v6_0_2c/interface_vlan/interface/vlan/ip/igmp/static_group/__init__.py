
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class static_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface-vlan/interface/vlan/ip/igmp/static-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mcast_address','__interface','__if_type','__value',)

  _yang_name = 'static-group'
  _rest_name = 'static-group'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    path_helper_ = kwargs.pop("path_helper", None)
    if path_helper_ is False:
      self._path_helper = False
    elif path_helper_ is not None and isinstance(path_helper_, xpathhelper.YANGPathHelper):
      self._path_helper = path_helper_
    elif hasattr(self, "_parent"):
      path_helper_ = getattr(self._parent, "_path_helper", False)
      self._path_helper = path_helper_
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
    self.__interface = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface': {}},), is_leaf=True, yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)
    self.__mcast_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mcast-address", rest_name="mcast-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Multicast Address to be Joined in the format A.B.C.D', u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='inet:ipv4-address', is_config=True)
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']}), is_leaf=True, yang_name="value", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-completion-actionpoint': u'IgmpsShowActionPoint'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='string-type', is_config=True)
    self.__if_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FortyGigabitEthernet': {}, u'Port-channel': {}, u'GigabitEthernet': {}, u'TenGigabitEthernet': {}, u'HundredGigabitEthernet': {}},), is_leaf=True, yang_name="if-type", rest_name="if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)

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
      return [u'interface-vlan', u'interface', u'vlan', u'ip', u'igmp', u'static-group']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Vlan', u'ip', u'igmp', u'static-group']

  def _get_mcast_address(self):
    """
    Getter method for mcast_address, mapped from YANG variable /interface_vlan/interface/vlan/ip/igmp/static_group/mcast_address (inet:ipv4-address)
    """
    return self.__mcast_address
      
  def _set_mcast_address(self, v, load=False):
    """
    Setter method for mcast_address, mapped from YANG variable /interface_vlan/interface/vlan/ip/igmp/static_group/mcast_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mcast_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mcast_address() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mcast-address", rest_name="mcast-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Multicast Address to be Joined in the format A.B.C.D', u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mcast_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mcast-address", rest_name="mcast-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Multicast Address to be Joined in the format A.B.C.D', u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__mcast_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mcast_address(self):
    self.__mcast_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mcast-address", rest_name="mcast-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Multicast Address to be Joined in the format A.B.C.D', u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='inet:ipv4-address', is_config=True)


  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /interface_vlan/interface/vlan/ip/igmp/static_group/interface (enumeration)
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /interface_vlan/interface/vlan/ip/igmp/static_group/interface (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface': {}},), is_leaf=True, yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with enumeration""",
          'defined-type': "brocade-igmp-snooping:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface': {}},), is_leaf=True, yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface': {}},), is_leaf=True, yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)


  def _get_if_type(self):
    """
    Getter method for if_type, mapped from YANG variable /interface_vlan/interface/vlan/ip/igmp/static_group/if_type (enumeration)
    """
    return self.__if_type
      
  def _set_if_type(self, v, load=False):
    """
    Setter method for if_type, mapped from YANG variable /interface_vlan/interface/vlan/ip/igmp/static_group/if_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_if_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_if_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FortyGigabitEthernet': {}, u'Port-channel': {}, u'GigabitEthernet': {}, u'TenGigabitEthernet': {}, u'HundredGigabitEthernet': {}},), is_leaf=True, yang_name="if-type", rest_name="if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """if_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-igmp-snooping:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FortyGigabitEthernet': {}, u'Port-channel': {}, u'GigabitEthernet': {}, u'TenGigabitEthernet': {}, u'HundredGigabitEthernet': {}},), is_leaf=True, yang_name="if-type", rest_name="if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)""",
        })

    self.__if_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_if_type(self):
    self.__if_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FortyGigabitEthernet': {}, u'Port-channel': {}, u'GigabitEthernet': {}, u'TenGigabitEthernet': {}, u'HundredGigabitEthernet': {}},), is_leaf=True, yang_name="if-type", rest_name="if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='enumeration', is_config=True)


  def _get_value(self):
    """
    Getter method for value, mapped from YANG variable /interface_vlan/interface/vlan/ip/igmp/static_group/value (string-type)
    """
    return self.__value
      
  def _set_value(self, v, load=False):
    """
    Setter method for value, mapped from YANG variable /interface_vlan/interface/vlan/ip/igmp/static_group/value (string-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']}), is_leaf=True, yang_name="value", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-completion-actionpoint': u'IgmpsShowActionPoint'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='string-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """value must be of a type compatible with string-type""",
          'defined-type': "brocade-igmp-snooping:string-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']}), is_leaf=True, yang_name="value", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-completion-actionpoint': u'IgmpsShowActionPoint'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='string-type', is_config=True)""",
        })

    self.__value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_value(self):
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']}), is_leaf=True, yang_name="value", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-completion-actionpoint': u'IgmpsShowActionPoint'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='string-type', is_config=True)

  mcast_address = __builtin__.property(_get_mcast_address, _set_mcast_address)
  interface = __builtin__.property(_get_interface, _set_interface)
  if_type = __builtin__.property(_get_if_type, _set_if_type)
  value = __builtin__.property(_get_value, _set_value)


  _pyangbind_elements = {'mcast_address': mcast_address, 'interface': interface, 'if_type': if_type, 'value': value, }


