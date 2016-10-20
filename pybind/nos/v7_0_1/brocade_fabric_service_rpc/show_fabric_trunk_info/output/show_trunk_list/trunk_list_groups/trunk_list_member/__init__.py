
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class trunk_list_member(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fabric-service - based on the path /brocade_fabric_service_rpc/show-fabric-trunk-info/output/show-trunk-list/trunk-list-groups/trunk-list-member. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__trunk_list_src_port','__trunk_list_interface_type','__trunk_list_src_interface','__trunk_list_nbr_rbridge_id','__trunk_list_nbr_port','__trunk_list_nbr_interface_type','__trunk_list_nbr_interface','__trunk_list_nbr_wwn','__trunk_list_is_primary',)

  _yang_name = 'trunk-list-member'
  _rest_name = 'trunk-list-member'

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
    self.__trunk_list_nbr_port = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-nbr-port", rest_name="trunk-list-nbr-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Neighbor port index'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)
    self.__trunk_list_nbr_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'Te|Fi', 'length': [u'2']}), is_leaf=True, yang_name="trunk-list-nbr-interface-type", rest_name="trunk-list-nbr-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Interface type of neighbour port'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interfacetype-type', is_config=True)
    self.__trunk_list_src_interface = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="trunk-list-src-interface", rest_name="trunk-list-src-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Source Interface'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interface:interface-type', is_config=True)
    self.__trunk_list_src_port = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-src-port", rest_name="trunk-list-src-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Source port index'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)
    self.__trunk_list_nbr_wwn = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]'}), is_leaf=True, yang_name="trunk-list-nbr-wwn", rest_name="trunk-list-nbr-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'WWN of neighbor switch'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='common-def:wwn-type', is_config=True)
    self.__trunk_list_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'Te|Fi', 'length': [u'2']}), is_leaf=True, yang_name="trunk-list-interface-type", rest_name="trunk-list-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Interface type'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interfacetype-type', is_config=True)
    self.__trunk_list_is_primary = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'True|False|true|false', 'length': [u'0..5']}), is_leaf=True, yang_name="trunk-list-is-primary", rest_name="trunk-list-is-primary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'True represents trunk master'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='trunk-list-is-primary-type', is_config=True)
    self.__trunk_list_nbr_rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-nbr-rbridge-id", rest_name="trunk-list-nbr-rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Neighbor rbridge-id. '}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)
    self.__trunk_list_nbr_interface = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="trunk-list-nbr-interface", rest_name="trunk-list-nbr-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Neighbour Interface'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interface:interface-type', is_config=True)

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
      return [u'brocade_fabric_service_rpc', u'show-fabric-trunk-info', u'output', u'show-trunk-list', u'trunk-list-groups', u'trunk-list-member']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-fabric-trunk-info', u'output', u'show-trunk-list', u'trunk-list-groups', u'trunk-list-member']

  def _get_trunk_list_src_port(self):
    """
    Getter method for trunk_list_src_port, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_src_port (uint32)

    YANG Description: Source port index of
the trunk member.
    """
    return self.__trunk_list_src_port
      
  def _set_trunk_list_src_port(self, v, load=False):
    """
    Setter method for trunk_list_src_port, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_src_port (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_list_src_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_list_src_port() directly.

    YANG Description: Source port index of
the trunk member.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-src-port", rest_name="trunk-list-src-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Source port index'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_list_src_port must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-src-port", rest_name="trunk-list-src-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Source port index'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)""",
        })

    self.__trunk_list_src_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_list_src_port(self):
    self.__trunk_list_src_port = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-src-port", rest_name="trunk-list-src-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Source port index'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)


  def _get_trunk_list_interface_type(self):
    """
    Getter method for trunk_list_interface_type, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_interface_type (interfacetype-type)

    YANG Description: Interface type.
It can take the following
values:
   Te - for 10G Ethernet interface
   Fi - for Fibre Channel
   interface.
    """
    return self.__trunk_list_interface_type
      
  def _set_trunk_list_interface_type(self, v, load=False):
    """
    Setter method for trunk_list_interface_type, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_interface_type (interfacetype-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_list_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_list_interface_type() directly.

    YANG Description: Interface type.
It can take the following
values:
   Te - for 10G Ethernet interface
   Fi - for Fibre Channel
   interface.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'Te|Fi', 'length': [u'2']}), is_leaf=True, yang_name="trunk-list-interface-type", rest_name="trunk-list-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Interface type'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interfacetype-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_list_interface_type must be of a type compatible with interfacetype-type""",
          'defined-type': "brocade-fabric-service:interfacetype-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'Te|Fi', 'length': [u'2']}), is_leaf=True, yang_name="trunk-list-interface-type", rest_name="trunk-list-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Interface type'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interfacetype-type', is_config=True)""",
        })

    self.__trunk_list_interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_list_interface_type(self):
    self.__trunk_list_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'Te|Fi', 'length': [u'2']}), is_leaf=True, yang_name="trunk-list-interface-type", rest_name="trunk-list-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Interface type'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interfacetype-type', is_config=True)


  def _get_trunk_list_src_interface(self):
    """
    Getter method for trunk_list_src_interface, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_src_interface (interface:interface-type)

    YANG Description: Source port interface info
