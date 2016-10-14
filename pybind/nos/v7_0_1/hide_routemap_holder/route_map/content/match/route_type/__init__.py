
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class route_type(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ip-policy - based on the path /hide-routemap-holder/route-map/content/match/route-type. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Route type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__route_type_rmm',)

  _yang_name = 'route-type'

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
    self.__route_type_rmm = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type-1': {'value': 2}, u'internal': {'value': 1}, u'type-2': {'value': 3}},), is_leaf=True, yang_name="route-type-rmm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='match-route-type-t', is_config=True)

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
      return [u'hide-routemap-holder', u'route-map', u'content', u'match', u'route-type']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'route-map', u'match', u'route-type']

  def _get_route_type_rmm(self):
    """
    Getter method for route_type_rmm, mapped from YANG variable /hide_routemap_holder/route_map/content/match/route_type/route_type_rmm (match-route-type-t)
    """
    return self.__route_type_rmm
      
  def _set_route_type_rmm(self, v, load=False):
    """
    Setter method for route_type_rmm, mapped from YANG variable /hide_routemap_holder/route_map/content/match/route_type/route_type_rmm (match-route-type-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_type_rmm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_type_rmm() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type-1': {'value': 2}, u'internal': {'value': 1}, u'type-2': {'value': 3}},), is_leaf=True, yang_name="route-type-rmm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='match-route-type-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_type_rmm must be of a type compatible with match-route-type-t""",
          'defined-type': "brocade-ip-policy:match-route-type-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type-1': {'value': 2}, u'internal': {'value': 1}, u'type-2': {'value': 3}},), is_leaf=True, yang_name="route-type-rmm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='match-route-type-t', is_config=True)""",
        })

    self.__route_type_rmm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_type_rmm(self):
    self.__route_type_rmm = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type-1': {'value': 2}, u'internal': {'value': 1}, u'type-2': {'value': 3}},), is_leaf=True, yang_name="route-type-rmm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='match-route-type-t', is_config=True)

  route_type_rmm = __builtin__.property(_get_route_type_rmm, _set_route_type_rmm)


  _pyangbind_elements = {'route_type_rmm': route_type_rmm, }


