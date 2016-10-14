
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import show_cluster_mctd_client
import show_cluster_mem_vlan
class mctd_client_state_state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mct-operational - based on the path /mctd-client-state-state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MCT Client Operational Information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__show_cluster_mctd_client','__show_cluster_mem_vlan',)

  _yang_name = 'mctd-client-state-state'

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
    self.__show_cluster_mem_vlan = YANGDynClass(base=YANGListType("cluster_id",show_cluster_mem_vlan.show_cluster_mem_vlan, yang_name="show-cluster-mem-vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cluster-id', extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-mem-vlan-mct', u'cli-suppress-show-path': None}}), is_container='list', yang_name="show-cluster-mem-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-mem-vlan-mct', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)
    self.__show_cluster_mctd_client = YANGDynClass(base=YANGListType("cluster_id",show_cluster_mctd_client.show_cluster_mctd_client, yang_name="show-cluster-mctd-client", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cluster-id', extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-client-state', u'cli-suppress-show-path': None}}), is_container='list', yang_name="show-cluster-mctd-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-client-state', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)

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
      return [u'mctd-client-state-state']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'mctd-client-state-state']

  def _get_show_cluster_mctd_client(self):
    """
    Getter method for show_cluster_mctd_client, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client (list)

    YANG Description: MCT cluster client states
    """
    return self.__show_cluster_mctd_client
      
  def _set_show_cluster_mctd_client(self, v, load=False):
    """
    Setter method for show_cluster_mctd_client, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_cluster_mctd_client is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_cluster_mctd_client() directly.

    YANG Description: MCT cluster client states
    """
    try:
      t = YANGDynClass(v,base=YANGListType("cluster_id",show_cluster_mctd_client.show_cluster_mctd_client, yang_name="show-cluster-mctd-client", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cluster-id', extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-client-state', u'cli-suppress-show-path': None}}), is_container='list', yang_name="show-cluster-mctd-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-client-state', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_cluster_mctd_client must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("cluster_id",show_cluster_mctd_client.show_cluster_mctd_client, yang_name="show-cluster-mctd-client", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cluster-id', extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-client-state', u'cli-suppress-show-path': None}}), is_container='list', yang_name="show-cluster-mctd-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-client-state', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)""",
        })

    self.__show_cluster_mctd_client = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_cluster_mctd_client(self):
    self.__show_cluster_mctd_client = YANGDynClass(base=YANGListType("cluster_id",show_cluster_mctd_client.show_cluster_mctd_client, yang_name="show-cluster-mctd-client", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cluster-id', extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-client-state', u'cli-suppress-show-path': None}}), is_container='list', yang_name="show-cluster-mctd-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-client-state', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)


  def _get_show_cluster_mem_vlan(self):
    """
    Getter method for show_cluster_mem_vlan, mapped from YANG variable /mctd_client_state_state/show_cluster_mem_vlan (list)

    YANG Description: Vlan Label Info for show cluster mem-vlan
    """
    return self.__show_cluster_mem_vlan
      
  def _set_show_cluster_mem_vlan(self, v, load=False):
    """
    Setter method for show_cluster_mem_vlan, mapped from YANG variable /mctd_client_state_state/show_cluster_mem_vlan (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_cluster_mem_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_cluster_mem_vlan() directly.

    YANG Description: Vlan Label Info for show cluster mem-vlan
    """
    try:
      t = YANGDynClass(v,base=YANGListType("cluster_id",show_cluster_mem_vlan.show_cluster_mem_vlan, yang_name="show-cluster-mem-vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cluster-id', extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-mem-vlan-mct', u'cli-suppress-show-path': None}}), is_container='list', yang_name="show-cluster-mem-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-mem-vlan-mct', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_cluster_mem_vlan must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("cluster_id",show_cluster_mem_vlan.show_cluster_mem_vlan, yang_name="show-cluster-mem-vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cluster-id', extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-mem-vlan-mct', u'cli-suppress-show-path': None}}), is_container='list', yang_name="show-cluster-mem-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-mem-vlan-mct', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)""",
        })

    self.__show_cluster_mem_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_cluster_mem_vlan(self):
    self.__show_cluster_mem_vlan = YANGDynClass(base=YANGListType("cluster_id",show_cluster_mem_vlan.show_cluster_mem_vlan, yang_name="show-cluster-mem-vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cluster-id', extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-mem-vlan-mct', u'cli-suppress-show-path': None}}), is_container='list', yang_name="show-cluster-mem-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-show-cluster-mem-vlan-mct', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)

  show_cluster_mctd_client = __builtin__.property(_get_show_cluster_mctd_client)
  show_cluster_mem_vlan = __builtin__.property(_get_show_cluster_mem_vlan)


  _pyangbind_elements = {'show_cluster_mctd_client': show_cluster_mctd_client, 'show_cluster_mem_vlan': show_cluster_mem_vlan, }


