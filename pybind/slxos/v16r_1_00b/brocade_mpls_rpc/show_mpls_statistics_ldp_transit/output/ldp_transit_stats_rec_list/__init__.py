
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ldp_transit_stats_rec_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-statistics-ldp-transit/output/ldp-transit-stats-rec-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ldp_transit_stats_prefix_fec','__ldp_transit_stats_packet_count','__ldp_transit_stats_byte_count','__ldp_transit_stats_rate_kbps',)

  _yang_name = 'ldp-transit-stats-rec-list'
  _rest_name = 'ldp-transit-stats-rec-list'

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
    self.__ldp_transit_stats_byte_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-transit-stats-byte-count", rest_name="ldp-transit-stats-byte-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)
    self.__ldp_transit_stats_rate_kbps = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-transit-stats-rate-kbps", rest_name="ldp-transit-stats-rate-kbps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)
    self.__ldp_transit_stats_prefix_fec = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-transit-stats-prefix-fec", rest_name="ldp-transit-stats-prefix-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__ldp_transit_stats_packet_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-transit-stats-packet-count", rest_name="ldp-transit-stats-packet-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-statistics-ldp-transit', u'output', u'ldp-transit-stats-rec-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-statistics-ldp-transit', u'output', u'ldp-transit-stats-rec-list']

  def _get_ldp_transit_stats_prefix_fec(self):
    """
    Getter method for ldp_transit_stats_prefix_fec, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_transit/output/ldp_transit_stats_rec_list/ldp_transit_stats_prefix_fec (inet:ipv4-address)

    YANG Description: Prefix FEC
    """
    return self.__ldp_transit_stats_prefix_fec
      
  def _set_ldp_transit_stats_prefix_fec(self, v, load=False):
    """
    Setter method for ldp_transit_stats_prefix_fec, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_transit/output/ldp_transit_stats_rec_list/ldp_transit_stats_prefix_fec (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_transit_stats_prefix_fec is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_transit_stats_prefix_fec() directly.

    YANG Description: Prefix FEC
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-transit-stats-prefix-fec", rest_name="ldp-transit-stats-prefix-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_transit_stats_prefix_fec must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-transit-stats-prefix-fec", rest_name="ldp-transit-stats-prefix-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__ldp_transit_stats_prefix_fec = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_transit_stats_prefix_fec(self):
    self.__ldp_transit_stats_prefix_fec = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-transit-stats-prefix-fec", rest_name="ldp-transit-stats-prefix-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_ldp_transit_stats_packet_count(self):
    """
    Getter method for ldp_transit_stats_packet_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_transit/output/ldp_transit_stats_rec_list/ldp_transit_stats_packet_count (uint64)

    YANG Description: Packet Count
    """
    return self.__ldp_transit_stats_packet_count
      
  def _set_ldp_transit_stats_packet_count(self, v, load=False):
    """
    Setter method for ldp_transit_stats_packet_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_transit/output/ldp_transit_stats_rec_list/ldp_transit_stats_packet_count (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_transit_stats_packet_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_transit_stats_packet_count() directly.

    YANG Description: Packet Count
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-transit-stats-packet-count", rest_name="ldp-transit-stats-packet-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_transit_stats_packet_count must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-transit-stats-packet-count", rest_name="ldp-transit-stats-packet-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)""",
        })

    self.__ldp_transit_stats_packet_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_transit_stats_packet_count(self):
    self.__ldp_transit_stats_packet_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-transit-stats-packet-count", rest_name="ldp-transit-stats-packet-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)


  def _get_ldp_transit_stats_byte_count(self):
    """
    Getter method for ldp_transit_stats_byte_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_transit/output/ldp_transit_stats_rec_list/ldp_transit_stats_byte_count (uint64)

    YANG Description: Byte Count
    """
    return self.__ldp_transit_stats_byte_count
      
  def _set_ldp_transit_stats_byte_count(self, v, load=False):
    """
    Setter method for ldp_transit_stats_byte_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_transit/output/ldp_transit_stats_rec_list/ldp_transit_stats_byte_count (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_transit_stats_byte_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_transit_stats_byte_count() directly.

    YANG Description: Byte Count
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-transit-stats-byte-count", rest_name="ldp-transit-stats-byte-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_transit_stats_byte_count must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-transit-stats-byte-count", rest_name="ldp-transit-stats-byte-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)""",
        })

    self.__ldp_transit_stats_byte_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_transit_stats_byte_count(self):
    self.__ldp_transit_stats_byte_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-transit-stats-byte-count", rest_name="ldp-transit-stats-byte-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)


  def _get_ldp_transit_stats_rate_kbps(self):
    """
    Getter method for ldp_transit_stats_rate_kbps, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_transit/output/ldp_transit_stats_rec_list/ldp_transit_stats_rate_kbps (uint64)

    YANG Description: Rate in Kbps
    """
    return self.__ldp_transit_stats_rate_kbps
      
  def _set_ldp_transit_stats_rate_kbps(self, v, load=False):
    """
    Setter method for ldp_transit_stats_rate_kbps, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_transit/output/ldp_transit_stats_rec_list/ldp_transit_stats_rate_kbps (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_transit_stats_rate_kbps is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_transit_stats_rate_kbps() directly.

    YANG Description: Rate in Kbps
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-transit-stats-rate-kbps", rest_name="ldp-transit-stats-rate-kbps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_transit_stats_rate_kbps must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-transit-stats-rate-kbps", rest_name="ldp-transit-stats-rate-kbps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)""",
        })

    self.__ldp_transit_stats_rate_kbps = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_transit_stats_rate_kbps(self):
    self.__ldp_transit_stats_rate_kbps = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-transit-stats-rate-kbps", rest_name="ldp-transit-stats-rate-kbps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)

  ldp_transit_stats_prefix_fec = __builtin__.property(_get_ldp_transit_stats_prefix_fec, _set_ldp_transit_stats_prefix_fec)
  ldp_transit_stats_packet_count = __builtin__.property(_get_ldp_transit_stats_packet_count, _set_ldp_transit_stats_packet_count)
  ldp_transit_stats_byte_count = __builtin__.property(_get_ldp_transit_stats_byte_count, _set_ldp_transit_stats_byte_count)
  ldp_transit_stats_rate_kbps = __builtin__.property(_get_ldp_transit_stats_rate_kbps, _set_ldp_transit_stats_rate_kbps)


  _pyangbind_elements = {'ldp_transit_stats_prefix_fec': ldp_transit_stats_prefix_fec, 'ldp_transit_stats_packet_count': ldp_transit_stats_packet_count, 'ldp_transit_stats_byte_count': ldp_transit_stats_byte_count, 'ldp_transit_stats_rate_kbps': ldp_transit_stats_rate_kbps, }


