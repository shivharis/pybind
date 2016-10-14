
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import packet_error_counters
import packet_counters
class statistics(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/rsvp/statistics. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MPLS RSVP global statistics
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__packet_error_counters','__packet_counters',)

  _yang_name = 'statistics'

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
    self.__packet_error_counters = YANGDynClass(base=packet_error_counters.packet_error_counters, is_container='container', yang_name="packet-error-counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-rsvp-packet-error-counters', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    self.__packet_counters = YANGDynClass(base=packet_counters.packet_counters, is_container='container', yang_name="packet-counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-rsvp-packet-counters-packet-counters-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)

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
      return [u'mpls-state', u'rsvp', u'statistics']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'mpls-state', u'rsvp', u'statistics']

  def _get_packet_error_counters(self):
    """
    Getter method for packet_error_counters, mapped from YANG variable /mpls_state/rsvp/statistics/packet_error_counters (container)

    YANG Description: RSVP error packet counters
    """
    return self.__packet_error_counters
      
  def _set_packet_error_counters(self, v, load=False):
    """
    Setter method for packet_error_counters, mapped from YANG variable /mpls_state/rsvp/statistics/packet_error_counters (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_packet_error_counters is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_packet_error_counters() directly.

    YANG Description: RSVP error packet counters
    """
    try:
      t = YANGDynClass(v,base=packet_error_counters.packet_error_counters, is_container='container', yang_name="packet-error-counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-rsvp-packet-error-counters', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """packet_error_counters must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=packet_error_counters.packet_error_counters, is_container='container', yang_name="packet-error-counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-rsvp-packet-error-counters', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__packet_error_counters = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_packet_error_counters(self):
    self.__packet_error_counters = YANGDynClass(base=packet_error_counters.packet_error_counters, is_container='container', yang_name="packet-error-counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-rsvp-packet-error-counters', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)


  def _get_packet_counters(self):
    """
    Getter method for packet_counters, mapped from YANG variable /mpls_state/rsvp/statistics/packet_counters (container)
    """
    return self.__packet_counters
      
  def _set_packet_counters(self, v, load=False):
    """
    Setter method for packet_counters, mapped from YANG variable /mpls_state/rsvp/statistics/packet_counters (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_packet_counters is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_packet_counters() directly.
    """
    try:
      t = YANGDynClass(v,base=packet_counters.packet_counters, is_container='container', yang_name="packet-counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-rsvp-packet-counters-packet-counters-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """packet_counters must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=packet_counters.packet_counters, is_container='container', yang_name="packet-counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-rsvp-packet-counters-packet-counters-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__packet_counters = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_packet_counters(self):
    self.__packet_counters = YANGDynClass(base=packet_counters.packet_counters, is_container='container', yang_name="packet-counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-rsvp-packet-counters-packet-counters-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)

  packet_error_counters = __builtin__.property(_get_packet_error_counters)
  packet_counters = __builtin__.property(_get_packet_counters)


  _pyangbind_elements = {'packet_error_counters': packet_error_counters, 'packet_counters': packet_counters, }


