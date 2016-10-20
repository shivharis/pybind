
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class bridge_domain_counter(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-nsm-operational - based on the path /bridge-domain-state/bridge-domain-counter. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description:  bridge_domain_counter
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__no_of_bd','__no_of_vpls_bd','__no_of_dynamic_mac','__no_of_static_mac',)

  _yang_name = 'bridge-domain-counter'
  _rest_name = 'bridge-domain-counter'

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
    self.__no_of_dynamic_mac = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-dynamic-mac", rest_name="no-of-dynamic-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    self.__no_of_vpls_bd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-vpls-bd", rest_name="no-of-vpls-bd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    self.__no_of_bd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-bd", rest_name="no-of-bd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    self.__no_of_static_mac = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-static-mac", rest_name="no-of-static-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)

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
      return [u'bridge-domain-state', u'bridge-domain-counter']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'bridge-domain-state', u'bridge-domain-counter']

  def _get_no_of_bd(self):
    """
    Getter method for no_of_bd, mapped from YANG variable /bridge_domain_state/bridge_domain_counter/no_of_bd (uint32)

    YANG Description: no_of_bd
    """
    return self.__no_of_bd
      
  def _set_no_of_bd(self, v, load=False):
    """
    Setter method for no_of_bd, mapped from YANG variable /bridge_domain_state/bridge_domain_counter/no_of_bd (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_of_bd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_of_bd() directly.

    YANG Description: no_of_bd
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-bd", rest_name="no-of-bd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_of_bd must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-bd", rest_name="no-of-bd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__no_of_bd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_of_bd(self):
    self.__no_of_bd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-bd", rest_name="no-of-bd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)


  def _get_no_of_vpls_bd(self):
    """
    Getter method for no_of_vpls_bd, mapped from YANG variable /bridge_domain_state/bridge_domain_counter/no_of_vpls_bd (uint32)

    YANG Description: no_of_vpls_bd
    """
    return self.__no_of_vpls_bd
      
  def _set_no_of_vpls_bd(self, v, load=False):
    """
    Setter method for no_of_vpls_bd, mapped from YANG variable /bridge_domain_state/bridge_domain_counter/no_of_vpls_bd (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_of_vpls_bd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_of_vpls_bd() directly.

    YANG Description: no_of_vpls_bd
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-vpls-bd", rest_name="no-of-vpls-bd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_of_vpls_bd must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-vpls-bd", rest_name="no-of-vpls-bd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__no_of_vpls_bd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_of_vpls_bd(self):
    self.__no_of_vpls_bd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-vpls-bd", rest_name="no-of-vpls-bd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)


  def _get_no_of_dynamic_mac(self):
    """
    Getter method for no_of_dynamic_mac, mapped from YANG variable /bridge_domain_state/bridge_domain_counter/no_of_dynamic_mac (uint32)

    YANG Description: no_of_dynamic_mac
    """
    return self.__no_of_dynamic_mac
      
  def _set_no_of_dynamic_mac(self, v, load=False):
    """
    Setter method for no_of_dynamic_mac, mapped from YANG variable /bridge_domain_state/bridge_domain_counter/no_of_dynamic_mac (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_of_dynamic_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_of_dynamic_mac() directly.

    YANG Description: no_of_dynamic_mac
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-dynamic-mac", rest_name="no-of-dynamic-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_of_dynamic_mac must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-dynamic-mac", rest_name="no-of-dynamic-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__no_of_dynamic_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_of_dynamic_mac(self):
    self.__no_of_dynamic_mac = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-dynamic-mac", rest_name="no-of-dynamic-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)


  def _get_no_of_static_mac(self):
    """
    Getter method for no_of_static_mac, mapped from YANG variable /bridge_domain_state/bridge_domain_counter/no_of_static_mac (uint32)

    YANG Description: no_of_static_mac
    """
    return self.__no_of_static_mac
      
  def _set_no_of_static_mac(self, v, load=False):
    """
    Setter method for no_of_static_mac, mapped from YANG variable /bridge_domain_state/bridge_domain_counter/no_of_static_mac (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_of_static_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_of_static_mac() directly.

    YANG Description: no_of_static_mac
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-static-mac", rest_name="no-of-static-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_of_static_mac must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-static-mac", rest_name="no-of-static-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__no_of_static_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_of_static_mac(self):
    self.__no_of_static_mac = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-static-mac", rest_name="no-of-static-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)

  no_of_bd = __builtin__.property(_get_no_of_bd)
  no_of_vpls_bd = __builtin__.property(_get_no_of_vpls_bd)
  no_of_dynamic_mac = __builtin__.property(_get_no_of_dynamic_mac)
  no_of_static_mac = __builtin__.property(_get_no_of_static_mac)


  _pyangbind_elements = {'no_of_bd': no_of_bd, 'no_of_vpls_bd': no_of_vpls_bd, 'no_of_dynamic_mac': no_of_dynamic_mac, 'no_of_static_mac': no_of_static_mac, }


