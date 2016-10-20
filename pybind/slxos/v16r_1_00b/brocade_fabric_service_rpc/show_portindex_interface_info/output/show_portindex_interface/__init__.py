
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import show_portindex
class show_portindex_interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fabric-service - based on the path /brocade_fabric_service_rpc/show-portindex-interface-info/output/show-portindex-interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__portsgroup_rbridgeid','__show_portindex',)

  _yang_name = 'show-portindex-interface'
  _rest_name = 'show-portindex-interface'

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
    self.__portsgroup_rbridgeid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="portsgroup-rbridgeid", rest_name="portsgroup-rbridgeid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'rbridge-id'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='common-def:rbridge-id-type', is_config=True)
    self.__show_portindex = YANGDynClass(base=YANGListType("port_index",show_portindex.show_portindex, yang_name="show-portindex", rest_name="show-portindex", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-index', extensions=None), is_container='list', yang_name="show-portindex", rest_name="show-portindex", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)

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
      return [u'brocade_fabric_service_rpc', u'show-portindex-interface-info', u'output', u'show-portindex-interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-portindex-interface-info', u'output', u'show-portindex-interface']

  def _get_portsgroup_rbridgeid(self):
    """
    Getter method for portsgroup_rbridgeid, mapped from YANG variable /brocade_fabric_service_rpc/show_portindex_interface_info/output/show_portindex_interface/portsgroup_rbridgeid (common-def:rbridge-id-type)

    YANG Description: The RBridge-ID of the switch
in the cluster.
    """
    return self.__portsgroup_rbridgeid
      
  def _set_portsgroup_rbridgeid(self, v, load=False):
    """
    Setter method for portsgroup_rbridgeid, mapped from YANG variable /brocade_fabric_service_rpc/show_portindex_interface_info/output/show_portindex_interface/portsgroup_rbridgeid (common-def:rbridge-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_portsgroup_rbridgeid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_portsgroup_rbridgeid() directly.

    YANG Description: The RBridge-ID of the switch
in the cluster.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="portsgroup-rbridgeid", rest_name="portsgroup-rbridgeid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'rbridge-id'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='common-def:rbridge-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """portsgroup_rbridgeid must be of a type compatible with common-def:rbridge-id-type""",
          'defined-type': "common-def:rbridge-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="portsgroup-rbridgeid", rest_name="portsgroup-rbridgeid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'rbridge-id'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='common-def:rbridge-id-type', is_config=True)""",
        })

    self.__portsgroup_rbridgeid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_portsgroup_rbridgeid(self):
    self.__portsgroup_rbridgeid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="portsgroup-rbridgeid", rest_name="portsgroup-rbridgeid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'rbridge-id'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='common-def:rbridge-id-type', is_config=True)


  def _get_show_portindex(self):
    """
    Getter method for show_portindex, mapped from YANG variable /brocade_fabric_service_rpc/show_portindex_interface_info/output/show_portindex_interface/show_portindex (list)
    """
    return self.__show_portindex
      
  def _set_show_portindex(self, v, load=False):
    """
    Setter method for show_portindex, mapped from YANG variable /brocade_fabric_service_rpc/show_portindex_interface_info/output/show_portindex_interface/show_portindex (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_portindex is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_portindex() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("port_index",show_portindex.show_portindex, yang_name="show-portindex", rest_name="show-portindex", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-index', extensions=None), is_container='list', yang_name="show-portindex", rest_name="show-portindex", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_portindex must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("port_index",show_portindex.show_portindex, yang_name="show-portindex", rest_name="show-portindex", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-index', extensions=None), is_container='list', yang_name="show-portindex", rest_name="show-portindex", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)""",
        })

    self.__show_portindex = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_portindex(self):
    self.__show_portindex = YANGDynClass(base=YANGListType("port_index",show_portindex.show_portindex, yang_name="show-portindex", rest_name="show-portindex", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-index', extensions=None), is_container='list', yang_name="show-portindex", rest_name="show-portindex", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)

  portsgroup_rbridgeid = __builtin__.property(_get_portsgroup_rbridgeid, _set_portsgroup_rbridgeid)
  show_portindex = __builtin__.property(_get_show_portindex, _set_show_portindex)


  _pyangbind_elements = {'portsgroup_rbridgeid': portsgroup_rbridgeid, 'show_portindex': show_portindex, }


