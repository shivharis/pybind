
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import cluster_fwdl_entries
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-firmware - based on the path /brocade_firmware_rpc/logical-chassis-fwdl-status/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__overall_status','__cluster_fwdl_entries',)

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
    self.__cluster_fwdl_entries = YANGDynClass(base=YANGListType(False,cluster_fwdl_entries.cluster_fwdl_entries, yang_name="cluster-fwdl-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="cluster-fwdl-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='list', is_config=True)
    self.__overall_status = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="overall-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Logical-chassis FWDL command status. 0-success, -1-retrieve-fail, -2-invalid rbridge-id'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)

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
      return [u'brocade_firmware_rpc', u'logical-chassis-fwdl-status', u'output']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'logical-chassis-fwdl-status', u'output']

  def _get_overall_status(self):
    """
    Getter method for overall_status, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/overall_status (int32)
    """
    return self.__overall_status
      
  def _set_overall_status(self, v, load=False):
    """
    Setter method for overall_status, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/overall_status (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_overall_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_overall_status() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="overall-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Logical-chassis FWDL command status. 0-success, -1-retrieve-fail, -2-invalid rbridge-id'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """overall_status must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="overall-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Logical-chassis FWDL command status. 0-success, -1-retrieve-fail, -2-invalid rbridge-id'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)""",
        })

    self.__overall_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_overall_status(self):
    self.__overall_status = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="overall-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Logical-chassis FWDL command status. 0-success, -1-retrieve-fail, -2-invalid rbridge-id'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)


  def _get_cluster_fwdl_entries(self):
    """
    Getter method for cluster_fwdl_entries, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries (list)
    """
    return self.__cluster_fwdl_entries
      
  def _set_cluster_fwdl_entries(self, v, load=False):
    """
    Setter method for cluster_fwdl_entries, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cluster_fwdl_entries is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cluster_fwdl_entries() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType(False,cluster_fwdl_entries.cluster_fwdl_entries, yang_name="cluster-fwdl-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="cluster-fwdl-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cluster_fwdl_entries must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,cluster_fwdl_entries.cluster_fwdl_entries, yang_name="cluster-fwdl-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="cluster-fwdl-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='list', is_config=True)""",
        })

    self.__cluster_fwdl_entries = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cluster_fwdl_entries(self):
    self.__cluster_fwdl_entries = YANGDynClass(base=YANGListType(False,cluster_fwdl_entries.cluster_fwdl_entries, yang_name="cluster-fwdl-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="cluster-fwdl-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='list', is_config=True)

  overall_status = __builtin__.property(_get_overall_status, _set_overall_status)
  cluster_fwdl_entries = __builtin__.property(_get_cluster_fwdl_entries, _set_cluster_fwdl_entries)


  _pyangbind_elements = {'overall_status': overall_status, 'cluster_fwdl_entries': cluster_fwdl_entries, }


