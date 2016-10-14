
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fcoe-ext - based on the path /brocade_fcoe_ext_rpc/fcoe-get-interface/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__fcoe_intf_name','__fcoe_intf_rbridge_id','__fcoe_intf_include_stats',)

  _yang_name = 'input'

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
    self.__fcoe_intf_include_stats = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-intf-include-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='boolean', is_config=True)
    self.__fcoe_intf_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3..32']}), is_leaf=True, yang_name="fcoe-intf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='fcoe:interface-fcoe-type', is_config=True)
    self.__fcoe_intf_rbridge_id = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'all'}),], is_leaf=True, yang_name="fcoe-intf-rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='common-def:rbridge-id-all-type', is_config=True)

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
      return [u'brocade_fcoe_ext_rpc', u'fcoe-get-interface', u'input']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'fcoe-get-interface', u'input']

  def _get_fcoe_intf_name(self):
    """
    Getter method for fcoe_intf_name, mapped from YANG variable /brocade_fcoe_ext_rpc/fcoe_get_interface/input/fcoe_intf_name (fcoe:interface-fcoe-type)

    YANG Description: This specifies the specific FCoE interface for 
which this rpc function is invoked. In response to
this request, the managed device returns the FCoE 
operational information for this interface.
    """
    return self.__fcoe_intf_name
      
  def _set_fcoe_intf_name(self, v, load=False):
    """
    Setter method for fcoe_intf_name, mapped from YANG variable /brocade_fcoe_ext_rpc/fcoe_get_interface/input/fcoe_intf_name (fcoe:interface-fcoe-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_intf_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_intf_name() directly.

    YANG Description: This specifies the specific FCoE interface for 
which this rpc function is invoked. In response to
this request, the managed device returns the FCoE 
operational information for this interface.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3..32']}), is_leaf=True, yang_name="fcoe-intf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='fcoe:interface-fcoe-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_intf_name must be of a type compatible with fcoe:interface-fcoe-type""",
          'defined-type': "fcoe:interface-fcoe-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3..32']}), is_leaf=True, yang_name="fcoe-intf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='fcoe:interface-fcoe-type', is_config=True)""",
        })

    self.__fcoe_intf_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_intf_name(self):
    self.__fcoe_intf_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3..32']}), is_leaf=True, yang_name="fcoe-intf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='fcoe:interface-fcoe-type', is_config=True)


  def _get_fcoe_intf_rbridge_id(self):
    """
    Getter method for fcoe_intf_rbridge_id, mapped from YANG variable /brocade_fcoe_ext_rpc/fcoe_get_interface/input/fcoe_intf_rbridge_id (common-def:rbridge-id-all-type)

    YANG Description: This specifies the rbridge-id for which this rpc 
function is invoked. In response to this request,
the managed device returns the FCoE operational 
information for all the interfaces of this 
rbridge-id or all rbridges if rbridge-id value is 'all'
    """
    return self.__fcoe_intf_rbridge_id
      
  def _set_fcoe_intf_rbridge_id(self, v, load=False):
    """
    Setter method for fcoe_intf_rbridge_id, mapped from YANG variable /brocade_fcoe_ext_rpc/fcoe_get_interface/input/fcoe_intf_rbridge_id (common-def:rbridge-id-all-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_intf_rbridge_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_intf_rbridge_id() directly.

    YANG Description: This specifies the rbridge-id for which this rpc 
function is invoked. In response to this request,
the managed device returns the FCoE operational 
information for all the interfaces of this 
rbridge-id or all rbridges if rbridge-id value is 'all'
    """
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'all'}),], is_leaf=True, yang_name="fcoe-intf-rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='common-def:rbridge-id-all-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_intf_rbridge_id must be of a type compatible with common-def:rbridge-id-all-type""",
          'defined-type': "common-def:rbridge-id-all-type",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'all'}),], is_leaf=True, yang_name="fcoe-intf-rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='common-def:rbridge-id-all-type', is_config=True)""",
        })

    self.__fcoe_intf_rbridge_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_intf_rbridge_id(self):
    self.__fcoe_intf_rbridge_id = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'all'}),], is_leaf=True, yang_name="fcoe-intf-rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='common-def:rbridge-id-all-type', is_config=True)


  def _get_fcoe_intf_include_stats(self):
    """
    Getter method for fcoe_intf_include_stats, mapped from YANG variable /brocade_fcoe_ext_rpc/fcoe_get_interface/input/fcoe_intf_include_stats (boolean)

    YANG Description: This specifies if the FCoE interface statistics 
should be included in the output.
    """
    return self.__fcoe_intf_include_stats
      
  def _set_fcoe_intf_include_stats(self, v, load=False):
    """
    Setter method for fcoe_intf_include_stats, mapped from YANG variable /brocade_fcoe_ext_rpc/fcoe_get_interface/input/fcoe_intf_include_stats (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_intf_include_stats is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_intf_include_stats() directly.

    YANG Description: This specifies if the FCoE interface statistics 
should be included in the output.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="fcoe-intf-include-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_intf_include_stats must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-intf-include-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='boolean', is_config=True)""",
        })

    self.__fcoe_intf_include_stats = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_intf_include_stats(self):
    self.__fcoe_intf_include_stats = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-intf-include-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='boolean', is_config=True)

  fcoe_intf_name = __builtin__.property(_get_fcoe_intf_name, _set_fcoe_intf_name)
  fcoe_intf_rbridge_id = __builtin__.property(_get_fcoe_intf_rbridge_id, _set_fcoe_intf_rbridge_id)
  fcoe_intf_include_stats = __builtin__.property(_get_fcoe_intf_include_stats, _set_fcoe_intf_include_stats)


  _pyangbind_elements = {'fcoe_intf_name': fcoe_intf_name, 'fcoe_intf_rbridge_id': fcoe_intf_rbridge_id, 'fcoe_intf_include_stats': fcoe_intf_include_stats, }

