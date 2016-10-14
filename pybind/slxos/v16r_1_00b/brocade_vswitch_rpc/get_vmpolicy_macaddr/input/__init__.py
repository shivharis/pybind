
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vswitch - based on the path /brocade_vswitch_rpc/get-vmpolicy-macaddr/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__mac','__vcenter','__datacenter','__last_rcvd_instance',)

  _yang_name = 'input'

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
    self.__datacenter = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="datacenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    self.__mac = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='yang:mac-address', is_config=True)
    self.__last_rcvd_instance = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-rcvd-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='uint32', is_config=True)
    self.__vcenter = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="vcenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)

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
      return [u'brocade_vswitch_rpc', u'get-vmpolicy-macaddr', u'input']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'get-vmpolicy-macaddr', u'input']

  def _get_mac(self):
    """
    Getter method for mac, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/input/mac (yang:mac-address)

    YANG Description: Mac address in HH:HH:HH:HH:HH:HH format
    """
    return self.__mac
      
  def _set_mac(self, v, load=False):
    """
    Setter method for mac, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/input/mac (yang:mac-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac() directly.

    YANG Description: Mac address in HH:HH:HH:HH:HH:HH format
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


  def _get_vcenter(self):
    """
    Getter method for vcenter, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/input/vcenter (string)

    YANG Description: vCenter name
    """
    return self.__vcenter
      
  def _set_vcenter(self, v, load=False):
    """
    Setter method for vcenter, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/input/vcenter (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vcenter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vcenter() directly.

    YANG Description: vCenter name
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="vcenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vcenter must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="vcenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)""",
        })

    self.__vcenter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vcenter(self):
    self.__vcenter = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="vcenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)


  def _get_datacenter(self):
    """
    Getter method for datacenter, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/input/datacenter (string)

    YANG Description: datacenter name
    """
    return self.__datacenter
      
  def _set_datacenter(self, v, load=False):
    """
    Setter method for datacenter, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/input/datacenter (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_datacenter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_datacenter() directly.

    YANG Description: datacenter name
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="datacenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """datacenter must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="datacenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)""",
        })

    self.__datacenter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_datacenter(self):
    self.__datacenter = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="datacenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)


  def _get_last_rcvd_instance(self):
    """
    Getter method for last_rcvd_instance, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/input/last_rcvd_instance (uint32)

    YANG Description: Last received record. 0 means this is the first request
    """
    return self.__last_rcvd_instance
      
  def _set_last_rcvd_instance(self, v, load=False):
    """
    Setter method for last_rcvd_instance, mapped from YANG variable /brocade_vswitch_rpc/get_vmpolicy_macaddr/input/last_rcvd_instance (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_rcvd_instance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_rcvd_instance() directly.

    YANG Description: Last received record. 0 means this is the first request
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-rcvd-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_rcvd_instance must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-rcvd-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='uint32', is_config=True)""",
        })

    self.__last_rcvd_instance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_rcvd_instance(self):
    self.__last_rcvd_instance = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-rcvd-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='uint32', is_config=True)

  mac = __builtin__.property(_get_mac, _set_mac)
  vcenter = __builtin__.property(_get_vcenter, _set_vcenter)
  datacenter = __builtin__.property(_get_datacenter, _set_datacenter)
  last_rcvd_instance = __builtin__.property(_get_last_rcvd_instance, _set_last_rcvd_instance)


  _pyangbind_elements = {'mac': mac, 'vcenter': vcenter, 'datacenter': datacenter, 'last_rcvd_instance': last_rcvd_instance, }


