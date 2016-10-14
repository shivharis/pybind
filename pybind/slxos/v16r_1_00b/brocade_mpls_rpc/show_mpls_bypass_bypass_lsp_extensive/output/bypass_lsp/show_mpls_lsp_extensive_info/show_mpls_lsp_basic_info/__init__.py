
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class show_mpls_lsp_basic_info(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-bypass-bypass-lsp-extensive/output/bypass-lsp/show-mpls-lsp-extensive-info/show-mpls-lsp-basic-info. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__lsp_name','__lsp_type_bypass','__lsp_type_dynamic','__lsp_from_address','__lsp_to_address','__lsp_tunnel_id','__lsp_lsp_id','__lsp_admin_up','__lsp_operational_up','__lsp_is_active','__lsp_path_name','__lsp_out_label','__lsp_out_interface_name',)

  _yang_name = 'show-mpls-lsp-basic-info'

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
    self.__lsp_to_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-to-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__lsp_out_interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="lsp-out-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__lsp_admin_up = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-admin-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_path_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="lsp-path-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__lsp_operational_up = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-operational-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_is_active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-is-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="lsp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__lsp_tunnel_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-tunnel-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__lsp_type_bypass = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-type-bypass", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_lsp_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-lsp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__lsp_from_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-from-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__lsp_type_dynamic = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-type-dynamic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_out_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-bypass-bypass-lsp-extensive', u'output', u'bypass-lsp', u'show-mpls-lsp-extensive-info', u'show-mpls-lsp-basic-info']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'show-mpls-bypass-bypass-lsp-extensive', u'output', u'bypass-lsp']

  def _get_lsp_name(self):
    """
    Getter method for lsp_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_name (string)

    YANG Description: MPLS LSP name
    """
    return self.__lsp_name
      
  def _set_lsp_name(self, v, load=False):
    """
    Setter method for lsp_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_name() directly.

    YANG Description: MPLS LSP name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="lsp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="lsp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__lsp_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_name(self):
    self.__lsp_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="lsp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_lsp_type_bypass(self):
    """
    Getter method for lsp_type_bypass, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_type_bypass (boolean)

    YANG Description: Lsp is bypass LSP
    """
    return self.__lsp_type_bypass
      
  def _set_lsp_type_bypass(self, v, load=False):
    """
    Setter method for lsp_type_bypass, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_type_bypass (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_type_bypass is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_type_bypass() directly.

    YANG Description: Lsp is bypass LSP
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-type-bypass", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_type_bypass must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-type-bypass", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_type_bypass = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_type_bypass(self):
    self.__lsp_type_bypass = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-type-bypass", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_type_dynamic(self):
    """
    Getter method for lsp_type_dynamic, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_type_dynamic (boolean)

    YANG Description: Lsp is a dynamically created LSP
    """
    return self.__lsp_type_dynamic
      
  def _set_lsp_type_dynamic(self, v, load=False):
    """
    Setter method for lsp_type_dynamic, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_type_dynamic (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_type_dynamic is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_type_dynamic() directly.

    YANG Description: Lsp is a dynamically created LSP
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-type-dynamic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_type_dynamic must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-type-dynamic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_type_dynamic = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_type_dynamic(self):
    self.__lsp_type_dynamic = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-type-dynamic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_from_address(self):
    """
    Getter method for lsp_from_address, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_from_address (inet:ipv4-address)

    YANG Description: LSP from address
    """
    return self.__lsp_from_address
      
  def _set_lsp_from_address(self, v, load=False):
    """
    Setter method for lsp_from_address, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_from_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_from_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_from_address() directly.

    YANG Description: LSP from address
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-from-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_from_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-from-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__lsp_from_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_from_address(self):
    self.__lsp_from_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-from-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_lsp_to_address(self):
    """
    Getter method for lsp_to_address, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_to_address (inet:ipv4-address)

    YANG Description: LSP to address
    """
    return self.__lsp_to_address
      
  def _set_lsp_to_address(self, v, load=False):
    """
    Setter method for lsp_to_address, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_to_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_to_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_to_address() directly.

    YANG Description: LSP to address
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-to-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_to_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-to-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__lsp_to_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_to_address(self):
    self.__lsp_to_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-to-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_lsp_tunnel_id(self):
    """
    Getter method for lsp_tunnel_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_tunnel_id (uint32)

    YANG Description: LSP Tunnel ID
    """
    return self.__lsp_tunnel_id
      
  def _set_lsp_tunnel_id(self, v, load=False):
    """
    Setter method for lsp_tunnel_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_tunnel_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_tunnel_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_tunnel_id() directly.

    YANG Description: LSP Tunnel ID
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-tunnel-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_tunnel_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-tunnel-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__lsp_tunnel_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_tunnel_id(self):
    self.__lsp_tunnel_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-tunnel-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_lsp_lsp_id(self):
    """
    Getter method for lsp_lsp_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_lsp_id (uint32)

    YANG Description: LSP instance id or LSP ID
    """
    return self.__lsp_lsp_id
      
  def _set_lsp_lsp_id(self, v, load=False):
    """
    Setter method for lsp_lsp_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_lsp_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_lsp_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_lsp_id() directly.

    YANG Description: LSP instance id or LSP ID
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-lsp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_lsp_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-lsp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__lsp_lsp_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_lsp_id(self):
    self.__lsp_lsp_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-lsp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_lsp_admin_up(self):
    """
    Getter method for lsp_admin_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_admin_up (boolean)

    YANG Description: LSP Admin State
    """
    return self.__lsp_admin_up
      
  def _set_lsp_admin_up(self, v, load=False):
    """
    Setter method for lsp_admin_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_admin_up (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_admin_up is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_admin_up() directly.

    YANG Description: LSP Admin State
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-admin-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_admin_up must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-admin-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_admin_up = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_admin_up(self):
    self.__lsp_admin_up = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-admin-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_operational_up(self):
    """
    Getter method for lsp_operational_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_operational_up (boolean)

    YANG Description: LSP operational-state
    """
    return self.__lsp_operational_up
      
  def _set_lsp_operational_up(self, v, load=False):
    """
    Setter method for lsp_operational_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_operational_up (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_operational_up is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_operational_up() directly.

    YANG Description: LSP operational-state
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-operational-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_operational_up must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-operational-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_operational_up = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_operational_up(self):
    self.__lsp_operational_up = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-operational-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_is_active(self):
    """
    Getter method for lsp_is_active, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_is_active (boolean)

    YANG Description: LSP operational and active
    """
    return self.__lsp_is_active
      
  def _set_lsp_is_active(self, v, load=False):
    """
    Setter method for lsp_is_active, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_is_active (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_is_active is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_is_active() directly.

    YANG Description: LSP operational and active
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-is-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_is_active must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-is-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_is_active = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_is_active(self):
    self.__lsp_is_active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-is-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_path_name(self):
    """
    Getter method for lsp_path_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_path_name (string)

    YANG Description: LSP path name
    """
    return self.__lsp_path_name
      
  def _set_lsp_path_name(self, v, load=False):
    """
    Setter method for lsp_path_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_path_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_path_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_path_name() directly.

    YANG Description: LSP path name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="lsp-path-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_path_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="lsp-path-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__lsp_path_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_path_name(self):
    self.__lsp_path_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="lsp-path-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_lsp_out_label(self):
    """
    Getter method for lsp_out_label, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_out_label (uint32)

    YANG Description: LSP out label
    """
    return self.__lsp_out_label
      
  def _set_lsp_out_label(self, v, load=False):
    """
    Setter method for lsp_out_label, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_out_label (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_out_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_out_label() directly.

    YANG Description: LSP out label
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_out_label must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__lsp_out_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_out_label(self):
    self.__lsp_out_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_lsp_out_interface_name(self):
    """
    Getter method for lsp_out_interface_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_out_interface_name (string)

    YANG Description: LSP outgoing interface name
    """
    return self.__lsp_out_interface_name
      
  def _set_lsp_out_interface_name(self, v, load=False):
    """
    Setter method for lsp_out_interface_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_bypass_lsp_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_basic_info/lsp_out_interface_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_out_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_out_interface_name() directly.

    YANG Description: LSP outgoing interface name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="lsp-out-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_out_interface_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="lsp-out-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__lsp_out_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_out_interface_name(self):
    self.__lsp_out_interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="lsp-out-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)

  lsp_name = __builtin__.property(_get_lsp_name, _set_lsp_name)
  lsp_type_bypass = __builtin__.property(_get_lsp_type_bypass, _set_lsp_type_bypass)
  lsp_type_dynamic = __builtin__.property(_get_lsp_type_dynamic, _set_lsp_type_dynamic)
  lsp_from_address = __builtin__.property(_get_lsp_from_address, _set_lsp_from_address)
  lsp_to_address = __builtin__.property(_get_lsp_to_address, _set_lsp_to_address)
  lsp_tunnel_id = __builtin__.property(_get_lsp_tunnel_id, _set_lsp_tunnel_id)
  lsp_lsp_id = __builtin__.property(_get_lsp_lsp_id, _set_lsp_lsp_id)
  lsp_admin_up = __builtin__.property(_get_lsp_admin_up, _set_lsp_admin_up)
  lsp_operational_up = __builtin__.property(_get_lsp_operational_up, _set_lsp_operational_up)
  lsp_is_active = __builtin__.property(_get_lsp_is_active, _set_lsp_is_active)
  lsp_path_name = __builtin__.property(_get_lsp_path_name, _set_lsp_path_name)
  lsp_out_label = __builtin__.property(_get_lsp_out_label, _set_lsp_out_label)
  lsp_out_interface_name = __builtin__.property(_get_lsp_out_interface_name, _set_lsp_out_interface_name)


  _pyangbind_elements = {'lsp_name': lsp_name, 'lsp_type_bypass': lsp_type_bypass, 'lsp_type_dynamic': lsp_type_dynamic, 'lsp_from_address': lsp_from_address, 'lsp_to_address': lsp_to_address, 'lsp_tunnel_id': lsp_tunnel_id, 'lsp_lsp_id': lsp_lsp_id, 'lsp_admin_up': lsp_admin_up, 'lsp_operational_up': lsp_operational_up, 'lsp_is_active': lsp_is_active, 'lsp_path_name': lsp_path_name, 'lsp_out_label': lsp_out_label, 'lsp_out_interface_name': lsp_out_interface_name, }


