
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import class_
class policy_map(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-policer - based on the path /policy-map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__po_name','__class_',)

  _yang_name = 'policy-map'

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
    self.__po_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="po-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Map Name (Max Size - 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    self.__class_ = YANGDynClass(base=YANGListType("cl_name",class_.class_, yang_name="class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cl-name', extensions={u'tailf-common': {u'info': u'Policy Map Class Configuration', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'policer-poclass-map', u'cli-mode-name': u'config-policymap-class'}}), is_container='list', yang_name="class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Map Class Configuration', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'policer-poclass-map', u'cli-mode-name': u'config-policymap-class'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='list', is_config=True)

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
      return [u'policy-map']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'policy-map']

  def _get_po_name(self):
    """
    Getter method for po_name, mapped from YANG variable /policy_map/po_name (map-name-type)
    """
    return self.__po_name
      
  def _set_po_name(self, v, load=False):
    """
    Setter method for po_name, mapped from YANG variable /policy_map/po_name (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_po_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_po_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="po-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Map Name (Max Size - 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """po_name must be of a type compatible with map-name-type""",
          'defined-type': "brocade-policer:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="po-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Map Name (Max Size - 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)""",
        })

    self.__po_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_po_name(self):
    self.__po_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="po-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Map Name (Max Size - 64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)


  def _get_class_(self):
    """
    Getter method for class_, mapped from YANG variable /policy_map/class (list)
    """
    return self.__class_
      
  def _set_class_(self, v, load=False):
    """
    Setter method for class_, mapped from YANG variable /policy_map/class (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_class_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_class_() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("cl_name",class_.class_, yang_name="class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cl-name', extensions={u'tailf-common': {u'info': u'Policy Map Class Configuration', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'policer-poclass-map', u'cli-mode-name': u'config-policymap-class'}}), is_container='list', yang_name="class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Map Class Configuration', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'policer-poclass-map', u'cli-mode-name': u'config-policymap-class'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """class_ must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("cl_name",class_.class_, yang_name="class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cl-name', extensions={u'tailf-common': {u'info': u'Policy Map Class Configuration', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'policer-poclass-map', u'cli-mode-name': u'config-policymap-class'}}), is_container='list', yang_name="class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Map Class Configuration', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'policer-poclass-map', u'cli-mode-name': u'config-policymap-class'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='list', is_config=True)""",
        })

    self.__class_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_class_(self):
    self.__class_ = YANGDynClass(base=YANGListType("cl_name",class_.class_, yang_name="class", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='cl-name', extensions={u'tailf-common': {u'info': u'Policy Map Class Configuration', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'policer-poclass-map', u'cli-mode-name': u'config-policymap-class'}}), is_container='list', yang_name="class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Map Class Configuration', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'policer-poclass-map', u'cli-mode-name': u'config-policymap-class'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='list', is_config=True)

  po_name = __builtin__.property(_get_po_name, _set_po_name)
  class_ = __builtin__.property(_get_class_, _set_class_)


  _pyangbind_elements = {'po_name': po_name, 'class_': class_, }


