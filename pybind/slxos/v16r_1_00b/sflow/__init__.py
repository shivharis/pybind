
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import source_interface
import collector
class sflow(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sflow - based on the path /sflow. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__enable','__null0_sampling','__collector_vrf','__source_interface','__collector','__polling_interval','__sample_rate',)

  _yang_name = 'sflow'
  _rest_name = 'sflow'

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
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable global sflow'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='empty', is_config=True)
    self.__polling_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(20), is_leaf=True, yang_name="polling-interval", rest_name="polling-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface counter polling interval', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='uint32', is_config=True)
    self.__null0_sampling = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="null0-sampling", rest_name="null0-sampling", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable Null0 Sampling On All Slots', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='empty', is_config=True)
    self.__sample_rate = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2048), is_leaf=True, yang_name="sample-rate", rest_name="sample-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface sampling rate', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='uint32', is_config=True)
    self.__source_interface = YANGDynClass(base=source_interface.source_interface, is_container='container', yang_name="source-interface", rest_name="source-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Set sFlow sourceIP interface', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='container', is_config=True)
    self.__collector_vrf = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="collector-vrf", rest_name="collector-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sflow Collector VRF Configuration', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='common-def:vrf-name', is_config=True)
    self.__collector = YANGDynClass(base=YANGListType("collector_ip_address collector_port_number use_vrf",collector.collector, yang_name="collector", rest_name="collector", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='collector-ip-address collector-port-number use-vrf', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'cli-sequence-commands': None, u'callpoint': u'SflowCollector', u'info': u'Sflow Collector Configuration'}}), is_container='list', yang_name="collector", rest_name="collector", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'cli-sequence-commands': None, u'callpoint': u'SflowCollector', u'info': u'Sflow Collector Configuration'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='list', is_config=True)

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
      return [u'sflow']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'sflow']

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /sflow/enable (empty)
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /sflow/enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable global sflow'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable global sflow'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='empty', is_config=True)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable global sflow'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='empty', is_config=True)


  def _get_null0_sampling(self):
    """
    Getter method for null0_sampling, mapped from YANG variable /sflow/null0_sampling (empty)
    """
    return self.__null0_sampling
      
  def _set_null0_sampling(self, v, load=False):
    """
    Setter method for null0_sampling, mapped from YANG variable /sflow/null0_sampling (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_null0_sampling is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_null0_sampling() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="null0-sampling", rest_name="null0-sampling", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable Null0 Sampling On All Slots', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """null0_sampling must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="null0-sampling", rest_name="null0-sampling", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable Null0 Sampling On All Slots', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='empty', is_config=True)""",
        })

    self.__null0_sampling = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_null0_sampling(self):
    self.__null0_sampling = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="null0-sampling", rest_name="null0-sampling", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable Null0 Sampling On All Slots', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='empty', is_config=True)


  def _get_collector_vrf(self):
    """
    Getter method for collector_vrf, mapped from YANG variable /sflow/collector_vrf (common-def:vrf-name)
    """
    return self.__collector_vrf
      
  def _set_collector_vrf(self, v, load=False):
    """
    Setter method for collector_vrf, mapped from YANG variable /sflow/collector_vrf (common-def:vrf-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_collector_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_collector_vrf() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="collector-vrf", rest_name="collector-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sflow Collector VRF Configuration', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='common-def:vrf-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """collector_vrf must be of a type compatible with common-def:vrf-name""",
          'defined-type': "common-def:vrf-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="collector-vrf", rest_name="collector-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sflow Collector VRF Configuration', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='common-def:vrf-name', is_config=True)""",
        })

    self.__collector_vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_collector_vrf(self):
    self.__collector_vrf = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="collector-vrf", rest_name="collector-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sflow Collector VRF Configuration', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='common-def:vrf-name', is_config=True)


  def _get_source_interface(self):
    """
    Getter method for source_interface, mapped from YANG variable /sflow/source_interface (container)
    """
    return self.__source_interface
      
  def _set_source_interface(self, v, load=False):
    """
    Setter method for source_interface, mapped from YANG variable /sflow/source_interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_interface() directly.
    """
    try:
      t = YANGDynClass(v,base=source_interface.source_interface, is_container='container', yang_name="source-interface", rest_name="source-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Set sFlow sourceIP interface', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=source_interface.source_interface, is_container='container', yang_name="source-interface", rest_name="source-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Set sFlow sourceIP interface', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='container', is_config=True)""",
        })

    self.__source_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_interface(self):
    self.__source_interface = YANGDynClass(base=source_interface.source_interface, is_container='container', yang_name="source-interface", rest_name="source-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Set sFlow sourceIP interface', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='container', is_config=True)


  def _get_collector(self):
    """
    Getter method for collector, mapped from YANG variable /sflow/collector (list)
    """
    return self.__collector
      
  def _set_collector(self, v, load=False):
    """
    Setter method for collector, mapped from YANG variable /sflow/collector (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_collector is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_collector() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("collector_ip_address collector_port_number use_vrf",collector.collector, yang_name="collector", rest_name="collector", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='collector-ip-address collector-port-number use-vrf', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'cli-sequence-commands': None, u'callpoint': u'SflowCollector', u'info': u'Sflow Collector Configuration'}}), is_container='list', yang_name="collector", rest_name="collector", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'cli-sequence-commands': None, u'callpoint': u'SflowCollector', u'info': u'Sflow Collector Configuration'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """collector must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("collector_ip_address collector_port_number use_vrf",collector.collector, yang_name="collector", rest_name="collector", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='collector-ip-address collector-port-number use-vrf', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'cli-sequence-commands': None, u'callpoint': u'SflowCollector', u'info': u'Sflow Collector Configuration'}}), is_container='list', yang_name="collector", rest_name="collector", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'cli-sequence-commands': None, u'callpoint': u'SflowCollector', u'info': u'Sflow Collector Configuration'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='list', is_config=True)""",
        })

    self.__collector = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_collector(self):
    self.__collector = YANGDynClass(base=YANGListType("collector_ip_address collector_port_number use_vrf",collector.collector, yang_name="collector", rest_name="collector", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='collector-ip-address collector-port-number use-vrf', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'cli-sequence-commands': None, u'callpoint': u'SflowCollector', u'info': u'Sflow Collector Configuration'}}), is_container='list', yang_name="collector", rest_name="collector", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'cli-sequence-commands': None, u'callpoint': u'SflowCollector', u'info': u'Sflow Collector Configuration'}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='list', is_config=True)


  def _get_polling_interval(self):
    """
    Getter method for polling_interval, mapped from YANG variable /sflow/polling_interval (uint32)
    """
    return self.__polling_interval
      
  def _set_polling_interval(self, v, load=False):
    """
    Setter method for polling_interval, mapped from YANG variable /sflow/polling_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_polling_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_polling_interval() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(20), is_leaf=True, yang_name="polling-interval", rest_name="polling-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface counter polling interval', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """polling_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(20), is_leaf=True, yang_name="polling-interval", rest_name="polling-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface counter polling interval', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='uint32', is_config=True)""",
        })

    self.__polling_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_polling_interval(self):
    self.__polling_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(20), is_leaf=True, yang_name="polling-interval", rest_name="polling-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface counter polling interval', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='uint32', is_config=True)


  def _get_sample_rate(self):
    """
    Getter method for sample_rate, mapped from YANG variable /sflow/sample_rate (uint32)
    """
    return self.__sample_rate
      
  def _set_sample_rate(self, v, load=False):
    """
    Setter method for sample_rate, mapped from YANG variable /sflow/sample_rate (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sample_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sample_rate() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2048), is_leaf=True, yang_name="sample-rate", rest_name="sample-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface sampling rate', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sample_rate must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2048), is_leaf=True, yang_name="sample-rate", rest_name="sample-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface sampling rate', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='uint32', is_config=True)""",
        })

    self.__sample_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sample_rate(self):
    self.__sample_rate = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2048), is_leaf=True, yang_name="sample-rate", rest_name="sample-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface sampling rate', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sflow', defining_module='brocade-sflow', yang_type='uint32', is_config=True)

  enable = __builtin__.property(_get_enable, _set_enable)
  null0_sampling = __builtin__.property(_get_null0_sampling, _set_null0_sampling)
  collector_vrf = __builtin__.property(_get_collector_vrf, _set_collector_vrf)
  source_interface = __builtin__.property(_get_source_interface, _set_source_interface)
  collector = __builtin__.property(_get_collector, _set_collector)
  polling_interval = __builtin__.property(_get_polling_interval, _set_polling_interval)
  sample_rate = __builtin__.property(_get_sample_rate, _set_sample_rate)


  _pyangbind_elements = {'enable': enable, 'null0_sampling': null0_sampling, 'collector_vrf': collector_vrf, 'source_interface': source_interface, 'collector': collector, 'polling_interval': polling_interval, 'sample_rate': sample_rate, }


