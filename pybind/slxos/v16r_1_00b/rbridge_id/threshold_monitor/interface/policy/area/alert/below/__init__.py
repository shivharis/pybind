
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class below(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/threshold-monitor/interface/policy/area/alert/below. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__below_highthresh_action','__below_lowthresh_action',)

  _yang_name = 'below'
  _rest_name = 'below'

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
    self.__below_lowthresh_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loginfo': {'value': 4}, u'none': {'value': 0}, u'all': {'value': 1}, u'raslog': {'value': 3}, u'email': {'value': 2}},), is_leaf=True, yang_name="below-lowthresh-action", rest_name="lowthresh-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'lowthresh-action'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-actions', is_config=True)
    self.__below_highthresh_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loginfo': {'value': 4}, u'none': {'value': 0}, u'all': {'value': 1}, u'raslog': {'value': 3}, u'email': {'value': 2}},), is_leaf=True, yang_name="below-highthresh-action", rest_name="highthresh-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'highthresh-action'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-actions', is_config=True)

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
      return [u'rbridge-id', u'threshold-monitor', u'interface', u'policy', u'area', u'alert', u'below']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'threshold-monitor', u'interface', u'policy', u'area', u'alert', u'below']

  def _get_below_highthresh_action(self):
    """
    Getter method for below_highthresh_action, mapped from YANG variable /rbridge_id/threshold_monitor/interface/policy/area/alert/below/below_highthresh_action (supported-actions)
    """
    return self.__below_highthresh_action
      
  def _set_below_highthresh_action(self, v, load=False):
    """
    Setter method for below_highthresh_action, mapped from YANG variable /rbridge_id/threshold_monitor/interface/policy/area/alert/below/below_highthresh_action (supported-actions)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_below_highthresh_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_below_highthresh_action() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loginfo': {'value': 4}, u'none': {'value': 0}, u'all': {'value': 1}, u'raslog': {'value': 3}, u'email': {'value': 2}},), is_leaf=True, yang_name="below-highthresh-action", rest_name="highthresh-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'highthresh-action'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-actions', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """below_highthresh_action must be of a type compatible with supported-actions""",
          'defined-type': "brocade-threshold-monitor:supported-actions",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loginfo': {'value': 4}, u'none': {'value': 0}, u'all': {'value': 1}, u'raslog': {'value': 3}, u'email': {'value': 2}},), is_leaf=True, yang_name="below-highthresh-action", rest_name="highthresh-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'highthresh-action'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-actions', is_config=True)""",
        })

    self.__below_highthresh_action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_below_highthresh_action(self):
    self.__below_highthresh_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loginfo': {'value': 4}, u'none': {'value': 0}, u'all': {'value': 1}, u'raslog': {'value': 3}, u'email': {'value': 2}},), is_leaf=True, yang_name="below-highthresh-action", rest_name="highthresh-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'highthresh-action'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-actions', is_config=True)


  def _get_below_lowthresh_action(self):
    """
    Getter method for below_lowthresh_action, mapped from YANG variable /rbridge_id/threshold_monitor/interface/policy/area/alert/below/below_lowthresh_action (supported-actions)
    """
    return self.__below_lowthresh_action
      
  def _set_below_lowthresh_action(self, v, load=False):
    """
    Setter method for below_lowthresh_action, mapped from YANG variable /rbridge_id/threshold_monitor/interface/policy/area/alert/below/below_lowthresh_action (supported-actions)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_below_lowthresh_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_below_lowthresh_action() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loginfo': {'value': 4}, u'none': {'value': 0}, u'all': {'value': 1}, u'raslog': {'value': 3}, u'email': {'value': 2}},), is_leaf=True, yang_name="below-lowthresh-action", rest_name="lowthresh-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'lowthresh-action'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-actions', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """below_lowthresh_action must be of a type compatible with supported-actions""",
          'defined-type': "brocade-threshold-monitor:supported-actions",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loginfo': {'value': 4}, u'none': {'value': 0}, u'all': {'value': 1}, u'raslog': {'value': 3}, u'email': {'value': 2}},), is_leaf=True, yang_name="below-lowthresh-action", rest_name="lowthresh-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'lowthresh-action'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-actions', is_config=True)""",
        })

    self.__below_lowthresh_action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_below_lowthresh_action(self):
    self.__below_lowthresh_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loginfo': {'value': 4}, u'none': {'value': 0}, u'all': {'value': 1}, u'raslog': {'value': 3}, u'email': {'value': 2}},), is_leaf=True, yang_name="below-lowthresh-action", rest_name="lowthresh-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'lowthresh-action'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-actions', is_config=True)

  below_highthresh_action = __builtin__.property(_get_below_highthresh_action, _set_below_highthresh_action)
  below_lowthresh_action = __builtin__.property(_get_below_lowthresh_action, _set_below_lowthresh_action)


  _pyangbind_elements = {'below_highthresh_action': below_highthresh_action, 'below_lowthresh_action': below_lowthresh_action, }


