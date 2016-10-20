
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ve
import loopback
class interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tunnels - based on the path /overlay-gateway/ip/interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ve','__loopback',)

  _yang_name = 'interface'
  _rest_name = 'interface'

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
    self.__ve = YANGDynClass(base=ve.ve, is_container='container', yang_name="ve", rest_name="Ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VE interface', u'cli-sequence-commands': None, u'alt-name': u'Ve'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    self.__loopback = YANGDynClass(base=loopback.loopback, is_container='container', yang_name="loopback", rest_name="Loopback", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback interface', u'alt-name': u'Loopback'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)

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
      return [u'overlay-gateway', u'ip', u'interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'overlay-gateway', u'ip', u'interface']

  def _get_ve(self):
    """
    Getter method for ve, mapped from YANG variable /overlay_gateway/ip/interface/ve (container)
    """
    return self.__ve
      
  def _set_ve(self, v, load=False):
    """
    Setter method for ve, mapped from YANG variable /overlay_gateway/ip/interface/ve (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ve is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ve() directly.
    """
    try:
      t = YANGDynClass(v,base=ve.ve, is_container='container', yang_name="ve", rest_name="Ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VE interface', u'cli-sequence-commands': None, u'alt-name': u'Ve'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ve must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ve.ve, is_container='container', yang_name="ve", rest_name="Ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VE interface', u'cli-sequence-commands': None, u'alt-name': u'Ve'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)""",
        })

    self.__ve = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ve(self):
    self.__ve = YANGDynClass(base=ve.ve, is_container='container', yang_name="ve", rest_name="Ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VE interface', u'cli-sequence-commands': None, u'alt-name': u'Ve'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)


  def _get_loopback(self):
    """
    Getter method for loopback, mapped from YANG variable /overlay_gateway/ip/interface/loopback (container)
    """
    return self.__loopback
      
  def _set_loopback(self, v, load=False):
    """
    Setter method for loopback, mapped from YANG variable /overlay_gateway/ip/interface/loopback (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_loopback is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_loopback() directly.
    """
    try:
      t = YANGDynClass(v,base=loopback.loopback, is_container='container', yang_name="loopback", rest_name="Loopback", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback interface', u'alt-name': u'Loopback'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """loopback must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=loopback.loopback, is_container='container', yang_name="loopback", rest_name="Loopback", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback interface', u'alt-name': u'Loopback'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)""",
        })

    self.__loopback = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_loopback(self):
    self.__loopback = YANGDynClass(base=loopback.loopback, is_container='container', yang_name="loopback", rest_name="Loopback", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback interface', u'alt-name': u'Loopback'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)

  ve = __builtin__.property(_get_ve, _set_ve)
  loopback = __builtin__.property(_get_loopback, _set_loopback)


  _pyangbind_elements = {'ve': ve, 'loopback': loopback, }


