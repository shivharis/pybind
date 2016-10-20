
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import tunnel_dst
import extend
import mac_learning
import bfd
class site(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tunnels - based on the path /overlay-gateway/site. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Site represents a remote VCS to which tunnel need to be
setup. Site is identified by a name.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__tunnel_dst','__extend','__mac_learning','__bfd_enable','__bfd','__shutdown',)

  _yang_name = 'site'
  _rest_name = 'site'

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
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,63}'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='site-id-type', is_config=True)
    self.__extend = YANGDynClass(base=extend.extend, is_container='container', yang_name="extend", rest_name="extend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure layer2 domains to be extended towards\nthis site.'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    self.__bfd = YANGDynClass(base=bfd.bfd, is_container='container', yang_name="bfd", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    self.__bfd_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-enable", rest_name="bfd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Create BFD session for the tunnels to the remote site.', u'cli-full-command': None, u'alt-name': u'bfd', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)
    self.__mac_learning = YANGDynClass(base=mac_learning.mac_learning, is_container='container', yang_name="mac-learning", rest_name="mac-learning", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC learning mode', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    self.__shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Admin disable tunnels to the remote site', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)
    self.__tunnel_dst = YANGDynClass(base=YANGListType("address",tunnel_dst.tunnel_dst, yang_name="tunnel-dst", rest_name="ip", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='address', extensions={u'tailf-common': {u'info': u'IP configuration for site.', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'alt-name': u'ip', u'callpoint': u'overlay-site-ip-cp'}}), is_container='list', yang_name="tunnel-dst", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP configuration for site.', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'alt-name': u'ip', u'callpoint': u'overlay-site-ip-cp'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='list', is_config=True)

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
      return [u'overlay-gateway', u'site']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'overlay-gateway', u'site']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /overlay_gateway/site/name (site-id-type)
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /overlay_gateway/site/name (site-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,63}'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='site-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with site-id-type""",
          'defined-type': "brocade-tunnels:site-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,63}'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='site-id-type', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,63}'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='site-id-type', is_config=True)


  def _get_tunnel_dst(self):
    """
    Getter method for tunnel_dst, mapped from YANG variable /overlay_gateway/site/tunnel_dst (list)

    YANG Description: Site IP address configuration represents
destination IP of tunnel to the site. Tunnel will
not be setup without the IP address configuration.
    """
    return self.__tunnel_dst
      
  def _set_tunnel_dst(self, v, load=False):
    """
    Setter method for tunnel_dst, mapped from YANG variable /overlay_gateway/site/tunnel_dst (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel_dst is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel_dst() directly.

    YANG Description: Site IP address configuration represents
destination IP of tunnel to the site. Tunnel will
not be setup without the IP address configuration.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("address",tunnel_dst.tunnel_dst, yang_name="tunnel-dst", rest_name="ip", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='address', extensions={u'tailf-common': {u'info': u'IP configuration for site.', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'alt-name': u'ip', u'callpoint': u'overlay-site-ip-cp'}}), is_container='list', yang_name="tunnel-dst", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP configuration for site.', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'alt-name': u'ip', u'callpoint': u'overlay-site-ip-cp'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel_dst must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("address",tunnel_dst.tunnel_dst, yang_name="tunnel-dst", rest_name="ip", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='address', extensions={u'tailf-common': {u'info': u'IP configuration for site.', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'alt-name': u'ip', u'callpoint': u'overlay-site-ip-cp'}}), is_container='list', yang_name="tunnel-dst", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP configuration for site.', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'alt-name': u'ip', u'callpoint': u'overlay-site-ip-cp'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='list', is_config=True)""",
        })

    self.__tunnel_dst = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel_dst(self):
    self.__tunnel_dst = YANGDynClass(base=YANGListType("address",tunnel_dst.tunnel_dst, yang_name="tunnel-dst", rest_name="ip", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='address', extensions={u'tailf-common': {u'info': u'IP configuration for site.', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'alt-name': u'ip', u'callpoint': u'overlay-site-ip-cp'}}), is_container='list', yang_name="tunnel-dst", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP configuration for site.', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'alt-name': u'ip', u'callpoint': u'overlay-site-ip-cp'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='list', is_config=True)


  def _get_extend(self):
    """
    Getter method for extend, mapped from YANG variable /overlay_gateway/site/extend (container)

    YANG Description: This configuration represents the layer2 domains to
be extended towards this site. In other words, it
represents switchport VLANs on the tunnels to the
site. VNI classification will be derived from 'map
vlan' configuration on this overlay gateway.
    """
    return self.__extend
      
  def _set_extend(self, v, load=False):
    """
    Setter method for extend, mapped from YANG variable /overlay_gateway/site/extend (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_extend is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_extend() directly.

    YANG Description: This configuration represents the layer2 domains to
be extended towards this site. In other words, it
represents switchport VLANs on the tunnels to the
site. VNI classification will be derived from 'map
vlan' configuration on this overlay gateway.
    """
    try:
      t = YANGDynClass(v,base=extend.extend, is_container='container', yang_name="extend", rest_name="extend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure layer2 domains to be extended towards\nthis site.'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """extend must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=extend.extend, is_container='container', yang_name="extend", rest_name="extend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure layer2 domains to be extended towards\nthis site.'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)""",
        })

    self.__extend = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_extend(self):
    self.__extend = YANGDynClass(base=extend.extend, is_container='container', yang_name="extend", rest_name="extend", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure layer2 domains to be extended towards\nthis site.'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)


  def _get_mac_learning(self):
    """
    Getter method for mac_learning, mapped from YANG variable /overlay_gateway/site/mac_learning (container)

    YANG Description: This configuration allows to specify MAC learning
mode for layer2-extension tunnels. By default 
dynamic MAC learning is used. It can be changed
to control plane learning via protocols like
BGP-EVPN.
    """
    return self.__mac_learning
      
  def _set_mac_learning(self, v, load=False):
    """
    Setter method for mac_learning, mapped from YANG variable /overlay_gateway/site/mac_learning (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_learning is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_learning() directly.

    YANG Description: This configuration allows to specify MAC learning
mode for layer2-extension tunnels. By default 
dynamic MAC learning is used. It can be changed
to control plane learning via protocols like
BGP-EVPN.
    """
    try:
      t = YANGDynClass(v,base=mac_learning.mac_learning, is_container='container', yang_name="mac-learning", rest_name="mac-learning", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC learning mode', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_learning must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mac_learning.mac_learning, is_container='container', yang_name="mac-learning", rest_name="mac-learning", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC learning mode', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)""",
        })

    self.__mac_learning = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_learning(self):
    self.__mac_learning = YANGDynClass(base=mac_learning.mac_learning, is_container='container', yang_name="mac-learning", rest_name="mac-learning", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC learning mode', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)


  def _get_bfd_enable(self):
    """
    Getter method for bfd_enable, mapped from YANG variable /overlay_gateway/site/bfd_enable (empty)

    YANG Description: Create BFD session for the tunnels to the remote site.
By default, BFD session is not created for the tunnels 
to the remote site.
    """
    return self.__bfd_enable
      
  def _set_bfd_enable(self, v, load=False):
    """
    Setter method for bfd_enable, mapped from YANG variable /overlay_gateway/site/bfd_enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_enable() directly.

    YANG Description: Create BFD session for the tunnels to the remote site.
By default, BFD session is not created for the tunnels 
to the remote site.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="bfd-enable", rest_name="bfd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Create BFD session for the tunnels to the remote site.', u'cli-full-command': None, u'alt-name': u'bfd', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-enable", rest_name="bfd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Create BFD session for the tunnels to the remote site.', u'cli-full-command': None, u'alt-name': u'bfd', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)""",
        })

    self.__bfd_enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_enable(self):
    self.__bfd_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-enable", rest_name="bfd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Create BFD session for the tunnels to the remote site.', u'cli-full-command': None, u'alt-name': u'bfd', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)


  def _get_bfd(self):
    """
    Getter method for bfd, mapped from YANG variable /overlay_gateway/site/bfd (container)
    """
    return self.__bfd
      
  def _set_bfd(self, v, load=False):
    """
    Setter method for bfd, mapped from YANG variable /overlay_gateway/site/bfd (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd() directly.
    """
    try:
      t = YANGDynClass(v,base=bfd.bfd, is_container='container', yang_name="bfd", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bfd.bfd, is_container='container', yang_name="bfd", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)""",
        })

    self.__bfd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd(self):
    self.__bfd = YANGDynClass(base=bfd.bfd, is_container='container', yang_name="bfd", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)


  def _get_shutdown(self):
    """
    Getter method for shutdown, mapped from YANG variable /overlay_gateway/site/shutdown (empty)

    YANG Description: Admin shutdown tunnels to this site. By default
