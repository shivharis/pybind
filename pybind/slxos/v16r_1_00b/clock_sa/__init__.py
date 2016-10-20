
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import clock
class clock_sa(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-clock - based on the path /clock-sa. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__clock',)

  _yang_name = 'clock-sa'
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
    self.__clock = YANGDynClass(base=clock.clock, is_container='container', yang_name="clock", rest_name="clock", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure System Timezone', u'callpoint': u'clock_timezone_cp', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-clock', defining_module='brocade-clock', yang_type='container', is_config=True)

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
      return [u'clock-sa']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_clock(self):
    """
    Getter method for clock, mapped from YANG variable /clock_sa/clock (container)
    """
    return self.__clock
      
  def _set_clock(self, v, load=False):
    """
    Setter method for clock, mapped from YANG variable /clock_sa/clock (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_clock is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_clock() directly.
    """
    try:
      t = YANGDynClass(v,base=clock.clock, is_container='container', yang_name="clock", rest_name="clock", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure System Timezone', u'callpoint': u'clock_timezone_cp', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-clock', defining_module='brocade-clock', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """clock must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=clock.clock, is_container='container', yang_name="clock", rest_name="clock", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure System Timezone', u'callpoint': u'clock_timezone_cp', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-clock', defining_module='brocade-clock', yang_type='container', is_config=True)""",
        })

    self.__clock = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_clock(self):
    self.__clock = YANGDynClass(base=clock.clock, is_container='container', yang_name="clock", rest_name="clock", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure System Timezone', u'callpoint': u'clock_timezone_cp', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-clock', defining_module='brocade-clock', yang_type='container', is_config=True)

  clock = __builtin__.property(_get_clock, _set_clock)


  _pyangbind_elements = {'clock': clock, }


