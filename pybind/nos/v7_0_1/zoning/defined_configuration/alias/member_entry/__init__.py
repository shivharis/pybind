
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class member_entry(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-zone - based on the path /zoning/defined-configuration/alias/member-entry. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__alias_entry_name',)

  _yang_name = 'member-entry'
  _rest_name = 'member-entry'

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
    self.__alias_entry_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7})(;[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7})*'}), is_leaf=True, yang_name="alias-entry-name", rest_name="alias-entry-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<WWN>;;Member-Name - add one or more WWN\nmembers to an alias, the [no] option removes\nonly one member at a time.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='string', is_config=True)

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
      return [u'zoning', u'defined-configuration', u'alias', u'member-entry']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'zoning', u'defined-configuration', u'alias', u'member-entry']

  def _get_alias_entry_name(self):
    """
    Getter method for alias_entry_name, mapped from YANG variable /zoning/defined_configuration/alias/member_entry/alias_entry_name (string)

    YANG Description: Use the member-entry command to add one
or more WWN members to an alias. Users
can specify multiple entries in a single
command by separating members with a
semi-colon. However when using the [no]
option to remove alias members, only
one member-entry can be removed at a
time.
    """
    return self.__alias_entry_name
      
  def _set_alias_entry_name(self, v, load=False):
    """
    Setter method for alias_entry_name, mapped from YANG variable /zoning/defined_configuration/alias/member_entry/alias_entry_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alias_entry_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alias_entry_name() directly.

    YANG Description: Use the member-entry command to add one
or more WWN members to an alias. Users
can specify multiple entries in a single
command by separating members with a
semi-colon. However when using the [no]
option to remove alias members, only
one member-entry can be removed at a
time.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7})(;[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7})*'}), is_leaf=True, yang_name="alias-entry-name", rest_name="alias-entry-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<WWN>;;Member-Name - add one or more WWN\nmembers to an alias, the [no] option removes\nonly one member at a time.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alias_entry_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7})(;[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7})*'}), is_leaf=True, yang_name="alias-entry-name", rest_name="alias-entry-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<WWN>;;Member-Name - add one or more WWN\nmembers to an alias, the [no] option removes\nonly one member at a time.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='string', is_config=True)""",
        })

    self.__alias_entry_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alias_entry_name(self):
    self.__alias_entry_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7})(;[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7})*'}), is_leaf=True, yang_name="alias-entry-name", rest_name="alias-entry-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<WWN>;;Member-Name - add one or more WWN\nmembers to an alias, the [no] option removes\nonly one member at a time.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='string', is_config=True)

  alias_entry_name = __builtin__.property(_get_alias_entry_name, _set_alias_entry_name)


  _pyangbind_elements = {'alias_entry_name': alias_entry_name, }


