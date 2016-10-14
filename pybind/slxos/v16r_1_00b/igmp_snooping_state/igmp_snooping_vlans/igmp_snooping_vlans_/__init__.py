
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vlan_groups
class igmp_snooping_vlans(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mc-hms-operational - based on the path /igmp-snooping-state/igmp-snooping-vlans/igmp-snooping-vlans. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Igmp snooping enabled interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__vlan_id','__multicast_router_ports','__is_querier','__igmp_operation_mode','__fast_leave','__qmrt','__lmqi','__qi','__version','__num_of_mcast_grps','__vlan_groups',)

  _yang_name = 'igmp-snooping-vlans'

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
    self.__multicast_router_ports = YANGDynClass(base=unicode, is_leaf=True, yang_name="multicast-router-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__igmp_operation_mode = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="igmp-operation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    self.__version = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    self.__vlan_groups = YANGDynClass(base=YANGListType("grp_ip_addr",vlan_groups.vlan_groups, yang_name="vlan-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='grp-ip-addr', extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-vlan-group', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vlan-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-vlan-group', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)
    self.__qmrt = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="qmrt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    self.__is_querier = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="is-querier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    self.__qi = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="qi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    self.__lmqi = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lmqi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    self.__fast_leave = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fast-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    self.__num_of_mcast_grps = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-mcast-grps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)

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
      return [u'igmp-snooping-state', u'igmp-snooping-vlans', u'igmp-snooping-vlans']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'igmp-snooping-state', u'igmp-snooping-vlans', u'igmp-snooping-vlans']

  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/vlan_id (uint32)

    YANG Description: vlan id
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/vlan_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: vlan id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_multicast_router_ports(self):
    """
    Getter method for multicast_router_ports, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/multicast_router_ports (string)

    YANG Description: Multicast Router ports
    """
    return self.__multicast_router_ports
      
  def _set_multicast_router_ports(self, v, load=False):
    """
    Setter method for multicast_router_ports, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/multicast_router_ports (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_multicast_router_ports is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_multicast_router_ports() directly.

    YANG Description: Multicast Router ports
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="multicast-router-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """multicast_router_ports must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="multicast-router-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__multicast_router_ports = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_multicast_router_ports(self):
    self.__multicast_router_ports = YANGDynClass(base=unicode, is_leaf=True, yang_name="multicast-router-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_is_querier(self):
    """
    Getter method for is_querier, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/is_querier (uint8)

    YANG Description: Is interface Querier enabled
    """
    return self.__is_querier
      
  def _set_is_querier(self, v, load=False):
    """
    Setter method for is_querier, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/is_querier (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_is_querier is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_is_querier() directly.

    YANG Description: Is interface Querier enabled
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="is-querier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """is_querier must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="is-querier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)""",
        })

    self.__is_querier = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_is_querier(self):
    self.__is_querier = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="is-querier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)


  def _get_igmp_operation_mode(self):
    """
    Getter method for igmp_operation_mode, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/igmp_operation_mode (uint32)

    YANG Description: IGMP Operation mode
    """
    return self.__igmp_operation_mode
      
  def _set_igmp_operation_mode(self, v, load=False):
    """
    Setter method for igmp_operation_mode, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/igmp_operation_mode (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmp_operation_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmp_operation_mode() directly.

    YANG Description: IGMP Operation mode
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="igmp-operation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmp_operation_mode must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="igmp-operation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__igmp_operation_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmp_operation_mode(self):
    self.__igmp_operation_mode = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="igmp-operation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_fast_leave(self):
    """
    Getter method for fast_leave, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/fast_leave (uint8)

    YANG Description: Is Fast Leave enabled
    """
    return self.__fast_leave
      
  def _set_fast_leave(self, v, load=False):
    """
    Setter method for fast_leave, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/fast_leave (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fast_leave is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fast_leave() directly.

    YANG Description: Is Fast Leave enabled
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fast-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fast_leave must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fast-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)""",
        })

    self.__fast_leave = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fast_leave(self):
    self.__fast_leave = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fast-leave", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)


  def _get_qmrt(self):
    """
    Getter method for qmrt, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/qmrt (uint32)

    YANG Description: Igmp query response time
    """
    return self.__qmrt
      
  def _set_qmrt(self, v, load=False):
    """
    Setter method for qmrt, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/qmrt (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_qmrt is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_qmrt() directly.

    YANG Description: Igmp query response time
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="qmrt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """qmrt must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="qmrt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__qmrt = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_qmrt(self):
    self.__qmrt = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="qmrt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_lmqi(self):
    """
    Getter method for lmqi, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/lmqi (uint32)

    YANG Description: Last Member Query Interval
    """
    return self.__lmqi
      
  def _set_lmqi(self, v, load=False):
    """
    Setter method for lmqi, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/lmqi (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lmqi is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lmqi() directly.

    YANG Description: Last Member Query Interval
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lmqi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lmqi must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lmqi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__lmqi = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lmqi(self):
    self.__lmqi = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lmqi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_qi(self):
    """
    Getter method for qi, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/qi (uint32)

    YANG Description: Query Interval
    """
    return self.__qi
      
  def _set_qi(self, v, load=False):
    """
    Setter method for qi, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/qi (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_qi is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_qi() directly.

    YANG Description: Query Interval
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="qi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """qi must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="qi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__qi = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_qi(self):
    self.__qi = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="qi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_version(self):
    """
    Getter method for version, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/version (uint8)

    YANG Description: Igmp Version
    """
    return self.__version
      
  def _set_version(self, v, load=False):
    """
    Setter method for version, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/version (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_version() directly.

    YANG Description: Igmp Version
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """version must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)""",
        })

    self.__version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_version(self):
    self.__version = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)


  def _get_num_of_mcast_grps(self):
    """
    Getter method for num_of_mcast_grps, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/num_of_mcast_grps (uint32)

    YANG Description: Number of Multicast Groups
    """
    return self.__num_of_mcast_grps
      
  def _set_num_of_mcast_grps(self, v, load=False):
    """
    Setter method for num_of_mcast_grps, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/num_of_mcast_grps (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_of_mcast_grps is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_of_mcast_grps() directly.

    YANG Description: Number of Multicast Groups
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-mcast-grps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_of_mcast_grps must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-mcast-grps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_of_mcast_grps = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_of_mcast_grps(self):
    self.__num_of_mcast_grps = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-mcast-grps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_vlan_groups(self):
    """
    Getter method for vlan_groups, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/vlan_groups (list)

    YANG Description: Group information on an interface
    """
    return self.__vlan_groups
      
  def _set_vlan_groups(self, v, load=False):
    """
    Setter method for vlan_groups, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/vlan_groups (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_groups() directly.

    YANG Description: Group information on an interface
    """
    try:
      t = YANGDynClass(v,base=YANGListType("grp_ip_addr",vlan_groups.vlan_groups, yang_name="vlan-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='grp-ip-addr', extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-vlan-group', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vlan-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-vlan-group', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_groups must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("grp_ip_addr",vlan_groups.vlan_groups, yang_name="vlan-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='grp-ip-addr', extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-vlan-group', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vlan-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-vlan-group', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)""",
        })

    self.__vlan_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_groups(self):
    self.__vlan_groups = YANGDynClass(base=YANGListType("grp_ip_addr",vlan_groups.vlan_groups, yang_name="vlan-groups", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='grp-ip-addr', extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-vlan-group', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vlan-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmp-snooping-vlan-group', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)

  vlan_id = __builtin__.property(_get_vlan_id)
  multicast_router_ports = __builtin__.property(_get_multicast_router_ports)
  is_querier = __builtin__.property(_get_is_querier)
  igmp_operation_mode = __builtin__.property(_get_igmp_operation_mode)
  fast_leave = __builtin__.property(_get_fast_leave)
  qmrt = __builtin__.property(_get_qmrt)
  lmqi = __builtin__.property(_get_lmqi)
  qi = __builtin__.property(_get_qi)
  version = __builtin__.property(_get_version)
  num_of_mcast_grps = __builtin__.property(_get_num_of_mcast_grps)
  vlan_groups = __builtin__.property(_get_vlan_groups)


  _pyangbind_elements = {'vlan_id': vlan_id, 'multicast_router_ports': multicast_router_ports, 'is_querier': is_querier, 'igmp_operation_mode': igmp_operation_mode, 'fast_leave': fast_leave, 'qmrt': qmrt, 'lmqi': lmqi, 'qi': qi, 'version': version, 'num_of_mcast_grps': num_of_mcast_grps, 'vlan_groups': vlan_groups, }


