
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class cos_traffic_class(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos - based on the path /qos/map/cos-traffic-class. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__name','__cos0','__cos1','__cos2','__cos3','__cos4','__cos5','__cos6','__cos7',)

  _yang_name = 'cos-traffic-class'

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
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)
    self.__cos7 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos7", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__cos6 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__cos5 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos5", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__cos4 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__cos3 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__cos2 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__cos1 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__cos0 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)

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
      return [u'qos', u'map', u'cos-traffic-class']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'qos', u'map', u'cos-traffic-class']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /qos/map/cos_traffic_class/name (map-name-type)
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /qos/map/cos_traffic_class/name (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with map-name-type""",
          'defined-type': "brocade-qos:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)


  def _get_cos0(self):
    """
    Getter method for cos0, mapped from YANG variable /qos/map/cos_traffic_class/cos0 (int32)
    """
    return self.__cos0
      
  def _set_cos0(self, v, load=False):
    """
    Setter method for cos0, mapped from YANG variable /qos/map/cos_traffic_class/cos0 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos0 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos0() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos0 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__cos0 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos0(self):
    self.__cos0 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_cos1(self):
    """
    Getter method for cos1, mapped from YANG variable /qos/map/cos_traffic_class/cos1 (int32)
    """
    return self.__cos1
      
  def _set_cos1(self, v, load=False):
    """
    Setter method for cos1, mapped from YANG variable /qos/map/cos_traffic_class/cos1 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos1() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos1 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__cos1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos1(self):
    self.__cos1 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_cos2(self):
    """
    Getter method for cos2, mapped from YANG variable /qos/map/cos_traffic_class/cos2 (int32)
    """
    return self.__cos2
      
  def _set_cos2(self, v, load=False):
    """
    Setter method for cos2, mapped from YANG variable /qos/map/cos_traffic_class/cos2 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos2() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos2 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__cos2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos2(self):
    self.__cos2 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_cos3(self):
    """
    Getter method for cos3, mapped from YANG variable /qos/map/cos_traffic_class/cos3 (int32)
    """
    return self.__cos3
      
  def _set_cos3(self, v, load=False):
    """
    Setter method for cos3, mapped from YANG variable /qos/map/cos_traffic_class/cos3 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos3 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos3() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos3 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__cos3 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos3(self):
    self.__cos3 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_cos4(self):
    """
    Getter method for cos4, mapped from YANG variable /qos/map/cos_traffic_class/cos4 (int32)
    """
    return self.__cos4
      
  def _set_cos4(self, v, load=False):
    """
    Setter method for cos4, mapped from YANG variable /qos/map/cos_traffic_class/cos4 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos4 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos4() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos4 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__cos4 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos4(self):
    self.__cos4 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_cos5(self):
    """
    Getter method for cos5, mapped from YANG variable /qos/map/cos_traffic_class/cos5 (int32)
    """
    return self.__cos5
      
  def _set_cos5(self, v, load=False):
    """
    Setter method for cos5, mapped from YANG variable /qos/map/cos_traffic_class/cos5 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos5 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos5() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos5", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos5 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos5", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__cos5 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos5(self):
    self.__cos5 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos5", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_cos6(self):
    """
    Getter method for cos6, mapped from YANG variable /qos/map/cos_traffic_class/cos6 (int32)
    """
    return self.__cos6
      
  def _set_cos6(self, v, load=False):
    """
    Setter method for cos6, mapped from YANG variable /qos/map/cos_traffic_class/cos6 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos6() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos6 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__cos6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos6(self):
    self.__cos6 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_cos7(self):
    """
    Getter method for cos7, mapped from YANG variable /qos/map/cos_traffic_class/cos7 (int32)
    """
    return self.__cos7
      
  def _set_cos7(self, v, load=False):
    """
    Setter method for cos7, mapped from YANG variable /qos/map/cos_traffic_class/cos7 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos7 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos7() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos7", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos7 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos7", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__cos7 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos7(self):
    self.__cos7 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="cos7", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  cos0 = __builtin__.property(_get_cos0, _set_cos0)
  cos1 = __builtin__.property(_get_cos1, _set_cos1)
  cos2 = __builtin__.property(_get_cos2, _set_cos2)
  cos3 = __builtin__.property(_get_cos3, _set_cos3)
  cos4 = __builtin__.property(_get_cos4, _set_cos4)
  cos5 = __builtin__.property(_get_cos5, _set_cos5)
  cos6 = __builtin__.property(_get_cos6, _set_cos6)
  cos7 = __builtin__.property(_get_cos7, _set_cos7)


  _pyangbind_elements = {'name': name, 'cos0': cos0, 'cos1': cos1, 'cos2': cos2, 'cos3': cos3, 'cos4': cos4, 'cos5': cos5, 'cos6': cos6, 'cos7': cos7, }


