
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vrf
import vlan
class server_ip(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos - based on the path /nas/server-ip. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__server_ip','__vrf','__vlan',)

  _yang_name = 'server-ip'

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
    self.__vlan = YANGDynClass(base=YANGListType("vlan_number",vlan.vlan, yang_name="vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-number', extensions={u'tailf-common': {u'info': u'Virtual LAN', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vlan'}}), is_container='list', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual LAN', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vlan'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)
    self.__vrf = YANGDynClass(base=YANGListType("vrf_name",vrf.vrf, yang_name="vrf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf-name', extensions={u'tailf-common': {u'info': u'Virtual Routing and Forwarding', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vrf'}}), is_container='list', yang_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual Routing and Forwarding', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vrf'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)
    self.__server_ip = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}),], is_leaf=True, yang_name="server-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='nas-ip-prefix', is_config=True)

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
      return [u'nas', u'server-ip']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'nas', u'server-ip']

  def _get_server_ip(self):
    """
    Getter method for server_ip, mapped from YANG variable /nas/server_ip/server_ip (nas-ip-prefix)
    """
    return self.__server_ip
      
  def _set_server_ip(self, v, load=False):
    """
    Setter method for server_ip, mapped from YANG variable /nas/server_ip/server_ip (nas-ip-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_server_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_server_ip() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}),], is_leaf=True, yang_name="server-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='nas-ip-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """server_ip must be of a type compatible with nas-ip-prefix""",
          'defined-type': "brocade-qos:nas-ip-prefix",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}),], is_leaf=True, yang_name="server-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='nas-ip-prefix', is_config=True)""",
        })

    self.__server_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_server_ip(self):
    self.__server_ip = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}),], is_leaf=True, yang_name="server-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='nas-ip-prefix', is_config=True)


  def _get_vrf(self):
    """
    Getter method for vrf, mapped from YANG variable /nas/server_ip/vrf (list)
    """
    return self.__vrf
      
  def _set_vrf(self, v, load=False):
    """
    Setter method for vrf, mapped from YANG variable /nas/server_ip/vrf (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("vrf_name",vrf.vrf, yang_name="vrf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf-name', extensions={u'tailf-common': {u'info': u'Virtual Routing and Forwarding', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vrf'}}), is_container='list', yang_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual Routing and Forwarding', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vrf'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vrf_name",vrf.vrf, yang_name="vrf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf-name', extensions={u'tailf-common': {u'info': u'Virtual Routing and Forwarding', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vrf'}}), is_container='list', yang_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual Routing and Forwarding', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vrf'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)""",
        })

    self.__vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf(self):
    self.__vrf = YANGDynClass(base=YANGListType("vrf_name",vrf.vrf, yang_name="vrf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf-name', extensions={u'tailf-common': {u'info': u'Virtual Routing and Forwarding', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vrf'}}), is_container='list', yang_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual Routing and Forwarding', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vrf'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)


  def _get_vlan(self):
    """
    Getter method for vlan, mapped from YANG variable /nas/server_ip/vlan (list)
    """
    return self.__vlan
      
  def _set_vlan(self, v, load=False):
    """
    Setter method for vlan, mapped from YANG variable /nas/server_ip/vlan (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("vlan_number",vlan.vlan, yang_name="vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-number', extensions={u'tailf-common': {u'info': u'Virtual LAN', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vlan'}}), is_container='list', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual LAN', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vlan'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vlan_number",vlan.vlan, yang_name="vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-number', extensions={u'tailf-common': {u'info': u'Virtual LAN', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vlan'}}), is_container='list', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual LAN', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vlan'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)""",
        })

    self.__vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan(self):
    self.__vlan = YANGDynClass(base=YANGListType("vlan_number",vlan.vlan, yang_name="vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-number', extensions={u'tailf-common': {u'info': u'Virtual LAN', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vlan'}}), is_container='list', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual LAN', u'cli-suppress-mode': None, u'callpoint': u'qos_nas_serverip_vlan'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)

  server_ip = __builtin__.property(_get_server_ip, _set_server_ip)
  vrf = __builtin__.property(_get_vrf, _set_vrf)
  vlan = __builtin__.property(_get_vlan, _set_vlan)


  _pyangbind_elements = {'server_ip': server_ip, 'vrf': vrf, 'vlan': vlan, }


