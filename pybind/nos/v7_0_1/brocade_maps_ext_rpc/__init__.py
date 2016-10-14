
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import maps_re_apply_policy
import maps_get_all_policy
import maps_get_default_rules
class brocade_maps_ext(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-maps-ext - based on the path /brocade_maps_ext_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This sub module defines show system-monitor data model
Copyright (c) 2011 by Brocade Communications Systems, Inc.
All rights reserved.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__maps_re_apply_policy','__maps_get_all_policy','__maps_get_default_rules',)

  _yang_name = 'brocade-maps-ext'

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
    self.__maps_get_default_rules = YANGDynClass(base=maps_get_default_rules.maps_get_default_rules, is_leaf=True, yang_name="maps-get-default-rules", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'maps-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='rpc', is_config=True)
    self.__maps_get_all_policy = YANGDynClass(base=maps_get_all_policy.maps_get_all_policy, is_leaf=True, yang_name="maps-get-all-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'maps-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='rpc', is_config=True)
    self.__maps_re_apply_policy = YANGDynClass(base=maps_re_apply_policy.maps_re_apply_policy, is_leaf=True, yang_name="maps-re-apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'maps-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='rpc', is_config=True)

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
      return [u'brocade_maps_ext_rpc']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return []

  def _get_maps_re_apply_policy(self):
    """
    Getter method for maps_re_apply_policy, mapped from YANG variable /brocade_maps_ext_rpc/maps_re_apply_policy (rpc)

    YANG Description: reapply maps policy
    """
    return self.__maps_re_apply_policy
      
  def _set_maps_re_apply_policy(self, v, load=False):
    """
    Setter method for maps_re_apply_policy, mapped from YANG variable /brocade_maps_ext_rpc/maps_re_apply_policy (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maps_re_apply_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maps_re_apply_policy() directly.

    YANG Description: reapply maps policy
    """
    try:
      t = YANGDynClass(v,base=maps_re_apply_policy.maps_re_apply_policy, is_leaf=True, yang_name="maps-re-apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'maps-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maps_re_apply_policy must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=maps_re_apply_policy.maps_re_apply_policy, is_leaf=True, yang_name="maps-re-apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'maps-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='rpc', is_config=True)""",
        })

    self.__maps_re_apply_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maps_re_apply_policy(self):
    self.__maps_re_apply_policy = YANGDynClass(base=maps_re_apply_policy.maps_re_apply_policy, is_leaf=True, yang_name="maps-re-apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'maps-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='rpc', is_config=True)


  def _get_maps_get_all_policy(self):
    """
    Getter method for maps_get_all_policy, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_all_policy (rpc)

    YANG Description: Shows the existing MAPS Policies
    """
    return self.__maps_get_all_policy
      
  def _set_maps_get_all_policy(self, v, load=False):
    """
    Setter method for maps_get_all_policy, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_all_policy (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maps_get_all_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maps_get_all_policy() directly.

    YANG Description: Shows the existing MAPS Policies
    """
    try:
      t = YANGDynClass(v,base=maps_get_all_policy.maps_get_all_policy, is_leaf=True, yang_name="maps-get-all-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'maps-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maps_get_all_policy must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=maps_get_all_policy.maps_get_all_policy, is_leaf=True, yang_name="maps-get-all-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'maps-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='rpc', is_config=True)""",
        })

    self.__maps_get_all_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maps_get_all_policy(self):
    self.__maps_get_all_policy = YANGDynClass(base=maps_get_all_policy.maps_get_all_policy, is_leaf=True, yang_name="maps-get-all-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'maps-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='rpc', is_config=True)


  def _get_maps_get_default_rules(self):
    """
    Getter method for maps_get_default_rules, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules (rpc)

    YANG Description: Shows the existing MAPS default rules
    """
    return self.__maps_get_default_rules
      
  def _set_maps_get_default_rules(self, v, load=False):
    """
    Setter method for maps_get_default_rules, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maps_get_default_rules is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maps_get_default_rules() directly.

    YANG Description: Shows the existing MAPS default rules
    """
    try:
      t = YANGDynClass(v,base=maps_get_default_rules.maps_get_default_rules, is_leaf=True, yang_name="maps-get-default-rules", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'maps-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maps_get_default_rules must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=maps_get_default_rules.maps_get_default_rules, is_leaf=True, yang_name="maps-get-default-rules", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'maps-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='rpc', is_config=True)""",
        })

    self.__maps_get_default_rules = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maps_get_default_rules(self):
    self.__maps_get_default_rules = YANGDynClass(base=maps_get_default_rules.maps_get_default_rules, is_leaf=True, yang_name="maps-get-default-rules", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'maps-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='rpc', is_config=True)

  maps_re_apply_policy = __builtin__.property(_get_maps_re_apply_policy, _set_maps_re_apply_policy)
  maps_get_all_policy = __builtin__.property(_get_maps_get_all_policy, _set_maps_get_all_policy)
  maps_get_default_rules = __builtin__.property(_get_maps_get_default_rules, _set_maps_get_default_rules)


  _pyangbind_elements = {'maps_re_apply_policy': maps_re_apply_policy, 'maps_get_all_policy': maps_get_all_policy, 'maps_get_default_rules': maps_get_default_rules, }

