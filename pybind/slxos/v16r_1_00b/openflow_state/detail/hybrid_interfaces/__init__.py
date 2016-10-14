
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class hybrid_interfaces(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/detail/hybrid-interfaces. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__hybrid_interface','__protected_vlans',)

  _yang_name = 'hybrid-interfaces'

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
    self.__protected_vlans = YANGDynClass(base=unicode, is_leaf=True, yang_name="protected-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    self.__hybrid_interface = YANGDynClass(base=unicode, is_leaf=True, yang_name="hybrid-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)

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
      return [u'openflow-state', u'detail', u'hybrid-interfaces']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'openflow-state', u'detail', u'hybrid-interfaces']

  def _get_hybrid_interface(self):
    """
    Getter method for hybrid_interface, mapped from YANG variable /openflow_state/detail/hybrid_interfaces/hybrid_interface (string)

    YANG Description: Hybrid Interface
    """
    return self.__hybrid_interface
      
  def _set_hybrid_interface(self, v, load=False):
    """
    Setter method for hybrid_interface, mapped from YANG variable /openflow_state/detail/hybrid_interfaces/hybrid_interface (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hybrid_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hybrid_interface() directly.

    YANG Description: Hybrid Interface
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="hybrid-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hybrid_interface must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="hybrid-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__hybrid_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hybrid_interface(self):
    self.__hybrid_interface = YANGDynClass(base=unicode, is_leaf=True, yang_name="hybrid-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)


  def _get_protected_vlans(self):
    """
    Getter method for protected_vlans, mapped from YANG variable /openflow_state/detail/hybrid_interfaces/protected_vlans (string)

    YANG Description: Protected Vlans
    """
    return self.__protected_vlans
      
  def _set_protected_vlans(self, v, load=False):
    """
    Setter method for protected_vlans, mapped from YANG variable /openflow_state/detail/hybrid_interfaces/protected_vlans (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protected_vlans is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protected_vlans() directly.

    YANG Description: Protected Vlans
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="protected-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protected_vlans must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="protected-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__protected_vlans = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protected_vlans(self):
    self.__protected_vlans = YANGDynClass(base=unicode, is_leaf=True, yang_name="protected-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)

  hybrid_interface = __builtin__.property(_get_hybrid_interface)
  protected_vlans = __builtin__.property(_get_protected_vlans)


  _pyangbind_elements = {'hybrid_interface': hybrid_interface, 'protected_vlans': protected_vlans, }


