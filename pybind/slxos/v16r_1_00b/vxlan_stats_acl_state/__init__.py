
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import extended_stats_data
class vxlan_stats_acl_state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ssm-operational - based on the path /vxlan-stats-acl-state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description:  Vxlan stats ACL information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__extended_stats_data',)

  _yang_name = 'vxlan-stats-acl-state'

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
    self.__extended_stats_data = YANGDynClass(base=YANGListType("acl_name seq_num",extended_stats_data.extended_stats_data, yang_name="extended-stats-data", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='acl-name seq-num', extensions={u'tailf-common': {u'callpoint': u'ssm-extended-stats-data', u'cli-suppress-show-path': None}}), is_container='list', yang_name="extended-stats-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-extended-stats-data', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)

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
      return [u'vxlan-stats-acl-state']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'vxlan-stats-acl-state']

  def _get_extended_stats_data(self):
    """
    Getter method for extended_stats_data, mapped from YANG variable /vxlan_stats_acl_state/extended_stats_data (list)

    YANG Description: Extended stats ACL
    """
    return self.__extended_stats_data
      
  def _set_extended_stats_data(self, v, load=False):
    """
    Setter method for extended_stats_data, mapped from YANG variable /vxlan_stats_acl_state/extended_stats_data (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_extended_stats_data is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_extended_stats_data() directly.

    YANG Description: Extended stats ACL
    """
    try:
      t = YANGDynClass(v,base=YANGListType("acl_name seq_num",extended_stats_data.extended_stats_data, yang_name="extended-stats-data", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='acl-name seq-num', extensions={u'tailf-common': {u'callpoint': u'ssm-extended-stats-data', u'cli-suppress-show-path': None}}), is_container='list', yang_name="extended-stats-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-extended-stats-data', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """extended_stats_data must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("acl_name seq_num",extended_stats_data.extended_stats_data, yang_name="extended-stats-data", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='acl-name seq-num', extensions={u'tailf-common': {u'callpoint': u'ssm-extended-stats-data', u'cli-suppress-show-path': None}}), is_container='list', yang_name="extended-stats-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-extended-stats-data', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)""",
        })

    self.__extended_stats_data = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_extended_stats_data(self):
    self.__extended_stats_data = YANGDynClass(base=YANGListType("acl_name seq_num",extended_stats_data.extended_stats_data, yang_name="extended-stats-data", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='acl-name seq-num', extensions={u'tailf-common': {u'callpoint': u'ssm-extended-stats-data', u'cli-suppress-show-path': None}}), is_container='list', yang_name="extended-stats-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-extended-stats-data', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)

  extended_stats_data = __builtin__.property(_get_extended_stats_data)


  _pyangbind_elements = {'extended_stats_data': extended_stats_data, }


