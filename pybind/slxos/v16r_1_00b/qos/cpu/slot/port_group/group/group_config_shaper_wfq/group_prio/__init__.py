
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import group_prio_config_shaper_wfq
class group_prio(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mls - based on the path /qos/cpu/slot/port-group/group/group-config-shaper-wfq/group-prio. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__group_prio_id','__group_prio_config_shaper_wfq',)

  _yang_name = 'group-prio'
  _rest_name = 'prio'

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
    self.__group_prio_config_shaper_wfq = YANGDynClass(base=group_prio_config_shaper_wfq.group_prio_config_shaper_wfq, is_container='container', presence=False, yang_name="group-prio-config-shaper-wfq", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)
    self.__group_prio_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..3']}), is_leaf=True, yang_name="group-prio-id", rest_name="group-prio-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='priority', is_config=True)

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
      return [u'qos', u'cpu', u'slot', u'port-group', u'group', u'group-config-shaper-wfq', u'group-prio']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos', u'cpu', u'slot', u'group', u'prio']

  def _get_group_prio_id(self):
    """
    Getter method for group_prio_id, mapped from YANG variable /qos/cpu/slot/port_group/group/group_config_shaper_wfq/group_prio/group_prio_id (priority)
    """
    return self.__group_prio_id
      
  def _set_group_prio_id(self, v, load=False):
    """
    Setter method for group_prio_id, mapped from YANG variable /qos/cpu/slot/port_group/group/group_config_shaper_wfq/group_prio/group_prio_id (priority)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_prio_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_prio_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..3']}), is_leaf=True, yang_name="group-prio-id", rest_name="group-prio-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='priority', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_prio_id must be of a type compatible with priority""",
          'defined-type': "brocade-qos-cpu:priority",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..3']}), is_leaf=True, yang_name="group-prio-id", rest_name="group-prio-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='priority', is_config=True)""",
        })

    self.__group_prio_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_prio_id(self):
    self.__group_prio_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..3']}), is_leaf=True, yang_name="group-prio-id", rest_name="group-prio-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='priority', is_config=True)


  def _get_group_prio_config_shaper_wfq(self):
    """
    Getter method for group_prio_config_shaper_wfq, mapped from YANG variable /qos/cpu/slot/port_group/group/group_config_shaper_wfq/group_prio/group_prio_config_shaper_wfq (container)
    """
    return self.__group_prio_config_shaper_wfq
      
  def _set_group_prio_config_shaper_wfq(self, v, load=False):
    """
    Setter method for group_prio_config_shaper_wfq, mapped from YANG variable /qos/cpu/slot/port_group/group/group_config_shaper_wfq/group_prio/group_prio_config_shaper_wfq (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_prio_config_shaper_wfq is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_prio_config_shaper_wfq() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=group_prio_config_shaper_wfq.group_prio_config_shaper_wfq, is_container='container', presence=False, yang_name="group-prio-config-shaper-wfq", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_prio_config_shaper_wfq must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=group_prio_config_shaper_wfq.group_prio_config_shaper_wfq, is_container='container', presence=False, yang_name="group-prio-config-shaper-wfq", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)""",
        })

    self.__group_prio_config_shaper_wfq = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_prio_config_shaper_wfq(self):
    self.__group_prio_config_shaper_wfq = YANGDynClass(base=group_prio_config_shaper_wfq.group_prio_config_shaper_wfq, is_container='container', presence=False, yang_name="group-prio-config-shaper-wfq", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)

  group_prio_id = __builtin__.property(_get_group_prio_id, _set_group_prio_id)
  group_prio_config_shaper_wfq = __builtin__.property(_get_group_prio_config_shaper_wfq, _set_group_prio_config_shaper_wfq)


  _pyangbind_elements = {'group_prio_id': group_prio_id, 'group_prio_config_shaper_wfq': group_prio_config_shaper_wfq, }


