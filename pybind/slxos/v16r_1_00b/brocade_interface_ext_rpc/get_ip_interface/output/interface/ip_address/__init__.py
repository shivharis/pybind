
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ip_address(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface-ext - based on the path /brocade_interface_ext_rpc/get-ip-interface/output/interface/ip-address. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This indicates whether IP address is primary/secondary
and corresponding Broadcast IP
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipv4','__ipv4_type','__broadcast','__ip_mtu',)

  _yang_name = 'ip-address'
  _rest_name = 'ip-address'

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
    self.__broadcast = YANGDynClass(base=unicode, is_leaf=True, yang_name="broadcast", rest_name="broadcast", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    self.__ip_mtu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1548..9216']}), is_leaf=True, yang_name="ip-mtu", rest_name="ip-mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='interface:mtu-type', is_config=True)
    self.__ipv4 = YANGDynClass(base=unicode, is_leaf=True, yang_name="ipv4", rest_name="ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    self.__ipv4_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'primary': {'value': 1}, u'secondary': {'value': 2}},), is_leaf=True, yang_name="ipv4-type", rest_name="ipv4-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)

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
      return [u'brocade_interface_ext_rpc', u'get-ip-interface', u'output', u'interface', u'ip-address']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-ip-interface', u'output', u'interface', u'ip-address']

  def _get_ipv4(self):
    """
    Getter method for ipv4, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/ip_address/ipv4 (string)

    YANG Description: A.B.C.D/M IP address in dotted decimal/Mask
    """
    return self.__ipv4
      
  def _set_ipv4(self, v, load=False):
    """
    Setter method for ipv4, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/ip_address/ipv4 (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4() directly.

    YANG Description: A.B.C.D/M IP address in dotted decimal/Mask
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ipv4", rest_name="ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4 must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ipv4", rest_name="ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)""",
        })

    self.__ipv4 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4(self):
    self.__ipv4 = YANGDynClass(base=unicode, is_leaf=True, yang_name="ipv4", rest_name="ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)


  def _get_ipv4_type(self):
    """
    Getter method for ipv4_type, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/ip_address/ipv4_type (enumeration)
    """
    return self.__ipv4_type
      
  def _set_ipv4_type(self, v, load=False):
    """
    Setter method for ipv4_type, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/ip_address/ipv4_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_type() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'primary': {'value': 1}, u'secondary': {'value': 2}},), is_leaf=True, yang_name="ipv4-type", rest_name="ipv4-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-interface-ext:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'primary': {'value': 1}, u'secondary': {'value': 2}},), is_leaf=True, yang_name="ipv4-type", rest_name="ipv4-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)""",
        })

    self.__ipv4_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_type(self):
    self.__ipv4_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'primary': {'value': 1}, u'secondary': {'value': 2}},), is_leaf=True, yang_name="ipv4-type", rest_name="ipv4-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)


  def _get_broadcast(self):
    """
    Getter method for broadcast, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/ip_address/broadcast (string)

    YANG Description: Broadcast IP address.
    """
    return self.__broadcast
      
  def _set_broadcast(self, v, load=False):
    """
    Setter method for broadcast, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/ip_address/broadcast (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_broadcast is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_broadcast() directly.

    YANG Description: Broadcast IP address.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="broadcast", rest_name="broadcast", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """broadcast must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="broadcast", rest_name="broadcast", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)""",
        })

    self.__broadcast = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_broadcast(self):
    self.__broadcast = YANGDynClass(base=unicode, is_leaf=True, yang_name="broadcast", rest_name="broadcast", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)


  def _get_ip_mtu(self):
    """
    Getter method for ip_mtu, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/ip_address/ip_mtu (interface:mtu-type)

    YANG Description: This specifies the IP MTU value of this 
interface.
    """
    return self.__ip_mtu
      
  def _set_ip_mtu(self, v, load=False):
    """
    Setter method for ip_mtu, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/ip_address/ip_mtu (interface:mtu-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_mtu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_mtu() directly.

    YANG Description: This specifies the IP MTU value of this 
interface.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1548..9216']}), is_leaf=True, yang_name="ip-mtu", rest_name="ip-mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='interface:mtu-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_mtu must be of a type compatible with interface:mtu-type""",
          'defined-type': "interface:mtu-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1548..9216']}), is_leaf=True, yang_name="ip-mtu", rest_name="ip-mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='interface:mtu-type', is_config=True)""",
        })

    self.__ip_mtu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_mtu(self):
    self.__ip_mtu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1548..9216']}), is_leaf=True, yang_name="ip-mtu", rest_name="ip-mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='interface:mtu-type', is_config=True)

  ipv4 = __builtin__.property(_get_ipv4, _set_ipv4)
  ipv4_type = __builtin__.property(_get_ipv4_type, _set_ipv4_type)
  broadcast = __builtin__.property(_get_broadcast, _set_broadcast)
  ip_mtu = __builtin__.property(_get_ip_mtu, _set_ip_mtu)


  _pyangbind_elements = {'ipv4': ipv4, 'ipv4_type': ipv4_type, 'broadcast': broadcast, 'ip_mtu': ip_mtu, }

