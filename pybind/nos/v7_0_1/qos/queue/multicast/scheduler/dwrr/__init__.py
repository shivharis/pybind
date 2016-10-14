
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class dwrr(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos - based on the path /qos/queue/multicast/scheduler/dwrr. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__dwrr_traffic_class0','__dwrr_traffic_class1','__dwrr_traffic_class2','__dwrr_traffic_class3','__dwrr_traffic_class4','__dwrr_traffic_class5','__dwrr_traffic_class6','__dwrr_traffic_class7',)

  _yang_name = 'dwrr'

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
    self.__dwrr_traffic_class3 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__dwrr_traffic_class2 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__dwrr_traffic_class1 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__dwrr_traffic_class0 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__dwrr_traffic_class7 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class7", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__dwrr_traffic_class6 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__dwrr_traffic_class5 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class5", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__dwrr_traffic_class4 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)

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
      return [u'qos', u'queue', u'multicast', u'scheduler', u'dwrr']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'qos', u'queue', u'multicast', u'scheduler', u'dwrr']

  def _get_dwrr_traffic_class0(self):
    """
    Getter method for dwrr_traffic_class0, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class0 (int32)
    """
    return self.__dwrr_traffic_class0
      
  def _set_dwrr_traffic_class0(self, v, load=False):
    """
    Setter method for dwrr_traffic_class0, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class0 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dwrr_traffic_class0 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dwrr_traffic_class0() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dwrr_traffic_class0 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__dwrr_traffic_class0 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dwrr_traffic_class0(self):
    self.__dwrr_traffic_class0 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_dwrr_traffic_class1(self):
    """
    Getter method for dwrr_traffic_class1, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class1 (int32)
    """
    return self.__dwrr_traffic_class1
      
  def _set_dwrr_traffic_class1(self, v, load=False):
    """
    Setter method for dwrr_traffic_class1, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class1 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dwrr_traffic_class1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dwrr_traffic_class1() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dwrr_traffic_class1 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__dwrr_traffic_class1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dwrr_traffic_class1(self):
    self.__dwrr_traffic_class1 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_dwrr_traffic_class2(self):
    """
    Getter method for dwrr_traffic_class2, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class2 (int32)
    """
    return self.__dwrr_traffic_class2
      
  def _set_dwrr_traffic_class2(self, v, load=False):
    """
    Setter method for dwrr_traffic_class2, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class2 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dwrr_traffic_class2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dwrr_traffic_class2() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dwrr_traffic_class2 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__dwrr_traffic_class2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dwrr_traffic_class2(self):
    self.__dwrr_traffic_class2 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_dwrr_traffic_class3(self):
    """
    Getter method for dwrr_traffic_class3, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class3 (int32)
    """
    return self.__dwrr_traffic_class3
      
  def _set_dwrr_traffic_class3(self, v, load=False):
    """
    Setter method for dwrr_traffic_class3, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class3 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dwrr_traffic_class3 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dwrr_traffic_class3() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dwrr_traffic_class3 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__dwrr_traffic_class3 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dwrr_traffic_class3(self):
    self.__dwrr_traffic_class3 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_dwrr_traffic_class4(self):
    """
    Getter method for dwrr_traffic_class4, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class4 (int32)
    """
    return self.__dwrr_traffic_class4
      
  def _set_dwrr_traffic_class4(self, v, load=False):
    """
    Setter method for dwrr_traffic_class4, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class4 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dwrr_traffic_class4 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dwrr_traffic_class4() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dwrr_traffic_class4 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__dwrr_traffic_class4 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dwrr_traffic_class4(self):
    self.__dwrr_traffic_class4 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_dwrr_traffic_class5(self):
    """
    Getter method for dwrr_traffic_class5, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class5 (int32)
    """
    return self.__dwrr_traffic_class5
      
  def _set_dwrr_traffic_class5(self, v, load=False):
    """
    Setter method for dwrr_traffic_class5, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class5 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dwrr_traffic_class5 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dwrr_traffic_class5() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class5", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dwrr_traffic_class5 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class5", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__dwrr_traffic_class5 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dwrr_traffic_class5(self):
    self.__dwrr_traffic_class5 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class5", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_dwrr_traffic_class6(self):
    """
    Getter method for dwrr_traffic_class6, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class6 (int32)
    """
    return self.__dwrr_traffic_class6
      
  def _set_dwrr_traffic_class6(self, v, load=False):
    """
    Setter method for dwrr_traffic_class6, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class6 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dwrr_traffic_class6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dwrr_traffic_class6() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dwrr_traffic_class6 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__dwrr_traffic_class6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dwrr_traffic_class6(self):
    self.__dwrr_traffic_class6 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_dwrr_traffic_class7(self):
    """
    Getter method for dwrr_traffic_class7, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class7 (int32)
    """
    return self.__dwrr_traffic_class7
      
  def _set_dwrr_traffic_class7(self, v, load=False):
    """
    Setter method for dwrr_traffic_class7, mapped from YANG variable /qos/queue/multicast/scheduler/dwrr/dwrr_traffic_class7 (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dwrr_traffic_class7 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dwrr_traffic_class7() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class7", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dwrr_traffic_class7 must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class7", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__dwrr_traffic_class7 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dwrr_traffic_class7(self):
    self.__dwrr_traffic_class7 = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="dwrr-traffic-class7", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)

  dwrr_traffic_class0 = __builtin__.property(_get_dwrr_traffic_class0, _set_dwrr_traffic_class0)
  dwrr_traffic_class1 = __builtin__.property(_get_dwrr_traffic_class1, _set_dwrr_traffic_class1)
  dwrr_traffic_class2 = __builtin__.property(_get_dwrr_traffic_class2, _set_dwrr_traffic_class2)
  dwrr_traffic_class3 = __builtin__.property(_get_dwrr_traffic_class3, _set_dwrr_traffic_class3)
  dwrr_traffic_class4 = __builtin__.property(_get_dwrr_traffic_class4, _set_dwrr_traffic_class4)
  dwrr_traffic_class5 = __builtin__.property(_get_dwrr_traffic_class5, _set_dwrr_traffic_class5)
  dwrr_traffic_class6 = __builtin__.property(_get_dwrr_traffic_class6, _set_dwrr_traffic_class6)
  dwrr_traffic_class7 = __builtin__.property(_get_dwrr_traffic_class7, _set_dwrr_traffic_class7)


  _pyangbind_elements = {'dwrr_traffic_class0': dwrr_traffic_class0, 'dwrr_traffic_class1': dwrr_traffic_class1, 'dwrr_traffic_class2': dwrr_traffic_class2, 'dwrr_traffic_class3': dwrr_traffic_class3, 'dwrr_traffic_class4': dwrr_traffic_class4, 'dwrr_traffic_class5': dwrr_traffic_class5, 'dwrr_traffic_class6': dwrr_traffic_class6, 'dwrr_traffic_class7': dwrr_traffic_class7, }


