
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import l2_hop_results
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-trilloam - based on the path /brocade_trilloam_rpc/l2traceroute-result/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__l2_hop_results','__l2traceroutedone','__reason',)

  _yang_name = 'output'
  _rest_name = 'output'

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
    self.__reason = YANGDynClass(base=unicode, is_leaf=True, yang_name="reason", rest_name="reason", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='string', is_config=True)
    self.__l2_hop_results = YANGDynClass(base=YANGListType(False,l2_hop_results.l2_hop_results, yang_name="l2-hop-results", rest_name="l2-hop-results", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="l2-hop-results", rest_name="l2-hop-results", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='list', is_config=True)
    self.__l2traceroutedone = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l2traceroutedone", rest_name="l2traceroutedone", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='boolean', is_config=True)

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
      return [u'brocade_trilloam_rpc', u'l2traceroute-result', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'l2traceroute-result', u'output']

  def _get_l2_hop_results(self):
    """
    Getter method for l2_hop_results, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute_result/output/l2_hop_results (list)
    """
    return self.__l2_hop_results
      
  def _set_l2_hop_results(self, v, load=False):
    """
    Setter method for l2_hop_results, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute_result/output/l2_hop_results (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l2_hop_results is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l2_hop_results() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType(False,l2_hop_results.l2_hop_results, yang_name="l2-hop-results", rest_name="l2-hop-results", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="l2-hop-results", rest_name="l2-hop-results", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l2_hop_results must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,l2_hop_results.l2_hop_results, yang_name="l2-hop-results", rest_name="l2-hop-results", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="l2-hop-results", rest_name="l2-hop-results", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='list', is_config=True)""",
        })

    self.__l2_hop_results = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l2_hop_results(self):
    self.__l2_hop_results = YANGDynClass(base=YANGListType(False,l2_hop_results.l2_hop_results, yang_name="l2-hop-results", rest_name="l2-hop-results", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="l2-hop-results", rest_name="l2-hop-results", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='list', is_config=True)


  def _get_l2traceroutedone(self):
    """
    Getter method for l2traceroutedone, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute_result/output/l2traceroutedone (boolean)

    YANG Description: Indicates that this is the final response
    """
    return self.__l2traceroutedone
      
  def _set_l2traceroutedone(self, v, load=False):
    """
    Setter method for l2traceroutedone, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute_result/output/l2traceroutedone (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l2traceroutedone is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l2traceroutedone() directly.

    YANG Description: Indicates that this is the final response
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="l2traceroutedone", rest_name="l2traceroutedone", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l2traceroutedone must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l2traceroutedone", rest_name="l2traceroutedone", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='boolean', is_config=True)""",
        })

    self.__l2traceroutedone = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l2traceroutedone(self):
    self.__l2traceroutedone = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="l2traceroutedone", rest_name="l2traceroutedone", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='boolean', is_config=True)


  def _get_reason(self):
    """
    Getter method for reason, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute_result/output/reason (string)

    YANG Description: Reason for this return, error string or success
    """
    return self.__reason
      
  def _set_reason(self, v, load=False):
    """
    Setter method for reason, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute_result/output/reason (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reason is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reason() directly.

    YANG Description: Reason for this return, error string or success
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="reason", rest_name="reason", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reason must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="reason", rest_name="reason", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='string', is_config=True)""",
        })

    self.__reason = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reason(self):
    self.__reason = YANGDynClass(base=unicode, is_leaf=True, yang_name="reason", rest_name="reason", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='string', is_config=True)

  l2_hop_results = __builtin__.property(_get_l2_hop_results, _set_l2_hop_results)
  l2traceroutedone = __builtin__.property(_get_l2traceroutedone, _set_l2traceroutedone)
  reason = __builtin__.property(_get_reason, _set_reason)


  _pyangbind_elements = {'l2_hop_results': l2_hop_results, 'l2traceroutedone': l2traceroutedone, 'reason': reason, }


