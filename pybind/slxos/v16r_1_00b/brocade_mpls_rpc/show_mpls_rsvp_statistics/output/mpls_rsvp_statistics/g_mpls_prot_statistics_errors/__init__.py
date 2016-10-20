
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class g_mpls_prot_statistics_errors(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-rsvp-statistics/output/mpls-rsvp-statistics/g_mpls_prot_statistics_errors. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Error statistics for MPLS PROT control packets
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__error_type_name','__error_type_count_rx','__error_type_count_since_last_cleared_rx',)

  _yang_name = 'g_mpls_prot_statistics_errors'
  _rest_name = 'g_mpls_prot_statistics_errors'

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
    self.__error_type_count_rx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="error_type_count_rx", rest_name="error_type_count_rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__error_type_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="error_type_name", rest_name="error_type_name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__error_type_count_since_last_cleared_rx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="error_type_count_since_last_cleared_rx", rest_name="error_type_count_since_last_cleared_rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-rsvp-statistics', u'output', u'mpls-rsvp-statistics', u'g_mpls_prot_statistics_errors']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-rsvp-statistics', u'output', u'mpls-rsvp-statistics', u'g_mpls_prot_statistics_errors']

  def _get_error_type_name(self):
    """
    Getter method for error_type_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_statistics/output/mpls_rsvp_statistics/g_mpls_prot_statistics_errors/error_type_name (string)

    YANG Description: Error descriptor
    """
    return self.__error_type_name
      
  def _set_error_type_name(self, v, load=False):
    """
    Setter method for error_type_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_statistics/output/mpls_rsvp_statistics/g_mpls_prot_statistics_errors/error_type_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_error_type_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_error_type_name() directly.

    YANG Description: Error descriptor
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="error_type_name", rest_name="error_type_name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """error_type_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="error_type_name", rest_name="error_type_name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__error_type_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_error_type_name(self):
    self.__error_type_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="error_type_name", rest_name="error_type_name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_error_type_count_rx(self):
    """
    Getter method for error_type_count_rx, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_statistics/output/mpls_rsvp_statistics/g_mpls_prot_statistics_errors/error_type_count_rx (uint32)

    YANG Description: Packet count RX
    """
    return self.__error_type_count_rx
      
  def _set_error_type_count_rx(self, v, load=False):
    """
    Setter method for error_type_count_rx, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_statistics/output/mpls_rsvp_statistics/g_mpls_prot_statistics_errors/error_type_count_rx (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_error_type_count_rx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_error_type_count_rx() directly.

    YANG Description: Packet count RX
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="error_type_count_rx", rest_name="error_type_count_rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """error_type_count_rx must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="error_type_count_rx", rest_name="error_type_count_rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__error_type_count_rx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_error_type_count_rx(self):
    self.__error_type_count_rx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="error_type_count_rx", rest_name="error_type_count_rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_error_type_count_since_last_cleared_rx(self):
    """
    Getter method for error_type_count_since_last_cleared_rx, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_statistics/output/mpls_rsvp_statistics/g_mpls_prot_statistics_errors/error_type_count_since_last_cleared_rx (uint32)

    YANG Description: Packet count since last cleared RX
    """
    return self.__error_type_count_since_last_cleared_rx
      
  def _set_error_type_count_since_last_cleared_rx(self, v, load=False):
    """
    Setter method for error_type_count_since_last_cleared_rx, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_statistics/output/mpls_rsvp_statistics/g_mpls_prot_statistics_errors/error_type_count_since_last_cleared_rx (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_error_type_count_since_last_cleared_rx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_error_type_count_since_last_cleared_rx() directly.

    YANG Description: Packet count since last cleared RX
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="error_type_count_since_last_cleared_rx", rest_name="error_type_count_since_last_cleared_rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """error_type_count_since_last_cleared_rx must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="error_type_count_since_last_cleared_rx", rest_name="error_type_count_since_last_cleared_rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__error_type_count_since_last_cleared_rx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_error_type_count_since_last_cleared_rx(self):
    self.__error_type_count_since_last_cleared_rx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="error_type_count_since_last_cleared_rx", rest_name="error_type_count_since_last_cleared_rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  error_type_name = __builtin__.property(_get_error_type_name, _set_error_type_name)
  error_type_count_rx = __builtin__.property(_get_error_type_count_rx, _set_error_type_count_rx)
  error_type_count_since_last_cleared_rx = __builtin__.property(_get_error_type_count_since_last_cleared_rx, _set_error_type_count_since_last_cleared_rx)


  _pyangbind_elements = {'error_type_name': error_type_name, 'error_type_count_rx': error_type_count_rx, 'error_type_count_since_last_cleared_rx': error_type_count_since_last_cleared_rx, }


