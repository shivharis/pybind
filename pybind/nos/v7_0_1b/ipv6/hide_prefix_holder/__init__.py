
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import prefix_list
class hide_prefix_holder(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /ipv6/hide-prefix-holder. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__prefix_list',)

  _yang_name = 'hide-prefix-holder'
  _rest_name = ''

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
    self.__prefix_list = YANGDynClass(base=YANGListType("name seq_keyword instance",prefix_list.prefix_list, yang_name="prefix-list", rest_name="prefix-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'63', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}), is_container='list', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'63', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)

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
      return [u'ipv6', u'hide-prefix-holder']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6']

  def _get_prefix_list(self):
    """
    Getter method for prefix_list, mapped from YANG variable /ipv6/hide_prefix_holder/prefix_list (list)

    YANG Description: IPv6 address prefix list.
    """
    return self.__prefix_list
      
  def _set_prefix_list(self, v, load=False):
    """
    Setter method for prefix_list, mapped from YANG variable /ipv6/hide_prefix_holder/prefix_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_list() directly.

    YANG Description: IPv6 address prefix list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name seq_keyword instance",prefix_list.prefix_list, yang_name="prefix-list", rest_name="prefix-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'63', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}), is_container='list', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'63', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name seq_keyword instance",prefix_list.prefix_list, yang_name="prefix-list", rest_name="prefix-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'63', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}), is_container='list', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'63', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)""",
        })

    self.__prefix_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_list(self):
    self.__prefix_list = YANGDynClass(base=YANGListType("name seq_keyword instance",prefix_list.prefix_list, yang_name="prefix-list", rest_name="prefix-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'63', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}), is_container='list', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'63', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)

  prefix_list = __builtin__.property(_get_prefix_list, _set_prefix_list)


  _pyangbind_elements = {'prefix_list': prefix_list, }


