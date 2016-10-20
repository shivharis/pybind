
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class xstp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-hardware - based on the path /hardware/custom-profile/kap-custom-profile/xstp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__xstp_hello_interval','__xstp_num_entry',)

  _yang_name = 'xstp'
  _rest_name = 'xstp'

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
    self.__xstp_num_entry = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 769']}), is_leaf=True, yang_name="xstp_num_entry", rest_name="num-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure number of XSTP keep-alive entries/per slot.', u'alt-name': u'num-entry'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='uint32', is_config=True)
    self.__xstp_hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1000 .. 6000']}), is_leaf=True, yang_name="xstp_hello_interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure xSTP hello interval.', u'alt-name': u'hello-interval'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='uint32', is_config=True)

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
      return [u'hardware', u'custom-profile', u'kap-custom-profile', u'xstp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'hardware', u'custom-profile', u'kap', u'xstp']

  def _get_xstp_hello_interval(self):
    """
    Getter method for xstp_hello_interval, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/xstp/xstp_hello_interval (uint32)
    """
    return self.__xstp_hello_interval
      
  def _set_xstp_hello_interval(self, v, load=False):
    """
    Setter method for xstp_hello_interval, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/xstp/xstp_hello_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_xstp_hello_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_xstp_hello_interval() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1000 .. 6000']}), is_leaf=True, yang_name="xstp_hello_interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure xSTP hello interval.', u'alt-name': u'hello-interval'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """xstp_hello_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1000 .. 6000']}), is_leaf=True, yang_name="xstp_hello_interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure xSTP hello interval.', u'alt-name': u'hello-interval'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='uint32', is_config=True)""",
        })

    self.__xstp_hello_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_xstp_hello_interval(self):
    self.__xstp_hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1000 .. 6000']}), is_leaf=True, yang_name="xstp_hello_interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure xSTP hello interval.', u'alt-name': u'hello-interval'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='uint32', is_config=True)


  def _get_xstp_num_entry(self):
    """
    Getter method for xstp_num_entry, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/xstp/xstp_num_entry (uint32)
    """
    return self.__xstp_num_entry
      
  def _set_xstp_num_entry(self, v, load=False):
    """
    Setter method for xstp_num_entry, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/xstp/xstp_num_entry (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_xstp_num_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_xstp_num_entry() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 769']}), is_leaf=True, yang_name="xstp_num_entry", rest_name="num-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure number of XSTP keep-alive entries/per slot.', u'alt-name': u'num-entry'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """xstp_num_entry must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 769']}), is_leaf=True, yang_name="xstp_num_entry", rest_name="num-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure number of XSTP keep-alive entries/per slot.', u'alt-name': u'num-entry'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='uint32', is_config=True)""",
        })

    self.__xstp_num_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_xstp_num_entry(self):
    self.__xstp_num_entry = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 769']}), is_leaf=True, yang_name="xstp_num_entry", rest_name="num-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure number of XSTP keep-alive entries/per slot.', u'alt-name': u'num-entry'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='uint32', is_config=True)

  xstp_hello_interval = __builtin__.property(_get_xstp_hello_interval, _set_xstp_hello_interval)
  xstp_num_entry = __builtin__.property(_get_xstp_num_entry, _set_xstp_num_entry)


  _pyangbind_elements = {'xstp_hello_interval': xstp_hello_interval, 'xstp_num_entry': xstp_num_entry, }


