
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class private_vlan_trunk(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/hundredgigabitethernet/switchport/mode/private-vlan/private-vlan-trunk. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__trunk_basic','__trunk_promiscuous','__trunk_host',)

  _yang_name = 'private-vlan-trunk'
  _rest_name = 'trunk'

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
    self.__trunk_basic = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trunk-basic", rest_name="trunk-basic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__trunk_promiscuous = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trunk-promiscuous", rest_name="promiscuous", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan trunk promiscuous', u'cli-full-command': None, u'alt-name': u'promiscuous'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__trunk_host = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trunk-host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan trunk host', u'cli-full-command': None, u'alt-name': u'host'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)

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
      return [u'interface', u'hundredgigabitethernet', u'switchport', u'mode', u'private-vlan', u'private-vlan-trunk']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'HundredGigabitEthernet', u'switchport', u'mode', u'private-vlan', u'trunk']

  def _get_trunk_basic(self):
    """
    Getter method for trunk_basic, mapped from YANG variable /interface/hundredgigabitethernet/switchport/mode/private_vlan/private_vlan_trunk/trunk_basic (empty)
    """
    return self.__trunk_basic
      
  def _set_trunk_basic(self, v, load=False):
    """
    Setter method for trunk_basic, mapped from YANG variable /interface/hundredgigabitethernet/switchport/mode/private_vlan/private_vlan_trunk/trunk_basic (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_basic is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_basic() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="trunk-basic", rest_name="trunk-basic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_basic must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trunk-basic", rest_name="trunk-basic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__trunk_basic = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_basic(self):
    self.__trunk_basic = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trunk-basic", rest_name="trunk-basic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_trunk_promiscuous(self):
    """
    Getter method for trunk_promiscuous, mapped from YANG variable /interface/hundredgigabitethernet/switchport/mode/private_vlan/private_vlan_trunk/trunk_promiscuous (empty)
    """
    return self.__trunk_promiscuous
      
  def _set_trunk_promiscuous(self, v, load=False):
    """
    Setter method for trunk_promiscuous, mapped from YANG variable /interface/hundredgigabitethernet/switchport/mode/private_vlan/private_vlan_trunk/trunk_promiscuous (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_promiscuous is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_promiscuous() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="trunk-promiscuous", rest_name="promiscuous", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan trunk promiscuous', u'cli-full-command': None, u'alt-name': u'promiscuous'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_promiscuous must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trunk-promiscuous", rest_name="promiscuous", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan trunk promiscuous', u'cli-full-command': None, u'alt-name': u'promiscuous'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__trunk_promiscuous = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_promiscuous(self):
    self.__trunk_promiscuous = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trunk-promiscuous", rest_name="promiscuous", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan trunk promiscuous', u'cli-full-command': None, u'alt-name': u'promiscuous'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_trunk_host(self):
    """
    Getter method for trunk_host, mapped from YANG variable /interface/hundredgigabitethernet/switchport/mode/private_vlan/private_vlan_trunk/trunk_host (empty)
    """
    return self.__trunk_host
      
  def _set_trunk_host(self, v, load=False):
    """
    Setter method for trunk_host, mapped from YANG variable /interface/hundredgigabitethernet/switchport/mode/private_vlan/private_vlan_trunk/trunk_host (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_host is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_host() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="trunk-host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan trunk host', u'cli-full-command': None, u'alt-name': u'host'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_host must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trunk-host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan trunk host', u'cli-full-command': None, u'alt-name': u'host'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__trunk_host = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_host(self):
    self.__trunk_host = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trunk-host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan trunk host', u'cli-full-command': None, u'alt-name': u'host'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)

  trunk_basic = __builtin__.property(_get_trunk_basic, _set_trunk_basic)
  trunk_promiscuous = __builtin__.property(_get_trunk_promiscuous, _set_trunk_promiscuous)
  trunk_host = __builtin__.property(_get_trunk_host, _set_trunk_host)


  _pyangbind_elements = {'trunk_basic': trunk_basic, 'trunk_promiscuous': trunk_promiscuous, 'trunk_host': trunk_host, }


