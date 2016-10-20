
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class controller_info(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/detail/controller-detail-list/controller-info. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__mode','__type','__connection_type','__ip_addr','__port','__vrf_name','__status','__role',)

  _yang_name = 'controller-info'
  _rest_name = 'controller-info'

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
    self.__connection_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-connection-type-tcp': {'value': 0}, u'dcm-connection-type-ssl': {'value': 1}},), is_leaf=True, yang_name="connection-type", rest_name="connection-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-connection-type', is_config=False)
    self.__status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-ctrlr-status-tcp-connecting': {'value': 3}, u'dcm-ctrlr-status-max': {'value': 8}, u'dcm-ctrlr-status-openf-handshake': {'value': 5}, u'dcm-ctrlr-status-init': {'value': 0}, u'dcm-ctrlr-status-tcp-established': {'value': 4}, u'dcm-ctrlr-status-close': {'value': 2}, u'dcm-ctrlr-status-openf-established': {'value': 6}, u'dcm-ctrlr-status-tcp-listening': {'value': 7}, u'dcm-ctrlr-status-unknown': {'value': 1}},), is_leaf=True, yang_name="status", rest_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-connection-status', is_config=False)
    self.__ip_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-addr", rest_name="ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    self.__vrf_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-connection-mode-passive': {'value': 1}, u'dcm-connection-mode-active': {'value': 0}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-connection-mode', is_config=False)
    self.__role = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-ctrlr-role-invalid': {'value': 0}, u'dcm-ctrlr-role-equal': {'value': 1}, u'dcm-ctrlr-role-slave': {'value': 3}, u'dcm-ctrlr-role-master': {'value': 2}},), is_leaf=True, yang_name="role", rest_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-role', is_config=False)
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ofv100': {'value': 0}, u'ofv130': {'value': 1}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-type', is_config=False)
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)

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
      return [u'openflow-state', u'detail', u'controller-detail-list', u'controller-info']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow-state', u'detail', u'controller-detail-list', u'controller-info']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/name (string)

    YANG Description: Controller name
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Controller name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)


  def _get_mode(self):
    """
    Getter method for mode, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/mode (ctrlr-connection-mode)

    YANG Description: Controller connection mode
    """
    return self.__mode
      
  def _set_mode(self, v, load=False):
    """
    Setter method for mode, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/mode (ctrlr-connection-mode)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode() directly.

    YANG Description: Controller connection mode
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-connection-mode-passive': {'value': 1}, u'dcm-connection-mode-active': {'value': 0}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-connection-mode', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode must be of a type compatible with ctrlr-connection-mode""",
          'defined-type': "brocade-openflow-operational:ctrlr-connection-mode",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-connection-mode-passive': {'value': 1}, u'dcm-connection-mode-active': {'value': 0}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-connection-mode', is_config=False)""",
        })

    self.__mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode(self):
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-connection-mode-passive': {'value': 1}, u'dcm-connection-mode-active': {'value': 0}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-connection-mode', is_config=False)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/type (ctrlr-type)

    YANG Description: type
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/type (ctrlr-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: type
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ofv100': {'value': 0}, u'ofv130': {'value': 1}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with ctrlr-type""",
          'defined-type': "brocade-openflow-operational:ctrlr-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ofv100': {'value': 0}, u'ofv130': {'value': 1}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-type', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ofv100': {'value': 0}, u'ofv130': {'value': 1}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-type', is_config=False)


  def _get_connection_type(self):
    """
    Getter method for connection_type, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/connection_type (ctrlr-connection-type)

    YANG Description: Controller connection type
    """
    return self.__connection_type
      
  def _set_connection_type(self, v, load=False):
    """
    Setter method for connection_type, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/connection_type (ctrlr-connection-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connection_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connection_type() directly.

    YANG Description: Controller connection type
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-connection-type-tcp': {'value': 0}, u'dcm-connection-type-ssl': {'value': 1}},), is_leaf=True, yang_name="connection-type", rest_name="connection-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-connection-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connection_type must be of a type compatible with ctrlr-connection-type""",
          'defined-type': "brocade-openflow-operational:ctrlr-connection-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-connection-type-tcp': {'value': 0}, u'dcm-connection-type-ssl': {'value': 1}},), is_leaf=True, yang_name="connection-type", rest_name="connection-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-connection-type', is_config=False)""",
        })

    self.__connection_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connection_type(self):
    self.__connection_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-connection-type-tcp': {'value': 0}, u'dcm-connection-type-ssl': {'value': 1}},), is_leaf=True, yang_name="connection-type", rest_name="connection-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-connection-type', is_config=False)


  def _get_ip_addr(self):
    """
    Getter method for ip_addr, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/ip_addr (inet:ipv4-address)

    YANG Description: IP address
    """
    return self.__ip_addr
      
  def _set_ip_addr(self, v, load=False):
    """
    Setter method for ip_addr, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/ip_addr (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_addr() directly.

    YANG Description: IP address
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-addr", rest_name="ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_addr must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-addr", rest_name="ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__ip_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_addr(self):
    self.__ip_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-addr", rest_name="ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/port (uint32)

    YANG Description: Port
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/port (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.

    YANG Description: Port
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_vrf_name(self):
    """
    Getter method for vrf_name, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/vrf_name (string)

    YANG Description: Vrf Name
    """
    return self.__vrf_name
      
  def _set_vrf_name(self, v, load=False):
    """
    Setter method for vrf_name, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/vrf_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf_name() directly.

    YANG Description: Vrf Name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__vrf_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf_name(self):
    self.__vrf_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)


  def _get_status(self):
    """
    Getter method for status, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/status (ctrlr-connection-status)

    YANG Description: Status
    """
    return self.__status
      
  def _set_status(self, v, load=False):
    """
    Setter method for status, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/status (ctrlr-connection-status)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_status() directly.

    YANG Description: Status
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-ctrlr-status-tcp-connecting': {'value': 3}, u'dcm-ctrlr-status-max': {'value': 8}, u'dcm-ctrlr-status-openf-handshake': {'value': 5}, u'dcm-ctrlr-status-init': {'value': 0}, u'dcm-ctrlr-status-tcp-established': {'value': 4}, u'dcm-ctrlr-status-close': {'value': 2}, u'dcm-ctrlr-status-openf-established': {'value': 6}, u'dcm-ctrlr-status-tcp-listening': {'value': 7}, u'dcm-ctrlr-status-unknown': {'value': 1}},), is_leaf=True, yang_name="status", rest_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-connection-status', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """status must be of a type compatible with ctrlr-connection-status""",
          'defined-type': "brocade-openflow-operational:ctrlr-connection-status",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-ctrlr-status-tcp-connecting': {'value': 3}, u'dcm-ctrlr-status-max': {'value': 8}, u'dcm-ctrlr-status-openf-handshake': {'value': 5}, u'dcm-ctrlr-status-init': {'value': 0}, u'dcm-ctrlr-status-tcp-established': {'value': 4}, u'dcm-ctrlr-status-close': {'value': 2}, u'dcm-ctrlr-status-openf-established': {'value': 6}, u'dcm-ctrlr-status-tcp-listening': {'value': 7}, u'dcm-ctrlr-status-unknown': {'value': 1}},), is_leaf=True, yang_name="status", rest_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-connection-status', is_config=False)""",
        })

    self.__status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_status(self):
    self.__status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-ctrlr-status-tcp-connecting': {'value': 3}, u'dcm-ctrlr-status-max': {'value': 8}, u'dcm-ctrlr-status-openf-handshake': {'value': 5}, u'dcm-ctrlr-status-init': {'value': 0}, u'dcm-ctrlr-status-tcp-established': {'value': 4}, u'dcm-ctrlr-status-close': {'value': 2}, u'dcm-ctrlr-status-openf-established': {'value': 6}, u'dcm-ctrlr-status-tcp-listening': {'value': 7}, u'dcm-ctrlr-status-unknown': {'value': 1}},), is_leaf=True, yang_name="status", rest_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-connection-status', is_config=False)


  def _get_role(self):
    """
    Getter method for role, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/role (ctrlr-role)

    YANG Description: Role
    """
    return self.__role
      
  def _set_role(self, v, load=False):
    """
    Setter method for role, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_info/role (ctrlr-role)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_role is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_role() directly.

    YANG Description: Role
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-ctrlr-role-invalid': {'value': 0}, u'dcm-ctrlr-role-equal': {'value': 1}, u'dcm-ctrlr-role-slave': {'value': 3}, u'dcm-ctrlr-role-master': {'value': 2}},), is_leaf=True, yang_name="role", rest_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-role', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """role must be of a type compatible with ctrlr-role""",
          'defined-type': "brocade-openflow-operational:ctrlr-role",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-ctrlr-role-invalid': {'value': 0}, u'dcm-ctrlr-role-equal': {'value': 1}, u'dcm-ctrlr-role-slave': {'value': 3}, u'dcm-ctrlr-role-master': {'value': 2}},), is_leaf=True, yang_name="role", rest_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-role', is_config=False)""",
        })

    self.__role = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_role(self):
    self.__role = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-ctrlr-role-invalid': {'value': 0}, u'dcm-ctrlr-role-equal': {'value': 1}, u'dcm-ctrlr-role-slave': {'value': 3}, u'dcm-ctrlr-role-master': {'value': 2}},), is_leaf=True, yang_name="role", rest_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='ctrlr-role', is_config=False)

  name = __builtin__.property(_get_name)
  mode = __builtin__.property(_get_mode)
  type = __builtin__.property(_get_type)
  connection_type = __builtin__.property(_get_connection_type)
  ip_addr = __builtin__.property(_get_ip_addr)
  port = __builtin__.property(_get_port)
  vrf_name = __builtin__.property(_get_vrf_name)
  status = __builtin__.property(_get_status)
  role = __builtin__.property(_get_role)


  _pyangbind_elements = {'name': name, 'mode': mode, 'type': type, 'connection_type': connection_type, 'ip_addr': ip_addr, 'port': port, 'vrf_name': vrf_name, 'status': status, 'role': role, }


