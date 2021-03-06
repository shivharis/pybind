
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class mac_refresh_time_config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /protocol/edge-loop-detection/mac-refresh-time-config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mac_refresh_time','__mac_refresh_type',)

  _yang_name = 'mac-refresh-time-config'
  _rest_name = 'mac-refresh'

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
    self.__mac_refresh_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'all': {'value': 1}, u'port': {'value': 2}},), is_leaf=True, yang_name="mac-refresh-type", rest_name="mac-refresh-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac refresh type.', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='enumeration', is_config=True)
    self.__mac_refresh_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..300']}), is_leaf=True, yang_name="mac-refresh-time", rest_name="mac-refresh-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'mac-refresh-time', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)

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
      return [u'protocol', u'edge-loop-detection', u'mac-refresh-time-config']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol', u'edge-loop-detection', u'mac-refresh']

  def _get_mac_refresh_time(self):
    """
    Getter method for mac_refresh_time, mapped from YANG variable /protocol/edge_loop_detection/mac_refresh_time_config/mac_refresh_time (uint32)
    """
    return self.__mac_refresh_time
      
  def _set_mac_refresh_time(self, v, load=False):
    """
    Setter method for mac_refresh_time, mapped from YANG variable /protocol/edge_loop_detection/mac_refresh_time_config/mac_refresh_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_refresh_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_refresh_time() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..300']}), is_leaf=True, yang_name="mac-refresh-time", rest_name="mac-refresh-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'mac-refresh-time', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_refresh_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..300']}), is_leaf=True, yang_name="mac-refresh-time", rest_name="mac-refresh-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'mac-refresh-time', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)""",
        })

    self.__mac_refresh_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_refresh_time(self):
    self.__mac_refresh_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..300']}), is_leaf=True, yang_name="mac-refresh-time", rest_name="mac-refresh-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'mac-refresh-time', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)


  def _get_mac_refresh_type(self):
    """
    Getter method for mac_refresh_type, mapped from YANG variable /protocol/edge_loop_detection/mac_refresh_time_config/mac_refresh_type (enumeration)
    """
    return self.__mac_refresh_type
      
  def _set_mac_refresh_type(self, v, load=False):
    """
    Setter method for mac_refresh_type, mapped from YANG variable /protocol/edge_loop_detection/mac_refresh_time_config/mac_refresh_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_refresh_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_refresh_type() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'all': {'value': 1}, u'port': {'value': 2}},), is_leaf=True, yang_name="mac-refresh-type", rest_name="mac-refresh-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac refresh type.', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_refresh_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-eld:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'all': {'value': 1}, u'port': {'value': 2}},), is_leaf=True, yang_name="mac-refresh-type", rest_name="mac-refresh-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac refresh type.', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='enumeration', is_config=True)""",
        })

    self.__mac_refresh_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_refresh_type(self):
    self.__mac_refresh_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'all': {'value': 1}, u'port': {'value': 2}},), is_leaf=True, yang_name="mac-refresh-type", rest_name="mac-refresh-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac refresh type.', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='enumeration', is_config=True)

  mac_refresh_time = __builtin__.property(_get_mac_refresh_time, _set_mac_refresh_time)
  mac_refresh_type = __builtin__.property(_get_mac_refresh_type, _set_mac_refresh_type)


  _pyangbind_elements = {'mac_refresh_time': mac_refresh_time, 'mac_refresh_type': mac_refresh_type, }


