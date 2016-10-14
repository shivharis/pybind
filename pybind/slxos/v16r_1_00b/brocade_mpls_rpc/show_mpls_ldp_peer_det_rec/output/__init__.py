
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-ldp-peer-det-rec/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ldp_peer_id','__ldp_peer_lblspid','__ldp_local_id','__ldp_local_lblspid','__ldp_peer_state','__ldp_peer_session_status','__ldp_entity_index','__ldp_peer_targeted','__ldp_peer_targeted_adj_added',)

  _yang_name = 'output'

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
    self.__ldp_peer_session_status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 0}, u'enable': {'value': 1}},), is_leaf=True, yang_name="ldp-peer-session-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='up-down', is_config=True)
    self.__ldp_local_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__ldp_peer_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-peer-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__ldp_peer_targeted = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-peer-targeted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)
    self.__ldp_local_lblspid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-local-lblspid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_peer_targeted_adj_added = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-peer-targeted-adj-added", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)
    self.__ldp_peer_lblspid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-peer-lblspid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_peer_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Initialized': {'value': 2}, u'OpenSent': {'value': 4}, u'OpenRec': {'value': 3}, u'Nonexistent': {'value': 1}, u'Operational': {'value': 5}},), is_leaf=True, yang_name="ldp-peer-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='ldp-state-name', is_config=True)
    self.__ldp_entity_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-entity-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-ldp-peer-det-rec', u'output']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'show-mpls-ldp-peer-det-rec', u'output']

  def _get_ldp_peer_id(self):
    """
    Getter method for ldp_peer_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_peer_id (inet:ipv4-address)

    YANG Description: Peer LDP ID
    """
    return self.__ldp_peer_id
      
  def _set_ldp_peer_id(self, v, load=False):
    """
    Setter method for ldp_peer_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_peer_id (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_peer_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_peer_id() directly.

    YANG Description: Peer LDP ID
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-peer-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_peer_id must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-peer-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__ldp_peer_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_peer_id(self):
    self.__ldp_peer_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-peer-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_ldp_peer_lblspid(self):
    """
    Getter method for ldp_peer_lblspid, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_peer_lblspid (uint32)

    YANG Description: Peer LBL SPACE ID
    """
    return self.__ldp_peer_lblspid
      
  def _set_ldp_peer_lblspid(self, v, load=False):
    """
    Setter method for ldp_peer_lblspid, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_peer_lblspid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_peer_lblspid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_peer_lblspid() directly.

    YANG Description: Peer LBL SPACE ID
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-peer-lblspid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_peer_lblspid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-peer-lblspid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_peer_lblspid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_peer_lblspid(self):
    self.__ldp_peer_lblspid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-peer-lblspid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_local_id(self):
    """
    Getter method for ldp_local_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_local_id (inet:ipv4-address)

    YANG Description: Local LDP ID
    """
    return self.__ldp_local_id
      
  def _set_ldp_local_id(self, v, load=False):
    """
    Setter method for ldp_local_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_local_id (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_local_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_local_id() directly.

    YANG Description: Local LDP ID
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_local_id must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__ldp_local_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_local_id(self):
    self.__ldp_local_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-local-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_ldp_local_lblspid(self):
    """
    Getter method for ldp_local_lblspid, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_local_lblspid (uint32)

    YANG Description: Peer LBL SPACE ID
    """
    return self.__ldp_local_lblspid
      
  def _set_ldp_local_lblspid(self, v, load=False):
    """
    Setter method for ldp_local_lblspid, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_local_lblspid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_local_lblspid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_local_lblspid() directly.

    YANG Description: Peer LBL SPACE ID
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-local-lblspid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_local_lblspid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-local-lblspid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_local_lblspid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_local_lblspid(self):
    self.__ldp_local_lblspid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-local-lblspid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_peer_state(self):
    """
    Getter method for ldp_peer_state, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_peer_state (ldp-state-name)

    YANG Description: Peer LDP state
    """
    return self.__ldp_peer_state
      
  def _set_ldp_peer_state(self, v, load=False):
    """
    Setter method for ldp_peer_state, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_peer_state (ldp-state-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_peer_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_peer_state() directly.

    YANG Description: Peer LDP state
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Initialized': {'value': 2}, u'OpenSent': {'value': 4}, u'OpenRec': {'value': 3}, u'Nonexistent': {'value': 1}, u'Operational': {'value': 5}},), is_leaf=True, yang_name="ldp-peer-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='ldp-state-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_peer_state must be of a type compatible with ldp-state-name""",
          'defined-type': "brocade-mpls:ldp-state-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Initialized': {'value': 2}, u'OpenSent': {'value': 4}, u'OpenRec': {'value': 3}, u'Nonexistent': {'value': 1}, u'Operational': {'value': 5}},), is_leaf=True, yang_name="ldp-peer-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='ldp-state-name', is_config=True)""",
        })

    self.__ldp_peer_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_peer_state(self):
    self.__ldp_peer_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Initialized': {'value': 2}, u'OpenSent': {'value': 4}, u'OpenRec': {'value': 3}, u'Nonexistent': {'value': 1}, u'Operational': {'value': 5}},), is_leaf=True, yang_name="ldp-peer-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='ldp-state-name', is_config=True)


  def _get_ldp_peer_session_status(self):
    """
    Getter method for ldp_peer_session_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_peer_session_status (up-down)

    YANG Description: LDP session status
    """
    return self.__ldp_peer_session_status
      
  def _set_ldp_peer_session_status(self, v, load=False):
    """
    Setter method for ldp_peer_session_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_peer_session_status (up-down)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_peer_session_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_peer_session_status() directly.

    YANG Description: LDP session status
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 0}, u'enable': {'value': 1}},), is_leaf=True, yang_name="ldp-peer-session-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='up-down', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_peer_session_status must be of a type compatible with up-down""",
          'defined-type': "brocade-mpls:up-down",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 0}, u'enable': {'value': 1}},), is_leaf=True, yang_name="ldp-peer-session-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='up-down', is_config=True)""",
        })

    self.__ldp_peer_session_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_peer_session_status(self):
    self.__ldp_peer_session_status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 0}, u'enable': {'value': 1}},), is_leaf=True, yang_name="ldp-peer-session-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='up-down', is_config=True)


  def _get_ldp_entity_index(self):
    """
    Getter method for ldp_entity_index, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_entity_index (uint32)

    YANG Description: Entity Idx
    """
    return self.__ldp_entity_index
      
  def _set_ldp_entity_index(self, v, load=False):
    """
    Setter method for ldp_entity_index, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_entity_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_entity_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_entity_index() directly.

    YANG Description: Entity Idx
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-entity-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_entity_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-entity-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_entity_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_entity_index(self):
    self.__ldp_entity_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-entity-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_peer_targeted(self):
    """
    Getter method for ldp_peer_targeted, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_peer_targeted (yes-no)

    YANG Description: Targeted
    """
    return self.__ldp_peer_targeted
      
  def _set_ldp_peer_targeted(self, v, load=False):
    """
    Setter method for ldp_peer_targeted, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_peer_targeted (yes-no)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_peer_targeted is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_peer_targeted() directly.

    YANG Description: Targeted
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-peer-targeted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_peer_targeted must be of a type compatible with yes-no""",
          'defined-type': "brocade-mpls:yes-no",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-peer-targeted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)""",
        })

    self.__ldp_peer_targeted = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_peer_targeted(self):
    self.__ldp_peer_targeted = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-peer-targeted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)


  def _get_ldp_peer_targeted_adj_added(self):
    """
    Getter method for ldp_peer_targeted_adj_added, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_peer_targeted_adj_added (yes-no)

    YANG Description: Targeted adjacency added
    """
    return self.__ldp_peer_targeted_adj_added
      
  def _set_ldp_peer_targeted_adj_added(self, v, load=False):
    """
    Setter method for ldp_peer_targeted_adj_added, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det_rec/output/ldp_peer_targeted_adj_added (yes-no)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_peer_targeted_adj_added is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_peer_targeted_adj_added() directly.

    YANG Description: Targeted adjacency added
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-peer-targeted-adj-added", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_peer_targeted_adj_added must be of a type compatible with yes-no""",
          'defined-type': "brocade-mpls:yes-no",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-peer-targeted-adj-added", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)""",
        })

    self.__ldp_peer_targeted_adj_added = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_peer_targeted_adj_added(self):
    self.__ldp_peer_targeted_adj_added = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-peer-targeted-adj-added", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)

  ldp_peer_id = __builtin__.property(_get_ldp_peer_id, _set_ldp_peer_id)
  ldp_peer_lblspid = __builtin__.property(_get_ldp_peer_lblspid, _set_ldp_peer_lblspid)
  ldp_local_id = __builtin__.property(_get_ldp_local_id, _set_ldp_local_id)
  ldp_local_lblspid = __builtin__.property(_get_ldp_local_lblspid, _set_ldp_local_lblspid)
  ldp_peer_state = __builtin__.property(_get_ldp_peer_state, _set_ldp_peer_state)
  ldp_peer_session_status = __builtin__.property(_get_ldp_peer_session_status, _set_ldp_peer_session_status)
  ldp_entity_index = __builtin__.property(_get_ldp_entity_index, _set_ldp_entity_index)
  ldp_peer_targeted = __builtin__.property(_get_ldp_peer_targeted, _set_ldp_peer_targeted)
  ldp_peer_targeted_adj_added = __builtin__.property(_get_ldp_peer_targeted_adj_added, _set_ldp_peer_targeted_adj_added)


  _pyangbind_elements = {'ldp_peer_id': ldp_peer_id, 'ldp_peer_lblspid': ldp_peer_lblspid, 'ldp_local_id': ldp_local_id, 'ldp_local_lblspid': ldp_local_lblspid, 'ldp_peer_state': ldp_peer_state, 'ldp_peer_session_status': ldp_peer_session_status, 'ldp_entity_index': ldp_entity_index, 'ldp_peer_targeted': ldp_peer_targeted, 'ldp_peer_targeted_adj_added': ldp_peer_targeted_adj_added, }


