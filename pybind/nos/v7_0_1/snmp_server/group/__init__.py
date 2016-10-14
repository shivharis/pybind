
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-snmp - based on the path /snmp-server/group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__group_name','__group_version','__group_auth_mode','__read','__write','__notify',)

  _yang_name = 'group'

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
    self.__group_version = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'v2c': {'value': 1}, u'v1': {'value': 0}, u'v3': {'value': 2}},), is_leaf=True, yang_name="group-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='group-version-type', is_config=True)
    self.__read = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), default=unicode("-"), is_leaf=True, yang_name="read", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'read\tSpecify a read view for the group', u'display-when': u"../group-version = 'v1' or\n../group-version = 'v2c' or\n../group-version = 'v3' or\n../group-auth-mode = 'auth' or\n../group-auth-mode = 'noauth' or\n../group-auth-mode = 'priv'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    self.__group_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), is_leaf=True, yang_name="group-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    self.__write = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), default=unicode("-"), is_leaf=True, yang_name="write", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'write\tSpecify a write view for the group', u'display-when': u"../group-version = 'v1' or\n            ../group-version = 'v2c' or\n            ../group-version = 'v3' or\n../group-auth-mode = 'auth' or\n            ../group-auth-mode = 'noauth' or\n            ../group-auth-mode = 'priv'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    self.__notify = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), default=unicode("-"), is_leaf=True, yang_name="notify", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'notify\tSpecify a notify view for the group', u'display-when': u"../group-version = 'v1' or\n            ../group-version = 'v2c' or\n            ../group-version = 'v3' or\n../group-auth-mode = 'auth' or\n            ../group-auth-mode = 'noauth' or\n            ../group-auth-mode = 'priv'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    self.__group_auth_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'noauth': {'value': 1}, u'auth': {'value': 2}, u'priv': {'value': 3}},), default=unicode("noauth"), is_leaf=True, yang_name="group-auth-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../group-version = 'v3'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='auth-mode-option', is_config=True)

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
      return [u'snmp-server', u'group']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'snmp-server', u'group']

  def _get_group_name(self):
    """
    Getter method for group_name, mapped from YANG variable /snmp_server/group/group_name (string)
    """
    return self.__group_name
      
  def _set_group_name(self, v, load=False):
    """
    Setter method for group_name, mapped from YANG variable /snmp_server/group/group_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), is_leaf=True, yang_name="group-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), is_leaf=True, yang_name="group-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)""",
        })

    self.__group_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_name(self):
    self.__group_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), is_leaf=True, yang_name="group-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)


  def _get_group_version(self):
    """
    Getter method for group_version, mapped from YANG variable /snmp_server/group/group_version (group-version-type)
    """
    return self.__group_version
      
  def _set_group_version(self, v, load=False):
    """
    Setter method for group_version, mapped from YANG variable /snmp_server/group/group_version (group-version-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_version() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'v2c': {'value': 1}, u'v1': {'value': 0}, u'v3': {'value': 2}},), is_leaf=True, yang_name="group-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='group-version-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_version must be of a type compatible with group-version-type""",
          'defined-type': "brocade-snmp:group-version-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'v2c': {'value': 1}, u'v1': {'value': 0}, u'v3': {'value': 2}},), is_leaf=True, yang_name="group-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='group-version-type', is_config=True)""",
        })

    self.__group_version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_version(self):
    self.__group_version = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'v2c': {'value': 1}, u'v1': {'value': 0}, u'v3': {'value': 2}},), is_leaf=True, yang_name="group-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='group-version-type', is_config=True)


  def _get_group_auth_mode(self):
    """
    Getter method for group_auth_mode, mapped from YANG variable /snmp_server/group/group_auth_mode (auth-mode-option)
    """
    return self.__group_auth_mode
      
  def _set_group_auth_mode(self, v, load=False):
    """
    Setter method for group_auth_mode, mapped from YANG variable /snmp_server/group/group_auth_mode (auth-mode-option)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_auth_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_auth_mode() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'noauth': {'value': 1}, u'auth': {'value': 2}, u'priv': {'value': 3}},), default=unicode("noauth"), is_leaf=True, yang_name="group-auth-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../group-version = 'v3'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='auth-mode-option', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_auth_mode must be of a type compatible with auth-mode-option""",
          'defined-type': "brocade-snmp:auth-mode-option",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'noauth': {'value': 1}, u'auth': {'value': 2}, u'priv': {'value': 3}},), default=unicode("noauth"), is_leaf=True, yang_name="group-auth-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../group-version = 'v3'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='auth-mode-option', is_config=True)""",
        })

    self.__group_auth_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_auth_mode(self):
    self.__group_auth_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'noauth': {'value': 1}, u'auth': {'value': 2}, u'priv': {'value': 3}},), default=unicode("noauth"), is_leaf=True, yang_name="group-auth-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../group-version = 'v3'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='auth-mode-option', is_config=True)


  def _get_read(self):
    """
    Getter method for read, mapped from YANG variable /snmp_server/group/read (string)
    """
    return self.__read
      
  def _set_read(self, v, load=False):
    """
    Setter method for read, mapped from YANG variable /snmp_server/group/read (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_read is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_read() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), default=unicode("-"), is_leaf=True, yang_name="read", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'read\tSpecify a read view for the group', u'display-when': u"../group-version = 'v1' or\n../group-version = 'v2c' or\n../group-version = 'v3' or\n../group-auth-mode = 'auth' or\n../group-auth-mode = 'noauth' or\n../group-auth-mode = 'priv'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """read must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), default=unicode("-"), is_leaf=True, yang_name="read", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'read\tSpecify a read view for the group', u'display-when': u"../group-version = 'v1' or\n../group-version = 'v2c' or\n../group-version = 'v3' or\n../group-auth-mode = 'auth' or\n../group-auth-mode = 'noauth' or\n../group-auth-mode = 'priv'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)""",
        })

    self.__read = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_read(self):
    self.__read = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), default=unicode("-"), is_leaf=True, yang_name="read", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'read\tSpecify a read view for the group', u'display-when': u"../group-version = 'v1' or\n../group-version = 'v2c' or\n../group-version = 'v3' or\n../group-auth-mode = 'auth' or\n../group-auth-mode = 'noauth' or\n../group-auth-mode = 'priv'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)


  def _get_write(self):
    """
    Getter method for write, mapped from YANG variable /snmp_server/group/write (string)
    """
    return self.__write
      
  def _set_write(self, v, load=False):
    """
    Setter method for write, mapped from YANG variable /snmp_server/group/write (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_write is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_write() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), default=unicode("-"), is_leaf=True, yang_name="write", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'write\tSpecify a write view for the group', u'display-when': u"../group-version = 'v1' or\n            ../group-version = 'v2c' or\n            ../group-version = 'v3' or\n../group-auth-mode = 'auth' or\n            ../group-auth-mode = 'noauth' or\n            ../group-auth-mode = 'priv'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """write must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), default=unicode("-"), is_leaf=True, yang_name="write", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'write\tSpecify a write view for the group', u'display-when': u"../group-version = 'v1' or\n            ../group-version = 'v2c' or\n            ../group-version = 'v3' or\n../group-auth-mode = 'auth' or\n            ../group-auth-mode = 'noauth' or\n            ../group-auth-mode = 'priv'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)""",
        })

    self.__write = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_write(self):
    self.__write = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), default=unicode("-"), is_leaf=True, yang_name="write", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'write\tSpecify a write view for the group', u'display-when': u"../group-version = 'v1' or\n            ../group-version = 'v2c' or\n            ../group-version = 'v3' or\n../group-auth-mode = 'auth' or\n            ../group-auth-mode = 'noauth' or\n            ../group-auth-mode = 'priv'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)


  def _get_notify(self):
    """
    Getter method for notify, mapped from YANG variable /snmp_server/group/notify (string)
    """
    return self.__notify
      
  def _set_notify(self, v, load=False):
    """
    Setter method for notify, mapped from YANG variable /snmp_server/group/notify (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_notify is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_notify() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), default=unicode("-"), is_leaf=True, yang_name="notify", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'notify\tSpecify a notify view for the group', u'display-when': u"../group-version = 'v1' or\n            ../group-version = 'v2c' or\n            ../group-version = 'v3' or\n../group-auth-mode = 'auth' or\n            ../group-auth-mode = 'noauth' or\n            ../group-auth-mode = 'priv'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """notify must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), default=unicode("-"), is_leaf=True, yang_name="notify", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'notify\tSpecify a notify view for the group', u'display-when': u"../group-version = 'v1' or\n            ../group-version = 'v2c' or\n            ../group-version = 'v3' or\n../group-auth-mode = 'auth' or\n            ../group-auth-mode = 'noauth' or\n            ../group-auth-mode = 'priv'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)""",
        })

    self.__notify = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_notify(self):
    self.__notify = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 32']}), default=unicode("-"), is_leaf=True, yang_name="notify", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'notify\tSpecify a notify view for the group', u'display-when': u"../group-version = 'v1' or\n            ../group-version = 'v2c' or\n            ../group-version = 'v3' or\n../group-auth-mode = 'auth' or\n            ../group-auth-mode = 'noauth' or\n            ../group-auth-mode = 'priv'"}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)

  group_name = __builtin__.property(_get_group_name, _set_group_name)
  group_version = __builtin__.property(_get_group_version, _set_group_version)
  group_auth_mode = __builtin__.property(_get_group_auth_mode, _set_group_auth_mode)
  read = __builtin__.property(_get_read, _set_read)
  write = __builtin__.property(_get_write, _set_write)
  notify = __builtin__.property(_get_notify, _set_notify)


  _pyangbind_elements = {'group_name': group_name, 'group_version': group_version, 'group_auth_mode': group_auth_mode, 'read': read, 'write': write, 'notify': notify, }


