
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class interface_nodespecific(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/interface-nodespecific. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ns_vlan','__ns_ethernet',)

  _yang_name = 'interface-nodespecific'
  _rest_name = 'interface-nodespecific'

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
    self.__ns_vlan = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="ns-vlan", rest_name="ns-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='int32', is_config=True)
    self.__ns_ethernet = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="ns-ethernet", rest_name="ns-ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='int32', is_config=True)

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
      return [u'rbridge-id', u'interface-nodespecific']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'interface-nodespecific']

  def _get_ns_vlan(self):
    """
    Getter method for ns_vlan, mapped from YANG variable /rbridge_id/interface_nodespecific/ns_vlan (int32)
    """
    return self.__ns_vlan
      
  def _set_ns_vlan(self, v, load=False):
    """
    Setter method for ns_vlan, mapped from YANG variable /rbridge_id/interface_nodespecific/ns_vlan (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ns_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ns_vlan() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="ns-vlan", rest_name="ns-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ns_vlan must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="ns-vlan", rest_name="ns-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='int32', is_config=True)""",
        })

    self.__ns_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ns_vlan(self):
    self.__ns_vlan = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="ns-vlan", rest_name="ns-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='int32', is_config=True)


  def _get_ns_ethernet(self):
    """
    Getter method for ns_ethernet, mapped from YANG variable /rbridge_id/interface_nodespecific/ns_ethernet (int32)
    """
    return self.__ns_ethernet
      
  def _set_ns_ethernet(self, v, load=False):
    """
    Setter method for ns_ethernet, mapped from YANG variable /rbridge_id/interface_nodespecific/ns_ethernet (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ns_ethernet is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ns_ethernet() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="ns-ethernet", rest_name="ns-ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ns_ethernet must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="ns-ethernet", rest_name="ns-ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='int32', is_config=True)""",
        })

    self.__ns_ethernet = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ns_ethernet(self):
    self.__ns_ethernet = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="ns-ethernet", rest_name="ns-ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-rbridge', defining_module='brocade-rbridge', yang_type='int32', is_config=True)

  ns_vlan = __builtin__.property(_get_ns_vlan, _set_ns_vlan)
  ns_ethernet = __builtin__.property(_get_ns_ethernet, _set_ns_ethernet)


  _pyangbind_elements = {'ns_vlan': ns_vlan, 'ns_ethernet': ns_ethernet, }


