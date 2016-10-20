
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class qos_mpls(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-operational - based on the path /traffic-class-exp-state/qos-mpls. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__map_type','__map_name','__enabled_slots','__traffic_class','__drop_preced','__exp','__dscp','__exptrafficvalues',)

  _yang_name = 'qos-mpls'
  _rest_name = 'qos-mpls'

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
    self.__enabled_slots = YANGDynClass(base=unicode, is_leaf=True, yang_name="enabled-slots", rest_name="enabled-slots", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='string', is_config=False)
    self.__exptrafficvalues = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="exptrafficvalues", rest_name="exptrafficvalues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)
    self.__traffic_class = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)
    self.__drop_preced = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="drop-preced", rest_name="drop-preced", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)
    self.__dscp = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="dscp", rest_name="dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)
    self.__exp = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="exp", rest_name="exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)
    self.__map_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="map-name", rest_name="map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='string', is_config=False)
    self.__map_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="map-type", rest_name="map-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='string', is_config=False)

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
      return [u'traffic-class-exp-state', u'qos-mpls']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'traffic-class-exp-state', u'qos-mpls']

  def _get_map_type(self):
    """
    Getter method for map_type, mapped from YANG variable /traffic_class_exp_state/qos_mpls/map_type (string)

    YANG Description: map_type
    """
    return self.__map_type
      
  def _set_map_type(self, v, load=False):
    """
    Setter method for map_type, mapped from YANG variable /traffic_class_exp_state/qos_mpls/map_type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_type() directly.

    YANG Description: map_type
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="map-type", rest_name="map-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="map-type", rest_name="map-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='string', is_config=False)""",
        })

    self.__map_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_type(self):
    self.__map_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="map-type", rest_name="map-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='string', is_config=False)


  def _get_map_name(self):
    """
    Getter method for map_name, mapped from YANG variable /traffic_class_exp_state/qos_mpls/map_name (string)

    YANG Description: map_name
    """
    return self.__map_name
      
  def _set_map_name(self, v, load=False):
    """
    Setter method for map_name, mapped from YANG variable /traffic_class_exp_state/qos_mpls/map_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_name() directly.

    YANG Description: map_name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="map-name", rest_name="map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="map-name", rest_name="map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='string', is_config=False)""",
        })

    self.__map_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_name(self):
    self.__map_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="map-name", rest_name="map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='string', is_config=False)


  def _get_enabled_slots(self):
    """
    Getter method for enabled_slots, mapped from YANG variable /traffic_class_exp_state/qos_mpls/enabled_slots (string)

    YANG Description: enabled_slots
    """
    return self.__enabled_slots
      
  def _set_enabled_slots(self, v, load=False):
    """
    Setter method for enabled_slots, mapped from YANG variable /traffic_class_exp_state/qos_mpls/enabled_slots (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled_slots is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled_slots() directly.

    YANG Description: enabled_slots
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="enabled-slots", rest_name="enabled-slots", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled_slots must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="enabled-slots", rest_name="enabled-slots", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='string', is_config=False)""",
        })

    self.__enabled_slots = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled_slots(self):
    self.__enabled_slots = YANGDynClass(base=unicode, is_leaf=True, yang_name="enabled-slots", rest_name="enabled-slots", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='string', is_config=False)


  def _get_traffic_class(self):
    """
    Getter method for traffic_class, mapped from YANG variable /traffic_class_exp_state/qos_mpls/traffic_class (uint32)

    YANG Description: traffic-class
    """
    return self.__traffic_class
      
  def _set_traffic_class(self, v, load=False):
    """
    Setter method for traffic_class, mapped from YANG variable /traffic_class_exp_state/qos_mpls/traffic_class (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_traffic_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_traffic_class() directly.

    YANG Description: traffic-class
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """traffic_class must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)""",
        })

    self.__traffic_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_traffic_class(self):
    self.__traffic_class = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)


  def _get_drop_preced(self):
    """
    Getter method for drop_preced, mapped from YANG variable /traffic_class_exp_state/qos_mpls/drop_preced (uint32)

    YANG Description: drop-preced
    """
    return self.__drop_preced
      
  def _set_drop_preced(self, v, load=False):
    """
    Setter method for drop_preced, mapped from YANG variable /traffic_class_exp_state/qos_mpls/drop_preced (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_drop_preced is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_drop_preced() directly.

    YANG Description: drop-preced
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="drop-preced", rest_name="drop-preced", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """drop_preced must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="drop-preced", rest_name="drop-preced", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)""",
        })

    self.__drop_preced = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_drop_preced(self):
    self.__drop_preced = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="drop-preced", rest_name="drop-preced", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)


  def _get_exp(self):
    """
    Getter method for exp, mapped from YANG variable /traffic_class_exp_state/qos_mpls/exp (uint32)

    YANG Description: exp-val
    """
    return self.__exp
      
  def _set_exp(self, v, load=False):
    """
    Setter method for exp, mapped from YANG variable /traffic_class_exp_state/qos_mpls/exp (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_exp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_exp() directly.

    YANG Description: exp-val
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="exp", rest_name="exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """exp must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="exp", rest_name="exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)""",
        })

    self.__exp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_exp(self):
    self.__exp = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="exp", rest_name="exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)


  def _get_dscp(self):
    """
    Getter method for dscp, mapped from YANG variable /traffic_class_exp_state/qos_mpls/dscp (uint32)

    YANG Description: dscp-val
    """
    return self.__dscp
      
  def _set_dscp(self, v, load=False):
    """
    Setter method for dscp, mapped from YANG variable /traffic_class_exp_state/qos_mpls/dscp (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dscp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dscp() directly.

    YANG Description: dscp-val
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="dscp", rest_name="dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dscp must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="dscp", rest_name="dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)""",
        })

    self.__dscp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dscp(self):
    self.__dscp = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="dscp", rest_name="dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)


  def _get_exptrafficvalues(self):
    """
    Getter method for exptrafficvalues, mapped from YANG variable /traffic_class_exp_state/qos_mpls/exptrafficvalues (uint32)

    YANG Description: exptrafficvalues
    """
    return self.__exptrafficvalues
      
  def _set_exptrafficvalues(self, v, load=False):
    """
    Setter method for exptrafficvalues, mapped from YANG variable /traffic_class_exp_state/qos_mpls/exptrafficvalues (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_exptrafficvalues is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_exptrafficvalues() directly.

    YANG Description: exptrafficvalues
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="exptrafficvalues", rest_name="exptrafficvalues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """exptrafficvalues must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="exptrafficvalues", rest_name="exptrafficvalues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)""",
        })

    self.__exptrafficvalues = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_exptrafficvalues(self):
    self.__exptrafficvalues = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="exptrafficvalues", rest_name="exptrafficvalues", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)

  map_type = __builtin__.property(_get_map_type)
  map_name = __builtin__.property(_get_map_name)
  enabled_slots = __builtin__.property(_get_enabled_slots)
  traffic_class = __builtin__.property(_get_traffic_class)
  drop_preced = __builtin__.property(_get_drop_preced)
  exp = __builtin__.property(_get_exp)
  dscp = __builtin__.property(_get_dscp)
  exptrafficvalues = __builtin__.property(_get_exptrafficvalues)


  _pyangbind_elements = {'map_type': map_type, 'map_name': map_name, 'enabled_slots': enabled_slots, 'traffic_class': traffic_class, 'drop_preced': drop_preced, 'exp': exp, 'dscp': dscp, 'exptrafficvalues': exptrafficvalues, }


