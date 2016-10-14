
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import last_config_update_time_for_xpaths
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vcs - based on the path /brocade_vcs_rpc/get-last-config-update-time-for-xpaths/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__last_config_update_time_for_xpaths',)

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
    self.__last_config_update_time_for_xpaths = YANGDynClass(base=YANGListType("xpath_string",last_config_update_time_for_xpaths.last_config_update_time_for_xpaths, yang_name="last-config-update-time-for-xpaths", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='xpath-string', extensions=None), is_container='list', yang_name="last-config-update-time-for-xpaths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='list', is_config=True)

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
      return [u'brocade_vcs_rpc', u'get-last-config-update-time-for-xpaths', u'output']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'get-last-config-update-time-for-xpaths', u'output']

  def _get_last_config_update_time_for_xpaths(self):
    """
    Getter method for last_config_update_time_for_xpaths, mapped from YANG variable /brocade_vcs_rpc/get_last_config_update_time_for_xpaths/output/last_config_update_time_for_xpaths (list)
    """
    return self.__last_config_update_time_for_xpaths
      
  def _set_last_config_update_time_for_xpaths(self, v, load=False):
    """
    Setter method for last_config_update_time_for_xpaths, mapped from YANG variable /brocade_vcs_rpc/get_last_config_update_time_for_xpaths/output/last_config_update_time_for_xpaths (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_config_update_time_for_xpaths is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_config_update_time_for_xpaths() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("xpath_string",last_config_update_time_for_xpaths.last_config_update_time_for_xpaths, yang_name="last-config-update-time-for-xpaths", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='xpath-string', extensions=None), is_container='list', yang_name="last-config-update-time-for-xpaths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_config_update_time_for_xpaths must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("xpath_string",last_config_update_time_for_xpaths.last_config_update_time_for_xpaths, yang_name="last-config-update-time-for-xpaths", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='xpath-string', extensions=None), is_container='list', yang_name="last-config-update-time-for-xpaths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='list', is_config=True)""",
        })

    self.__last_config_update_time_for_xpaths = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_config_update_time_for_xpaths(self):
    self.__last_config_update_time_for_xpaths = YANGDynClass(base=YANGListType("xpath_string",last_config_update_time_for_xpaths.last_config_update_time_for_xpaths, yang_name="last-config-update-time-for-xpaths", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='xpath-string', extensions=None), is_container='list', yang_name="last-config-update-time-for-xpaths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='list', is_config=True)

  last_config_update_time_for_xpaths = __builtin__.property(_get_last_config_update_time_for_xpaths, _set_last_config_update_time_for_xpaths)


  _pyangbind_elements = {'last_config_update_time_for_xpaths': last_config_update_time_for_xpaths, }


