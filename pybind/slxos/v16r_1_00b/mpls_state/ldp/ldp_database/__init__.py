
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import mpls_ldp_database_downstream
import mpls_ldp_database_upstream
class ldp_database(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/ldp-database. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: LDP database operational Information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ldp_database_peer_ip','__ldp_database_own_ip','__mpls_ldp_database_downstream','__mpls_ldp_database_upstream',)

  _yang_name = 'ldp-database'

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
    self.__ldp_database_own_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-database-own-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__mpls_ldp_database_upstream = YANGDynClass(base=YANGListType("mpls_ldp_database_us_fec_prefix",mpls_ldp_database_upstream.mpls_ldp_database_upstream, yang_name="mpls-ldp-database-upstream", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-ldp-database-us-fec-prefix', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-upstream', u'cli-suppress-show-path': None}}), is_container='list', yang_name="mpls-ldp-database-upstream", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-upstream', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    self.__ldp_database_peer_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-database-peer-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__mpls_ldp_database_downstream = YANGDynClass(base=YANGListType("mpls_ldp_database_ds_fec_prefix",mpls_ldp_database_downstream.mpls_ldp_database_downstream, yang_name="mpls-ldp-database-downstream", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-ldp-database-ds-fec-prefix', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-downstream', u'cli-suppress-show-path': None}}), is_container='list', yang_name="mpls-ldp-database-downstream", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-downstream', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

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
      return [u'mpls-state', u'ldp', u'ldp-database']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'mpls-state', u'ldp', u'ldp-database']

  def _get_ldp_database_peer_ip(self):
    """
    Getter method for ldp_database_peer_ip, mapped from YANG variable /mpls_state/ldp/ldp_database/ldp_database_peer_ip (inet:ipv4-address)

    YANG Description: LDP Peer IP Address
    """
    return self.__ldp_database_peer_ip
      
  def _set_ldp_database_peer_ip(self, v, load=False):
    """
    Setter method for ldp_database_peer_ip, mapped from YANG variable /mpls_state/ldp/ldp_database/ldp_database_peer_ip (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_database_peer_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_database_peer_ip() directly.

    YANG Description: LDP Peer IP Address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-database-peer-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_database_peer_ip must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-database-peer-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__ldp_database_peer_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_database_peer_ip(self):
    self.__ldp_database_peer_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-database-peer-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_ldp_database_own_ip(self):
    """
    Getter method for ldp_database_own_ip, mapped from YANG variable /mpls_state/ldp/ldp_database/ldp_database_own_ip (inet:ipv4-address)

    YANG Description: LDP Own IP Address
    """
    return self.__ldp_database_own_ip
      
  def _set_ldp_database_own_ip(self, v, load=False):
    """
    Setter method for ldp_database_own_ip, mapped from YANG variable /mpls_state/ldp/ldp_database/ldp_database_own_ip (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_database_own_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_database_own_ip() directly.

    YANG Description: LDP Own IP Address
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-database-own-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_database_own_ip must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-database-own-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__ldp_database_own_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_database_own_ip(self):
    self.__ldp_database_own_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-database-own-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_mpls_ldp_database_downstream(self):
    """
    Getter method for mpls_ldp_database_downstream, mapped from YANG variable /mpls_state/ldp/ldp_database/mpls_ldp_database_downstream (list)

    YANG Description: ldp database downstream
    """
    return self.__mpls_ldp_database_downstream
      
  def _set_mpls_ldp_database_downstream(self, v, load=False):
    """
    Setter method for mpls_ldp_database_downstream, mapped from YANG variable /mpls_state/ldp/ldp_database/mpls_ldp_database_downstream (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_ldp_database_downstream is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_ldp_database_downstream() directly.

    YANG Description: ldp database downstream
    """
    try:
      t = YANGDynClass(v,base=YANGListType("mpls_ldp_database_ds_fec_prefix",mpls_ldp_database_downstream.mpls_ldp_database_downstream, yang_name="mpls-ldp-database-downstream", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-ldp-database-ds-fec-prefix', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-downstream', u'cli-suppress-show-path': None}}), is_container='list', yang_name="mpls-ldp-database-downstream", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-downstream', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_ldp_database_downstream must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("mpls_ldp_database_ds_fec_prefix",mpls_ldp_database_downstream.mpls_ldp_database_downstream, yang_name="mpls-ldp-database-downstream", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-ldp-database-ds-fec-prefix', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-downstream', u'cli-suppress-show-path': None}}), is_container='list', yang_name="mpls-ldp-database-downstream", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-downstream', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__mpls_ldp_database_downstream = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_ldp_database_downstream(self):
    self.__mpls_ldp_database_downstream = YANGDynClass(base=YANGListType("mpls_ldp_database_ds_fec_prefix",mpls_ldp_database_downstream.mpls_ldp_database_downstream, yang_name="mpls-ldp-database-downstream", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-ldp-database-ds-fec-prefix', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-downstream', u'cli-suppress-show-path': None}}), is_container='list', yang_name="mpls-ldp-database-downstream", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-downstream', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)


  def _get_mpls_ldp_database_upstream(self):
    """
    Getter method for mpls_ldp_database_upstream, mapped from YANG variable /mpls_state/ldp/ldp_database/mpls_ldp_database_upstream (list)

    YANG Description: ldp database upstream
    """
    return self.__mpls_ldp_database_upstream
      
  def _set_mpls_ldp_database_upstream(self, v, load=False):
    """
    Setter method for mpls_ldp_database_upstream, mapped from YANG variable /mpls_state/ldp/ldp_database/mpls_ldp_database_upstream (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_ldp_database_upstream is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_ldp_database_upstream() directly.

    YANG Description: ldp database upstream
    """
    try:
      t = YANGDynClass(v,base=YANGListType("mpls_ldp_database_us_fec_prefix",mpls_ldp_database_upstream.mpls_ldp_database_upstream, yang_name="mpls-ldp-database-upstream", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-ldp-database-us-fec-prefix', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-upstream', u'cli-suppress-show-path': None}}), is_container='list', yang_name="mpls-ldp-database-upstream", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-upstream', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_ldp_database_upstream must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("mpls_ldp_database_us_fec_prefix",mpls_ldp_database_upstream.mpls_ldp_database_upstream, yang_name="mpls-ldp-database-upstream", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-ldp-database-us-fec-prefix', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-upstream', u'cli-suppress-show-path': None}}), is_container='list', yang_name="mpls-ldp-database-upstream", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-upstream', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__mpls_ldp_database_upstream = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_ldp_database_upstream(self):
    self.__mpls_ldp_database_upstream = YANGDynClass(base=YANGListType("mpls_ldp_database_us_fec_prefix",mpls_ldp_database_upstream.mpls_ldp_database_upstream, yang_name="mpls-ldp-database-upstream", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-ldp-database-us-fec-prefix', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-upstream', u'cli-suppress-show-path': None}}), is_container='list', yang_name="mpls-ldp-database-upstream", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-database-upstream', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

  ldp_database_peer_ip = __builtin__.property(_get_ldp_database_peer_ip)
  ldp_database_own_ip = __builtin__.property(_get_ldp_database_own_ip)
  mpls_ldp_database_downstream = __builtin__.property(_get_mpls_ldp_database_downstream)
  mpls_ldp_database_upstream = __builtin__.property(_get_mpls_ldp_database_upstream)


  _pyangbind_elements = {'ldp_database_peer_ip': ldp_database_peer_ip, 'ldp_database_own_ip': ldp_database_own_ip, 'mpls_ldp_database_downstream': mpls_ldp_database_downstream, 'mpls_ldp_database_upstream': mpls_ldp_database_upstream, }