It is in the format
rbridge-id/slot/port.
    """
    return self.__trunk_list_src_interface
      
  def _set_trunk_list_src_interface(self, v, load=False):
    """
    Setter method for trunk_list_src_interface, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_src_interface (interface:interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_list_src_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_list_src_interface() directly.

    YANG Description: Source port interface info
It is in the format
rbridge-id/slot/port.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="trunk-list-src-interface", rest_name="trunk-list-src-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Source Interface'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interface:interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_list_src_interface must be of a type compatible with interface:interface-type""",
          'defined-type': "interface:interface-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="trunk-list-src-interface", rest_name="trunk-list-src-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Source Interface'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interface:interface-type', is_config=True)""",
        })

    self.__trunk_list_src_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_list_src_interface(self):
    self.__trunk_list_src_interface = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="trunk-list-src-interface", rest_name="trunk-list-src-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Source Interface'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interface:interface-type', is_config=True)


  def _get_trunk_list_nbr_rbridge_id(self):
    """
    Getter method for trunk_list_nbr_rbridge_id, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_nbr_rbridge_id (uint32)

    YANG Description: RBbridge id of the neighboring
switch that connects to this
trunk member port.
    """
    return self.__trunk_list_nbr_rbridge_id
      
  def _set_trunk_list_nbr_rbridge_id(self, v, load=False):
    """
    Setter method for trunk_list_nbr_rbridge_id, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_nbr_rbridge_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_list_nbr_rbridge_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_list_nbr_rbridge_id() directly.

    YANG Description: RBbridge id of the neighboring
switch that connects to this
trunk member port.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-nbr-rbridge-id", rest_name="trunk-list-nbr-rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Neighbor rbridge-id. '}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_list_nbr_rbridge_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-nbr-rbridge-id", rest_name="trunk-list-nbr-rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Neighbor rbridge-id. '}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)""",
        })

    self.__trunk_list_nbr_rbridge_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_list_nbr_rbridge_id(self):
    self.__trunk_list_nbr_rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-nbr-rbridge-id", rest_name="trunk-list-nbr-rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Neighbor rbridge-id. '}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)


  def _get_trunk_list_nbr_port(self):
    """
    Getter method for trunk_list_nbr_port, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_nbr_port (uint32)

    YANG Description: Neighbor port index of the
trunk member.
    """
    return self.__trunk_list_nbr_port
      
  def _set_trunk_list_nbr_port(self, v, load=False):
    """
    Setter method for trunk_list_nbr_port, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_nbr_port (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_list_nbr_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_list_nbr_port() directly.

    YANG Description: Neighbor port index of the
trunk member.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-nbr-port", rest_name="trunk-list-nbr-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Neighbor port index'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_list_nbr_port must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-nbr-port", rest_name="trunk-list-nbr-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Neighbor port index'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)""",
        })

    self.__trunk_list_nbr_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_list_nbr_port(self):
    self.__trunk_list_nbr_port = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-nbr-port", rest_name="trunk-list-nbr-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Neighbor port index'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)


  def _get_trunk_list_nbr_interface_type(self):
    """
    Getter method for trunk_list_nbr_interface_type, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_nbr_interface_type (interfacetype-type)

    YANG Description: Interface type.
