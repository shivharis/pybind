
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class path_insert(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/path/path-insert. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__path_insert_ip','__path_insert_type','__path_insert_before_hop_ip',)

  _yang_name = 'path-insert'
  _rest_name = 'insert'

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
    self.__path_insert_before_hop_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="path-insert-before-hop-ip", rest_name="before", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'add before hop ip address', u'cli-full-command': None, u'alt-name': u'before', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__path_insert_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'strict': {'value': 1}, u'loose': {'value': 2}},), is_leaf=True, yang_name="path-insert-type", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'path hop type', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='strict-loose-hop', is_config=True)
    self.__path_insert_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="path-insert-ip", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D;;path hop ip address', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'path', u'path-insert']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'mpls', u'path', u'insert']

  def _get_path_insert_ip(self):
    """
    Getter method for path_insert_ip, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/path/path_insert/path_insert_ip (inet:ipv4-address)
    """
    return self.__path_insert_ip
      
  def _set_path_insert_ip(self, v, load=False):
    """
    Setter method for path_insert_ip, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/path/path_insert/path_insert_ip (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_insert_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_insert_ip() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="path-insert-ip", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D;;path hop ip address', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_insert_ip must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="path-insert-ip", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D;;path hop ip address', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__path_insert_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_insert_ip(self):
    self.__path_insert_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="path-insert-ip", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D;;path hop ip address', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_path_insert_type(self):
    """
    Getter method for path_insert_type, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/path/path_insert/path_insert_type (strict-loose-hop)
    """
    return self.__path_insert_type
      
  def _set_path_insert_type(self, v, load=False):
    """
    Setter method for path_insert_type, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/path/path_insert/path_insert_type (strict-loose-hop)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_insert_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_insert_type() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'strict': {'value': 1}, u'loose': {'value': 2}},), is_leaf=True, yang_name="path-insert-type", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'path hop type', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='strict-loose-hop', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_insert_type must be of a type compatible with strict-loose-hop""",
          'defined-type': "brocade-mpls:strict-loose-hop",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'strict': {'value': 1}, u'loose': {'value': 2}},), is_leaf=True, yang_name="path-insert-type", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'path hop type', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='strict-loose-hop', is_config=True)""",
        })

    self.__path_insert_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_insert_type(self):
    self.__path_insert_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'strict': {'value': 1}, u'loose': {'value': 2}},), is_leaf=True, yang_name="path-insert-type", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'path hop type', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='strict-loose-hop', is_config=True)


  def _get_path_insert_before_hop_ip(self):
    """
    Getter method for path_insert_before_hop_ip, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/path/path_insert/path_insert_before_hop_ip (inet:ipv4-address)
    """
    return self.__path_insert_before_hop_ip
      
  def _set_path_insert_before_hop_ip(self, v, load=False):
    """
    Setter method for path_insert_before_hop_ip, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/path/path_insert/path_insert_before_hop_ip (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_insert_before_hop_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_insert_before_hop_ip() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="path-insert-before-hop-ip", rest_name="before", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'add before hop ip address', u'cli-full-command': None, u'alt-name': u'before', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_insert_before_hop_ip must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="path-insert-before-hop-ip", rest_name="before", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'add before hop ip address', u'cli-full-command': None, u'alt-name': u'before', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__path_insert_before_hop_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_insert_before_hop_ip(self):
    self.__path_insert_before_hop_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="path-insert-before-hop-ip", rest_name="before", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'add before hop ip address', u'cli-full-command': None, u'alt-name': u'before', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)

  path_insert_ip = __builtin__.property(_get_path_insert_ip, _set_path_insert_ip)
  path_insert_type = __builtin__.property(_get_path_insert_type, _set_path_insert_type)
  path_insert_before_hop_ip = __builtin__.property(_get_path_insert_before_hop_ip, _set_path_insert_before_hop_ip)


  _pyangbind_elements = {'path_insert_ip': path_insert_ip, 'path_insert_type': path_insert_type, 'path_insert_before_hop_ip': path_insert_before_hop_ip, }


