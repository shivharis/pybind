
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import route_entry_list
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-route/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__number_route_entry','__route_entry_list',)

  _yang_name = 'output'
  _rest_name = 'output'

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
    self.__route_entry_list = YANGDynClass(base=YANGListType(False,route_entry_list.route_entry_list, yang_name="route-entry-list", rest_name="route-entry-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="route-entry-list", rest_name="route-entry-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    self.__number_route_entry = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="number-route-entry", rest_name="number-route-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-route', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-route', u'output']

  def _get_number_route_entry(self):
    """
    Getter method for number_route_entry, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/number_route_entry (uint32)
    """
    return self.__number_route_entry
      
  def _set_number_route_entry(self, v, load=False):
    """
    Setter method for number_route_entry, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/number_route_entry (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_number_route_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_number_route_entry() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="number-route-entry", rest_name="number-route-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """number_route_entry must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="number-route-entry", rest_name="number-route-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__number_route_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_number_route_entry(self):
    self.__number_route_entry = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="number-route-entry", rest_name="number-route-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_route_entry_list(self):
    """
    Getter method for route_entry_list, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list (list)
    """
    return self.__route_entry_list
      
  def _set_route_entry_list(self, v, load=False):
    """
    Setter method for route_entry_list, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_entry_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_entry_list() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType(False,route_entry_list.route_entry_list, yang_name="route-entry-list", rest_name="route-entry-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="route-entry-list", rest_name="route-entry-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_entry_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,route_entry_list.route_entry_list, yang_name="route-entry-list", rest_name="route-entry-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="route-entry-list", rest_name="route-entry-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)""",
        })

    self.__route_entry_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_entry_list(self):
    self.__route_entry_list = YANGDynClass(base=YANGListType(False,route_entry_list.route_entry_list, yang_name="route-entry-list", rest_name="route-entry-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="route-entry-list", rest_name="route-entry-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)

  number_route_entry = __builtin__.property(_get_number_route_entry, _set_number_route_entry)
  route_entry_list = __builtin__.property(_get_route_entry_list, _set_route_entry_list)


  _pyangbind_elements = {'number_route_entry': number_route_entry, 'route_entry_list': route_entry_list, }


