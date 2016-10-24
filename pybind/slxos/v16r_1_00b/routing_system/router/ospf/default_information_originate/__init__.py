
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class default_information_originate(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/ospf/default-information-originate. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__always','__def_orig_metric','__def_orig_metric_type','__def_orig_route_map',)

  _yang_name = 'default-information-originate'
  _rest_name = 'default-information-originate'

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
    self.__always = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="always", rest_name="always", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Always advertise default route'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    self.__def_orig_route_map = YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="def-orig-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map reference', u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='string', is_config=True)
    self.__def_orig_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="def-orig-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF metric for default route', u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    self.__def_orig_metric_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type1': {'value': 1}, u'type2': {'value': 2}},), is_leaf=True, yang_name="def-orig-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF metric type for default route', u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='metric-type', is_config=True)

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
      return [u'routing-system', u'router', u'ospf', u'default-information-originate']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'ospf', u'default-information-originate']

  def _get_always(self):
    """
    Getter method for always, mapped from YANG variable /routing_system/router/ospf/default_information_originate/always (empty)
    """
    return self.__always
      
  def _set_always(self, v, load=False):
    """
    Setter method for always, mapped from YANG variable /routing_system/router/ospf/default_information_originate/always (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_always is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_always() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="always", rest_name="always", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Always advertise default route'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """always must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="always", rest_name="always", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Always advertise default route'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__always = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_always(self):
    self.__always = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="always", rest_name="always", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Always advertise default route'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)


  def _get_def_orig_metric(self):
    """
    Getter method for def_orig_metric, mapped from YANG variable /routing_system/router/ospf/default_information_originate/def_orig_metric (uint32)
    """
    return self.__def_orig_metric
      
  def _set_def_orig_metric(self, v, load=False):
    """
    Setter method for def_orig_metric, mapped from YANG variable /routing_system/router/ospf/default_information_originate/def_orig_metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_def_orig_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_def_orig_metric() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="def-orig-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF metric for default route', u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """def_orig_metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="def-orig-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF metric for default route', u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)""",
        })

    self.__def_orig_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_def_orig_metric(self):
    self.__def_orig_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="def-orig-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF metric for default route', u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)


  def _get_def_orig_metric_type(self):
    """
    Getter method for def_orig_metric_type, mapped from YANG variable /routing_system/router/ospf/default_information_originate/def_orig_metric_type (metric-type)
    """
    return self.__def_orig_metric_type
      
  def _set_def_orig_metric_type(self, v, load=False):
    """
    Setter method for def_orig_metric_type, mapped from YANG variable /routing_system/router/ospf/default_information_originate/def_orig_metric_type (metric-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_def_orig_metric_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_def_orig_metric_type() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type1': {'value': 1}, u'type2': {'value': 2}},), is_leaf=True, yang_name="def-orig-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF metric type for default route', u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='metric-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """def_orig_metric_type must be of a type compatible with metric-type""",
          'defined-type': "brocade-ospf:metric-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type1': {'value': 1}, u'type2': {'value': 2}},), is_leaf=True, yang_name="def-orig-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF metric type for default route', u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='metric-type', is_config=True)""",
        })

    self.__def_orig_metric_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_def_orig_metric_type(self):
    self.__def_orig_metric_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type1': {'value': 1}, u'type2': {'value': 2}},), is_leaf=True, yang_name="def-orig-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF metric type for default route', u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='metric-type', is_config=True)


  def _get_def_orig_route_map(self):
    """
    Getter method for def_orig_route_map, mapped from YANG variable /routing_system/router/ospf/default_information_originate/def_orig_route_map (string)
    """
    return self.__def_orig_route_map
      
  def _set_def_orig_route_map(self, v, load=False):
    """
    Setter method for def_orig_route_map, mapped from YANG variable /routing_system/router/ospf/default_information_originate/def_orig_route_map (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_def_orig_route_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_def_orig_route_map() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, default=unicode(""), is_leaf=True, yang_name="def-orig-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map reference', u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """def_orig_route_map must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="def-orig-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map reference', u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='string', is_config=True)""",
        })

    self.__def_orig_route_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_def_orig_route_map(self):
    self.__def_orig_route_map = YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="def-orig-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map reference', u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='string', is_config=True)

  always = __builtin__.property(_get_always, _set_always)
  def_orig_metric = __builtin__.property(_get_def_orig_metric, _set_def_orig_metric)
  def_orig_metric_type = __builtin__.property(_get_def_orig_metric_type, _set_def_orig_metric_type)
  def_orig_route_map = __builtin__.property(_get_def_orig_route_map, _set_def_orig_route_map)


  _pyangbind_elements = {'always': always, 'def_orig_metric': def_orig_metric, 'def_orig_metric_type': def_orig_metric_type, 'def_orig_route_map': def_orig_route_map, }

