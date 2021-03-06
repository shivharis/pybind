
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ipv6_interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/interface/ve/ipv6/ipv6-local-anycast-gateway/ipv6-track/ipv6-interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipv6_interface_type','__ipv6_interface_name','__ipv6_interface_priority',)

  _yang_name = 'ipv6-interface'
  _rest_name = 'interface'

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
    self.__ipv6_interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2})'}),], is_leaf=True, yang_name="ipv6-interface-name", rest_name="ipv6-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='vrrp:track-ifname', is_config=True)
    self.__ipv6_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 10}, u'port-channel': {'value': 3}},), is_leaf=True, yang_name="ipv6-interface-type", rest_name="ipv6-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='vrrp:track-iftype', is_config=True)
    self.__ipv6_interface_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="ipv6-interface-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Track Priority', u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='uint32', is_config=True)

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
      return [u'rbridge-id', u'interface', u've', u'ipv6', u'ipv6-local-anycast-gateway', u'ipv6-track', u'ipv6-interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'interface', u'Ve', u'ipv6', u'fabric-virtual-gateway', u'track', u'interface']

  def _get_ipv6_interface_type(self):
    """
    Getter method for ipv6_interface_type, mapped from YANG variable /rbridge_id/interface/ve/ipv6/ipv6_local_anycast_gateway/ipv6_track/ipv6_interface/ipv6_interface_type (vrrp:track-iftype)
    """
    return self.__ipv6_interface_type
      
  def _set_ipv6_interface_type(self, v, load=False):
    """
    Setter method for ipv6_interface_type, mapped from YANG variable /rbridge_id/interface/ve/ipv6/ipv6_local_anycast_gateway/ipv6_track/ipv6_interface/ipv6_interface_type (vrrp:track-iftype)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_interface_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 10}, u'port-channel': {'value': 3}},), is_leaf=True, yang_name="ipv6-interface-type", rest_name="ipv6-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='vrrp:track-iftype', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_interface_type must be of a type compatible with vrrp:track-iftype""",
          'defined-type': "vrrp:track-iftype",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 10}, u'port-channel': {'value': 3}},), is_leaf=True, yang_name="ipv6-interface-type", rest_name="ipv6-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='vrrp:track-iftype', is_config=True)""",
        })

    self.__ipv6_interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_interface_type(self):
    self.__ipv6_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 10}, u'port-channel': {'value': 3}},), is_leaf=True, yang_name="ipv6-interface-type", rest_name="ipv6-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='vrrp:track-iftype', is_config=True)


  def _get_ipv6_interface_name(self):
    """
    Getter method for ipv6_interface_name, mapped from YANG variable /rbridge_id/interface/ve/ipv6/ipv6_local_anycast_gateway/ipv6_track/ipv6_interface/ipv6_interface_name (vrrp:track-ifname)
    """
    return self.__ipv6_interface_name
      
  def _set_ipv6_interface_name(self, v, load=False):
    """
    Setter method for ipv6_interface_name, mapped from YANG variable /rbridge_id/interface/ve/ipv6/ipv6_local_anycast_gateway/ipv6_track/ipv6_interface/ipv6_interface_name (vrrp:track-ifname)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_interface_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2})'}),], is_leaf=True, yang_name="ipv6-interface-name", rest_name="ipv6-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='vrrp:track-ifname', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_interface_name must be of a type compatible with vrrp:track-ifname""",
          'defined-type': "vrrp:track-ifname",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2})'}),], is_leaf=True, yang_name="ipv6-interface-name", rest_name="ipv6-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='vrrp:track-ifname', is_config=True)""",
        })

    self.__ipv6_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_interface_name(self):
    self.__ipv6_interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2})'}),], is_leaf=True, yang_name="ipv6-interface-name", rest_name="ipv6-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='vrrp:track-ifname', is_config=True)


  def _get_ipv6_interface_priority(self):
    """
    Getter method for ipv6_interface_priority, mapped from YANG variable /rbridge_id/interface/ve/ipv6/ipv6_local_anycast_gateway/ipv6_track/ipv6_interface/ipv6_interface_priority (uint32)

    YANG Description: Track Priority
    """
    return self.__ipv6_interface_priority
      
  def _set_ipv6_interface_priority(self, v, load=False):
    """
    Setter method for ipv6_interface_priority, mapped from YANG variable /rbridge_id/interface/ve/ipv6/ipv6_local_anycast_gateway/ipv6_track/ipv6_interface/ipv6_interface_priority (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_interface_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_interface_priority() directly.

    YANG Description: Track Priority
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="ipv6-interface-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Track Priority', u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_interface_priority must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="ipv6-interface-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Track Priority', u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='uint32', is_config=True)""",
        })

    self.__ipv6_interface_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_interface_priority(self):
    self.__ipv6_interface_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="ipv6-interface-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Track Priority', u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='uint32', is_config=True)

  ipv6_interface_type = __builtin__.property(_get_ipv6_interface_type, _set_ipv6_interface_type)
  ipv6_interface_name = __builtin__.property(_get_ipv6_interface_name, _set_ipv6_interface_name)
  ipv6_interface_priority = __builtin__.property(_get_ipv6_interface_priority, _set_ipv6_interface_priority)


  _pyangbind_elements = {'ipv6_interface_type': ipv6_interface_type, 'ipv6_interface_name': ipv6_interface_name, 'ipv6_interface_priority': ipv6_interface_priority, }


