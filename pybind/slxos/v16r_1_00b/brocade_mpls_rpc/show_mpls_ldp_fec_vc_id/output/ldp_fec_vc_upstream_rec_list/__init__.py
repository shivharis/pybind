
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ldp_fec_vc_upstream_rec_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-ldp-fec-vc-id/output/ldp-fec-vc-upstream-rec-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ldp_fec_vc_local_ldp_id_up','__ldp_fec_vc_local_ldp_lblspc_up','__ldp_fec_vc_peer_ldp_id_up','__ldp_fec_vc_peer_ldp_lblspc_up','__ldp_fec_vc_label_up','__ldp_fec_vc_feccb_up','__ldp_fec_vc_fec_um_state_dw',)

  _yang_name = 'ldp-fec-vc-upstream-rec-list'

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
    self.__ldp_fec_vc_peer_ldp_id_up = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-vc-peer-ldp-id-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__ldp_fec_vc_label_up = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-label-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_fec_vc_fec_um_state_dw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-fec-um-state-dw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='int32', is_config=True)
    self.__ldp_fec_vc_feccb_up = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-feccb-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_fec_vc_local_ldp_id_up = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-vc-local-ldp-id-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__ldp_fec_vc_peer_ldp_lblspc_up = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-peer-ldp-lblspc-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_fec_vc_local_ldp_lblspc_up = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-local-ldp-lblspc-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-ldp-fec-vc-id', u'output', u'ldp-fec-vc-upstream-rec-list']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'show-mpls-ldp-fec-vc-id', u'output', u'ldp-fec-vc-upstream-rec-list']

  def _get_ldp_fec_vc_local_ldp_id_up(self):
    """
    Getter method for ldp_fec_vc_local_ldp_id_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc_id/output/ldp_fec_vc_upstream_rec_list/ldp_fec_vc_local_ldp_id_up (inet:ipv4-address)

    YANG Description: Local LDP ID
    """
    return self.__ldp_fec_vc_local_ldp_id_up
      
  def _set_ldp_fec_vc_local_ldp_id_up(self, v, load=False):
    """
    Setter method for ldp_fec_vc_local_ldp_id_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc_id/output/ldp_fec_vc_upstream_rec_list/ldp_fec_vc_local_ldp_id_up (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_vc_local_ldp_id_up is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_vc_local_ldp_id_up() directly.

    YANG Description: Local LDP ID
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-vc-local-ldp-id-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_vc_local_ldp_id_up must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-vc-local-ldp-id-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__ldp_fec_vc_local_ldp_id_up = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_vc_local_ldp_id_up(self):
    self.__ldp_fec_vc_local_ldp_id_up = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-vc-local-ldp-id-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_ldp_fec_vc_local_ldp_lblspc_up(self):
    """
    Getter method for ldp_fec_vc_local_ldp_lblspc_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc_id/output/ldp_fec_vc_upstream_rec_list/ldp_fec_vc_local_ldp_lblspc_up (uint32)

    YANG Description: Local LDP Label Space
    """
    return self.__ldp_fec_vc_local_ldp_lblspc_up
      
  def _set_ldp_fec_vc_local_ldp_lblspc_up(self, v, load=False):
    """
    Setter method for ldp_fec_vc_local_ldp_lblspc_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc_id/output/ldp_fec_vc_upstream_rec_list/ldp_fec_vc_local_ldp_lblspc_up (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_vc_local_ldp_lblspc_up is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_vc_local_ldp_lblspc_up() directly.

    YANG Description: Local LDP Label Space
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-local-ldp-lblspc-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_vc_local_ldp_lblspc_up must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-local-ldp-lblspc-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_fec_vc_local_ldp_lblspc_up = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_vc_local_ldp_lblspc_up(self):
    self.__ldp_fec_vc_local_ldp_lblspc_up = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-local-ldp-lblspc-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_fec_vc_peer_ldp_id_up(self):
    """
    Getter method for ldp_fec_vc_peer_ldp_id_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc_id/output/ldp_fec_vc_upstream_rec_list/ldp_fec_vc_peer_ldp_id_up (inet:ipv4-address)

    YANG Description: Peer LDP ID
    """
    return self.__ldp_fec_vc_peer_ldp_id_up
      
  def _set_ldp_fec_vc_peer_ldp_id_up(self, v, load=False):
    """
    Setter method for ldp_fec_vc_peer_ldp_id_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc_id/output/ldp_fec_vc_upstream_rec_list/ldp_fec_vc_peer_ldp_id_up (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_vc_peer_ldp_id_up is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_vc_peer_ldp_id_up() directly.

    YANG Description: Peer LDP ID
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-vc-peer-ldp-id-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_vc_peer_ldp_id_up must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-vc-peer-ldp-id-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__ldp_fec_vc_peer_ldp_id_up = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_vc_peer_ldp_id_up(self):
    self.__ldp_fec_vc_peer_ldp_id_up = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-vc-peer-ldp-id-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_ldp_fec_vc_peer_ldp_lblspc_up(self):
    """
    Getter method for ldp_fec_vc_peer_ldp_lblspc_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc_id/output/ldp_fec_vc_upstream_rec_list/ldp_fec_vc_peer_ldp_lblspc_up (uint32)

    YANG Description: Peer LDP Label Space
    """
    return self.__ldp_fec_vc_peer_ldp_lblspc_up
      
  def _set_ldp_fec_vc_peer_ldp_lblspc_up(self, v, load=False):
    """
    Setter method for ldp_fec_vc_peer_ldp_lblspc_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc_id/output/ldp_fec_vc_upstream_rec_list/ldp_fec_vc_peer_ldp_lblspc_up (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_vc_peer_ldp_lblspc_up is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_vc_peer_ldp_lblspc_up() directly.

    YANG Description: Peer LDP Label Space
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-peer-ldp-lblspc-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_vc_peer_ldp_lblspc_up must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-peer-ldp-lblspc-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_fec_vc_peer_ldp_lblspc_up = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_vc_peer_ldp_lblspc_up(self):
    self.__ldp_fec_vc_peer_ldp_lblspc_up = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-peer-ldp-lblspc-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_fec_vc_label_up(self):
    """
    Getter method for ldp_fec_vc_label_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc_id/output/ldp_fec_vc_upstream_rec_list/ldp_fec_vc_label_up (uint32)

    YANG Description: Label
    """
    return self.__ldp_fec_vc_label_up
      
  def _set_ldp_fec_vc_label_up(self, v, load=False):
    """
    Setter method for ldp_fec_vc_label_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc_id/output/ldp_fec_vc_upstream_rec_list/ldp_fec_vc_label_up (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_vc_label_up is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_vc_label_up() directly.

    YANG Description: Label
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-label-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_vc_label_up must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-label-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_fec_vc_label_up = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_vc_label_up(self):
    self.__ldp_fec_vc_label_up = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-label-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_fec_vc_feccb_up(self):
    """
    Getter method for ldp_fec_vc_feccb_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc_id/output/ldp_fec_vc_upstream_rec_list/ldp_fec_vc_feccb_up (uint32)

    YANG Description: CB
    """
    return self.__ldp_fec_vc_feccb_up
      
  def _set_ldp_fec_vc_feccb_up(self, v, load=False):
    """
    Setter method for ldp_fec_vc_feccb_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc_id/output/ldp_fec_vc_upstream_rec_list/ldp_fec_vc_feccb_up (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_vc_feccb_up is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_vc_feccb_up() directly.

    YANG Description: CB
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-feccb-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_vc_feccb_up must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-feccb-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_fec_vc_feccb_up = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_vc_feccb_up(self):
    self.__ldp_fec_vc_feccb_up = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-feccb-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_fec_vc_fec_um_state_dw(self):
    """
    Getter method for ldp_fec_vc_fec_um_state_dw, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc_id/output/ldp_fec_vc_upstream_rec_list/ldp_fec_vc_fec_um_state_dw (int32)

    YANG Description: UM State
    """
    return self.__ldp_fec_vc_fec_um_state_dw
      
  def _set_ldp_fec_vc_fec_um_state_dw(self, v, load=False):
    """
    Setter method for ldp_fec_vc_fec_um_state_dw, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc_id/output/ldp_fec_vc_upstream_rec_list/ldp_fec_vc_fec_um_state_dw (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_vc_fec_um_state_dw is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_vc_fec_um_state_dw() directly.

    YANG Description: UM State
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-fec-um-state-dw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_vc_fec_um_state_dw must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-fec-um-state-dw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='int32', is_config=True)""",
        })

    self.__ldp_fec_vc_fec_um_state_dw = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_vc_fec_um_state_dw(self):
    self.__ldp_fec_vc_fec_um_state_dw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-fec-um-state-dw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='int32', is_config=True)

  ldp_fec_vc_local_ldp_id_up = __builtin__.property(_get_ldp_fec_vc_local_ldp_id_up, _set_ldp_fec_vc_local_ldp_id_up)
  ldp_fec_vc_local_ldp_lblspc_up = __builtin__.property(_get_ldp_fec_vc_local_ldp_lblspc_up, _set_ldp_fec_vc_local_ldp_lblspc_up)
  ldp_fec_vc_peer_ldp_id_up = __builtin__.property(_get_ldp_fec_vc_peer_ldp_id_up, _set_ldp_fec_vc_peer_ldp_id_up)
  ldp_fec_vc_peer_ldp_lblspc_up = __builtin__.property(_get_ldp_fec_vc_peer_ldp_lblspc_up, _set_ldp_fec_vc_peer_ldp_lblspc_up)
  ldp_fec_vc_label_up = __builtin__.property(_get_ldp_fec_vc_label_up, _set_ldp_fec_vc_label_up)
  ldp_fec_vc_feccb_up = __builtin__.property(_get_ldp_fec_vc_feccb_up, _set_ldp_fec_vc_feccb_up)
  ldp_fec_vc_fec_um_state_dw = __builtin__.property(_get_ldp_fec_vc_fec_um_state_dw, _set_ldp_fec_vc_fec_um_state_dw)


  _pyangbind_elements = {'ldp_fec_vc_local_ldp_id_up': ldp_fec_vc_local_ldp_id_up, 'ldp_fec_vc_local_ldp_lblspc_up': ldp_fec_vc_local_ldp_lblspc_up, 'ldp_fec_vc_peer_ldp_id_up': ldp_fec_vc_peer_ldp_id_up, 'ldp_fec_vc_peer_ldp_lblspc_up': ldp_fec_vc_peer_ldp_lblspc_up, 'ldp_fec_vc_label_up': ldp_fec_vc_label_up, 'ldp_fec_vc_feccb_up': ldp_fec_vc_feccb_up, 'ldp_fec_vc_fec_um_state_dw': ldp_fec_vc_fec_um_state_dw, }


