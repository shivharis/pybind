
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class permit_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-dai - based on the path /arp/access-list/permit/permit-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ip_type','__host_ip','__mac_type','__host_mac','__log',)

  _yang_name = 'permit-list'
  _rest_name = 'ip'

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
    self.__ip_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 1}},), is_leaf=True, yang_name="ip-type", rest_name="ip-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='enumeration', is_config=True)
    self.__mac_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 1}},), is_leaf=True, yang_name="mac-type", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC address', u'alt-name': u'mac', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='enumeration', is_config=True)
    self.__host_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host-ip", rest_name="host-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4Address;;Source IPv4 Address A.B.C.D'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='inet:ipv4-address', is_config=True)
    self.__host_mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="host-mac", rest_name="host-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MACADDRESS;;Mac address in HHHH.HHHH.HHHH format.', u'typepoint': u'mac_address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='string', is_config=True)
    self.__log = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log", rest_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Log packet'}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='empty', is_config=True)

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
      return [u'arp', u'access-list', u'permit', u'permit-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'arp', u'access-list', u'permit', u'ip']

  def _get_ip_type(self):
    """
    Getter method for ip_type, mapped from YANG variable /arp/access_list/permit/permit_list/ip_type (enumeration)
    """
    return self.__ip_type
      
  def _set_ip_type(self, v, load=False):
    """
    Setter method for ip_type, mapped from YANG variable /arp/access_list/permit/permit_list/ip_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 1}},), is_leaf=True, yang_name="ip-type", rest_name="ip-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-dai:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 1}},), is_leaf=True, yang_name="ip-type", rest_name="ip-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='enumeration', is_config=True)""",
        })

    self.__ip_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_type(self):
    self.__ip_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 1}},), is_leaf=True, yang_name="ip-type", rest_name="ip-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='enumeration', is_config=True)


  def _get_host_ip(self):
    """
    Getter method for host_ip, mapped from YANG variable /arp/access_list/permit/permit_list/host_ip (inet:ipv4-address)
    """
    return self.__host_ip
      
  def _set_host_ip(self, v, load=False):
    """
    Setter method for host_ip, mapped from YANG variable /arp/access_list/permit/permit_list/host_ip (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host_ip() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host-ip", rest_name="host-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4Address;;Source IPv4 Address A.B.C.D'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host_ip must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host-ip", rest_name="host-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4Address;;Source IPv4 Address A.B.C.D'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__host_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host_ip(self):
    self.__host_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host-ip", rest_name="host-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4Address;;Source IPv4 Address A.B.C.D'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='inet:ipv4-address', is_config=True)


  def _get_mac_type(self):
    """
    Getter method for mac_type, mapped from YANG variable /arp/access_list/permit/permit_list/mac_type (enumeration)
    """
    return self.__mac_type
      
  def _set_mac_type(self, v, load=False):
    """
    Setter method for mac_type, mapped from YANG variable /arp/access_list/permit/permit_list/mac_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 1}},), is_leaf=True, yang_name="mac-type", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC address', u'alt-name': u'mac', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-dai:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 1}},), is_leaf=True, yang_name="mac-type", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC address', u'alt-name': u'mac', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='enumeration', is_config=True)""",
        })

    self.__mac_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_type(self):
    self.__mac_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 1}},), is_leaf=True, yang_name="mac-type", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC address', u'alt-name': u'mac', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='enumeration', is_config=True)


  def _get_host_mac(self):
    """
    Getter method for host_mac, mapped from YANG variable /arp/access_list/permit/permit_list/host_mac (string)
    """
    return self.__host_mac
      
  def _set_host_mac(self, v, load=False):
    """
    Setter method for host_mac, mapped from YANG variable /arp/access_list/permit/permit_list/host_mac (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host_mac() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="host-mac", rest_name="host-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MACADDRESS;;Mac address in HHHH.HHHH.HHHH format.', u'typepoint': u'mac_address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host_mac must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="host-mac", rest_name="host-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MACADDRESS;;Mac address in HHHH.HHHH.HHHH format.', u'typepoint': u'mac_address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='string', is_config=True)""",
        })

    self.__host_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host_mac(self):
    self.__host_mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="host-mac", rest_name="host-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MACADDRESS;;Mac address in HHHH.HHHH.HHHH format.', u'typepoint': u'mac_address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='string', is_config=True)


  def _get_log(self):
    """
    Getter method for log, mapped from YANG variable /arp/access_list/permit/permit_list/log (empty)
    """
    return self.__log
      
  def _set_log(self, v, load=False):
    """
    Setter method for log, mapped from YANG variable /arp/access_list/permit/permit_list/log (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="log", rest_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Log packet'}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log", rest_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Log packet'}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='empty', is_config=True)""",
        })

    self.__log = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log(self):
    self.__log = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log", rest_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Log packet'}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='empty', is_config=True)

  ip_type = __builtin__.property(_get_ip_type, _set_ip_type)
  host_ip = __builtin__.property(_get_host_ip, _set_host_ip)
  mac_type = __builtin__.property(_get_mac_type, _set_mac_type)
  host_mac = __builtin__.property(_get_host_mac, _set_host_mac)
  log = __builtin__.property(_get_log, _set_log)


  _pyangbind_elements = {'ip_type': ip_type, 'host_ip': host_ip, 'mac_type': mac_type, 'host_mac': host_mac, 'log': log, }


