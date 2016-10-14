
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import transit_overlay
class overlay_transit(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vxlan-visibility - based on the path /overlay-transit. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__user_transit_name','__transit_overlay',)

  _yang_name = 'overlay-transit'

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
    self.__user_transit_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="user-transit-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'User Transit Name (Max 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='user-transit-name-type', is_config=True)
    self.__transit_overlay = YANGDynClass(base=YANGListType("access_group in_out",transit_overlay.transit_overlay, yang_name="transit-overlay", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='access-group in-out', extensions={u'tailf-common': {u'info': u'overlay', u'cli-suppress-mode': None, u'alt-name': u'overlay', u'callpoint': u'VxlanVisibilityTransitOverlayCallpoint'}}), is_container='list', yang_name="transit-overlay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'overlay', u'cli-suppress-mode': None, u'alt-name': u'overlay', u'callpoint': u'VxlanVisibilityTransitOverlayCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)

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
      return [u'overlay-transit']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'overlay-transit']

  def _get_user_transit_name(self):
    """
    Getter method for user_transit_name, mapped from YANG variable /overlay_transit/user_transit_name (user-transit-name-type)
    """
    return self.__user_transit_name
      
  def _set_user_transit_name(self, v, load=False):
    """
    Setter method for user_transit_name, mapped from YANG variable /overlay_transit/user_transit_name (user-transit-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_user_transit_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_user_transit_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="user-transit-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'User Transit Name (Max 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='user-transit-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """user_transit_name must be of a type compatible with user-transit-name-type""",
          'defined-type': "brocade-vxlan-visibility:user-transit-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="user-transit-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'User Transit Name (Max 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='user-transit-name-type', is_config=True)""",
        })

    self.__user_transit_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_user_transit_name(self):
    self.__user_transit_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="user-transit-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'User Transit Name (Max 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='user-transit-name-type', is_config=True)


  def _get_transit_overlay(self):
    """
    Getter method for transit_overlay, mapped from YANG variable /overlay_transit/transit_overlay (list)
    """
    return self.__transit_overlay
      
  def _set_transit_overlay(self, v, load=False):
    """
    Setter method for transit_overlay, mapped from YANG variable /overlay_transit/transit_overlay (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transit_overlay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transit_overlay() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("access_group in_out",transit_overlay.transit_overlay, yang_name="transit-overlay", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='access-group in-out', extensions={u'tailf-common': {u'info': u'overlay', u'cli-suppress-mode': None, u'alt-name': u'overlay', u'callpoint': u'VxlanVisibilityTransitOverlayCallpoint'}}), is_container='list', yang_name="transit-overlay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'overlay', u'cli-suppress-mode': None, u'alt-name': u'overlay', u'callpoint': u'VxlanVisibilityTransitOverlayCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transit_overlay must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("access_group in_out",transit_overlay.transit_overlay, yang_name="transit-overlay", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='access-group in-out', extensions={u'tailf-common': {u'info': u'overlay', u'cli-suppress-mode': None, u'alt-name': u'overlay', u'callpoint': u'VxlanVisibilityTransitOverlayCallpoint'}}), is_container='list', yang_name="transit-overlay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'overlay', u'cli-suppress-mode': None, u'alt-name': u'overlay', u'callpoint': u'VxlanVisibilityTransitOverlayCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)""",
        })

    self.__transit_overlay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transit_overlay(self):
    self.__transit_overlay = YANGDynClass(base=YANGListType("access_group in_out",transit_overlay.transit_overlay, yang_name="transit-overlay", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='access-group in-out', extensions={u'tailf-common': {u'info': u'overlay', u'cli-suppress-mode': None, u'alt-name': u'overlay', u'callpoint': u'VxlanVisibilityTransitOverlayCallpoint'}}), is_container='list', yang_name="transit-overlay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'overlay', u'cli-suppress-mode': None, u'alt-name': u'overlay', u'callpoint': u'VxlanVisibilityTransitOverlayCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)

  user_transit_name = __builtin__.property(_get_user_transit_name, _set_user_transit_name)
  transit_overlay = __builtin__.property(_get_transit_overlay, _set_transit_overlay)


  _pyangbind_elements = {'user_transit_name': user_transit_name, 'transit_overlay': transit_overlay, }

