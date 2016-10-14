
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import master_vlan
import member_vlan
import member_bd
class topology_group_data(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-nsm-operational - based on the path /topology-group-state/topology-group-data. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: topology-group id
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__topology_group_id','__l2_protocol','__master_vlan','__member_vlan','__member_bd',)

  _yang_name = 'topology-group-data'

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
    self.__member_vlan = YANGDynClass(base=YANGListType("vlan_id",member_vlan.member_vlan, yang_name="member-vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'nsm-member-vlan', u'cli-suppress-show-path': None}}), is_container='list', yang_name="member-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-member-vlan', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    self.__l2_protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="l2-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    self.__member_bd = YANGDynClass(base=YANGListType("bd_id",member_bd.member_bd, yang_name="member-bd", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'nsm-member-bd', u'cli-suppress-show-path': None}}), is_container='list', yang_name="member-bd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-member-bd', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    self.__topology_group_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="topology-group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint16', is_config=False)
    self.__master_vlan = YANGDynClass(base=master_vlan.master_vlan, is_container='container', yang_name="master-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-master-vlan', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='container', is_config=False)

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
      return [u'topology-group-state', u'topology-group-data']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'topology-group-state', u'topology-group-data']

  def _get_topology_group_id(self):
    """
    Getter method for topology_group_id, mapped from YANG variable /topology_group_state/topology_group_data/topology_group_id (uint16)

    YANG Description: Topology group id
    """
    return self.__topology_group_id
      
  def _set_topology_group_id(self, v, load=False):
    """
    Setter method for topology_group_id, mapped from YANG variable /topology_group_state/topology_group_data/topology_group_id (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_topology_group_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_topology_group_id() directly.

    YANG Description: Topology group id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="topology-group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """topology_group_id must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="topology-group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint16', is_config=False)""",
        })

    self.__topology_group_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_topology_group_id(self):
    self.__topology_group_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="topology-group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint16', is_config=False)


  def _get_l2_protocol(self):
    """
    Getter method for l2_protocol, mapped from YANG variable /topology_group_state/topology_group_data/l2_protocol (string)

    YANG Description: L2 Protocol Configured
    """
    return self.__l2_protocol
      
  def _set_l2_protocol(self, v, load=False):
    """
    Setter method for l2_protocol, mapped from YANG variable /topology_group_state/topology_group_data/l2_protocol (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l2_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l2_protocol() directly.

    YANG Description: L2 Protocol Configured
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="l2-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l2_protocol must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="l2-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)""",
        })

    self.__l2_protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l2_protocol(self):
    self.__l2_protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="l2-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)


  def _get_master_vlan(self):
    """
    Getter method for master_vlan, mapped from YANG variable /topology_group_state/topology_group_data/master_vlan (container)

    YANG Description: master vlan info
    """
    return self.__master_vlan
      
  def _set_master_vlan(self, v, load=False):
    """
    Setter method for master_vlan, mapped from YANG variable /topology_group_state/topology_group_data/master_vlan (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_master_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_master_vlan() directly.

    YANG Description: master vlan info
    """
    try:
      t = YANGDynClass(v,base=master_vlan.master_vlan, is_container='container', yang_name="master-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-master-vlan', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """master_vlan must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=master_vlan.master_vlan, is_container='container', yang_name="master-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-master-vlan', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='container', is_config=False)""",
        })

    self.__master_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_master_vlan(self):
    self.__master_vlan = YANGDynClass(base=master_vlan.master_vlan, is_container='container', yang_name="master-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-master-vlan', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='container', is_config=False)


  def _get_member_vlan(self):
    """
    Getter method for member_vlan, mapped from YANG variable /topology_group_state/topology_group_data/member_vlan (list)

    YANG Description: member vlan info
    """
    return self.__member_vlan
      
  def _set_member_vlan(self, v, load=False):
    """
    Setter method for member_vlan, mapped from YANG variable /topology_group_state/topology_group_data/member_vlan (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_member_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_member_vlan() directly.

    YANG Description: member vlan info
    """
    try:
      t = YANGDynClass(v,base=YANGListType("vlan_id",member_vlan.member_vlan, yang_name="member-vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'nsm-member-vlan', u'cli-suppress-show-path': None}}), is_container='list', yang_name="member-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-member-vlan', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """member_vlan must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vlan_id",member_vlan.member_vlan, yang_name="member-vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'nsm-member-vlan', u'cli-suppress-show-path': None}}), is_container='list', yang_name="member-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-member-vlan', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)""",
        })

    self.__member_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_member_vlan(self):
    self.__member_vlan = YANGDynClass(base=YANGListType("vlan_id",member_vlan.member_vlan, yang_name="member-vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'nsm-member-vlan', u'cli-suppress-show-path': None}}), is_container='list', yang_name="member-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-member-vlan', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)


  def _get_member_bd(self):
    """
    Getter method for member_bd, mapped from YANG variable /topology_group_state/topology_group_data/member_bd (list)

    YANG Description: member bd info
    """
    return self.__member_bd
      
  def _set_member_bd(self, v, load=False):
    """
    Setter method for member_bd, mapped from YANG variable /topology_group_state/topology_group_data/member_bd (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_member_bd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_member_bd() directly.

    YANG Description: member bd info
    """
    try:
      t = YANGDynClass(v,base=YANGListType("bd_id",member_bd.member_bd, yang_name="member-bd", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'nsm-member-bd', u'cli-suppress-show-path': None}}), is_container='list', yang_name="member-bd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-member-bd', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """member_bd must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("bd_id",member_bd.member_bd, yang_name="member-bd", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'nsm-member-bd', u'cli-suppress-show-path': None}}), is_container='list', yang_name="member-bd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-member-bd', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)""",
        })

    self.__member_bd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_member_bd(self):
    self.__member_bd = YANGDynClass(base=YANGListType("bd_id",member_bd.member_bd, yang_name="member-bd", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'nsm-member-bd', u'cli-suppress-show-path': None}}), is_container='list', yang_name="member-bd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-member-bd', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)

  topology_group_id = __builtin__.property(_get_topology_group_id)
  l2_protocol = __builtin__.property(_get_l2_protocol)
  master_vlan = __builtin__.property(_get_master_vlan)
  member_vlan = __builtin__.property(_get_member_vlan)
  member_bd = __builtin__.property(_get_member_bd)


  _pyangbind_elements = {'topology_group_id': topology_group_id, 'l2_protocol': l2_protocol, 'master_vlan': master_vlan, 'member_vlan': member_vlan, 'member_bd': member_bd, }


