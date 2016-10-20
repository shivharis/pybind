
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import system_max
import arp_entry
class hide_arp_holder(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-arp - based on the path /hide-arp-holder. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__system_max','__arp_entry',)

  _yang_name = 'hide-arp-holder'
  _rest_name = ''

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
    self.__system_max = YANGDynClass(base=system_max.system_max, is_container='container', yang_name="system-max", rest_name="system-max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure system-wide maximum values', u'hidden': u'full', u'callpoint': u'ArpConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='container', is_config=True)
    self.__arp_entry = YANGDynClass(base=YANGListType("arp_ip_address",arp_entry.arp_entry, yang_name="arp-entry", rest_name="arp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='arp-ip-address', extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}), is_container='list', yang_name="arp-entry", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='list', is_config=True)

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
      return [u'hide-arp-holder']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_system_max(self):
    """
    Getter method for system_max, mapped from YANG variable /hide_arp_holder/system_max (container)

    YANG Description: Configure system-wide maximum values (reload required)'.
           This support is obsoleted.
    """
    return self.__system_max
      
  def _set_system_max(self, v, load=False):
    """
    Setter method for system_max, mapped from YANG variable /hide_arp_holder/system_max (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_system_max is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_system_max() directly.

    YANG Description: Configure system-wide maximum values (reload required)'.
           This support is obsoleted.
    """
    try:
      t = YANGDynClass(v,base=system_max.system_max, is_container='container', yang_name="system-max", rest_name="system-max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure system-wide maximum values', u'hidden': u'full', u'callpoint': u'ArpConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """system_max must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=system_max.system_max, is_container='container', yang_name="system-max", rest_name="system-max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure system-wide maximum values', u'hidden': u'full', u'callpoint': u'ArpConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='container', is_config=True)""",
        })

    self.__system_max = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_system_max(self):
    self.__system_max = YANGDynClass(base=system_max.system_max, is_container='container', yang_name="system-max", rest_name="system-max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure system-wide maximum values', u'hidden': u'full', u'callpoint': u'ArpConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='container', is_config=True)


  def _get_arp_entry(self):
    """
    Getter method for arp_entry, mapped from YANG variable /hide_arp_holder/arp_entry (list)
    """
    return self.__arp_entry
      
  def _set_arp_entry(self, v, load=False):
    """
    Setter method for arp_entry, mapped from YANG variable /hide_arp_holder/arp_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_arp_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_arp_entry() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("arp_ip_address",arp_entry.arp_entry, yang_name="arp-entry", rest_name="arp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='arp-ip-address', extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}), is_container='list', yang_name="arp-entry", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """arp_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("arp_ip_address",arp_entry.arp_entry, yang_name="arp-entry", rest_name="arp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='arp-ip-address', extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}), is_container='list', yang_name="arp-entry", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='list', is_config=True)""",
        })

    self.__arp_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_arp_entry(self):
    self.__arp_entry = YANGDynClass(base=YANGListType("arp_ip_address",arp_entry.arp_entry, yang_name="arp-entry", rest_name="arp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='arp-ip-address', extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}), is_container='list', yang_name="arp-entry", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='list', is_config=True)

  system_max = __builtin__.property(_get_system_max, _set_system_max)
  arp_entry = __builtin__.property(_get_arp_entry, _set_arp_entry)


  _pyangbind_elements = {'system_max': system_max, 'arp_entry': arp_entry, }