It can take the following
values:
   Te - for 10G Ethernet interface
   Fi - for Fibre Channel
   interface.
    """
    return self.__trunk_list_nbr_interface_type
      
  def _set_trunk_list_nbr_interface_type(self, v, load=False):
    """
    Setter method for trunk_list_nbr_interface_type, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_nbr_interface_type (interfacetype-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_list_nbr_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_list_nbr_interface_type() directly.

    YANG Description: Interface type.
It can take the following
values:
   Te - for 10G Ethernet interface
   Fi - for Fibre Channel
   interface.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'Te|Fi', 'length': [u'2']}), is_leaf=True, yang_name="trunk-list-nbr-interface-type", rest_name="trunk-list-nbr-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Interface type of neighbour port'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interfacetype-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_list_nbr_interface_type must be of a type compatible with interfacetype-type""",
          'defined-type': "brocade-fabric-service:interfacetype-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'Te|Fi', 'length': [u'2']}), is_leaf=True, yang_name="trunk-list-nbr-interface-type", rest_name="trunk-list-nbr-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Interface type of neighbour port'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interfacetype-type', is_config=True)""",
        })

    self.__trunk_list_nbr_interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_list_nbr_interface_type(self):
    self.__trunk_list_nbr_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'Te|Fi', 'length': [u'2']}), is_leaf=True, yang_name="trunk-list-nbr-interface-type", rest_name="trunk-list-nbr-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Interface type of neighbour port'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interfacetype-type', is_config=True)


  def _get_trunk_list_nbr_interface(self):
    """
    Getter method for trunk_list_nbr_interface, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_nbr_interface (interface:interface-type)

    YANG Description: Neighbour port interface info
It is in the format
rbridge-id/slot/port.
    """
    return self.__trunk_list_nbr_interface
      
  def _set_trunk_list_nbr_interface(self, v, load=False):
    """
    Setter method for trunk_list_nbr_interface, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_nbr_interface (interface:interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_list_nbr_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_list_nbr_interface() directly.

    YANG Description: Neighbour port interface info
It is in the format
rbridge-id/slot/port.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="trunk-list-nbr-interface", rest_name="trunk-list-nbr-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Neighbour Interface'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interface:interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_list_nbr_interface must be of a type compatible with interface:interface-type""",
          'defined-type': "interface:interface-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="trunk-list-nbr-interface", rest_name="trunk-list-nbr-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Neighbour Interface'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interface:interface-type', is_config=True)""",
        })

    self.__trunk_list_nbr_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_list_nbr_interface(self):
    self.__trunk_list_nbr_interface = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="trunk-list-nbr-interface", rest_name="trunk-list-nbr-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Neighbour Interface'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interface:interface-type', is_config=True)


  def _get_trunk_list_nbr_wwn(self):
    """
    Getter method for trunk_list_nbr_wwn, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_nbr_wwn (common-def:wwn-type)

    YANG Description: WWN of the neighboring
