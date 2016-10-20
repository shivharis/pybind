
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class mpls_ldp_database_upstream(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/ldp-database/mpls-ldp-database-upstream. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: ldp database upstream
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mpls_ldp_database_us_fec_label','__mpls_ldp_database_us_fec_prefix','__mpls_ldp_database_us_fec_prefix_length','__mpls_ldp_database_us_fec_type','__mpls_ldp_database_us_fec_stale',)

  _yang_name = 'mpls-ldp-database-upstream'
  _rest_name = 'mpls-ldp-database-upstream'

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
    self.__mpls_ldp_database_us_fec_stale = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-ldp-database-us-fec-stale", rest_name="mpls-ldp-database-us-fec-stale", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    self.__mpls_ldp_database_us_fec_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-ldp-database-us-fec-prefix", rest_name="mpls-ldp-database-us-fec-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__mpls_ldp_database_us_fec_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-ldp-database-us-fec-label", rest_name="mpls-ldp-database-us-fec-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__mpls_ldp_database_us_fec_prefix_length = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-ldp-database-us-fec-prefix-length", rest_name="mpls-ldp-database-us-fec-prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__mpls_ldp_database_us_fec_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-ldp-database-us-fec-type", rest_name="mpls-ldp-database-us-fec-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

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
      return [u'mpls-state', u'ldp', u'ldp-database', u'mpls-ldp-database-upstream']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'ldp', u'ldp-database', u'mpls-ldp-database-upstream']

  def _get_mpls_ldp_database_us_fec_label(self):
    """
    Getter method for mpls_ldp_database_us_fec_label, mapped from YANG variable /mpls_state/ldp/ldp_database/mpls_ldp_database_upstream/mpls_ldp_database_us_fec_label (uint32)

    YANG Description: mpls ldp database fec label 
    """
    return self.__mpls_ldp_database_us_fec_label
      
  def _set_mpls_ldp_database_us_fec_label(self, v, load=False):
    """
    Setter method for mpls_ldp_database_us_fec_label, mapped from YANG variable /mpls_state/ldp/ldp_database/mpls_ldp_database_upstream/mpls_ldp_database_us_fec_label (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_ldp_database_us_fec_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_ldp_database_us_fec_label() directly.

    YANG Description: mpls ldp database fec label 
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-ldp-database-us-fec-label", rest_name="mpls-ldp-database-us-fec-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_ldp_database_us_fec_label must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-ldp-database-us-fec-label", rest_name="mpls-ldp-database-us-fec-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__mpls_ldp_database_us_fec_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_ldp_database_us_fec_label(self):
    self.__mpls_ldp_database_us_fec_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-ldp-database-us-fec-label", rest_name="mpls-ldp-database-us-fec-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_mpls_ldp_database_us_fec_prefix(self):
    """
    Getter method for mpls_ldp_database_us_fec_prefix, mapped from YANG variable /mpls_state/ldp/ldp_database/mpls_ldp_database_upstream/mpls_ldp_database_us_fec_prefix (inet:ipv4-address)

    YANG Description: mpls ldp database fec prefix 
    """
    return self.__mpls_ldp_database_us_fec_prefix
      
  def _set_mpls_ldp_database_us_fec_prefix(self, v, load=False):
    """
    Setter method for mpls_ldp_database_us_fec_prefix, mapped from YANG variable /mpls_state/ldp/ldp_database/mpls_ldp_database_upstream/mpls_ldp_database_us_fec_prefix (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_ldp_database_us_fec_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_ldp_database_us_fec_prefix() directly.

    YANG Description: mpls ldp database fec prefix 
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-ldp-database-us-fec-prefix", rest_name="mpls-ldp-database-us-fec-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_ldp_database_us_fec_prefix must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-ldp-database-us-fec-prefix", rest_name="mpls-ldp-database-us-fec-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__mpls_ldp_database_us_fec_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_ldp_database_us_fec_prefix(self):
    self.__mpls_ldp_database_us_fec_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-ldp-database-us-fec-prefix", rest_name="mpls-ldp-database-us-fec-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_mpls_ldp_database_us_fec_prefix_length(self):
    """
    Getter method for mpls_ldp_database_us_fec_prefix_length, mapped from YANG variable /mpls_state/ldp/ldp_database/mpls_ldp_database_upstream/mpls_ldp_database_us_fec_prefix_length (uint32)

    YANG Description: mpls ldp database fec prefix length 
    """
    return self.__mpls_ldp_database_us_fec_prefix_length
      
  def _set_mpls_ldp_database_us_fec_prefix_length(self, v, load=False):
    """
    Setter method for mpls_ldp_database_us_fec_prefix_length, mapped from YANG variable /mpls_state/ldp/ldp_database/mpls_ldp_database_upstream/mpls_ldp_database_us_fec_prefix_length (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_ldp_database_us_fec_prefix_length is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_ldp_database_us_fec_prefix_length() directly.

    YANG Description: mpls ldp database fec prefix length 
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-ldp-database-us-fec-prefix-length", rest_name="mpls-ldp-database-us-fec-prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_ldp_database_us_fec_prefix_length must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-ldp-database-us-fec-prefix-length", rest_name="mpls-ldp-database-us-fec-prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__mpls_ldp_database_us_fec_prefix_length = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_ldp_database_us_fec_prefix_length(self):
    self.__mpls_ldp_database_us_fec_prefix_length = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-ldp-database-us-fec-prefix-length", rest_name="mpls-ldp-database-us-fec-prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_mpls_ldp_database_us_fec_type(self):
    """
    Getter method for mpls_ldp_database_us_fec_type, mapped from YANG variable /mpls_state/ldp/ldp_database/mpls_ldp_database_upstream/mpls_ldp_database_us_fec_type (uint32)

    YANG Description: mpls ldp database fec type  
    """
    return self.__mpls_ldp_database_us_fec_type
      
  def _set_mpls_ldp_database_us_fec_type(self, v, load=False):
    """
    Setter method for mpls_ldp_database_us_fec_type, mapped from YANG variable /mpls_state/ldp/ldp_database/mpls_ldp_database_upstream/mpls_ldp_database_us_fec_type (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_ldp_database_us_fec_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_ldp_database_us_fec_type() directly.

    YANG Description: mpls ldp database fec type  
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-ldp-database-us-fec-type", rest_name="mpls-ldp-database-us-fec-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_ldp_database_us_fec_type must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-ldp-database-us-fec-type", rest_name="mpls-ldp-database-us-fec-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__mpls_ldp_database_us_fec_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_ldp_database_us_fec_type(self):
    self.__mpls_ldp_database_us_fec_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-ldp-database-us-fec-type", rest_name="mpls-ldp-database-us-fec-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_mpls_ldp_database_us_fec_stale(self):
    """
    Getter method for mpls_ldp_database_us_fec_stale, mapped from YANG variable /mpls_state/ldp/ldp_database/mpls_ldp_database_upstream/mpls_ldp_database_us_fec_stale (boolean)

    YANG Description: mpls ldp database fec stale  
    """
    return self.__mpls_ldp_database_us_fec_stale
      
  def _set_mpls_ldp_database_us_fec_stale(self, v, load=False):
    """
    Setter method for mpls_ldp_database_us_fec_stale, mapped from YANG variable /mpls_state/ldp/ldp_database/mpls_ldp_database_upstream/mpls_ldp_database_us_fec_stale (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_ldp_database_us_fec_stale is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_ldp_database_us_fec_stale() directly.

    YANG Description: mpls ldp database fec stale  
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mpls-ldp-database-us-fec-stale", rest_name="mpls-ldp-database-us-fec-stale", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_ldp_database_us_fec_stale must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-ldp-database-us-fec-stale", rest_name="mpls-ldp-database-us-fec-stale", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__mpls_ldp_database_us_fec_stale = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_ldp_database_us_fec_stale(self):
    self.__mpls_ldp_database_us_fec_stale = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-ldp-database-us-fec-stale", rest_name="mpls-ldp-database-us-fec-stale", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)

  mpls_ldp_database_us_fec_label = __builtin__.property(_get_mpls_ldp_database_us_fec_label)
  mpls_ldp_database_us_fec_prefix = __builtin__.property(_get_mpls_ldp_database_us_fec_prefix)
  mpls_ldp_database_us_fec_prefix_length = __builtin__.property(_get_mpls_ldp_database_us_fec_prefix_length)
  mpls_ldp_database_us_fec_type = __builtin__.property(_get_mpls_ldp_database_us_fec_type)
  mpls_ldp_database_us_fec_stale = __builtin__.property(_get_mpls_ldp_database_us_fec_stale)


  _pyangbind_elements = {'mpls_ldp_database_us_fec_label': mpls_ldp_database_us_fec_label, 'mpls_ldp_database_us_fec_prefix': mpls_ldp_database_us_fec_prefix, 'mpls_ldp_database_us_fec_prefix_length': mpls_ldp_database_us_fec_prefix_length, 'mpls_ldp_database_us_fec_type': mpls_ldp_database_us_fec_type, 'mpls_ldp_database_us_fec_stale': mpls_ldp_database_us_fec_stale, }


