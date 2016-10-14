
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class igmps_prefix_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-igmp-snooping - based on the path /igmp-snooping/ip/igmp/ssm-map/igmps-prefix-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__igmps_prefix_list_name','__igmps_prefix_src_addr',)

  _yang_name = 'igmps-prefix-list'

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
    self.__igmps_prefix_src_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="igmps-prefix-src-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D     Source address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='inet:ipv4-address', is_config=True)
    self.__igmps_prefix_list_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="igmps-prefix-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASCII string    Access-list name or number'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='string', is_config=True)

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
      return [u'igmp-snooping', u'ip', u'igmp', u'ssm-map', u'igmps-prefix-list']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'ip', u'igmp', u'ssm-map']

  def _get_igmps_prefix_list_name(self):
    """
    Getter method for igmps_prefix_list_name, mapped from YANG variable /igmp_snooping/ip/igmp/ssm_map/igmps_prefix_list/igmps_prefix_list_name (string)
    """
    return self.__igmps_prefix_list_name
      
  def _set_igmps_prefix_list_name(self, v, load=False):
    """
    Setter method for igmps_prefix_list_name, mapped from YANG variable /igmp_snooping/ip/igmp/ssm_map/igmps_prefix_list/igmps_prefix_list_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_prefix_list_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_prefix_list_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="igmps-prefix-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASCII string    Access-list name or number'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_prefix_list_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="igmps-prefix-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASCII string    Access-list name or number'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='string', is_config=True)""",
        })

    self.__igmps_prefix_list_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_prefix_list_name(self):
    self.__igmps_prefix_list_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="igmps-prefix-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASCII string    Access-list name or number'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='string', is_config=True)


  def _get_igmps_prefix_src_addr(self):
    """
    Getter method for igmps_prefix_src_addr, mapped from YANG variable /igmp_snooping/ip/igmp/ssm_map/igmps_prefix_list/igmps_prefix_src_addr (inet:ipv4-address)
    """
    return self.__igmps_prefix_src_addr
      
  def _set_igmps_prefix_src_addr(self, v, load=False):
    """
    Setter method for igmps_prefix_src_addr, mapped from YANG variable /igmp_snooping/ip/igmp/ssm_map/igmps_prefix_list/igmps_prefix_src_addr (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmps_prefix_src_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmps_prefix_src_addr() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="igmps-prefix-src-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D     Source address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmps_prefix_src_addr must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="igmps-prefix-src-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D     Source address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__igmps_prefix_src_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmps_prefix_src_addr(self):
    self.__igmps_prefix_src_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="igmps-prefix-src-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D     Source address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='inet:ipv4-address', is_config=True)

  igmps_prefix_list_name = __builtin__.property(_get_igmps_prefix_list_name, _set_igmps_prefix_list_name)
  igmps_prefix_src_addr = __builtin__.property(_get_igmps_prefix_src_addr, _set_igmps_prefix_src_addr)


  _pyangbind_elements = {'igmps_prefix_list_name': igmps_prefix_list_name, 'igmps_prefix_src_addr': igmps_prefix_src_addr, }


