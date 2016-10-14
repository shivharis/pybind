
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import rule
import group
class classifier(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vlan - based on the path /vlan/classifier. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__rule','__group',)

  _yang_name = 'classifier'

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
    self.__group = YANGDynClass(base=YANGListType("groupid oper rule_name ruleid",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='groupid oper rule-name ruleid', extensions={u'tailf-common': {u'info': u'Vlan classification groups commands', u'cli-suppress-mode': None, u'callpoint': u'VlanClassifier_group', u'cli-suppress-no': None}}), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan classification groups commands', u'cli-suppress-mode': None, u'callpoint': u'VlanClassifier_group', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='list', is_config=True)
    self.__rule = YANGDynClass(base=YANGListType("ruleid",rule.rule, yang_name="rule", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ruleid', extensions={u'tailf-common': {u'info': u'Vlan classification rules commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-incomplete-command': None, u'callpoint': u'VlanClassifier_rule'}}), is_container='list', yang_name="rule", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan classification rules commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-incomplete-command': None, u'callpoint': u'VlanClassifier_rule'}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='list', is_config=True)

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
      return [u'vlan', u'classifier']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'vlan', u'classifier']

  def _get_rule(self):
    """
    Getter method for rule, mapped from YANG variable /vlan/classifier/rule (list)
    """
    return self.__rule
      
  def _set_rule(self, v, load=False):
    """
    Setter method for rule, mapped from YANG variable /vlan/classifier/rule (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rule is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rule() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("ruleid",rule.rule, yang_name="rule", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ruleid', extensions={u'tailf-common': {u'info': u'Vlan classification rules commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-incomplete-command': None, u'callpoint': u'VlanClassifier_rule'}}), is_container='list', yang_name="rule", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan classification rules commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-incomplete-command': None, u'callpoint': u'VlanClassifier_rule'}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rule must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ruleid",rule.rule, yang_name="rule", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ruleid', extensions={u'tailf-common': {u'info': u'Vlan classification rules commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-incomplete-command': None, u'callpoint': u'VlanClassifier_rule'}}), is_container='list', yang_name="rule", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan classification rules commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-incomplete-command': None, u'callpoint': u'VlanClassifier_rule'}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='list', is_config=True)""",
        })

    self.__rule = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rule(self):
    self.__rule = YANGDynClass(base=YANGListType("ruleid",rule.rule, yang_name="rule", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ruleid', extensions={u'tailf-common': {u'info': u'Vlan classification rules commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-incomplete-command': None, u'callpoint': u'VlanClassifier_rule'}}), is_container='list', yang_name="rule", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan classification rules commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-incomplete-command': None, u'callpoint': u'VlanClassifier_rule'}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='list', is_config=True)


  def _get_group(self):
    """
    Getter method for group, mapped from YANG variable /vlan/classifier/group (list)
    """
    return self.__group
      
  def _set_group(self, v, load=False):
    """
    Setter method for group, mapped from YANG variable /vlan/classifier/group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("groupid oper rule_name ruleid",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='groupid oper rule-name ruleid', extensions={u'tailf-common': {u'info': u'Vlan classification groups commands', u'cli-suppress-mode': None, u'callpoint': u'VlanClassifier_group', u'cli-suppress-no': None}}), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan classification groups commands', u'cli-suppress-mode': None, u'callpoint': u'VlanClassifier_group', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("groupid oper rule_name ruleid",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='groupid oper rule-name ruleid', extensions={u'tailf-common': {u'info': u'Vlan classification groups commands', u'cli-suppress-mode': None, u'callpoint': u'VlanClassifier_group', u'cli-suppress-no': None}}), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan classification groups commands', u'cli-suppress-mode': None, u'callpoint': u'VlanClassifier_group', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='list', is_config=True)""",
        })

    self.__group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group(self):
    self.__group = YANGDynClass(base=YANGListType("groupid oper rule_name ruleid",group.group, yang_name="group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='groupid oper rule-name ruleid', extensions={u'tailf-common': {u'info': u'Vlan classification groups commands', u'cli-suppress-mode': None, u'callpoint': u'VlanClassifier_group', u'cli-suppress-no': None}}), is_container='list', yang_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan classification groups commands', u'cli-suppress-mode': None, u'callpoint': u'VlanClassifier_group', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='list', is_config=True)

  rule = __builtin__.property(_get_rule, _set_rule)
  group = __builtin__.property(_get_group, _set_group)


  _pyangbind_elements = {'rule': rule, 'group': group, }


