
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vlan_vni_mapping
import vlan
class map_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tunnels - based on the path /overlay-gateway/map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__vlan_vni_mapping','__vlan',)

  _yang_name = 'map'

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
    self.__vlan = YANGDynClass(base=vlan.vlan, is_container='container', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify VLAN to VNI mappings for the Overlay Gateway.', u'callpoint': u'autoVlanToVNIMappingCallPoint', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    self.__vlan_vni_mapping = YANGDynClass(base=YANGListType("vid",vlan_vni_mapping.vlan_vni_mapping, yang_name="vlan-vni-mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vid', extensions={u'tailf-common': {u'callpoint': u'vlanToVNIMappingCallPoint', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="vlan-vni-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'vlanToVNIMappingCallPoint', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='list', is_config=True)

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
      return [u'overlay-gateway', u'map']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'overlay-gateway', u'map']

  def _get_vlan_vni_mapping(self):
    """
    Getter method for vlan_vni_mapping, mapped from YANG variable /overlay_gateway/map/vlan_vni_mapping (list)
    """
    return self.__vlan_vni_mapping
      
  def _set_vlan_vni_mapping(self, v, load=False):
    """
    Setter method for vlan_vni_mapping, mapped from YANG variable /overlay_gateway/map/vlan_vni_mapping (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_vni_mapping is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_vni_mapping() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("vid",vlan_vni_mapping.vlan_vni_mapping, yang_name="vlan-vni-mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vid', extensions={u'tailf-common': {u'callpoint': u'vlanToVNIMappingCallPoint', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="vlan-vni-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'vlanToVNIMappingCallPoint', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_vni_mapping must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vid",vlan_vni_mapping.vlan_vni_mapping, yang_name="vlan-vni-mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vid', extensions={u'tailf-common': {u'callpoint': u'vlanToVNIMappingCallPoint', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="vlan-vni-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'vlanToVNIMappingCallPoint', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='list', is_config=True)""",
        })

    self.__vlan_vni_mapping = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_vni_mapping(self):
    self.__vlan_vni_mapping = YANGDynClass(base=YANGListType("vid",vlan_vni_mapping.vlan_vni_mapping, yang_name="vlan-vni-mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vid', extensions={u'tailf-common': {u'callpoint': u'vlanToVNIMappingCallPoint', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="vlan-vni-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'vlanToVNIMappingCallPoint', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='list', is_config=True)


  def _get_vlan(self):
    """
    Getter method for vlan, mapped from YANG variable /overlay_gateway/map/vlan (container)
    """
    return self.__vlan
      
  def _set_vlan(self, v, load=False):
    """
    Setter method for vlan, mapped from YANG variable /overlay_gateway/map/vlan (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan() directly.
    """
    try:
      t = YANGDynClass(v,base=vlan.vlan, is_container='container', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify VLAN to VNI mappings for the Overlay Gateway.', u'callpoint': u'autoVlanToVNIMappingCallPoint', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vlan.vlan, is_container='container', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify VLAN to VNI mappings for the Overlay Gateway.', u'callpoint': u'autoVlanToVNIMappingCallPoint', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)""",
        })

    self.__vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan(self):
    self.__vlan = YANGDynClass(base=vlan.vlan, is_container='container', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify VLAN to VNI mappings for the Overlay Gateway.', u'callpoint': u'autoVlanToVNIMappingCallPoint', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)

  vlan_vni_mapping = __builtin__.property(_get_vlan_vni_mapping, _set_vlan_vni_mapping)
  vlan = __builtin__.property(_get_vlan, _set_vlan)


  _pyangbind_elements = {'vlan_vni_mapping': vlan_vni_mapping, 'vlan': vlan, }


