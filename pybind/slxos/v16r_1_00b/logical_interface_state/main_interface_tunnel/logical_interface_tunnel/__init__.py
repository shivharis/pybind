
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class logical_interface_tunnel(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-nsm-operational - based on the path /logical-interface-state/main-interface-tunnel/logical-interface-tunnel. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: logical interface tunnel
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__logical_interface_name','__source_type','__protocol_status','__admin_status','__lif_index','__bridge_domain_index','__interface_name','__is_binded','__vni_tni',)

  _yang_name = 'logical-interface-tunnel'

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
    self.__vni_tni = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vni-tni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    self.__lif_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lif-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    self.__bridge_domain_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bridge-domain-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    self.__protocol_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protocol-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)
    self.__source_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="source-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    self.__admin_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)
    self.__is_binded = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-binded", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)
    self.__logical_interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="logical-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    self.__interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)

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
      return [u'logical-interface-state', u'main-interface-tunnel', u'logical-interface-tunnel']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'logical-interface-state', u'main-interface-tunnel', u'logical-interface-tunnel']

  def _get_logical_interface_name(self):
    """
    Getter method for logical_interface_name, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/logical_interface_name (string)

    YANG Description: Logical Interface name
    """
    return self.__logical_interface_name
      
  def _set_logical_interface_name(self, v, load=False):
    """
    Setter method for logical_interface_name, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/logical_interface_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_logical_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_logical_interface_name() directly.

    YANG Description: Logical Interface name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="logical-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """logical_interface_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="logical-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)""",
        })

    self.__logical_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_logical_interface_name(self):
    self.__logical_interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="logical-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)


  def _get_source_type(self):
    """
    Getter method for source_type, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/source_type (string)

    YANG Description: source type
    """
    return self.__source_type
      
  def _set_source_type(self, v, load=False):
    """
    Setter method for source_type, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/source_type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_type() directly.

    YANG Description: source type
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="source-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="source-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)""",
        })

    self.__source_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_type(self):
    self.__source_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="source-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)


  def _get_protocol_status(self):
    """
    Getter method for protocol_status, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/protocol_status (boolean)

    YANG Description: Protocol Status
    """
    return self.__protocol_status
      
  def _set_protocol_status(self, v, load=False):
    """
    Setter method for protocol_status, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/protocol_status (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol_status() directly.

    YANG Description: Protocol Status
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="protocol-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol_status must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protocol-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)""",
        })

    self.__protocol_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol_status(self):
    self.__protocol_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protocol-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)


  def _get_admin_status(self):
    """
    Getter method for admin_status, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/admin_status (boolean)

    YANG Description: Admin Status
    """
    return self.__admin_status
      
  def _set_admin_status(self, v, load=False):
    """
    Setter method for admin_status, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/admin_status (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_admin_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_admin_status() directly.

    YANG Description: Admin Status
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """admin_status must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)""",
        })

    self.__admin_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_admin_status(self):
    self.__admin_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)


  def _get_lif_index(self):
    """
    Getter method for lif_index, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/lif_index (uint32)

    YANG Description: Lif index
    """
    return self.__lif_index
      
  def _set_lif_index(self, v, load=False):
    """
    Setter method for lif_index, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/lif_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lif_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lif_index() directly.

    YANG Description: Lif index
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lif-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lif_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lif-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__lif_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lif_index(self):
    self.__lif_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lif-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)


  def _get_bridge_domain_index(self):
    """
    Getter method for bridge_domain_index, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/bridge_domain_index (uint32)

    YANG Description: Bridge Domain index
    """
    return self.__bridge_domain_index
      
  def _set_bridge_domain_index(self, v, load=False):
    """
    Setter method for bridge_domain_index, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/bridge_domain_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bridge_domain_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bridge_domain_index() directly.

    YANG Description: Bridge Domain index
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bridge-domain-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bridge_domain_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bridge-domain-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__bridge_domain_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bridge_domain_index(self):
    self.__bridge_domain_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bridge-domain-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)


  def _get_interface_name(self):
    """
    Getter method for interface_name, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/interface_name (string)

    YANG Description: interface name
    """
    return self.__interface_name
      
  def _set_interface_name(self, v, load=False):
    """
    Setter method for interface_name, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/interface_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_name() directly.

    YANG Description: interface name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)""",
        })

    self.__interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_name(self):
    self.__interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)


  def _get_is_binded(self):
    """
    Getter method for is_binded, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/is_binded (boolean)

    YANG Description: Is the lif binded
    """
    return self.__is_binded
      
  def _set_is_binded(self, v, load=False):
    """
    Setter method for is_binded, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/is_binded (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_is_binded is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_is_binded() directly.

    YANG Description: Is the lif binded
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="is-binded", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """is_binded must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-binded", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)""",
        })

    self.__is_binded = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_is_binded(self):
    self.__is_binded = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-binded", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)


  def _get_vni_tni(self):
    """
    Getter method for vni_tni, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/vni_tni (uint32)

    YANG Description: VNI or TNI
    """
    return self.__vni_tni
      
  def _set_vni_tni(self, v, load=False):
    """
    Setter method for vni_tni, mapped from YANG variable /logical_interface_state/main_interface_tunnel/logical_interface_tunnel/vni_tni (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vni_tni is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vni_tni() directly.

    YANG Description: VNI or TNI
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vni-tni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vni_tni must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vni-tni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__vni_tni = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vni_tni(self):
    self.__vni_tni = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vni-tni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)

  logical_interface_name = __builtin__.property(_get_logical_interface_name)
  source_type = __builtin__.property(_get_source_type)
  protocol_status = __builtin__.property(_get_protocol_status)
  admin_status = __builtin__.property(_get_admin_status)
  lif_index = __builtin__.property(_get_lif_index)
  bridge_domain_index = __builtin__.property(_get_bridge_domain_index)
  interface_name = __builtin__.property(_get_interface_name)
  is_binded = __builtin__.property(_get_is_binded)
  vni_tni = __builtin__.property(_get_vni_tni)


  _pyangbind_elements = {'logical_interface_name': logical_interface_name, 'source_type': source_type, 'protocol_status': protocol_status, 'admin_status': admin_status, 'lif_index': lif_index, 'bridge_domain_index': bridge_domain_index, 'interface_name': interface_name, 'is_binded': is_binded, 'vni_tni': vni_tni, }


