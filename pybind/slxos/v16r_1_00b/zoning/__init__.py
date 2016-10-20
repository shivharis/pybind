
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import defined_configuration
import enabled_configuration
class zoning(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-zone - based on the path /zoning. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__defined_configuration','__enabled_configuration',)

  _yang_name = 'zoning'
  _rest_name = 'zoning'

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
    self.__defined_configuration = YANGDynClass(base=defined_configuration.defined_configuration, is_container='container', yang_name="defined-configuration", rest_name="defined-configuration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Defined DB entries'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='container', is_config=True)
    self.__enabled_configuration = YANGDynClass(base=enabled_configuration.enabled_configuration, is_container='container', yang_name="enabled-configuration", rest_name="enabled-configuration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enabled DB entries', u'callpoint': u'zone_effective_cfg', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='container', is_config=True)

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
      return [u'zoning']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'zoning']

  def _get_defined_configuration(self):
    """
    Getter method for defined_configuration, mapped from YANG variable /zoning/defined_configuration (container)
    """
    return self.__defined_configuration
      
  def _set_defined_configuration(self, v, load=False):
    """
    Setter method for defined_configuration, mapped from YANG variable /zoning/defined_configuration (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_defined_configuration is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_defined_configuration() directly.
    """
    try:
      t = YANGDynClass(v,base=defined_configuration.defined_configuration, is_container='container', yang_name="defined-configuration", rest_name="defined-configuration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Defined DB entries'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """defined_configuration must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=defined_configuration.defined_configuration, is_container='container', yang_name="defined-configuration", rest_name="defined-configuration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Defined DB entries'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='container', is_config=True)""",
        })

    self.__defined_configuration = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_defined_configuration(self):
    self.__defined_configuration = YANGDynClass(base=defined_configuration.defined_configuration, is_container='container', yang_name="defined-configuration", rest_name="defined-configuration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Defined DB entries'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='container', is_config=True)


  def _get_enabled_configuration(self):
    """
    Getter method for enabled_configuration, mapped from YANG variable /zoning/enabled_configuration (container)
    """
    return self.__enabled_configuration
      
  def _set_enabled_configuration(self, v, load=False):
    """
    Setter method for enabled_configuration, mapped from YANG variable /zoning/enabled_configuration (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled_configuration is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled_configuration() directly.
    """
    try:
      t = YANGDynClass(v,base=enabled_configuration.enabled_configuration, is_container='container', yang_name="enabled-configuration", rest_name="enabled-configuration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enabled DB entries', u'callpoint': u'zone_effective_cfg', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled_configuration must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=enabled_configuration.enabled_configuration, is_container='container', yang_name="enabled-configuration", rest_name="enabled-configuration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enabled DB entries', u'callpoint': u'zone_effective_cfg', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='container', is_config=True)""",
        })

    self.__enabled_configuration = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled_configuration(self):
    self.__enabled_configuration = YANGDynClass(base=enabled_configuration.enabled_configuration, is_container='container', yang_name="enabled-configuration", rest_name="enabled-configuration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enabled DB entries', u'callpoint': u'zone_effective_cfg', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='container', is_config=True)

  defined_configuration = __builtin__.property(_get_defined_configuration, _set_defined_configuration)
  enabled_configuration = __builtin__.property(_get_enabled_configuration, _set_enabled_configuration)


  _pyangbind_elements = {'defined_configuration': defined_configuration, 'enabled_configuration': enabled_configuration, }


