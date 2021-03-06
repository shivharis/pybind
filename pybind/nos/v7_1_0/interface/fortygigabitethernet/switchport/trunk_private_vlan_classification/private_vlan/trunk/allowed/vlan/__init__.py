
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import add_
import remove_
class vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/fortygigabitethernet/switchport/trunk-private-vlan-classification/private-vlan/trunk/allowed/vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__add_','__remove_',)

  _yang_name = 'vlan'
  _rest_name = 'vlan'

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
    self.__add_ = YANGDynClass(base=YANGListType("trunk_vlan_id trunk_ctag_id",add_.add_, yang_name="add", rest_name="add", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trunk-vlan-id trunk-ctag-id', extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}), is_container='list', yang_name="add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)
    self.__remove_ = YANGDynClass(base=YANGListType("trunk_vlan_id trunk_ctag_id",remove_.remove_, yang_name="remove", rest_name="remove", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trunk-vlan-id trunk-ctag-id', extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-remove-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}), is_container='list', yang_name="remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-remove-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)

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
      return [u'interface', u'fortygigabitethernet', u'switchport', u'trunk-private-vlan-classification', u'private-vlan', u'trunk', u'allowed', u'vlan']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'FortyGigabitEthernet', u'switchport', u'private-vlan', u'trunk', u'allowed', u'vlan']

  def _get_add_(self):
    """
    Getter method for add_, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk_private_vlan_classification/private_vlan/trunk/allowed/vlan/add (list)
    """
    return self.__add_
      
  def _set_add_(self, v, load=False):
    """
    Setter method for add_, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk_private_vlan_classification/private_vlan/trunk/allowed/vlan/add (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_add_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_add_() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("trunk_vlan_id trunk_ctag_id",add_.add_, yang_name="add", rest_name="add", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trunk-vlan-id trunk-ctag-id', extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}), is_container='list', yang_name="add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """add_ must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("trunk_vlan_id trunk_ctag_id",add_.add_, yang_name="add", rest_name="add", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trunk-vlan-id trunk-ctag-id', extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}), is_container='list', yang_name="add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)""",
        })

    self.__add_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_add_(self):
    self.__add_ = YANGDynClass(base=YANGListType("trunk_vlan_id trunk_ctag_id",add_.add_, yang_name="add", rest_name="add", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trunk-vlan-id trunk-ctag-id', extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}), is_container='list', yang_name="add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)


  def _get_remove_(self):
    """
    Getter method for remove_, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk_private_vlan_classification/private_vlan/trunk/allowed/vlan/remove (list)
    """
    return self.__remove_
      
  def _set_remove_(self, v, load=False):
    """
    Setter method for remove_, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk_private_vlan_classification/private_vlan/trunk/allowed/vlan/remove (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remove_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remove_() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("trunk_vlan_id trunk_ctag_id",remove_.remove_, yang_name="remove", rest_name="remove", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trunk-vlan-id trunk-ctag-id', extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-remove-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}), is_container='list', yang_name="remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-remove-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remove_ must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("trunk_vlan_id trunk_ctag_id",remove_.remove_, yang_name="remove", rest_name="remove", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trunk-vlan-id trunk-ctag-id', extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-remove-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}), is_container='list', yang_name="remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-remove-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)""",
        })

    self.__remove_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remove_(self):
    self.__remove_ = YANGDynClass(base=YANGListType("trunk_vlan_id trunk_ctag_id",remove_.remove_, yang_name="remove", rest_name="remove", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trunk-vlan-id trunk-ctag-id', extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-remove-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}), is_container='list', yang_name="remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ctag-pvlan-classification-phy-remove-config', u'cli-no-key-completion': None, u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)

  add_ = __builtin__.property(_get_add_, _set_add_)
  remove_ = __builtin__.property(_get_remove_, _set_remove_)


  _pyangbind_elements = {'add_': add_, 'remove_': remove_, }


