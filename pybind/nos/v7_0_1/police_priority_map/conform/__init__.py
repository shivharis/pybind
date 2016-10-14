
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class conform(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-policer - based on the path /police-priority-map/conform. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__map_pri0_conform','__map_pri1_conform','__map_pri2_conform','__map_pri3_conform','__map_pri4_conform','__map_pri5_conform','__map_pri6_conform','__map_pri7_conform',)

  _yang_name = 'conform'

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
    self.__map_pri0_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri0-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 0', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    self.__map_pri7_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri7-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 7', u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    self.__map_pri4_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri4-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 4', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    self.__map_pri1_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri1-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 1', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    self.__map_pri5_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri5-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 5', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    self.__map_pri3_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri3-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 3', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    self.__map_pri2_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri2-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 2', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    self.__map_pri6_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri6-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 6', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)

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
      return [u'police-priority-map', u'conform']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'police-priority-map', u'conform']

  def _get_map_pri0_conform(self):
    """
    Getter method for map_pri0_conform, mapped from YANG variable /police_priority_map/conform/map_pri0_conform (priority-value)
    """
    return self.__map_pri0_conform
      
  def _set_map_pri0_conform(self, v, load=False):
    """
    Setter method for map_pri0_conform, mapped from YANG variable /police_priority_map/conform/map_pri0_conform (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri0_conform is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri0_conform() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri0-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 0', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri0_conform must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri0-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 0', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri0_conform = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri0_conform(self):
    self.__map_pri0_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri0-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 0', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)


  def _get_map_pri1_conform(self):
    """
    Getter method for map_pri1_conform, mapped from YANG variable /police_priority_map/conform/map_pri1_conform (priority-value)
    """
    return self.__map_pri1_conform
      
  def _set_map_pri1_conform(self, v, load=False):
    """
    Setter method for map_pri1_conform, mapped from YANG variable /police_priority_map/conform/map_pri1_conform (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri1_conform is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri1_conform() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri1-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 1', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri1_conform must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri1-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 1', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri1_conform = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri1_conform(self):
    self.__map_pri1_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri1-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 1', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)


  def _get_map_pri2_conform(self):
    """
    Getter method for map_pri2_conform, mapped from YANG variable /police_priority_map/conform/map_pri2_conform (priority-value)
    """
    return self.__map_pri2_conform
      
  def _set_map_pri2_conform(self, v, load=False):
    """
    Setter method for map_pri2_conform, mapped from YANG variable /police_priority_map/conform/map_pri2_conform (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri2_conform is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri2_conform() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri2-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 2', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri2_conform must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri2-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 2', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri2_conform = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri2_conform(self):
    self.__map_pri2_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri2-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 2', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)


  def _get_map_pri3_conform(self):
    """
    Getter method for map_pri3_conform, mapped from YANG variable /police_priority_map/conform/map_pri3_conform (priority-value)
    """
    return self.__map_pri3_conform
      
  def _set_map_pri3_conform(self, v, load=False):
    """
    Setter method for map_pri3_conform, mapped from YANG variable /police_priority_map/conform/map_pri3_conform (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri3_conform is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri3_conform() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri3-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 3', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri3_conform must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri3-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 3', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri3_conform = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri3_conform(self):
    self.__map_pri3_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri3-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 3', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)


  def _get_map_pri4_conform(self):
    """
    Getter method for map_pri4_conform, mapped from YANG variable /police_priority_map/conform/map_pri4_conform (priority-value)
    """
    return self.__map_pri4_conform
      
  def _set_map_pri4_conform(self, v, load=False):
    """
    Setter method for map_pri4_conform, mapped from YANG variable /police_priority_map/conform/map_pri4_conform (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri4_conform is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri4_conform() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri4-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 4', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri4_conform must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri4-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 4', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri4_conform = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri4_conform(self):
    self.__map_pri4_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri4-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 4', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)


  def _get_map_pri5_conform(self):
    """
    Getter method for map_pri5_conform, mapped from YANG variable /police_priority_map/conform/map_pri5_conform (priority-value)
    """
    return self.__map_pri5_conform
      
  def _set_map_pri5_conform(self, v, load=False):
    """
    Setter method for map_pri5_conform, mapped from YANG variable /police_priority_map/conform/map_pri5_conform (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri5_conform is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri5_conform() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri5-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 5', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri5_conform must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri5-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 5', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri5_conform = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri5_conform(self):
    self.__map_pri5_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri5-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 5', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)


  def _get_map_pri6_conform(self):
    """
    Getter method for map_pri6_conform, mapped from YANG variable /police_priority_map/conform/map_pri6_conform (priority-value)
    """
    return self.__map_pri6_conform
      
  def _set_map_pri6_conform(self, v, load=False):
    """
    Setter method for map_pri6_conform, mapped from YANG variable /police_priority_map/conform/map_pri6_conform (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri6_conform is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri6_conform() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri6-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 6', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri6_conform must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri6-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 6', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri6_conform = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri6_conform(self):
    self.__map_pri6_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri6-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 6', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)


  def _get_map_pri7_conform(self):
    """
    Getter method for map_pri7_conform, mapped from YANG variable /police_priority_map/conform/map_pri7_conform (priority-value)
    """
    return self.__map_pri7_conform
      
  def _set_map_pri7_conform(self, v, load=False):
    """
    Setter method for map_pri7_conform, mapped from YANG variable /police_priority_map/conform/map_pri7_conform (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri7_conform is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri7_conform() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri7-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 7', u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri7_conform must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri7-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 7', u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri7_conform = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri7_conform(self):
    self.__map_pri7_conform = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri7-conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 7', u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)

  map_pri0_conform = __builtin__.property(_get_map_pri0_conform, _set_map_pri0_conform)
  map_pri1_conform = __builtin__.property(_get_map_pri1_conform, _set_map_pri1_conform)
  map_pri2_conform = __builtin__.property(_get_map_pri2_conform, _set_map_pri2_conform)
  map_pri3_conform = __builtin__.property(_get_map_pri3_conform, _set_map_pri3_conform)
  map_pri4_conform = __builtin__.property(_get_map_pri4_conform, _set_map_pri4_conform)
  map_pri5_conform = __builtin__.property(_get_map_pri5_conform, _set_map_pri5_conform)
  map_pri6_conform = __builtin__.property(_get_map_pri6_conform, _set_map_pri6_conform)
  map_pri7_conform = __builtin__.property(_get_map_pri7_conform, _set_map_pri7_conform)


  _pyangbind_elements = {'map_pri0_conform': map_pri0_conform, 'map_pri1_conform': map_pri1_conform, 'map_pri2_conform': map_pri2_conform, 'map_pri3_conform': map_pri3_conform, 'map_pri4_conform': map_pri4_conform, 'map_pri5_conform': map_pri5_conform, 'map_pri6_conform': map_pri6_conform, 'map_pri7_conform': map_pri7_conform, }


