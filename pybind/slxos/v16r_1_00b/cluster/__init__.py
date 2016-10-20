
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import member_vlan
import peer
import client
class cluster(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mct - based on the path /cluster. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__cluster_name','__cluster_id','__member_vlan','__peer','__client_interfaces_shutdown','__client_isolation_strict','__designated_forwarder_hold_time','__deploy','__client',)

  _yang_name = 'cluster'
  _rest_name = 'cluster'

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
    self.__member_vlan = YANGDynClass(base=member_vlan.member_vlan, is_container='container', yang_name="member-vlan", rest_name="member-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MCT member vlan ', u'cli-suppress-show-conf-path': None, u'cli-suppress-no': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='container', is_config=True)
    self.__deploy = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="deploy", rest_name="deploy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Deploy the Cluster', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)
    self.__designated_forwarder_hold_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..60']}), is_leaf=True, yang_name="designated-forwarder-hold-time", rest_name="designated-forwarder-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time in seconds to wait before electing a designated forwarder (Range:<1-60>, default:3)', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='uint16', is_config=True)
    self.__cluster_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="cluster-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the Cluster (MAX: 64 Characters)', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='common-def:name-string64', is_config=True)
    self.__client_isolation_strict = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="client-isolation-strict", rest_name="client-isolation-strict", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure cluster client isolation mode strict', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)
    self.__cluster_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="cluster-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Id for the Cluster (Range: 1 - 65535', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='uint32', is_config=True)
    self.__client = YANGDynClass(base=YANGListType("client_name client_id",client.client, yang_name="client", rest_name="client", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='client-name client-id', extensions={u'tailf-common': {u'info': u'Cluster Client name for Node Specific configuration', u'cli-full-no': None, u'sort-priority': u'133', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'MctClientCallpoint', u'cli-mode-name': u'config-cluster-client-$(client-id)'}}), is_container='list', yang_name="client", rest_name="client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Cluster Client name for Node Specific configuration', u'cli-full-no': None, u'sort-priority': u'133', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'MctClientCallpoint', u'cli-mode-name': u'config-cluster-client-$(client-id)'}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='list', is_config=True)
    self.__peer = YANGDynClass(base=YANGListType("peer_ip",peer.peer, yang_name="peer", rest_name="peer", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='peer-ip', extensions={u'tailf-common': {u'info': u'Cluster Peer related configuration', u'cli-suppress-mode': None, u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-suppress-show-conf-path': None, u'cli-full-command': None, u'callpoint': u'MctPeerCallpoint'}}), is_container='list', yang_name="peer", rest_name="peer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Cluster Peer related configuration', u'cli-suppress-mode': None, u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-suppress-show-conf-path': None, u'cli-full-command': None, u'callpoint': u'MctPeerCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='list', is_config=True)
    self.__client_interfaces_shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="client-interfaces-shutdown", rest_name="client-interfaces-shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable the cluster client interfaces', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)

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
      return [u'cluster']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cluster']

  def _get_cluster_name(self):
    """
    Getter method for cluster_name, mapped from YANG variable /cluster/cluster_name (common-def:name-string64)

    YANG Description: Name for the Cluster (MAX: 64 Characters)
    """
    return self.__cluster_name
      
  def _set_cluster_name(self, v, load=False):
    """
    Setter method for cluster_name, mapped from YANG variable /cluster/cluster_name (common-def:name-string64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cluster_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cluster_name() directly.

    YANG Description: Name for the Cluster (MAX: 64 Characters)
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="cluster-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the Cluster (MAX: 64 Characters)', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='common-def:name-string64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cluster_name must be of a type compatible with common-def:name-string64""",
          'defined-type': "common-def:name-string64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="cluster-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the Cluster (MAX: 64 Characters)', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='common-def:name-string64', is_config=True)""",
        })

    self.__cluster_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cluster_name(self):
    self.__cluster_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="cluster-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the Cluster (MAX: 64 Characters)', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='common-def:name-string64', is_config=True)


  def _get_cluster_id(self):
    """
    Getter method for cluster_id, mapped from YANG variable /cluster/cluster_id (uint32)
    """
    return self.__cluster_id
      
  def _set_cluster_id(self, v, load=False):
    """
    Setter method for cluster_id, mapped from YANG variable /cluster/cluster_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cluster_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cluster_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="cluster-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Id for the Cluster (Range: 1 - 65535', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cluster_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="cluster-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Id for the Cluster (Range: 1 - 65535', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='uint32', is_config=True)""",
        })

    self.__cluster_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cluster_id(self):
    self.__cluster_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="cluster-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Id for the Cluster (Range: 1 - 65535', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='uint32', is_config=True)


  def _get_member_vlan(self):
    """
    Getter method for member_vlan, mapped from YANG variable /cluster/member_vlan (container)

    YANG Description: Member vlan's part of the  MCT .
    """
    return self.__member_vlan
      
  def _set_member_vlan(self, v, load=False):
    """
    Setter method for member_vlan, mapped from YANG variable /cluster/member_vlan (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_member_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_member_vlan() directly.

    YANG Description: Member vlan's part of the  MCT .
    """
    try:
      t = YANGDynClass(v,base=member_vlan.member_vlan, is_container='container', yang_name="member-vlan", rest_name="member-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MCT member vlan ', u'cli-suppress-show-conf-path': None, u'cli-suppress-no': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """member_vlan must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=member_vlan.member_vlan, is_container='container', yang_name="member-vlan", rest_name="member-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MCT member vlan ', u'cli-suppress-show-conf-path': None, u'cli-suppress-no': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='container', is_config=True)""",
        })

    self.__member_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_member_vlan(self):
    self.__member_vlan = YANGDynClass(base=member_vlan.member_vlan, is_container='container', yang_name="member-vlan", rest_name="member-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MCT member vlan ', u'cli-suppress-show-conf-path': None, u'cli-suppress-no': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='container', is_config=True)


  def _get_peer(self):
    """
    Getter method for peer, mapped from YANG variable /cluster/peer (list)
    """
    return self.__peer
      
  def _set_peer(self, v, load=False):
    """
    Setter method for peer, mapped from YANG variable /cluster/peer (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("peer_ip",peer.peer, yang_name="peer", rest_name="peer", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='peer-ip', extensions={u'tailf-common': {u'info': u'Cluster Peer related configuration', u'cli-suppress-mode': None, u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-suppress-show-conf-path': None, u'cli-full-command': None, u'callpoint': u'MctPeerCallpoint'}}), is_container='list', yang_name="peer", rest_name="peer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Cluster Peer related configuration', u'cli-suppress-mode': None, u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-suppress-show-conf-path': None, u'cli-full-command': None, u'callpoint': u'MctPeerCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("peer_ip",peer.peer, yang_name="peer", rest_name="peer", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='peer-ip', extensions={u'tailf-common': {u'info': u'Cluster Peer related configuration', u'cli-suppress-mode': None, u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-suppress-show-conf-path': None, u'cli-full-command': None, u'callpoint': u'MctPeerCallpoint'}}), is_container='list', yang_name="peer", rest_name="peer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Cluster Peer related configuration', u'cli-suppress-mode': None, u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-suppress-show-conf-path': None, u'cli-full-command': None, u'callpoint': u'MctPeerCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='list', is_config=True)""",
        })

    self.__peer = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer(self):
    self.__peer = YANGDynClass(base=YANGListType("peer_ip",peer.peer, yang_name="peer", rest_name="peer", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='peer-ip', extensions={u'tailf-common': {u'info': u'Cluster Peer related configuration', u'cli-suppress-mode': None, u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-suppress-show-conf-path': None, u'cli-full-command': None, u'callpoint': u'MctPeerCallpoint'}}), is_container='list', yang_name="peer", rest_name="peer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Cluster Peer related configuration', u'cli-suppress-mode': None, u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-suppress-show-conf-path': None, u'cli-full-command': None, u'callpoint': u'MctPeerCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='list', is_config=True)


  def _get_client_interfaces_shutdown(self):
    """
    Getter method for client_interfaces_shutdown, mapped from YANG variable /cluster/client_interfaces_shutdown (empty)
    """
    return self.__client_interfaces_shutdown
      
  def _set_client_interfaces_shutdown(self, v, load=False):
    """
    Setter method for client_interfaces_shutdown, mapped from YANG variable /cluster/client_interfaces_shutdown (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_interfaces_shutdown is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_interfaces_shutdown() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="client-interfaces-shutdown", rest_name="client-interfaces-shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable the cluster client interfaces', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_interfaces_shutdown must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="client-interfaces-shutdown", rest_name="client-interfaces-shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable the cluster client interfaces', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)""",
        })

    self.__client_interfaces_shutdown = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_interfaces_shutdown(self):
    self.__client_interfaces_shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="client-interfaces-shutdown", rest_name="client-interfaces-shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable the cluster client interfaces', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)


  def _get_client_isolation_strict(self):
    """
    Getter method for client_isolation_strict, mapped from YANG variable /cluster/client_isolation_strict (empty)
    """
    return self.__client_isolation_strict
      
  def _set_client_isolation_strict(self, v, load=False):
    """
    Setter method for client_isolation_strict, mapped from YANG variable /cluster/client_isolation_strict (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_isolation_strict is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_isolation_strict() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="client-isolation-strict", rest_name="client-isolation-strict", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure cluster client isolation mode strict', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_isolation_strict must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="client-isolation-strict", rest_name="client-isolation-strict", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure cluster client isolation mode strict', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)""",
        })

    self.__client_isolation_strict = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_isolation_strict(self):
    self.__client_isolation_strict = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="client-isolation-strict", rest_name="client-isolation-strict", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure cluster client isolation mode strict', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)


  def _get_designated_forwarder_hold_time(self):
    """
    Getter method for designated_forwarder_hold_time, mapped from YANG variable /cluster/designated_forwarder_hold_time (uint16)
    """
    return self.__designated_forwarder_hold_time
      
  def _set_designated_forwarder_hold_time(self, v, load=False):
    """
    Setter method for designated_forwarder_hold_time, mapped from YANG variable /cluster/designated_forwarder_hold_time (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_designated_forwarder_hold_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_designated_forwarder_hold_time() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..60']}), is_leaf=True, yang_name="designated-forwarder-hold-time", rest_name="designated-forwarder-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time in seconds to wait before electing a designated forwarder (Range:<1-60>, default:3)', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """designated_forwarder_hold_time must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..60']}), is_leaf=True, yang_name="designated-forwarder-hold-time", rest_name="designated-forwarder-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time in seconds to wait before electing a designated forwarder (Range:<1-60>, default:3)', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='uint16', is_config=True)""",
        })

    self.__designated_forwarder_hold_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_designated_forwarder_hold_time(self):
    self.__designated_forwarder_hold_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..60']}), is_leaf=True, yang_name="designated-forwarder-hold-time", rest_name="designated-forwarder-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time in seconds to wait before electing a designated forwarder (Range:<1-60>, default:3)', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='uint16', is_config=True)


  def _get_deploy(self):
    """
    Getter method for deploy, mapped from YANG variable /cluster/deploy (empty)
    """
    return self.__deploy
      
  def _set_deploy(self, v, load=False):
    """
    Setter method for deploy, mapped from YANG variable /cluster/deploy (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_deploy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_deploy() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="deploy", rest_name="deploy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Deploy the Cluster', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """deploy must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="deploy", rest_name="deploy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Deploy the Cluster', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)""",
        })

    self.__deploy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_deploy(self):
    self.__deploy = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="deploy", rest_name="deploy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Deploy the Cluster', u'cli-suppress-show-conf-path': None, u'cli-suppress-show-match': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='empty', is_config=True)


  def _get_client(self):
    """
    Getter method for client, mapped from YANG variable /cluster/client (list)
    """
    return self.__client
      
  def _set_client(self, v, load=False):
    """
    Setter method for client, mapped from YANG variable /cluster/client (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("client_name client_id",client.client, yang_name="client", rest_name="client", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='client-name client-id', extensions={u'tailf-common': {u'info': u'Cluster Client name for Node Specific configuration', u'cli-full-no': None, u'sort-priority': u'133', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'MctClientCallpoint', u'cli-mode-name': u'config-cluster-client-$(client-id)'}}), is_container='list', yang_name="client", rest_name="client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Cluster Client name for Node Specific configuration', u'cli-full-no': None, u'sort-priority': u'133', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'MctClientCallpoint', u'cli-mode-name': u'config-cluster-client-$(client-id)'}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("client_name client_id",client.client, yang_name="client", rest_name="client", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='client-name client-id', extensions={u'tailf-common': {u'info': u'Cluster Client name for Node Specific configuration', u'cli-full-no': None, u'sort-priority': u'133', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'MctClientCallpoint', u'cli-mode-name': u'config-cluster-client-$(client-id)'}}), is_container='list', yang_name="client", rest_name="client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Cluster Client name for Node Specific configuration', u'cli-full-no': None, u'sort-priority': u'133', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'MctClientCallpoint', u'cli-mode-name': u'config-cluster-client-$(client-id)'}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='list', is_config=True)""",
        })

    self.__client = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client(self):
    self.__client = YANGDynClass(base=YANGListType("client_name client_id",client.client, yang_name="client", rest_name="client", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='client-name client-id', extensions={u'tailf-common': {u'info': u'Cluster Client name for Node Specific configuration', u'cli-full-no': None, u'sort-priority': u'133', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'MctClientCallpoint', u'cli-mode-name': u'config-cluster-client-$(client-id)'}}), is_container='list', yang_name="client", rest_name="client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Cluster Client name for Node Specific configuration', u'cli-full-no': None, u'sort-priority': u'133', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'MctClientCallpoint', u'cli-mode-name': u'config-cluster-client-$(client-id)'}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='list', is_config=True)

  cluster_name = __builtin__.property(_get_cluster_name, _set_cluster_name)
  cluster_id = __builtin__.property(_get_cluster_id, _set_cluster_id)
  member_vlan = __builtin__.property(_get_member_vlan, _set_member_vlan)
  peer = __builtin__.property(_get_peer, _set_peer)
  client_interfaces_shutdown = __builtin__.property(_get_client_interfaces_shutdown, _set_client_interfaces_shutdown)
  client_isolation_strict = __builtin__.property(_get_client_isolation_strict, _set_client_isolation_strict)
  designated_forwarder_hold_time = __builtin__.property(_get_designated_forwarder_hold_time, _set_designated_forwarder_hold_time)
  deploy = __builtin__.property(_get_deploy, _set_deploy)
  client = __builtin__.property(_get_client, _set_client)


  _pyangbind_elements = {'cluster_name': cluster_name, 'cluster_id': cluster_id, 'member_vlan': member_vlan, 'peer': peer, 'client_interfaces_shutdown': client_interfaces_shutdown, 'client_isolation_strict': client_isolation_strict, 'designated_forwarder_hold_time': designated_forwarder_hold_time, 'deploy': deploy, 'client': client, }


