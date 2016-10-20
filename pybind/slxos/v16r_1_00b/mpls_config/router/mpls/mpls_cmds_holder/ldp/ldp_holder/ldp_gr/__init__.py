
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ldp_gr(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/ldp/ldp-holder/ldp-gr. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ldp_gr_helper_only','__ldp_gr_max_neighbor_reconnect_time','__ldp_gr_max_neighbor_recovery_time','__ldp_gr_reconnect_time','__ldp_gr_recovery_time',)

  _yang_name = 'ldp-gr'
  _rest_name = 'graceful-restart'

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
    self.__ldp_gr_max_neighbor_reconnect_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..300']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-max-neighbor-reconnect-time", rest_name="max-neighbor-reconnect-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Maximum time to wait for neighbor to reconnect (60-300 sec)', u'cli-full-no': None, u'alt-name': u'max-neighbor-reconnect-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_gr_max_neighbor_recovery_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-max-neighbor-recovery-time", rest_name="max-neighbor-recovery-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Maximum time to wait for neighbor to recover (60-3600 sec)', u'cli-full-no': None, u'alt-name': u'max-neighbor-recovery-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_gr_recovery_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-recovery-time", rest_name="recovery-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Recovery time (60-3600 sec)', u'cli-full-no': None, u'alt-name': u'recovery-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_gr_helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-gr-helper-only", rest_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Helper only mode', u'cli-full-no': None, u'alt-name': u'helper-only'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    self.__ldp_gr_reconnect_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..300']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-reconnect-time", rest_name="reconnect-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Session reconnect time (60-300 sec)', u'cli-full-no': None, u'alt-name': u'reconnect-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'ldp', u'ldp-holder', u'ldp-gr']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'mpls', u'ldp', u'graceful-restart']

  def _get_ldp_gr_helper_only(self):
    """
    Getter method for ldp_gr_helper_only, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_gr/ldp_gr_helper_only (empty)
    """
    return self.__ldp_gr_helper_only
      
  def _set_ldp_gr_helper_only(self, v, load=False):
    """
    Setter method for ldp_gr_helper_only, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_gr/ldp_gr_helper_only (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_gr_helper_only is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_gr_helper_only() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ldp-gr-helper-only", rest_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Helper only mode', u'cli-full-no': None, u'alt-name': u'helper-only'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_gr_helper_only must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-gr-helper-only", rest_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Helper only mode', u'cli-full-no': None, u'alt-name': u'helper-only'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__ldp_gr_helper_only = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_gr_helper_only(self):
    self.__ldp_gr_helper_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-gr-helper-only", rest_name="helper-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Helper only mode', u'cli-full-no': None, u'alt-name': u'helper-only'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)


  def _get_ldp_gr_max_neighbor_reconnect_time(self):
    """
    Getter method for ldp_gr_max_neighbor_reconnect_time, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_gr/ldp_gr_max_neighbor_reconnect_time (uint32)
    """
    return self.__ldp_gr_max_neighbor_reconnect_time
      
  def _set_ldp_gr_max_neighbor_reconnect_time(self, v, load=False):
    """
    Setter method for ldp_gr_max_neighbor_reconnect_time, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_gr/ldp_gr_max_neighbor_reconnect_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_gr_max_neighbor_reconnect_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_gr_max_neighbor_reconnect_time() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..300']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-max-neighbor-reconnect-time", rest_name="max-neighbor-reconnect-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Maximum time to wait for neighbor to reconnect (60-300 sec)', u'cli-full-no': None, u'alt-name': u'max-neighbor-reconnect-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_gr_max_neighbor_reconnect_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..300']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-max-neighbor-reconnect-time", rest_name="max-neighbor-reconnect-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Maximum time to wait for neighbor to reconnect (60-300 sec)', u'cli-full-no': None, u'alt-name': u'max-neighbor-reconnect-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_gr_max_neighbor_reconnect_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_gr_max_neighbor_reconnect_time(self):
    self.__ldp_gr_max_neighbor_reconnect_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..300']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-max-neighbor-reconnect-time", rest_name="max-neighbor-reconnect-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Maximum time to wait for neighbor to reconnect (60-300 sec)', u'cli-full-no': None, u'alt-name': u'max-neighbor-reconnect-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_gr_max_neighbor_recovery_time(self):
    """
    Getter method for ldp_gr_max_neighbor_recovery_time, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_gr/ldp_gr_max_neighbor_recovery_time (uint32)
    """
    return self.__ldp_gr_max_neighbor_recovery_time
      
  def _set_ldp_gr_max_neighbor_recovery_time(self, v, load=False):
    """
    Setter method for ldp_gr_max_neighbor_recovery_time, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_gr/ldp_gr_max_neighbor_recovery_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_gr_max_neighbor_recovery_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_gr_max_neighbor_recovery_time() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-max-neighbor-recovery-time", rest_name="max-neighbor-recovery-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Maximum time to wait for neighbor to recover (60-3600 sec)', u'cli-full-no': None, u'alt-name': u'max-neighbor-recovery-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_gr_max_neighbor_recovery_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-max-neighbor-recovery-time", rest_name="max-neighbor-recovery-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Maximum time to wait for neighbor to recover (60-3600 sec)', u'cli-full-no': None, u'alt-name': u'max-neighbor-recovery-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_gr_max_neighbor_recovery_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_gr_max_neighbor_recovery_time(self):
    self.__ldp_gr_max_neighbor_recovery_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-max-neighbor-recovery-time", rest_name="max-neighbor-recovery-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Maximum time to wait for neighbor to recover (60-3600 sec)', u'cli-full-no': None, u'alt-name': u'max-neighbor-recovery-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_gr_reconnect_time(self):
    """
    Getter method for ldp_gr_reconnect_time, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_gr/ldp_gr_reconnect_time (uint32)
    """
    return self.__ldp_gr_reconnect_time
      
  def _set_ldp_gr_reconnect_time(self, v, load=False):
    """
    Setter method for ldp_gr_reconnect_time, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_gr/ldp_gr_reconnect_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_gr_reconnect_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_gr_reconnect_time() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..300']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-reconnect-time", rest_name="reconnect-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Session reconnect time (60-300 sec)', u'cli-full-no': None, u'alt-name': u'reconnect-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_gr_reconnect_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..300']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-reconnect-time", rest_name="reconnect-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Session reconnect time (60-300 sec)', u'cli-full-no': None, u'alt-name': u'reconnect-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_gr_reconnect_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_gr_reconnect_time(self):
    self.__ldp_gr_reconnect_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..300']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-reconnect-time", rest_name="reconnect-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Session reconnect time (60-300 sec)', u'cli-full-no': None, u'alt-name': u'reconnect-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_gr_recovery_time(self):
    """
    Getter method for ldp_gr_recovery_time, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_gr/ldp_gr_recovery_time (uint32)
    """
    return self.__ldp_gr_recovery_time
      
  def _set_ldp_gr_recovery_time(self, v, load=False):
    """
    Setter method for ldp_gr_recovery_time, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_gr/ldp_gr_recovery_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_gr_recovery_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_gr_recovery_time() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-recovery-time", rest_name="recovery-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Recovery time (60-3600 sec)', u'cli-full-no': None, u'alt-name': u'recovery-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_gr_recovery_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-recovery-time", rest_name="recovery-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Recovery time (60-3600 sec)', u'cli-full-no': None, u'alt-name': u'recovery-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_gr_recovery_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_gr_recovery_time(self):
    self.__ldp_gr_recovery_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(120), is_leaf=True, yang_name="ldp-gr-recovery-time", rest_name="recovery-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Recovery time (60-3600 sec)', u'cli-full-no': None, u'alt-name': u'recovery-time'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  ldp_gr_helper_only = __builtin__.property(_get_ldp_gr_helper_only, _set_ldp_gr_helper_only)
  ldp_gr_max_neighbor_reconnect_time = __builtin__.property(_get_ldp_gr_max_neighbor_reconnect_time, _set_ldp_gr_max_neighbor_reconnect_time)
  ldp_gr_max_neighbor_recovery_time = __builtin__.property(_get_ldp_gr_max_neighbor_recovery_time, _set_ldp_gr_max_neighbor_recovery_time)
  ldp_gr_reconnect_time = __builtin__.property(_get_ldp_gr_reconnect_time, _set_ldp_gr_reconnect_time)
  ldp_gr_recovery_time = __builtin__.property(_get_ldp_gr_recovery_time, _set_ldp_gr_recovery_time)


  _pyangbind_elements = {'ldp_gr_helper_only': ldp_gr_helper_only, 'ldp_gr_max_neighbor_reconnect_time': ldp_gr_max_neighbor_reconnect_time, 'ldp_gr_max_neighbor_recovery_time': ldp_gr_max_neighbor_recovery_time, 'ldp_gr_reconnect_time': ldp_gr_reconnect_time, 'ldp_gr_recovery_time': ldp_gr_recovery_time, }


