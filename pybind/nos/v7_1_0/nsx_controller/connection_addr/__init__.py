
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class connection_addr(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tunnels - based on the path /nsx-controller/connection-addr. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Connection method, IP address and port information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__address','__port','__method',)

  _yang_name = 'connection-addr'
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
    self.__method = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ssl': {'value': 2}, u'tcp': {'value': 1}},), default=unicode("ssl"), is_leaf=True, yang_name="method", rest_name="method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Connection method', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='enumeration', is_config=True)
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(6632), is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NSX controller port number', u'cli-suppress-no': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='uint32', is_config=True)
    self.__address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address of NSX controller', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='inet:ip-address', is_config=True)

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
      return [u'nsx-controller', u'connection-addr']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'nsx-controller', u'ip']

  def _get_address(self):
    """
    Getter method for address, mapped from YANG variable /nsx_controller/connection_addr/address (inet:ip-address)

    YANG Description: IP address of the NSX controller. Only IPv4 address
is supported.
    """
    return self.__address
      
  def _set_address(self, v, load=False):
    """
    Setter method for address, mapped from YANG variable /nsx_controller/connection_addr/address (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.

    YANG Description: IP address of the NSX controller. Only IPv4 address
is supported.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address of NSX controller', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='inet:ip-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address of NSX controller', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='inet:ip-address', is_config=True)""",
        })

    self.__address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address(self):
    self.__address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address of NSX controller', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='inet:ip-address', is_config=True)


  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /nsx_controller/connection_addr/port (uint32)

    YANG Description: TCP port number for the NSX controller. This is an
optional parameter; default value is 6632.
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /nsx_controller/connection_addr/port (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.

    YANG Description: TCP port number for the NSX controller. This is an
optional parameter; default value is 6632.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(6632), is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NSX controller port number', u'cli-suppress-no': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(6632), is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NSX controller port number', u'cli-suppress-no': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='uint32', is_config=True)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(6632), is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NSX controller port number', u'cli-suppress-no': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='uint32', is_config=True)


  def _get_method(self):
    """
    Getter method for method, mapped from YANG variable /nsx_controller/connection_addr/method (enumeration)

    YANG Description: This parameter defines the connection method to be
usedto connect to NSX controller. By default SSL is
used
    """
    return self.__method
      
  def _set_method(self, v, load=False):
    """
    Setter method for method, mapped from YANG variable /nsx_controller/connection_addr/method (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_method is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_method() directly.

    YANG Description: This parameter defines the connection method to be
usedto connect to NSX controller. By default SSL is
used
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ssl': {'value': 2}, u'tcp': {'value': 1}},), default=unicode("ssl"), is_leaf=True, yang_name="method", rest_name="method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Connection method', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """method must be of a type compatible with enumeration""",
          'defined-type': "brocade-tunnels:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ssl': {'value': 2}, u'tcp': {'value': 1}},), default=unicode("ssl"), is_leaf=True, yang_name="method", rest_name="method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Connection method', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='enumeration', is_config=True)""",
        })

    self.__method = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_method(self):
    self.__method = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ssl': {'value': 2}, u'tcp': {'value': 1}},), default=unicode("ssl"), is_leaf=True, yang_name="method", rest_name="method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Connection method', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='enumeration', is_config=True)

  address = __builtin__.property(_get_address, _set_address)
  port = __builtin__.property(_get_port, _set_port)
  method = __builtin__.property(_get_method, _set_method)


  _pyangbind_elements = {'address': address, 'port': port, 'method': method, }


