
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ethernet
import port_channel
class logical_interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-bridge-domain - based on the path /bridge-domain/logical-interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ethernet','__port_channel',)

  _yang_name = 'logical-interface'
  _rest_name = 'logical-interface'

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
    self.__ethernet = YANGDynClass(base=YANGListType("lif_bind_id",ethernet.ethernet, yang_name="ethernet", rest_name="ethernet", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lif-bind-id', extensions={u'tailf-common': {u'info': u'Bind an ethernet logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainLifBindCallpoint'}}), is_container='list', yang_name="ethernet", rest_name="ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind an ethernet logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainLifBindCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-bridge-domain', defining_module='brocade-bridge-domain', yang_type='list', is_config=True)
    self.__port_channel = YANGDynClass(base=YANGListType("pc_lif_bind_id",port_channel.port_channel, yang_name="port-channel", rest_name="port-channel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pc-lif-bind-id', extensions={u'tailf-common': {u'info': u'Bind a port-channel logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainPortChannelLifBindCallpoint'}}), is_container='list', yang_name="port-channel", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind a port-channel logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainPortChannelLifBindCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-bridge-domain', defining_module='brocade-bridge-domain', yang_type='list', is_config=True)

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
      return [u'bridge-domain', u'logical-interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'bridge-domain', u'logical-interface']

  def _get_ethernet(self):
    """
    Getter method for ethernet, mapped from YANG variable /bridge_domain/logical_interface/ethernet (list)
    """
    return self.__ethernet
      
  def _set_ethernet(self, v, load=False):
    """
    Setter method for ethernet, mapped from YANG variable /bridge_domain/logical_interface/ethernet (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ethernet is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ethernet() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("lif_bind_id",ethernet.ethernet, yang_name="ethernet", rest_name="ethernet", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lif-bind-id', extensions={u'tailf-common': {u'info': u'Bind an ethernet logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainLifBindCallpoint'}}), is_container='list', yang_name="ethernet", rest_name="ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind an ethernet logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainLifBindCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-bridge-domain', defining_module='brocade-bridge-domain', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ethernet must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("lif_bind_id",ethernet.ethernet, yang_name="ethernet", rest_name="ethernet", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lif-bind-id', extensions={u'tailf-common': {u'info': u'Bind an ethernet logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainLifBindCallpoint'}}), is_container='list', yang_name="ethernet", rest_name="ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind an ethernet logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainLifBindCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-bridge-domain', defining_module='brocade-bridge-domain', yang_type='list', is_config=True)""",
        })

    self.__ethernet = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ethernet(self):
    self.__ethernet = YANGDynClass(base=YANGListType("lif_bind_id",ethernet.ethernet, yang_name="ethernet", rest_name="ethernet", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lif-bind-id', extensions={u'tailf-common': {u'info': u'Bind an ethernet logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainLifBindCallpoint'}}), is_container='list', yang_name="ethernet", rest_name="ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind an ethernet logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainLifBindCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-bridge-domain', defining_module='brocade-bridge-domain', yang_type='list', is_config=True)


  def _get_port_channel(self):
    """
    Getter method for port_channel, mapped from YANG variable /bridge_domain/logical_interface/port_channel (list)
    """
    return self.__port_channel
      
  def _set_port_channel(self, v, load=False):
    """
    Setter method for port_channel, mapped from YANG variable /bridge_domain/logical_interface/port_channel (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_channel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_channel() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("pc_lif_bind_id",port_channel.port_channel, yang_name="port-channel", rest_name="port-channel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pc-lif-bind-id', extensions={u'tailf-common': {u'info': u'Bind a port-channel logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainPortChannelLifBindCallpoint'}}), is_container='list', yang_name="port-channel", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind a port-channel logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainPortChannelLifBindCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-bridge-domain', defining_module='brocade-bridge-domain', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_channel must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("pc_lif_bind_id",port_channel.port_channel, yang_name="port-channel", rest_name="port-channel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pc-lif-bind-id', extensions={u'tailf-common': {u'info': u'Bind a port-channel logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainPortChannelLifBindCallpoint'}}), is_container='list', yang_name="port-channel", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind a port-channel logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainPortChannelLifBindCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-bridge-domain', defining_module='brocade-bridge-domain', yang_type='list', is_config=True)""",
        })

    self.__port_channel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_channel(self):
    self.__port_channel = YANGDynClass(base=YANGListType("pc_lif_bind_id",port_channel.port_channel, yang_name="port-channel", rest_name="port-channel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pc-lif-bind-id', extensions={u'tailf-common': {u'info': u'Bind a port-channel logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainPortChannelLifBindCallpoint'}}), is_container='list', yang_name="port-channel", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind a port-channel logical interface to this Bridge Domain', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'BridgeDomainPortChannelLifBindCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-bridge-domain', defining_module='brocade-bridge-domain', yang_type='list', is_config=True)

  ethernet = __builtin__.property(_get_ethernet, _set_ethernet)
  port_channel = __builtin__.property(_get_port_channel, _set_port_channel)


  _pyangbind_elements = {'ethernet': ethernet, 'port_channel': port_channel, }


