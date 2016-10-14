
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class seq(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ip-access-list - based on the path /ip-acl/ip/access-list/standard/hide-ip-acl-std/seq. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__seq_id','__action','__src_host_any_sip','__src_host_ip','__src_mask','__count','__log','__copy_sflow',)

  _yang_name = 'seq'

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
    self.__count = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Packet count', u'cli-optional-in-sequence': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='empty', is_config=True)
    self.__log = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Log Packet', u'cli-optional-in-sequence': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='empty', is_config=True)
    self.__seq_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="seq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='seq-id-std-ext', is_config=True)
    self.__src_host_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-host-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='sip', is_config=True)
    self.__copy_sflow = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="copy-sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-optional-in-sequence': None, u'info': u'Copy to sFlow Collector', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='empty', is_config=True)
    self.__action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'hard-drop': {'value': 3}, u'permit': {'value': 1}},), is_leaf=True, yang_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)
    self.__src_host_any_sip = YANGDynClass(base=[RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 2}, u'any': {'value': 1}},),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),], is_leaf=True, yang_name="src-host-any-sip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='union', is_config=True)
    self.__src_mask = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='sip-mask', is_config=True)

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
      return [u'ip-acl', u'ip', u'access-list', u'standard', u'hide-ip-acl-std', u'seq']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'ip', u'access-list', u'standard', u'seq']

  def _get_seq_id(self):
    """
    Getter method for seq_id, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/seq_id (seq-id-std-ext)
    """
    return self.__seq_id
      
  def _set_seq_id(self, v, load=False):
    """
    Setter method for seq_id, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/seq_id (seq-id-std-ext)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_seq_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_seq_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="seq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='seq-id-std-ext', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """seq_id must be of a type compatible with seq-id-std-ext""",
          'defined-type': "brocade-ip-access-list:seq-id-std-ext",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="seq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='seq-id-std-ext', is_config=True)""",
        })

    self.__seq_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_seq_id(self):
    self.__seq_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="seq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='seq-id-std-ext', is_config=True)


  def _get_action(self):
    """
    Getter method for action, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/action (enumeration)
    """
    return self.__action
      
  def _set_action(self, v, load=False):
    """
    Setter method for action, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/action (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'hard-drop': {'value': 3}, u'permit': {'value': 1}},), is_leaf=True, yang_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action must be of a type compatible with enumeration""",
          'defined-type': "brocade-ip-access-list:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'hard-drop': {'value': 3}, u'permit': {'value': 1}},), is_leaf=True, yang_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)""",
        })

    self.__action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action(self):
    self.__action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'hard-drop': {'value': 3}, u'permit': {'value': 1}},), is_leaf=True, yang_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)


  def _get_src_host_any_sip(self):
    """
    Getter method for src_host_any_sip, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/src_host_any_sip (union)
    """
    return self.__src_host_any_sip
      
  def _set_src_host_any_sip(self, v, load=False):
    """
    Setter method for src_host_any_sip, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/src_host_any_sip (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_host_any_sip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_host_any_sip() directly.
    """
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 2}, u'any': {'value': 1}},),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),], is_leaf=True, yang_name="src-host-any-sip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_host_any_sip must be of a type compatible with union""",
          'defined-type': "brocade-ip-access-list:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 2}, u'any': {'value': 1}},),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),], is_leaf=True, yang_name="src-host-any-sip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='union', is_config=True)""",
        })

    self.__src_host_any_sip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_host_any_sip(self):
    self.__src_host_any_sip = YANGDynClass(base=[RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 2}, u'any': {'value': 1}},),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),], is_leaf=True, yang_name="src-host-any-sip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='union', is_config=True)


  def _get_src_host_ip(self):
    """
    Getter method for src_host_ip, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/src_host_ip (sip)
    """
    return self.__src_host_ip
      
  def _set_src_host_ip(self, v, load=False):
    """
    Setter method for src_host_ip, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/src_host_ip (sip)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_host_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_host_ip() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-host-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='sip', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_host_ip must be of a type compatible with sip""",
          'defined-type': "brocade-ip-access-list:sip",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-host-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='sip', is_config=True)""",
        })

    self.__src_host_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_host_ip(self):
    self.__src_host_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-host-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='sip', is_config=True)


  def _get_src_mask(self):
    """
    Getter method for src_mask, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/src_mask (sip-mask)
    """
    return self.__src_mask
      
  def _set_src_mask(self, v, load=False):
    """
    Setter method for src_mask, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/src_mask (sip-mask)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_mask is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_mask() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='sip-mask', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_mask must be of a type compatible with sip-mask""",
          'defined-type': "brocade-ip-access-list:sip-mask",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='sip-mask', is_config=True)""",
        })

    self.__src_mask = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_mask(self):
    self.__src_mask = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='sip-mask', is_config=True)


  def _get_count(self):
    """
    Getter method for count, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/count (empty)
    """
    return self.__count
      
  def _set_count(self, v, load=False):
    """
    Setter method for count, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/count (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_count() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Packet count', u'cli-optional-in-sequence': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """count must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Packet count', u'cli-optional-in-sequence': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='empty', is_config=True)""",
        })

    self.__count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_count(self):
    self.__count = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Packet count', u'cli-optional-in-sequence': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='empty', is_config=True)


  def _get_log(self):
    """
    Getter method for log, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/log (empty)
    """
    return self.__log
      
  def _set_log(self, v, load=False):
    """
    Setter method for log, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/log (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Log Packet', u'cli-optional-in-sequence': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Log Packet', u'cli-optional-in-sequence': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='empty', is_config=True)""",
        })

    self.__log = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log(self):
    self.__log = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Log Packet', u'cli-optional-in-sequence': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='empty', is_config=True)


  def _get_copy_sflow(self):
    """
    Getter method for copy_sflow, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/copy_sflow (empty)
    """
    return self.__copy_sflow
      
  def _set_copy_sflow(self, v, load=False):
    """
    Setter method for copy_sflow, mapped from YANG variable /ip_acl/ip/access_list/standard/hide_ip_acl_std/seq/copy_sflow (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_copy_sflow is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_copy_sflow() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="copy-sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-optional-in-sequence': None, u'info': u'Copy to sFlow Collector', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """copy_sflow must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="copy-sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-optional-in-sequence': None, u'info': u'Copy to sFlow Collector', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='empty', is_config=True)""",
        })

    self.__copy_sflow = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_copy_sflow(self):
    self.__copy_sflow = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="copy-sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-optional-in-sequence': None, u'info': u'Copy to sFlow Collector', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='empty', is_config=True)

  seq_id = __builtin__.property(_get_seq_id, _set_seq_id)
  action = __builtin__.property(_get_action, _set_action)
  src_host_any_sip = __builtin__.property(_get_src_host_any_sip, _set_src_host_any_sip)
  src_host_ip = __builtin__.property(_get_src_host_ip, _set_src_host_ip)
  src_mask = __builtin__.property(_get_src_mask, _set_src_mask)
  count = __builtin__.property(_get_count, _set_count)
  log = __builtin__.property(_get_log, _set_log)
  copy_sflow = __builtin__.property(_get_copy_sflow, _set_copy_sflow)


  _pyangbind_elements = {'seq_id': seq_id, 'action': action, 'src_host_any_sip': src_host_any_sip, 'src_host_ip': src_host_ip, 'src_mask': src_mask, 'count': count, 'log': log, 'copy_sflow': copy_sflow, }


