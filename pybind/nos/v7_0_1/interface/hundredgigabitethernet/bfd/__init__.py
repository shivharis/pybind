
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import interval
class bfd(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/hundredgigabitethernet/bfd. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Create BFD session on this interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__interval','__bfd_shutdown',)

  _yang_name = 'bfd'
  _rest_name = 'bfd'

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
    self.__bfd_shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Administratively shutdown the BFD session.', u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__interval = YANGDynClass(base=interval.interval, is_container='container', yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD desired min transmit interval in milliseconds.', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

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
      return [u'interface', u'hundredgigabitethernet', u'bfd']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'HundredGigabitEthernet', u'bfd']

  def _get_interval(self):
    """
    Getter method for interval, mapped from YANG variable /interface/hundredgigabitethernet/bfd/interval (container)

    YANG Description: Configure BFD desired min transmit interval in milliseconds.
    """
    return self.__interval
      
  def _set_interval(self, v, load=False):
    """
    Setter method for interval, mapped from YANG variable /interface/hundredgigabitethernet/bfd/interval (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interval() directly.

    YANG Description: Configure BFD desired min transmit interval in milliseconds.
    """
    try:
      t = YANGDynClass(v,base=interval.interval, is_container='container', yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD desired min transmit interval in milliseconds.', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interval must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interval.interval, is_container='container', yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD desired min transmit interval in milliseconds.', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interval(self):
    self.__interval = YANGDynClass(base=interval.interval, is_container='container', yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD desired min transmit interval in milliseconds.', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_bfd_shutdown(self):
    """
    Getter method for bfd_shutdown, mapped from YANG variable /interface/hundredgigabitethernet/bfd/bfd_shutdown (empty)

    YANG Description: Administratively shutdown the BFD session.
    """
    return self.__bfd_shutdown
      
  def _set_bfd_shutdown(self, v, load=False):
    """
    Setter method for bfd_shutdown, mapped from YANG variable /interface/hundredgigabitethernet/bfd/bfd_shutdown (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_shutdown is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_shutdown() directly.

    YANG Description: Administratively shutdown the BFD session.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="bfd-shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Administratively shutdown the BFD session.', u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_shutdown must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Administratively shutdown the BFD session.', u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__bfd_shutdown = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_shutdown(self):
    self.__bfd_shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Administratively shutdown the BFD session.', u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)

  interval = __builtin__.property(_get_interval, _set_interval)
  bfd_shutdown = __builtin__.property(_get_bfd_shutdown, _set_bfd_shutdown)


  _pyangbind_elements = {'interval': interval, 'bfd_shutdown': bfd_shutdown, }


