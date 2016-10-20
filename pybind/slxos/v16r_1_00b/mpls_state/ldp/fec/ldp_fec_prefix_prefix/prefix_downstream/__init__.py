
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class prefix_downstream(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/fec/ldp-fec-prefix-prefix/prefix-downstream. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__local_ldp_id','__local_ldp_lblspc','__peer_ldp_id','__peer_ldp_lblspc','__label','__state','__fec_filtered_state','__fec_stale','__feccb','__fec_dm_state_dw',)

  _yang_name = 'prefix-downstream'
  _rest_name = 'prefix-downstream'

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
    self.__local_ldp_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="local-ldp-id", rest_name="local-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__fec_filtered_state = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fec-filtered-state", rest_name="fec-filtered-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__fec_stale = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fec-stale", rest_name="fec-stale", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="label", rest_name="label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__peer_ldp_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="peer-ldp-id", rest_name="peer-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__state = YANGDynClass(base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__feccb = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="feccb", rest_name="feccb", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__peer_ldp_lblspc = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-ldp-lblspc", rest_name="peer-ldp-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__local_ldp_lblspc = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-ldp-lblspc", rest_name="local-ldp-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__fec_dm_state_dw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fec-dm-state-dw", rest_name="fec-dm-state-dw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

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
      return [u'mpls-state', u'ldp', u'fec', u'ldp-fec-prefix-prefix', u'prefix-downstream']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'ldp', u'fec', u'ldp-fec-prefix-prefix', u'prefix-downstream']

  def _get_local_ldp_id(self):
    """
    Getter method for local_ldp_id, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/local_ldp_id (inet:ipv4-address)

    YANG Description: prefix_local_ldp_id_dw
    """
    return self.__local_ldp_id
      
  def _set_local_ldp_id(self, v, load=False):
    """
    Setter method for local_ldp_id, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/local_ldp_id (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_ldp_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_ldp_id() directly.

    YANG Description: prefix_local_ldp_id_dw
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="local-ldp-id", rest_name="local-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_ldp_id must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="local-ldp-id", rest_name="local-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__local_ldp_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_ldp_id(self):
    self.__local_ldp_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="local-ldp-id", rest_name="local-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_local_ldp_lblspc(self):
    """
    Getter method for local_ldp_lblspc, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/local_ldp_lblspc (uint32)

    YANG Description: prefix_local_ldp_lblspc_dw
    """
    return self.__local_ldp_lblspc
      
  def _set_local_ldp_lblspc(self, v, load=False):
    """
    Setter method for local_ldp_lblspc, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/local_ldp_lblspc (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_ldp_lblspc is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_ldp_lblspc() directly.

    YANG Description: prefix_local_ldp_lblspc_dw
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-ldp-lblspc", rest_name="local-ldp-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_ldp_lblspc must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-ldp-lblspc", rest_name="local-ldp-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__local_ldp_lblspc = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_ldp_lblspc(self):
    self.__local_ldp_lblspc = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-ldp-lblspc", rest_name="local-ldp-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_peer_ldp_id(self):
    """
    Getter method for peer_ldp_id, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/peer_ldp_id (inet:ipv4-address)

    YANG Description: prefix_peer_ldp_id_dw
    """
    return self.__peer_ldp_id
      
  def _set_peer_ldp_id(self, v, load=False):
    """
    Setter method for peer_ldp_id, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/peer_ldp_id (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_ldp_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_ldp_id() directly.

    YANG Description: prefix_peer_ldp_id_dw
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="peer-ldp-id", rest_name="peer-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_ldp_id must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="peer-ldp-id", rest_name="peer-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__peer_ldp_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_ldp_id(self):
    self.__peer_ldp_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="peer-ldp-id", rest_name="peer-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_peer_ldp_lblspc(self):
    """
    Getter method for peer_ldp_lblspc, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/peer_ldp_lblspc (uint32)

    YANG Description: prefix_peer_ldp_lblspc_dw
    """
    return self.__peer_ldp_lblspc
      
  def _set_peer_ldp_lblspc(self, v, load=False):
    """
    Setter method for peer_ldp_lblspc, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/peer_ldp_lblspc (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_ldp_lblspc is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_ldp_lblspc() directly.

    YANG Description: prefix_peer_ldp_lblspc_dw
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-ldp-lblspc", rest_name="peer-ldp-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_ldp_lblspc must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-ldp-lblspc", rest_name="peer-ldp-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__peer_ldp_lblspc = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_ldp_lblspc(self):
    self.__peer_ldp_lblspc = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-ldp-lblspc", rest_name="peer-ldp-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_label(self):
    """
    Getter method for label, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/label (uint32)

    YANG Description: prefix_label_dw
    """
    return self.__label
      
  def _set_label(self, v, load=False):
    """
    Setter method for label, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/label (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_label() directly.

    YANG Description: prefix_label_dw
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="label", rest_name="label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """label must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="label", rest_name="label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_label(self):
    self.__label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="label", rest_name="label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/state (string)

    YANG Description: prefix state dw
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/state (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: prefix state dw
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_fec_filtered_state(self):
    """
    Getter method for fec_filtered_state, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/fec_filtered_state (uint32)

    YANG Description: fec_prefix_fec_filtered_state_dw
    """
    return self.__fec_filtered_state
      
  def _set_fec_filtered_state(self, v, load=False):
    """
    Setter method for fec_filtered_state, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/fec_filtered_state (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fec_filtered_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fec_filtered_state() directly.

    YANG Description: fec_prefix_fec_filtered_state_dw
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fec-filtered-state", rest_name="fec-filtered-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fec_filtered_state must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fec-filtered-state", rest_name="fec-filtered-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__fec_filtered_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fec_filtered_state(self):
    self.__fec_filtered_state = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fec-filtered-state", rest_name="fec-filtered-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_fec_stale(self):
    """
    Getter method for fec_stale, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/fec_stale (uint32)

    YANG Description: prefix_fec_stale_dw
    """
    return self.__fec_stale
      
  def _set_fec_stale(self, v, load=False):
    """
    Setter method for fec_stale, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/fec_stale (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fec_stale is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fec_stale() directly.

    YANG Description: prefix_fec_stale_dw
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fec-stale", rest_name="fec-stale", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fec_stale must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fec-stale", rest_name="fec-stale", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__fec_stale = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fec_stale(self):
    self.__fec_stale = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fec-stale", rest_name="fec-stale", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_feccb(self):
    """
    Getter method for feccb, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/feccb (uint32)

    YANG Description: prefix_feccb_dw
    """
    return self.__feccb
      
  def _set_feccb(self, v, load=False):
    """
    Setter method for feccb, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/feccb (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_feccb is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_feccb() directly.

    YANG Description: prefix_feccb_dw
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="feccb", rest_name="feccb", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """feccb must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="feccb", rest_name="feccb", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__feccb = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_feccb(self):
    self.__feccb = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="feccb", rest_name="feccb", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_fec_dm_state_dw(self):
    """
    Getter method for fec_dm_state_dw, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/fec_dm_state_dw (uint32)

    YANG Description: prefix_fec_dm_state_dw
    """
    return self.__fec_dm_state_dw
      
  def _set_fec_dm_state_dw(self, v, load=False):
    """
    Setter method for fec_dm_state_dw, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_downstream/fec_dm_state_dw (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fec_dm_state_dw is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fec_dm_state_dw() directly.

    YANG Description: prefix_fec_dm_state_dw
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fec-dm-state-dw", rest_name="fec-dm-state-dw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fec_dm_state_dw must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fec-dm-state-dw", rest_name="fec-dm-state-dw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__fec_dm_state_dw = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fec_dm_state_dw(self):
    self.__fec_dm_state_dw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fec-dm-state-dw", rest_name="fec-dm-state-dw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

  local_ldp_id = __builtin__.property(_get_local_ldp_id)
  local_ldp_lblspc = __builtin__.property(_get_local_ldp_lblspc)
  peer_ldp_id = __builtin__.property(_get_peer_ldp_id)
  peer_ldp_lblspc = __builtin__.property(_get_peer_ldp_lblspc)
  label = __builtin__.property(_get_label)
  state = __builtin__.property(_get_state)
  fec_filtered_state = __builtin__.property(_get_fec_filtered_state)
  fec_stale = __builtin__.property(_get_fec_stale)
  feccb = __builtin__.property(_get_feccb)
  fec_dm_state_dw = __builtin__.property(_get_fec_dm_state_dw)


  _pyangbind_elements = {'local_ldp_id': local_ldp_id, 'local_ldp_lblspc': local_ldp_lblspc, 'peer_ldp_id': peer_ldp_id, 'peer_ldp_lblspc': peer_ldp_lblspc, 'label': label, 'state': state, 'fec_filtered_state': fec_filtered_state, 'fec_stale': fec_stale, 'feccb': feccb, 'fec_dm_state_dw': fec_dm_state_dw, }


