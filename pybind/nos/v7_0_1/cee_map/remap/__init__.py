
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import fabric_priority
import lossless_priority
class remap(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-cee-map - based on the path /cee-map/remap. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fabric_priority','__lossless_priority',)

  _yang_name = 'remap'
  _rest_name = 'remap'

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
    self.__lossless_priority = YANGDynClass(base=lossless_priority.lossless_priority, is_container='container', yang_name="lossless-priority", rest_name="lossless-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' CoS for lossless priority'}}, namespace='urn:brocade.com:mgmt:brocade-cee-map', defining_module='brocade-cee-map', yang_type='container', is_config=True)
    self.__fabric_priority = YANGDynClass(base=fabric_priority.fabric_priority, is_container='container', yang_name="fabric-priority", rest_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' CoS for fabric priority'}}, namespace='urn:brocade.com:mgmt:brocade-cee-map', defining_module='brocade-cee-map', yang_type='container', is_config=True)

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
      return [u'cee-map', u'remap']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cee-map', u'remap']

  def _get_fabric_priority(self):
    """
    Getter method for fabric_priority, mapped from YANG variable /cee_map/remap/fabric_priority (container)
    """
    return self.__fabric_priority
      
  def _set_fabric_priority(self, v, load=False):
    """
    Setter method for fabric_priority, mapped from YANG variable /cee_map/remap/fabric_priority (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fabric_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fabric_priority() directly.
    """
    try:
      t = YANGDynClass(v,base=fabric_priority.fabric_priority, is_container='container', yang_name="fabric-priority", rest_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' CoS for fabric priority'}}, namespace='urn:brocade.com:mgmt:brocade-cee-map', defining_module='brocade-cee-map', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fabric_priority must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=fabric_priority.fabric_priority, is_container='container', yang_name="fabric-priority", rest_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' CoS for fabric priority'}}, namespace='urn:brocade.com:mgmt:brocade-cee-map', defining_module='brocade-cee-map', yang_type='container', is_config=True)""",
        })

    self.__fabric_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fabric_priority(self):
    self.__fabric_priority = YANGDynClass(base=fabric_priority.fabric_priority, is_container='container', yang_name="fabric-priority", rest_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' CoS for fabric priority'}}, namespace='urn:brocade.com:mgmt:brocade-cee-map', defining_module='brocade-cee-map', yang_type='container', is_config=True)


  def _get_lossless_priority(self):
    """
    Getter method for lossless_priority, mapped from YANG variable /cee_map/remap/lossless_priority (container)
    """
    return self.__lossless_priority
      
  def _set_lossless_priority(self, v, load=False):
    """
    Setter method for lossless_priority, mapped from YANG variable /cee_map/remap/lossless_priority (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lossless_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lossless_priority() directly.
    """
    try:
      t = YANGDynClass(v,base=lossless_priority.lossless_priority, is_container='container', yang_name="lossless-priority", rest_name="lossless-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' CoS for lossless priority'}}, namespace='urn:brocade.com:mgmt:brocade-cee-map', defining_module='brocade-cee-map', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lossless_priority must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=lossless_priority.lossless_priority, is_container='container', yang_name="lossless-priority", rest_name="lossless-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' CoS for lossless priority'}}, namespace='urn:brocade.com:mgmt:brocade-cee-map', defining_module='brocade-cee-map', yang_type='container', is_config=True)""",
        })

    self.__lossless_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lossless_priority(self):
    self.__lossless_priority = YANGDynClass(base=lossless_priority.lossless_priority, is_container='container', yang_name="lossless-priority", rest_name="lossless-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' CoS for lossless priority'}}, namespace='urn:brocade.com:mgmt:brocade-cee-map', defining_module='brocade-cee-map', yang_type='container', is_config=True)

  fabric_priority = __builtin__.property(_get_fabric_priority, _set_fabric_priority)
  lossless_priority = __builtin__.property(_get_lossless_priority, _set_lossless_priority)


  _pyangbind_elements = {'fabric_priority': fabric_priority, 'lossless_priority': lossless_priority, }


