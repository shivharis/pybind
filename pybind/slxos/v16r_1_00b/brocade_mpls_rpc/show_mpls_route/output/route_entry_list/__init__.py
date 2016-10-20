
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class route_entry_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-route/output/route-entry-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__entry_number','__dest_prefix','__prefix_length','__gateway','__vif_index','__out_interface_name','__out_label','__protocol','__metric','__use_count',)

  _yang_name = 'route-entry-list'
  _rest_name = 'route-entry-list'

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
    self.__protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__vif_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vif-index", rest_name="vif-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__use_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="use-count", rest_name="use-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__out_interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="out-interface-name", rest_name="out-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__prefix_length = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="prefix-length", rest_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__entry_number = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="entry-number", rest_name="entry-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__out_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="out-label", rest_name="out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__dest_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dest-prefix", rest_name="dest-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)
    self.__gateway = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway", rest_name="gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-route', u'output', u'route-entry-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-route', u'output', u'route-entry-list']

  def _get_entry_number(self):
    """
    Getter method for entry_number, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/entry_number (uint32)
    """
    return self.__entry_number
      
  def _set_entry_number(self, v, load=False):
    """
    Setter method for entry_number, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/entry_number (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_entry_number is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_entry_number() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="entry-number", rest_name="entry-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """entry_number must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="entry-number", rest_name="entry-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__entry_number = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_entry_number(self):
    self.__entry_number = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="entry-number", rest_name="entry-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_dest_prefix(self):
    """
    Getter method for dest_prefix, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/dest_prefix (mpls-ipv4-address)
    """
    return self.__dest_prefix
      
  def _set_dest_prefix(self, v, load=False):
    """
    Setter method for dest_prefix, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/dest_prefix (mpls-ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dest_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dest_prefix() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dest-prefix", rest_name="dest-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dest_prefix must be of a type compatible with mpls-ipv4-address""",
          'defined-type': "brocade-mpls:mpls-ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dest-prefix", rest_name="dest-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)""",
        })

    self.__dest_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dest_prefix(self):
    self.__dest_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dest-prefix", rest_name="dest-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)


  def _get_prefix_length(self):
    """
    Getter method for prefix_length, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/prefix_length (uint32)
    """
    return self.__prefix_length
      
  def _set_prefix_length(self, v, load=False):
    """
    Setter method for prefix_length, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/prefix_length (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_length is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_length() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="prefix-length", rest_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_length must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="prefix-length", rest_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__prefix_length = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_length(self):
    self.__prefix_length = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="prefix-length", rest_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_gateway(self):
    """
    Getter method for gateway, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/gateway (mpls-ipv4-address)
    """
    return self.__gateway
      
  def _set_gateway(self, v, load=False):
    """
    Setter method for gateway, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/gateway (mpls-ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gateway is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gateway() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway", rest_name="gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gateway must be of a type compatible with mpls-ipv4-address""",
          'defined-type': "brocade-mpls:mpls-ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway", rest_name="gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)""",
        })

    self.__gateway = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gateway(self):
    self.__gateway = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway", rest_name="gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)


  def _get_vif_index(self):
    """
    Getter method for vif_index, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/vif_index (uint32)
    """
    return self.__vif_index
      
  def _set_vif_index(self, v, load=False):
    """
    Setter method for vif_index, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/vif_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vif_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vif_index() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vif-index", rest_name="vif-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vif_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vif-index", rest_name="vif-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__vif_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vif_index(self):
    self.__vif_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vif-index", rest_name="vif-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_out_interface_name(self):
    """
    Getter method for out_interface_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/out_interface_name (string)
    """
    return self.__out_interface_name
      
  def _set_out_interface_name(self, v, load=False):
    """
    Setter method for out_interface_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/out_interface_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_interface_name() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="out-interface-name", rest_name="out-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_interface_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="out-interface-name", rest_name="out-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__out_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_interface_name(self):
    self.__out_interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="out-interface-name", rest_name="out-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_out_label(self):
    """
    Getter method for out_label, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/out_label (uint32)
    """
    return self.__out_label
      
  def _set_out_label(self, v, load=False):
    """
    Setter method for out_label, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/out_label (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_label() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="out-label", rest_name="out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_label must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="out-label", rest_name="out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__out_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_label(self):
    self.__out_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="out-label", rest_name="out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_protocol(self):
    """
    Getter method for protocol, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/protocol (string)
    """
    return self.__protocol
      
  def _set_protocol(self, v, load=False):
    """
    Setter method for protocol, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/protocol (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol(self):
    self.__protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_metric(self):
    """
    Getter method for metric, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/metric (uint32)
    """
    return self.__metric
      
  def _set_metric(self, v, load=False):
    """
    Setter method for metric, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric(self):
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_use_count(self):
    """
    Getter method for use_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/use_count (uint32)
    """
    return self.__use_count
      
  def _set_use_count(self, v, load=False):
    """
    Setter method for use_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_route/output/route_entry_list/use_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_use_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_use_count() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="use-count", rest_name="use-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """use_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="use-count", rest_name="use-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__use_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_use_count(self):
    self.__use_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="use-count", rest_name="use-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  entry_number = __builtin__.property(_get_entry_number, _set_entry_number)
  dest_prefix = __builtin__.property(_get_dest_prefix, _set_dest_prefix)
  prefix_length = __builtin__.property(_get_prefix_length, _set_prefix_length)
  gateway = __builtin__.property(_get_gateway, _set_gateway)
  vif_index = __builtin__.property(_get_vif_index, _set_vif_index)
  out_interface_name = __builtin__.property(_get_out_interface_name, _set_out_interface_name)
  out_label = __builtin__.property(_get_out_label, _set_out_label)
  protocol = __builtin__.property(_get_protocol, _set_protocol)
  metric = __builtin__.property(_get_metric, _set_metric)
  use_count = __builtin__.property(_get_use_count, _set_use_count)


  _pyangbind_elements = {'entry_number': entry_number, 'dest_prefix': dest_prefix, 'prefix_length': prefix_length, 'gateway': gateway, 'vif_index': vif_index, 'out_interface_name': out_interface_name, 'out_label': out_label, 'protocol': protocol, 'metric': metric, 'use_count': use_count, }


