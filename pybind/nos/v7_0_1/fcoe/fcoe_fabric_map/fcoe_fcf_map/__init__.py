
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import fcf_map_fif_rbid
class fcoe_fcf_map(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fcoe - based on the path /fcoe/fcoe-fabric-map/fcoe-fcf-map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The list of FCF Groups. Each row contains the FCF group
name, member FCoE map, FCF rbid and FDF rbids
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__fcf_map_name','__fcf_map_fcf_rbid','__fcf_map_fif_rbid',)

  _yang_name = 'fcoe-fcf-map'

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
    self.__fcf_map_fif_rbid = YANGDynClass(base=fcf_map_fif_rbid.fcf_map_fif_rbid, is_container='container', yang_name="fcf-map-fif-rbid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FIF rbridge-id/s in the FCF Group', u'alt-name': u'fif-rbid', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)
    self.__fcf_map_fcf_rbid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="fcf-map-fcf-rbid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u"Configure FCF Box's rbridge-id in the FCF Group", u'alt-name': u'fcf-rbid'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='uint32', is_config=True)
    self.__fcf_map_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..31']}), is_leaf=True, yang_name="fcf-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='fcf-map-name-type', is_config=True)

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
      return [u'fcoe', u'fcoe-fabric-map', u'fcoe-fcf-map']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'fcoe', u'fabric-map', u'fcf-group']

  def _get_fcf_map_name(self):
    """
    Getter method for fcf_map_name, mapped from YANG variable /fcoe/fcoe_fabric_map/fcoe_fcf_map/fcf_map_name (fcf-map-name-type)

    YANG Description: This specifies the FCF group name.
    """
    return self.__fcf_map_name
      
  def _set_fcf_map_name(self, v, load=False):
    """
    Setter method for fcf_map_name, mapped from YANG variable /fcoe/fcoe_fabric_map/fcoe_fcf_map/fcf_map_name (fcf-map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcf_map_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcf_map_name() directly.

    YANG Description: This specifies the FCF group name.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..31']}), is_leaf=True, yang_name="fcf-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='fcf-map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcf_map_name must be of a type compatible with fcf-map-name-type""",
          'defined-type': "brocade-fcoe:fcf-map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..31']}), is_leaf=True, yang_name="fcf-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='fcf-map-name-type', is_config=True)""",
        })

    self.__fcf_map_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcf_map_name(self):
    self.__fcf_map_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..31']}), is_leaf=True, yang_name="fcf-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='fcf-map-name-type', is_config=True)


  def _get_fcf_map_fcf_rbid(self):
    """
    Getter method for fcf_map_fcf_rbid, mapped from YANG variable /fcoe/fcoe_fabric_map/fcoe_fcf_map/fcf_map_fcf_rbid (uint32)

    YANG Description: This specifies the FCF's rbridge-id in the
FCF Group
    """
    return self.__fcf_map_fcf_rbid
      
  def _set_fcf_map_fcf_rbid(self, v, load=False):
    """
    Setter method for fcf_map_fcf_rbid, mapped from YANG variable /fcoe/fcoe_fabric_map/fcoe_fcf_map/fcf_map_fcf_rbid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcf_map_fcf_rbid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcf_map_fcf_rbid() directly.

    YANG Description: This specifies the FCF's rbridge-id in the
FCF Group
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="fcf-map-fcf-rbid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u"Configure FCF Box's rbridge-id in the FCF Group", u'alt-name': u'fcf-rbid'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcf_map_fcf_rbid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="fcf-map-fcf-rbid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u"Configure FCF Box's rbridge-id in the FCF Group", u'alt-name': u'fcf-rbid'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='uint32', is_config=True)""",
        })

    self.__fcf_map_fcf_rbid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcf_map_fcf_rbid(self):
    self.__fcf_map_fcf_rbid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="fcf-map-fcf-rbid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u"Configure FCF Box's rbridge-id in the FCF Group", u'alt-name': u'fcf-rbid'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='uint32', is_config=True)


  def _get_fcf_map_fif_rbid(self):
    """
    Getter method for fcf_map_fif_rbid, mapped from YANG variable /fcoe/fcoe_fabric_map/fcoe_fcf_map/fcf_map_fif_rbid (container)

    YANG Description: This specifies the FIF rbridge-id/s in the
FCF Group
    """
    return self.__fcf_map_fif_rbid
      
  def _set_fcf_map_fif_rbid(self, v, load=False):
    """
    Setter method for fcf_map_fif_rbid, mapped from YANG variable /fcoe/fcoe_fabric_map/fcoe_fcf_map/fcf_map_fif_rbid (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcf_map_fif_rbid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcf_map_fif_rbid() directly.

    YANG Description: This specifies the FIF rbridge-id/s in the
FCF Group
    """
    try:
      t = YANGDynClass(v,base=fcf_map_fif_rbid.fcf_map_fif_rbid, is_container='container', yang_name="fcf-map-fif-rbid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FIF rbridge-id/s in the FCF Group', u'alt-name': u'fif-rbid', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcf_map_fif_rbid must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=fcf_map_fif_rbid.fcf_map_fif_rbid, is_container='container', yang_name="fcf-map-fif-rbid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FIF rbridge-id/s in the FCF Group', u'alt-name': u'fif-rbid', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)""",
        })

    self.__fcf_map_fif_rbid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcf_map_fif_rbid(self):
    self.__fcf_map_fif_rbid = YANGDynClass(base=fcf_map_fif_rbid.fcf_map_fif_rbid, is_container='container', yang_name="fcf-map-fif-rbid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FIF rbridge-id/s in the FCF Group', u'alt-name': u'fif-rbid', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)

  fcf_map_name = __builtin__.property(_get_fcf_map_name, _set_fcf_map_name)
  fcf_map_fcf_rbid = __builtin__.property(_get_fcf_map_fcf_rbid, _set_fcf_map_fcf_rbid)
  fcf_map_fif_rbid = __builtin__.property(_get_fcf_map_fif_rbid, _set_fcf_map_fif_rbid)


  _pyangbind_elements = {'fcf_map_name': fcf_map_name, 'fcf_map_fcf_rbid': fcf_map_fcf_rbid, 'fcf_map_fif_rbid': fcf_map_fif_rbid, }


