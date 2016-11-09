
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import map_
import map_apply
class qos_mpls(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mpls - based on the path /qos-mpls. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__map_','__map_apply',)

  _yang_name = 'qos-mpls'
  _rest_name = 'qos-mpls'

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
    self.__map_ = YANGDynClass(base=map_.map_, is_container='container', yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MPLS QoS map'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='container', is_config=True)
    self.__map_apply = YANGDynClass(base=map_apply.map_apply, is_container='container', yang_name="map-apply", rest_name="map-apply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure apply map', u'callpoint': u'ApplyQosMplsCallpoint', u'sort-priority': u'47'}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='container', is_config=True)

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
      return [u'qos-mpls']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos-mpls']

  def _get_map_(self):
    """
    Getter method for map_, mapped from YANG variable /qos_mpls/map (container)
    """
    return self.__map_
      
  def _set_map_(self, v, load=False):
    """
    Setter method for map_, mapped from YANG variable /qos_mpls/map (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_() directly.
    """
    try:
      t = YANGDynClass(v,base=map_.map_, is_container='container', yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MPLS QoS map'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=map_.map_, is_container='container', yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MPLS QoS map'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='container', is_config=True)""",
        })

    self.__map_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_(self):
    self.__map_ = YANGDynClass(base=map_.map_, is_container='container', yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MPLS QoS map'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='container', is_config=True)


  def _get_map_apply(self):
    """
    Getter method for map_apply, mapped from YANG variable /qos_mpls/map_apply (container)
    """
    return self.__map_apply
      
  def _set_map_apply(self, v, load=False):
    """
    Setter method for map_apply, mapped from YANG variable /qos_mpls/map_apply (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_apply is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_apply() directly.
    """
    try:
      t = YANGDynClass(v,base=map_apply.map_apply, is_container='container', yang_name="map-apply", rest_name="map-apply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure apply map', u'callpoint': u'ApplyQosMplsCallpoint', u'sort-priority': u'47'}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_apply must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=map_apply.map_apply, is_container='container', yang_name="map-apply", rest_name="map-apply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure apply map', u'callpoint': u'ApplyQosMplsCallpoint', u'sort-priority': u'47'}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='container', is_config=True)""",
        })

    self.__map_apply = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_apply(self):
    self.__map_apply = YANGDynClass(base=map_apply.map_apply, is_container='container', yang_name="map-apply", rest_name="map-apply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure apply map', u'callpoint': u'ApplyQosMplsCallpoint', u'sort-priority': u'47'}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='container', is_config=True)

  map_ = __builtin__.property(_get_map_, _set_map_)
  map_apply = __builtin__.property(_get_map_apply, _set_map_apply)


  _pyangbind_elements = {'map_': map_, 'map_apply': map_apply, }

