
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class priority(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/mpls-interface/interface-dynamic-bypass/mpls-interface-dynamic-bypass-sub-cmds/priority. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface_dynamic_bypass_setup_priority','__interface_dynamic_bypass_holding_priority',)

  _yang_name = 'priority'

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
    self.__interface_dynamic_bypass_holding_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="interface-dynamic-bypass-holding-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None, u'info': u'NUMBER:0-7;;holding priority'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__interface_dynamic_bypass_setup_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="interface-dynamic-bypass-setup-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:0-7;;setup priority', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'mpls-interface', u'interface-dynamic-bypass', u'mpls-interface-dynamic-bypass-sub-cmds', u'priority']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'router', u'mpls', u'mpls-interface', u'dynamic-bypass', u'priority']

  def _get_interface_dynamic_bypass_setup_priority(self):
    """
    Getter method for interface_dynamic_bypass_setup_priority, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_dynamic_bypass/mpls_interface_dynamic_bypass_sub_cmds/priority/interface_dynamic_bypass_setup_priority (uint32)
    """
    return self.__interface_dynamic_bypass_setup_priority
      
  def _set_interface_dynamic_bypass_setup_priority(self, v, load=False):
    """
    Setter method for interface_dynamic_bypass_setup_priority, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_dynamic_bypass/mpls_interface_dynamic_bypass_sub_cmds/priority/interface_dynamic_bypass_setup_priority (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_dynamic_bypass_setup_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_dynamic_bypass_setup_priority() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="interface-dynamic-bypass-setup-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:0-7;;setup priority', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_dynamic_bypass_setup_priority must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="interface-dynamic-bypass-setup-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:0-7;;setup priority', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__interface_dynamic_bypass_setup_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_dynamic_bypass_setup_priority(self):
    self.__interface_dynamic_bypass_setup_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="interface-dynamic-bypass-setup-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:0-7;;setup priority', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_interface_dynamic_bypass_holding_priority(self):
    """
    Getter method for interface_dynamic_bypass_holding_priority, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_dynamic_bypass/mpls_interface_dynamic_bypass_sub_cmds/priority/interface_dynamic_bypass_holding_priority (uint32)
    """
    return self.__interface_dynamic_bypass_holding_priority
      
  def _set_interface_dynamic_bypass_holding_priority(self, v, load=False):
    """
    Setter method for interface_dynamic_bypass_holding_priority, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_dynamic_bypass/mpls_interface_dynamic_bypass_sub_cmds/priority/interface_dynamic_bypass_holding_priority (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_dynamic_bypass_holding_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_dynamic_bypass_holding_priority() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="interface-dynamic-bypass-holding-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None, u'info': u'NUMBER:0-7;;holding priority'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_dynamic_bypass_holding_priority must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="interface-dynamic-bypass-holding-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None, u'info': u'NUMBER:0-7;;holding priority'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__interface_dynamic_bypass_holding_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_dynamic_bypass_holding_priority(self):
    self.__interface_dynamic_bypass_holding_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="interface-dynamic-bypass-holding-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None, u'info': u'NUMBER:0-7;;holding priority'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  interface_dynamic_bypass_setup_priority = __builtin__.property(_get_interface_dynamic_bypass_setup_priority, _set_interface_dynamic_bypass_setup_priority)
  interface_dynamic_bypass_holding_priority = __builtin__.property(_get_interface_dynamic_bypass_holding_priority, _set_interface_dynamic_bypass_holding_priority)


  _pyangbind_elements = {'interface_dynamic_bypass_setup_priority': interface_dynamic_bypass_setup_priority, 'interface_dynamic_bypass_holding_priority': interface_dynamic_bypass_holding_priority, }


