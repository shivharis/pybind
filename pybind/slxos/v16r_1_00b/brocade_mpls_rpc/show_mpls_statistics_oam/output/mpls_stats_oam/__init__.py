
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import reply_rc
class mpls_stats_oam(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-statistics-oam/output/mpls-stats-oam. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__usr_ping_count','__usr_traceroute_count','__req_sent','__req_recv','__req_timeout','__reply_sent','__reply_recv','__reply_rc',)

  _yang_name = 'mpls-stats-oam'

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
    self.__req_recv = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="req_recv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__usr_traceroute_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr_traceroute_count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__reply_rc = YANGDynClass(base=YANGListType(False,reply_rc.reply_rc, yang_name="reply_rc", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="reply_rc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    self.__req_timeout = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="req_timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__reply_recv = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reply_recv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__reply_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reply_sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__req_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="req_sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__usr_ping_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr_ping_count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-statistics-oam', u'output', u'mpls-stats-oam']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'show-mpls-statistics-oam', u'output', u'mpls-stats-oam']

  def _get_usr_ping_count(self):
    """
    Getter method for usr_ping_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/usr_ping_count (uint32)

    YANG Description: User ping request processed
    """
    return self.__usr_ping_count
      
  def _set_usr_ping_count(self, v, load=False):
    """
    Setter method for usr_ping_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/usr_ping_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_usr_ping_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_usr_ping_count() directly.

    YANG Description: User ping request processed
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr_ping_count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """usr_ping_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr_ping_count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__usr_ping_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_usr_ping_count(self):
    self.__usr_ping_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr_ping_count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_usr_traceroute_count(self):
    """
    Getter method for usr_traceroute_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/usr_traceroute_count (uint32)

    YANG Description: User traceroute request processed
    """
    return self.__usr_traceroute_count
      
  def _set_usr_traceroute_count(self, v, load=False):
    """
    Setter method for usr_traceroute_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/usr_traceroute_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_usr_traceroute_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_usr_traceroute_count() directly.

    YANG Description: User traceroute request processed
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr_traceroute_count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """usr_traceroute_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr_traceroute_count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__usr_traceroute_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_usr_traceroute_count(self):
    self.__usr_traceroute_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usr_traceroute_count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_req_sent(self):
    """
    Getter method for req_sent, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/req_sent (uint32)

    YANG Description: Echo requests sent
    """
    return self.__req_sent
      
  def _set_req_sent(self, v, load=False):
    """
    Setter method for req_sent, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/req_sent (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_req_sent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_req_sent() directly.

    YANG Description: Echo requests sent
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="req_sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """req_sent must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="req_sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__req_sent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_req_sent(self):
    self.__req_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="req_sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_req_recv(self):
    """
    Getter method for req_recv, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/req_recv (uint32)

    YANG Description: Echo requests received
    """
    return self.__req_recv
      
  def _set_req_recv(self, v, load=False):
    """
    Setter method for req_recv, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/req_recv (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_req_recv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_req_recv() directly.

    YANG Description: Echo requests received
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="req_recv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """req_recv must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="req_recv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__req_recv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_req_recv(self):
    self.__req_recv = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="req_recv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_req_timeout(self):
    """
    Getter method for req_timeout, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/req_timeout (uint32)

    YANG Description: Echo requests timedout
    """
    return self.__req_timeout
      
  def _set_req_timeout(self, v, load=False):
    """
    Setter method for req_timeout, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/req_timeout (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_req_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_req_timeout() directly.

    YANG Description: Echo requests timedout
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="req_timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """req_timeout must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="req_timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__req_timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_req_timeout(self):
    self.__req_timeout = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="req_timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_reply_sent(self):
    """
    Getter method for reply_sent, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/reply_sent (uint32)

    YANG Description: Echo replies sent
    """
    return self.__reply_sent
      
  def _set_reply_sent(self, v, load=False):
    """
    Setter method for reply_sent, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/reply_sent (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reply_sent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reply_sent() directly.

    YANG Description: Echo replies sent
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reply_sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reply_sent must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reply_sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__reply_sent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reply_sent(self):
    self.__reply_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reply_sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_reply_recv(self):
    """
    Getter method for reply_recv, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/reply_recv (uint32)

    YANG Description: Echo replies received
    """
    return self.__reply_recv
      
  def _set_reply_recv(self, v, load=False):
    """
    Setter method for reply_recv, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/reply_recv (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reply_recv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reply_recv() directly.

    YANG Description: Echo replies received
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reply_recv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reply_recv must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reply_recv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__reply_recv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reply_recv(self):
    self.__reply_recv = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reply_recv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_reply_rc(self):
    """
    Getter method for reply_rc, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/reply_rc (list)

    YANG Description: Echo reply return codes
    """
    return self.__reply_rc
      
  def _set_reply_rc(self, v, load=False):
    """
    Setter method for reply_rc, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_oam/output/mpls_stats_oam/reply_rc (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reply_rc is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reply_rc() directly.

    YANG Description: Echo reply return codes
    """
    try:
      t = YANGDynClass(v,base=YANGListType(False,reply_rc.reply_rc, yang_name="reply_rc", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="reply_rc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reply_rc must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,reply_rc.reply_rc, yang_name="reply_rc", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="reply_rc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)""",
        })

    self.__reply_rc = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reply_rc(self):
    self.__reply_rc = YANGDynClass(base=YANGListType(False,reply_rc.reply_rc, yang_name="reply_rc", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="reply_rc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)

  usr_ping_count = __builtin__.property(_get_usr_ping_count, _set_usr_ping_count)
  usr_traceroute_count = __builtin__.property(_get_usr_traceroute_count, _set_usr_traceroute_count)
  req_sent = __builtin__.property(_get_req_sent, _set_req_sent)
  req_recv = __builtin__.property(_get_req_recv, _set_req_recv)
  req_timeout = __builtin__.property(_get_req_timeout, _set_req_timeout)
  reply_sent = __builtin__.property(_get_reply_sent, _set_reply_sent)
  reply_recv = __builtin__.property(_get_reply_recv, _set_reply_recv)
  reply_rc = __builtin__.property(_get_reply_rc, _set_reply_rc)


  _pyangbind_elements = {'usr_ping_count': usr_ping_count, 'usr_traceroute_count': usr_traceroute_count, 'req_sent': req_sent, 'req_recv': req_recv, 'req_timeout': req_timeout, 'reply_sent': reply_sent, 'reply_recv': reply_recv, 'reply_rc': reply_rc, }

