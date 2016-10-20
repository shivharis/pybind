
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-preprovision - based on the path /brocade_preprovision_rpc/show-bare-metal-state/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bare_metal_state',)

  _yang_name = 'output'
  _rest_name = 'output'

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
    self.__bare_metal_state = YANGDynClass(base=unicode, is_leaf=True, yang_name="bare-metal-state", rest_name="bare-metal-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-preprovision', defining_module='brocade-preprovision', yang_type='string', is_config=True)

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
      return [u'brocade_preprovision_rpc', u'show-bare-metal-state', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-bare-metal-state', u'output']

  def _get_bare_metal_state(self):
    """
    Getter method for bare_metal_state, mapped from YANG variable /brocade_preprovision_rpc/show_bare_metal_state/output/bare_metal_state (string)

    YANG Description: This leaf indicates the bare-metal state on the system.
    """
    return self.__bare_metal_state
      
  def _set_bare_metal_state(self, v, load=False):
    """
    Setter method for bare_metal_state, mapped from YANG variable /brocade_preprovision_rpc/show_bare_metal_state/output/bare_metal_state (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bare_metal_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bare_metal_state() directly.

    YANG Description: This leaf indicates the bare-metal state on the system.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="bare-metal-state", rest_name="bare-metal-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-preprovision', defining_module='brocade-preprovision', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bare_metal_state must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="bare-metal-state", rest_name="bare-metal-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-preprovision', defining_module='brocade-preprovision', yang_type='string', is_config=True)""",
        })

    self.__bare_metal_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bare_metal_state(self):
    self.__bare_metal_state = YANGDynClass(base=unicode, is_leaf=True, yang_name="bare-metal-state", rest_name="bare-metal-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-preprovision', defining_module='brocade-preprovision', yang_type='string', is_config=True)

  bare_metal_state = __builtin__.property(_get_bare_metal_state, _set_bare_metal_state)


  _pyangbind_elements = {'bare_metal_state': bare_metal_state, }


