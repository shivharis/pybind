
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import pvlan_tag
import native
import allowed
class trunk(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/hundredgigabitethernet/switchport/private-vlan/trunk. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: trunk
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__pvlan_tag','__native','__allowed',)

  _yang_name = 'trunk'
  _rest_name = 'trunk'

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
    self.__pvlan_tag = YANGDynClass(base=pvlan_tag.pvlan_tag, is_container='container', yang_name="pvlan-tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable tagging', u'alt-name': u'tag', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__allowed = YANGDynClass(base=allowed.allowed, is_container='container', yang_name="allowed", rest_name="allowed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__native = YANGDynClass(base=native.native, is_container='container', yang_name="native", rest_name="native", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

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
      return [u'interface', u'hundredgigabitethernet', u'switchport', u'private-vlan', u'trunk']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'HundredGigabitEthernet', u'switchport', u'private-vlan', u'trunk']

  def _get_pvlan_tag(self):
    """
    Getter method for pvlan_tag, mapped from YANG variable /interface/hundredgigabitethernet/switchport/private_vlan/trunk/pvlan_tag (container)

    YANG Description: This specifies vlan tagging characteristics for a 
trunk port.
    """
    return self.__pvlan_tag
      
  def _set_pvlan_tag(self, v, load=False):
    """
    Setter method for pvlan_tag, mapped from YANG variable /interface/hundredgigabitethernet/switchport/private_vlan/trunk/pvlan_tag (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pvlan_tag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pvlan_tag() directly.

    YANG Description: This specifies vlan tagging characteristics for a 
trunk port.
    """
    try:
      t = YANGDynClass(v,base=pvlan_tag.pvlan_tag, is_container='container', yang_name="pvlan-tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable tagging', u'alt-name': u'tag', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pvlan_tag must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=pvlan_tag.pvlan_tag, is_container='container', yang_name="pvlan-tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable tagging', u'alt-name': u'tag', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__pvlan_tag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pvlan_tag(self):
    self.__pvlan_tag = YANGDynClass(base=pvlan_tag.pvlan_tag, is_container='container', yang_name="pvlan-tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable tagging', u'alt-name': u'tag', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_native(self):
    """
    Getter method for native, mapped from YANG variable /interface/hundredgigabitethernet/switchport/private_vlan/trunk/native (container)

    YANG Description: Set the native VLAN characteristics of the
Layer2 trunk interface
    """
    return self.__native
      
  def _set_native(self, v, load=False):
    """
    Setter method for native, mapped from YANG variable /interface/hundredgigabitethernet/switchport/private_vlan/trunk/native (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_native is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_native() directly.

    YANG Description: Set the native VLAN characteristics of the
Layer2 trunk interface
    """
    try:
      t = YANGDynClass(v,base=native.native, is_container='container', yang_name="native", rest_name="native", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """native must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=native.native, is_container='container', yang_name="native", rest_name="native", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__native = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_native(self):
    self.__native = YANGDynClass(base=native.native, is_container='container', yang_name="native", rest_name="native", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_allowed(self):
    """
    Getter method for allowed, mapped from YANG variable /interface/hundredgigabitethernet/switchport/private_vlan/trunk/allowed (container)

    YANG Description: Set the VLANs that will Xmit/Rx through the Layer2 interface
    """
    return self.__allowed
      
  def _set_allowed(self, v, load=False):
    """
    Setter method for allowed, mapped from YANG variable /interface/hundredgigabitethernet/switchport/private_vlan/trunk/allowed (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_allowed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_allowed() directly.

    YANG Description: Set the VLANs that will Xmit/Rx through the Layer2 interface
    """
    try:
      t = YANGDynClass(v,base=allowed.allowed, is_container='container', yang_name="allowed", rest_name="allowed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """allowed must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=allowed.allowed, is_container='container', yang_name="allowed", rest_name="allowed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__allowed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_allowed(self):
    self.__allowed = YANGDynClass(base=allowed.allowed, is_container='container', yang_name="allowed", rest_name="allowed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

  pvlan_tag = __builtin__.property(_get_pvlan_tag, _set_pvlan_tag)
  native = __builtin__.property(_get_native, _set_native)
  allowed = __builtin__.property(_get_allowed, _set_allowed)


  _pyangbind_elements = {'pvlan_tag': pvlan_tag, 'native': native, 'allowed': allowed, }


