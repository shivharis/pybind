
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vlan_label_info
class show_cluster_mem_vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-l2sys-operational - based on the path /mct-l2ys-state/show-cluster-mem-vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__cluster_id','__num_vlans','__vlan_label_info',)

  _yang_name = 'show-cluster-mem-vlan'

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
    self.__vlan_label_info = YANGDynClass(base=vlan_label_info.vlan_label_info, is_container='container', yang_name="vlan-label-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'l2sys-vlan-label-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='container', is_config=False)
    self.__cluster_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)
    self.__num_vlans = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)

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
      return [u'mct-l2ys-state', u'show-cluster-mem-vlan']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'mct-l2ys-state', u'show-cluster-mem-vlan']

  def _get_cluster_id(self):
    """
    Getter method for cluster_id, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_vlan/cluster_id (uint32)
    """
    return self.__cluster_id
      
  def _set_cluster_id(self, v, load=False):
    """
    Setter method for cluster_id, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_vlan/cluster_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cluster_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cluster_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cluster_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)""",
        })

    self.__cluster_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cluster_id(self):
    self.__cluster_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)


  def _get_num_vlans(self):
    """
    Getter method for num_vlans, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_vlan/num_vlans (uint32)

    YANG Description: No. of Vlans configured
    """
    return self.__num_vlans
      
  def _set_num_vlans(self, v, load=False):
    """
    Setter method for num_vlans, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_vlan/num_vlans (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_vlans is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_vlans() directly.

    YANG Description: No. of Vlans configured
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_vlans must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_vlans = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_vlans(self):
    self.__num_vlans = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)


  def _get_vlan_label_info(self):
    """
    Getter method for vlan_label_info, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_vlan/vlan_label_info (container)

    YANG Description: Vlan Label Info
    """
    return self.__vlan_label_info
      
  def _set_vlan_label_info(self, v, load=False):
    """
    Setter method for vlan_label_info, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_vlan/vlan_label_info (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_label_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_label_info() directly.

    YANG Description: Vlan Label Info
    """
    try:
      t = YANGDynClass(v,base=vlan_label_info.vlan_label_info, is_container='container', yang_name="vlan-label-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'l2sys-vlan-label-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_label_info must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vlan_label_info.vlan_label_info, is_container='container', yang_name="vlan-label-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'l2sys-vlan-label-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='container', is_config=False)""",
        })

    self.__vlan_label_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_label_info(self):
    self.__vlan_label_info = YANGDynClass(base=vlan_label_info.vlan_label_info, is_container='container', yang_name="vlan-label-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'l2sys-vlan-label-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='container', is_config=False)

  cluster_id = __builtin__.property(_get_cluster_id)
  num_vlans = __builtin__.property(_get_num_vlans)
  vlan_label_info = __builtin__.property(_get_vlan_label_info)


  _pyangbind_elements = {'cluster_id': cluster_id, 'num_vlans': num_vlans, 'vlan_label_info': vlan_label_info, }


