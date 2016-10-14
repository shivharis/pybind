
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vmpolicy_macaddr(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vswitch - based on the path /brocade_vswitch_rpc/get-vmpolicy-macaddr/output/vmpolicy-macaddr. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__mac','__name','__datacenter','__dvpg_nn','__port_nn','__port_prof',)

  _yang_name = 'vmpolicy-macaddr'

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
    self.__datacenter = YANGDynClass(base=unicode, is_leaf=True, yang_name="datacenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    self.__port_prof = YANGDynClass(base=unicode, is_leaf=True, yang_name="port-prof", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    self.__dvpg_nn = YANGDynClass(base=unicode, is_leaf=True, yang_name="dvpg-nn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    self.__mac = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='yang:mac-address', is_config=True)
    self.__port_nn = YANGDynClass(base=unicode, is_leaf=True, yang_name="port-nn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)

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
      return [u'brocade_vswitch_rpc', u'get-vmpolicy-macaddr', u'output', u'vmpolicy-macaddr']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'get-vmpolicy-macaddr', u'output', u'vmpolicy-macaddr']

  def _get_mac(self):
    """
    Getter method for mac, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/output/vmpolicy_macaddr/mac (yang:mac-address)

    YANG Description: vnic Mac address in HH:HH:HH:HH:HH:HH format
    """
    return self.__mac
      
  def _set_mac(self, v, load=False):
    """
    Setter method for mac, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/output/vmpolicy_macaddr/mac (yang:mac-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac() directly.

    YANG Description: vnic Mac address in HH:HH:HH:HH:HH:HH format
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='yang:mac-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac must be of a type compatible with yang:mac-address""",
          'defined-type': "yang:mac-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='yang:mac-address', is_config=True)""",
        })

    self.__mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac(self):
    self.__mac = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='yang:mac-address', is_config=True)


  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/output/vmpolicy_macaddr/name (string)

    YANG Description: virutal machine name
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/output/vmpolicy_macaddr/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: virutal machine name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)


  def _get_datacenter(self):
    """
    Getter method for datacenter, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/output/vmpolicy_macaddr/datacenter (string)

    YANG Description: host datacenter
    """
    return self.__datacenter
      
  def _set_datacenter(self, v, load=False):
    """
    Setter method for datacenter, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/output/vmpolicy_macaddr/datacenter (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_datacenter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_datacenter() directly.

    YANG Description: host datacenter
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="datacenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """datacenter must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="datacenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)""",
        })

    self.__datacenter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_datacenter(self):
    self.__datacenter = YANGDynClass(base=unicode, is_leaf=True, yang_name="datacenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)


  def _get_dvpg_nn(self):
    """
    Getter method for dvpg_nn, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/output/vmpolicy_macaddr/dvpg_nn (string)

    YANG Description: distributed virtual port group
    """
    return self.__dvpg_nn
      
  def _set_dvpg_nn(self, v, load=False):
    """
    Setter method for dvpg_nn, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/output/vmpolicy_macaddr/dvpg_nn (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dvpg_nn is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dvpg_nn() directly.

    YANG Description: distributed virtual port group
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="dvpg-nn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dvpg_nn must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="dvpg-nn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)""",
        })

    self.__dvpg_nn = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dvpg_nn(self):
    self.__dvpg_nn = YANGDynClass(base=unicode, is_leaf=True, yang_name="dvpg-nn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)


  def _get_port_nn(self):
    """
    Getter method for port_nn, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/output/vmpolicy_macaddr/port_nn (string)

    YANG Description: vm port ID
    """
    return self.__port_nn
      
  def _set_port_nn(self, v, load=False):
    """
    Setter method for port_nn, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/output/vmpolicy_macaddr/port_nn (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_nn is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_nn() directly.

    YANG Description: vm port ID
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="port-nn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_nn must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="port-nn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)""",
        })

    self.__port_nn = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_nn(self):
    self.__port_nn = YANGDynClass(base=unicode, is_leaf=True, yang_name="port-nn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)


  def _get_port_prof(self):
    """
    Getter method for port_prof, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/output/vmpolicy_macaddr/port_prof (string)

    YANG Description: port profile
    """
    return self.__port_prof
      
  def _set_port_prof(self, v, load=False):
    """
    Setter method for port_prof, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/output/vmpolicy_macaddr/port_prof (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_prof is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_prof() directly.

    YANG Description: port profile
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="port-prof", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_prof must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="port-prof", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)""",
        })

    self.__port_prof = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_prof(self):
    self.__port_prof = YANGDynClass(base=unicode, is_leaf=True, yang_name="port-prof", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)

  mac = __builtin__.property(_get_mac, _set_mac)
  name = __builtin__.property(_get_name, _set_name)
  datacenter = __builtin__.property(_get_datacenter, _set_datacenter)
  dvpg_nn = __builtin__.property(_get_dvpg_nn, _set_dvpg_nn)
  port_nn = __builtin__.property(_get_port_nn, _set_port_nn)
  port_prof = __builtin__.property(_get_port_prof, _set_port_prof)


  _pyangbind_elements = {'mac': mac, 'name': name, 'datacenter': datacenter, 'dvpg_nn': dvpg_nn, 'port_nn': port_nn, 'port_prof': port_prof, }

