
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class fcoe_map_fabric_map(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fcoe - based on the path /fcoe/fcoe-map/fcoe-map-fabric-map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of FCoE Fabric map in the FCoE map. Each row
represents Fabric Map name.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__fcoe_map_fabric_map_name',)

  _yang_name = 'fcoe-map-fabric-map'

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
    self.__fcoe_map_fabric_map_name = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'})), is_leaf=False, yang_name="fcoe-map-fabric-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the fabric Map in the FCoE Map', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='common-def:name-string32', is_config=True)

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
      return [u'fcoe', u'fcoe-map', u'fcoe-map-fabric-map']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'fcoe', u'fcoe-map', u'fabric-map']

  def _get_fcoe_map_fabric_map_name(self):
    """
    Getter method for fcoe_map_fabric_map_name, mapped from YANG variable /fcoe/fcoe_map/fcoe_map_fabric_map/fcoe_map_fabric_map_name (common-def:name-string32)

    YANG Description: This specifies the FCoE fabric map name.
    """
    return self.__fcoe_map_fabric_map_name
      
  def _set_fcoe_map_fabric_map_name(self, v, load=False):
    """
    Setter method for fcoe_map_fabric_map_name, mapped from YANG variable /fcoe/fcoe_map/fcoe_map_fabric_map/fcoe_map_fabric_map_name (common-def:name-string32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_map_fabric_map_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_map_fabric_map_name() directly.

    YANG Description: This specifies the FCoE fabric map name.
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'})), is_leaf=False, yang_name="fcoe-map-fabric-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the fabric Map in the FCoE Map', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='common-def:name-string32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_map_fabric_map_name must be of a type compatible with common-def:name-string32""",
          'defined-type': "common-def:name-string32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'})), is_leaf=False, yang_name="fcoe-map-fabric-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the fabric Map in the FCoE Map', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='common-def:name-string32', is_config=True)""",
        })

    self.__fcoe_map_fabric_map_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_map_fabric_map_name(self):
    self.__fcoe_map_fabric_map_name = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'})), is_leaf=False, yang_name="fcoe-map-fabric-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the fabric Map in the FCoE Map', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='common-def:name-string32', is_config=True)

  fcoe_map_fabric_map_name = __builtin__.property(_get_fcoe_map_fabric_map_name, _set_fcoe_map_fabric_map_name)


  _pyangbind_elements = {'fcoe_map_fabric_map_name': fcoe_map_fabric_map_name, }