switch that connects to this
trunk member port.
    """
    return self.__trunk_list_nbr_wwn
      
  def _set_trunk_list_nbr_wwn(self, v, load=False):
    """
    Setter method for trunk_list_nbr_wwn, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_nbr_wwn (common-def:wwn-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_list_nbr_wwn is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_list_nbr_wwn() directly.

    YANG Description: WWN of the neighboring
switch that connects to this
trunk member port.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]'}), is_leaf=True, yang_name="trunk-list-nbr-wwn", rest_name="trunk-list-nbr-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'WWN of neighbor switch'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='common-def:wwn-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_list_nbr_wwn must be of a type compatible with common-def:wwn-type""",
          'defined-type': "common-def:wwn-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]'}), is_leaf=True, yang_name="trunk-list-nbr-wwn", rest_name="trunk-list-nbr-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'WWN of neighbor switch'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='common-def:wwn-type', is_config=True)""",
        })

    self.__trunk_list_nbr_wwn = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_list_nbr_wwn(self):
    self.__trunk_list_nbr_wwn = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F]'}), is_leaf=True, yang_name="trunk-list-nbr-wwn", rest_name="trunk-list-nbr-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'WWN of neighbor switch'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='common-def:wwn-type', is_config=True)


  def _get_trunk_list_is_primary(self):
    """
    Getter method for trunk_list_is_primary, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_is_primary (trunk-list-is-primary-type)

    YANG Description: This parameter is set to True
for trunk master.
    """
    return self.__trunk_list_is_primary
      
  def _set_trunk_list_is_primary(self, v, load=False):
    """
    Setter method for trunk_list_is_primary, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member/trunk_list_is_primary (trunk-list-is-primary-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_list_is_primary is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_list_is_primary() directly.

    YANG Description: This parameter is set to True
for trunk master.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'True|False|true|false', 'length': [u'0..5']}), is_leaf=True, yang_name="trunk-list-is-primary", rest_name="trunk-list-is-primary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'True represents trunk master'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='trunk-list-is-primary-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_list_is_primary must be of a type compatible with trunk-list-is-primary-type""",
          'defined-type': "brocade-fabric-service:trunk-list-is-primary-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'True|False|true|false', 'length': [u'0..5']}), is_leaf=True, yang_name="trunk-list-is-primary", rest_name="trunk-list-is-primary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'True represents trunk master'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='trunk-list-is-primary-type', is_config=True)""",
        })

    self.__trunk_list_is_primary = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_list_is_primary(self):
    self.__trunk_list_is_primary = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'True|False|true|false', 'length': [u'0..5']}), is_leaf=True, yang_name="trunk-list-is-primary", rest_name="trunk-list-is-primary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'True represents trunk master'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='trunk-list-is-primary-type', is_config=True)

  trunk_list_src_port = __builtin__.property(_get_trunk_list_src_port, _set_trunk_list_src_port)
  trunk_list_interface_type = __builtin__.property(_get_trunk_list_interface_type, _set_trunk_list_interface_type)
  trunk_list_src_interface = __builtin__.property(_get_trunk_list_src_interface, _set_trunk_list_src_interface)
  trunk_list_nbr_rbridge_id = __builtin__.property(_get_trunk_list_nbr_rbridge_id, _set_trunk_list_nbr_rbridge_id)
  trunk_list_nbr_port = __builtin__.property(_get_trunk_list_nbr_port, _set_trunk_list_nbr_port)
  trunk_list_nbr_interface_type = __builtin__.property(_get_trunk_list_nbr_interface_type, _set_trunk_list_nbr_interface_type)
  trunk_list_nbr_interface = __builtin__.property(_get_trunk_list_nbr_interface, _set_trunk_list_nbr_interface)
  trunk_list_nbr_wwn = __builtin__.property(_get_trunk_list_nbr_wwn, _set_trunk_list_nbr_wwn)
  trunk_list_is_primary = __builtin__.property(_get_trunk_list_is_primary, _set_trunk_list_is_primary)


  _pyangbind_elements = {'trunk_list_src_port': trunk_list_src_port, 'trunk_list_interface_type': trunk_list_interface_type, 'trunk_list_src_interface': trunk_list_src_interface, 'trunk_list_nbr_rbridge_id': trunk_list_nbr_rbridge_id, 'trunk_list_nbr_port': trunk_list_nbr_port, 'trunk_list_nbr_interface_type': trunk_list_nbr_interface_type, 'trunk_list_nbr_interface': trunk_list_nbr_interface, 'trunk_list_nbr_wwn': trunk_list_nbr_wwn, 'trunk_list_is_primary': trunk_list_is_primary, }


