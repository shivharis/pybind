
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import default_information_originate
import redistribute
class af_common_attributes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/isis/router-isis-cmds-holder/address-family/ipv6/af-ipv6-unicast/af-ipv6-attributes/af-common-attributes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__default_information_originate','__default_metric','__distance','__maximum_paths','__redistribute',)

  _yang_name = 'af-common-attributes'
  _rest_name = ''

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
    self.__default_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="default-metric", rest_name="default-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Metric for route redistribution', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    self.__distance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(115), is_leaf=True, yang_name="distance", rest_name="distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Define an administrative distance', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    self.__default_information_originate = YANGDynClass(base=default_information_originate.default_information_originate, is_container='container', presence=False, yang_name="default-information-originate", rest_name="default-information-originate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Control origination of default route', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    self.__maximum_paths = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(8), is_leaf=True, yang_name="maximum-paths", rest_name="maximum-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Calculate multiple paths', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    self.__redistribute = YANGDynClass(base=redistribute.redistribute, is_container='container', presence=False, yang_name="redistribute", rest_name="redistribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Redistribute information from another routing protocol', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)

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
      return [u'routing-system', u'router', u'isis', u'router-isis-cmds-holder', u'address-family', u'ipv6', u'af-ipv6-unicast', u'af-ipv6-attributes', u'af-common-attributes']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'isis', u'address-family', u'ipv6', u'unicast']

  def _get_default_information_originate(self):
    """
    Getter method for default_information_originate, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/af_common_attributes/default_information_originate (container)
    """
    return self.__default_information_originate
      
  def _set_default_information_originate(self, v, load=False):
    """
    Setter method for default_information_originate, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/af_common_attributes/default_information_originate (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_information_originate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_information_originate() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=default_information_originate.default_information_originate, is_container='container', presence=False, yang_name="default-information-originate", rest_name="default-information-originate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Control origination of default route', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_information_originate must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=default_information_originate.default_information_originate, is_container='container', presence=False, yang_name="default-information-originate", rest_name="default-information-originate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Control origination of default route', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)""",
        })

    self.__default_information_originate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_information_originate(self):
    self.__default_information_originate = YANGDynClass(base=default_information_originate.default_information_originate, is_container='container', presence=False, yang_name="default-information-originate", rest_name="default-information-originate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Control origination of default route', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)


  def _get_default_metric(self):
    """
    Getter method for default_metric, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/af_common_attributes/default_metric (uint32)
    """
    return self.__default_metric
      
  def _set_default_metric(self, v, load=False):
    """
    Setter method for default_metric, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/af_common_attributes/default_metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_metric() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="default-metric", rest_name="default-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Metric for route redistribution', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="default-metric", rest_name="default-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Metric for route redistribution', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)""",
        })

    self.__default_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_metric(self):
    self.__default_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="default-metric", rest_name="default-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Metric for route redistribution', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)


  def _get_distance(self):
    """
    Getter method for distance, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/af_common_attributes/distance (uint32)
    """
    return self.__distance
      
  def _set_distance(self, v, load=False):
    """
    Setter method for distance, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/af_common_attributes/distance (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_distance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_distance() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(115), is_leaf=True, yang_name="distance", rest_name="distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Define an administrative distance', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """distance must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(115), is_leaf=True, yang_name="distance", rest_name="distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Define an administrative distance', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)""",
        })

    self.__distance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_distance(self):
    self.__distance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(115), is_leaf=True, yang_name="distance", rest_name="distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Define an administrative distance', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)


  def _get_maximum_paths(self):
    """
    Getter method for maximum_paths, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/af_common_attributes/maximum_paths (uint32)
    """
    return self.__maximum_paths
      
  def _set_maximum_paths(self, v, load=False):
    """
    Setter method for maximum_paths, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/af_common_attributes/maximum_paths (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maximum_paths is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maximum_paths() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(8), is_leaf=True, yang_name="maximum-paths", rest_name="maximum-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Calculate multiple paths', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maximum_paths must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(8), is_leaf=True, yang_name="maximum-paths", rest_name="maximum-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Calculate multiple paths', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)""",
        })

    self.__maximum_paths = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maximum_paths(self):
    self.__maximum_paths = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(8), is_leaf=True, yang_name="maximum-paths", rest_name="maximum-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Calculate multiple paths', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)


  def _get_redistribute(self):
    """
    Getter method for redistribute, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/af_common_attributes/redistribute (container)
    """
    return self.__redistribute
      
  def _set_redistribute(self, v, load=False):
    """
    Setter method for redistribute, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/af_common_attributes/redistribute (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redistribute is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redistribute() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=redistribute.redistribute, is_container='container', presence=False, yang_name="redistribute", rest_name="redistribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Redistribute information from another routing protocol', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redistribute must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=redistribute.redistribute, is_container='container', presence=False, yang_name="redistribute", rest_name="redistribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Redistribute information from another routing protocol', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)""",
        })

    self.__redistribute = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redistribute(self):
    self.__redistribute = YANGDynClass(base=redistribute.redistribute, is_container='container', presence=False, yang_name="redistribute", rest_name="redistribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Redistribute information from another routing protocol', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)

  default_information_originate = __builtin__.property(_get_default_information_originate, _set_default_information_originate)
  default_metric = __builtin__.property(_get_default_metric, _set_default_metric)
  distance = __builtin__.property(_get_distance, _set_distance)
  maximum_paths = __builtin__.property(_get_maximum_paths, _set_maximum_paths)
  redistribute = __builtin__.property(_get_redistribute, _set_redistribute)


  _pyangbind_elements = {'default_information_originate': default_information_originate, 'default_metric': default_metric, 'distance': distance, 'maximum_paths': maximum_paths, 'redistribute': redistribute, }


