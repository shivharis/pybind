
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import net
import router_isis_attributes
import address_family
class router_isis_cmds_holder(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/isis/router-isis-cmds-holder. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__net','__router_isis_attributes','__address_family',)

  _yang_name = 'router-isis-cmds-holder'
  _rest_name = ''

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    path_helper_ = kwargs.pop("path_helper", None)
    if path_helper_ is False:
      self._path_helper = False
    elif path_helper_ is not None and isinstance(path_helper_, xpathhelper.YANGPathHelper):
      self._path_helper = path_helper_
    elif hasattr(self, "_parent"):
      path_helper_ = getattr(self._parent, "_path_helper", False)
      self._path_helper = path_helper_
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
    self.__net = YANGDynClass(base=YANGListType("net_cmd",net.net, yang_name="net", rest_name="net", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='net-cmd', extensions={u'tailf-common': {u'info': u'Define NSAP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'IsisNet'}}), is_container='list', yang_name="net", rest_name="net", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define NSAP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'IsisNet'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='list', is_config=True)
    self.__router_isis_attributes = YANGDynClass(base=router_isis_attributes.router_isis_attributes, is_container='container', yang_name="router-isis-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    self.__address_family = YANGDynClass(base=address_family.address_family, is_container='container', yang_name="address-family", rest_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enter Address Family command mode', u'cli-incomplete-no': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)

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
      return [u'routing-system', u'router', u'isis', u'router-isis-cmds-holder']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'isis']

  def _get_net(self):
    """
    Getter method for net, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/net (list)
    """
    return self.__net
      
  def _set_net(self, v, load=False):
    """
    Setter method for net, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/net (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_net is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_net() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("net_cmd",net.net, yang_name="net", rest_name="net", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='net-cmd', extensions={u'tailf-common': {u'info': u'Define NSAP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'IsisNet'}}), is_container='list', yang_name="net", rest_name="net", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define NSAP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'IsisNet'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """net must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("net_cmd",net.net, yang_name="net", rest_name="net", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='net-cmd', extensions={u'tailf-common': {u'info': u'Define NSAP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'IsisNet'}}), is_container='list', yang_name="net", rest_name="net", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define NSAP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'IsisNet'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='list', is_config=True)""",
        })

    self.__net = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_net(self):
    self.__net = YANGDynClass(base=YANGListType("net_cmd",net.net, yang_name="net", rest_name="net", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='net-cmd', extensions={u'tailf-common': {u'info': u'Define NSAP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'IsisNet'}}), is_container='list', yang_name="net", rest_name="net", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define NSAP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'IsisNet'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='list', is_config=True)


  def _get_router_isis_attributes(self):
    """
    Getter method for router_isis_attributes, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/router_isis_attributes (container)
    """
    return self.__router_isis_attributes
      
  def _set_router_isis_attributes(self, v, load=False):
    """
    Setter method for router_isis_attributes, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/router_isis_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_isis_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_isis_attributes() directly.
    """
    try:
      t = YANGDynClass(v,base=router_isis_attributes.router_isis_attributes, is_container='container', yang_name="router-isis-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_isis_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=router_isis_attributes.router_isis_attributes, is_container='container', yang_name="router-isis-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)""",
        })

    self.__router_isis_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_isis_attributes(self):
    self.__router_isis_attributes = YANGDynClass(base=router_isis_attributes.router_isis_attributes, is_container='container', yang_name="router-isis-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)


  def _get_address_family(self):
    """
    Getter method for address_family, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family (container)
    """
    return self.__address_family
      
  def _set_address_family(self, v, load=False):
    """
    Setter method for address_family, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address_family is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address_family() directly.
    """
    try:
      t = YANGDynClass(v,base=address_family.address_family, is_container='container', yang_name="address-family", rest_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enter Address Family command mode', u'cli-incomplete-no': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address_family must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=address_family.address_family, is_container='container', yang_name="address-family", rest_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enter Address Family command mode', u'cli-incomplete-no': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)""",
        })

    self.__address_family = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address_family(self):
    self.__address_family = YANGDynClass(base=address_family.address_family, is_container='container', yang_name="address-family", rest_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enter Address Family command mode', u'cli-incomplete-no': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)

  net = __builtin__.property(_get_net, _set_net)
  router_isis_attributes = __builtin__.property(_get_router_isis_attributes, _set_router_isis_attributes)
  address_family = __builtin__.property(_get_address_family, _set_address_family)


  _pyangbind_elements = {'net': net, 'router_isis_attributes': router_isis_attributes, 'address_family': address_family, }

