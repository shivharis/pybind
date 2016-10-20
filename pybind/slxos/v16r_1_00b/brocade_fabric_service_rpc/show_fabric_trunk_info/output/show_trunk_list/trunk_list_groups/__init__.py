
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import trunk_list_member
class trunk_list_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fabric-service - based on the path /brocade_fabric_service_rpc/show-fabric-trunk-info/output/show-trunk-list/trunk-list-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__trunk_list_group','__trunk_list_member',)

  _yang_name = 'trunk-list-groups'
  _rest_name = 'trunk-list-groups'

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
    self.__trunk_list_member = YANGDynClass(base=YANGListType(False,trunk_list_member.trunk_list_member, yang_name="trunk-list-member", rest_name="trunk-list-member", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="trunk-list-member", rest_name="trunk-list-member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)
    self.__trunk_list_group = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-group", rest_name="trunk-list-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Trunk group the interface\nbelongs to'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)

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
      return [u'brocade_fabric_service_rpc', u'show-fabric-trunk-info', u'output', u'show-trunk-list', u'trunk-list-groups']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-fabric-trunk-info', u'output', u'show-trunk-list', u'trunk-list-groups']

  def _get_trunk_list_group(self):
    """
    Getter method for trunk_list_group, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_group (uint32)

    YANG Description: Provides the trunk group number
the interface belongs to.
Trunk members of a trunk group
have the same group number.
    """
    return self.__trunk_list_group
      
  def _set_trunk_list_group(self, v, load=False):
    """
    Setter method for trunk_list_group, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_group (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_list_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_list_group() directly.

    YANG Description: Provides the trunk group number
the interface belongs to.
Trunk members of a trunk group
have the same group number.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-group", rest_name="trunk-list-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Trunk group the interface\nbelongs to'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_list_group must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-group", rest_name="trunk-list-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Trunk group the interface\nbelongs to'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)""",
        })

    self.__trunk_list_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_list_group(self):
    self.__trunk_list_group = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="trunk-list-group", rest_name="trunk-list-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Trunk group the interface\nbelongs to'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)


  def _get_trunk_list_member(self):
    """
    Getter method for trunk_list_member, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member (list)
    """
    return self.__trunk_list_member
      
  def _set_trunk_list_member(self, v, load=False):
    """
    Setter method for trunk_list_member, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info/output/show_trunk_list/trunk_list_groups/trunk_list_member (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_list_member is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_list_member() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType(False,trunk_list_member.trunk_list_member, yang_name="trunk-list-member", rest_name="trunk-list-member", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="trunk-list-member", rest_name="trunk-list-member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_list_member must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,trunk_list_member.trunk_list_member, yang_name="trunk-list-member", rest_name="trunk-list-member", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="trunk-list-member", rest_name="trunk-list-member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)""",
        })

    self.__trunk_list_member = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_list_member(self):
    self.__trunk_list_member = YANGDynClass(base=YANGListType(False,trunk_list_member.trunk_list_member, yang_name="trunk-list-member", rest_name="trunk-list-member", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="trunk-list-member", rest_name="trunk-list-member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)

  trunk_list_group = __builtin__.property(_get_trunk_list_group, _set_trunk_list_group)
  trunk_list_member = __builtin__.property(_get_trunk_list_member, _set_trunk_list_member)


  _pyangbind_elements = {'trunk_list_group': trunk_list_group, 'trunk_list_member': trunk_list_member, }