tunnels are admin enabled.
    """
    return self.__shutdown
      
  def _set_shutdown(self, v, load=False):
    """
    Setter method for shutdown, mapped from YANG variable /overlay_gateway/site/shutdown (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_shutdown is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_shutdown() directly.

    YANG Description: Admin shutdown tunnels to this site. By default
tunnels are admin enabled.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Admin disable tunnels to the remote site', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """shutdown must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Admin disable tunnels to the remote site', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)""",
        })

    self.__shutdown = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_shutdown(self):
    self.__shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Admin disable tunnels to the remote site', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  tunnel_dst = __builtin__.property(_get_tunnel_dst, _set_tunnel_dst)
  extend = __builtin__.property(_get_extend, _set_extend)
  mac_learning = __builtin__.property(_get_mac_learning, _set_mac_learning)
  bfd_enable = __builtin__.property(_get_bfd_enable, _set_bfd_enable)
  bfd = __builtin__.property(_get_bfd, _set_bfd)
  shutdown = __builtin__.property(_get_shutdown, _set_shutdown)


  _pyangbind_elements = {'name': name, 'tunnel_dst': tunnel_dst, 'extend': extend, 'mac_learning': mac_learning, 'bfd_enable': bfd_enable, 'bfd': bfd, 'shutdown': shutdown, }


