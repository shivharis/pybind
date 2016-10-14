
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import fwdl_entries
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-firmware - based on the path /brocade_firmware_rpc/fwdl-status/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__number_of_entries','__fwdl_state','__fwdl_entries',)

  _yang_name = 'output'

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
    self.__fwdl_entries = YANGDynClass(base=YANGListType(False,fwdl_entries.fwdl_entries, yang_name="fwdl-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="fwdl-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='list', is_config=True)
    self.__number_of_entries = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="number-of-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'This specifies the number of status entries'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)
    self.__fwdl_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in-progress': {'value': 1}, u'downloaded': {'value': 2}, u'completed': {'value': 4}, u'failed': {'value': 3}},), is_leaf=True, yang_name="fwdl-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Firmware download state'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)

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
      return [u'brocade_firmware_rpc', u'fwdl-status', u'output']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'fwdl-status', u'output']

  def _get_number_of_entries(self):
    """
    Getter method for number_of_entries, mapped from YANG variable /brocade_firmware_rpc/fwdl_status/output/number_of_entries (uint32)
    """
    return self.__number_of_entries
      
  def _set_number_of_entries(self, v, load=False):
    """
    Setter method for number_of_entries, mapped from YANG variable /brocade_firmware_rpc/fwdl_status/output/number_of_entries (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_number_of_entries is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_number_of_entries() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="number-of-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'This specifies the number of status entries'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """number_of_entries must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="number-of-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'This specifies the number of status entries'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)""",
        })

    self.__number_of_entries = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_number_of_entries(self):
    self.__number_of_entries = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="number-of-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'This specifies the number of status entries'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)


  def _get_fwdl_state(self):
    """
    Getter method for fwdl_state, mapped from YANG variable /brocade_firmware_rpc/fwdl_status/output/fwdl_state (enumeration)
    """
    return self.__fwdl_state
      
  def _set_fwdl_state(self, v, load=False):
    """
    Setter method for fwdl_state, mapped from YANG variable /brocade_firmware_rpc/fwdl_status/output/fwdl_state (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fwdl_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fwdl_state() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in-progress': {'value': 1}, u'downloaded': {'value': 2}, u'completed': {'value': 4}, u'failed': {'value': 3}},), is_leaf=True, yang_name="fwdl-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Firmware download state'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fwdl_state must be of a type compatible with enumeration""",
          'defined-type': "brocade-firmware:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in-progress': {'value': 1}, u'downloaded': {'value': 2}, u'completed': {'value': 4}, u'failed': {'value': 3}},), is_leaf=True, yang_name="fwdl-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Firmware download state'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)""",
        })

    self.__fwdl_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fwdl_state(self):
    self.__fwdl_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in-progress': {'value': 1}, u'downloaded': {'value': 2}, u'completed': {'value': 4}, u'failed': {'value': 3}},), is_leaf=True, yang_name="fwdl-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Firmware download state'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)


  def _get_fwdl_entries(self):
    """
    Getter method for fwdl_entries, mapped from YANG variable /brocade_firmware_rpc/fwdl_status/output/fwdl_entries (list)
    """
    return self.__fwdl_entries
      
  def _set_fwdl_entries(self, v, load=False):
    """
    Setter method for fwdl_entries, mapped from YANG variable /brocade_firmware_rpc/fwdl_status/output/fwdl_entries (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fwdl_entries is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fwdl_entries() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType(False,fwdl_entries.fwdl_entries, yang_name="fwdl-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="fwdl-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fwdl_entries must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,fwdl_entries.fwdl_entries, yang_name="fwdl-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="fwdl-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='list', is_config=True)""",
        })

    self.__fwdl_entries = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fwdl_entries(self):
    self.__fwdl_entries = YANGDynClass(base=YANGListType(False,fwdl_entries.fwdl_entries, yang_name="fwdl-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="fwdl-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='list', is_config=True)

  number_of_entries = __builtin__.property(_get_number_of_entries, _set_number_of_entries)
  fwdl_state = __builtin__.property(_get_fwdl_state, _set_fwdl_state)
  fwdl_entries = __builtin__.property(_get_fwdl_entries, _set_fwdl_entries)


  _pyangbind_elements = {'number_of_entries': number_of_entries, 'fwdl_state': fwdl_state, 'fwdl_entries': fwdl_entries, }


