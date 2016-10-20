
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class config_include_any(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/lsp/instances/config-include-any. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__admin_group_id','__admin_group_name',)

  _yang_name = 'config-include-any'
  _rest_name = 'config-include-any'

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
    self.__admin_group_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="admin-group-id", rest_name="admin-group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__admin_group_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="admin-group-name", rest_name="admin-group-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)

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
      return [u'mpls-state', u'lsp', u'instances', u'config-include-any']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'lsp', u'instances', u'config-include-any']

  def _get_admin_group_id(self):
    """
    Getter method for admin_group_id, mapped from YANG variable /mpls_state/lsp/instances/config_include_any/admin_group_id (uint32)

    YANG Description: lsp_admin_group_id
    """
    return self.__admin_group_id
      
  def _set_admin_group_id(self, v, load=False):
    """
    Setter method for admin_group_id, mapped from YANG variable /mpls_state/lsp/instances/config_include_any/admin_group_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_admin_group_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_admin_group_id() directly.

    YANG Description: lsp_admin_group_id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="admin-group-id", rest_name="admin-group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """admin_group_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="admin-group-id", rest_name="admin-group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__admin_group_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_admin_group_id(self):
    self.__admin_group_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="admin-group-id", rest_name="admin-group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_admin_group_name(self):
    """
    Getter method for admin_group_name, mapped from YANG variable /mpls_state/lsp/instances/config_include_any/admin_group_name (string)

    YANG Description: lsp_admin_group_name
    """
    return self.__admin_group_name
      
  def _set_admin_group_name(self, v, load=False):
    """
    Setter method for admin_group_name, mapped from YANG variable /mpls_state/lsp/instances/config_include_any/admin_group_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_admin_group_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_admin_group_name() directly.

    YANG Description: lsp_admin_group_name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="admin-group-name", rest_name="admin-group-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """admin_group_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="admin-group-name", rest_name="admin-group-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__admin_group_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_admin_group_name(self):
    self.__admin_group_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="admin-group-name", rest_name="admin-group-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)

  admin_group_id = __builtin__.property(_get_admin_group_id)
  admin_group_name = __builtin__.property(_get_admin_group_name)


  _pyangbind_elements = {'admin_group_id': admin_group_id, 'admin_group_name': admin_group_name, }


