
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-firmware - based on the path /brocade_firmware_rpc/logical-chassis-fwdl-sanity/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__user','__password','__host','__directory','__file','__rbridge_id','__auto_activate','__coldboot','__protocol',)

  _yang_name = 'input'

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
    self.__protocol = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ftp': {'value': 1}, u'scp': {'value': 2}, u'sftp': {'value': 3}},), is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Protocol type : ftp, scp or sftp'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)
    self.__rbridge_id = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'all'}),], is_leaf=True, yang_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"Enter 'all' for firmware download on all nodes in the \nlogical-chassis or comma seperated rbridge-ids like 'rbridge-id 3,4,7-9,20'"}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rbridge-ids-all-type', is_config=True)
    self.__coldboot = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="coldboot", parent=self, choice=(u'cluster-options', u'coldboot'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Perform non ISSU firmware download.'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='empty', is_config=True)
    self.__host = YANGDynClass(base=unicode, is_leaf=True, yang_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Host ipv4/ipv6 address'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__user = YANGDynClass(base=unicode, is_leaf=True, yang_name="user", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Username'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__file = YANGDynClass(base=unicode, is_leaf=True, yang_name="file", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Package release file, example - release.plist'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__directory = YANGDynClass(base=unicode, is_leaf=True, yang_name="directory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Directory'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__password = YANGDynClass(base=unicode, is_leaf=True, yang_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Password', u'suppress-echo': u'true'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__auto_activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="auto-activate", parent=self, choice=(u'cluster-options', u'auto-activate'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'To activate new firmware on all nodes'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='empty', is_config=True)

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
      return [u'brocade_firmware_rpc', u'logical-chassis-fwdl-sanity', u'input']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'logical-chassis-fwdl-sanity', u'input']

  def _get_user(self):
    """
    Getter method for user, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/user (string)
    """
    return self.__user
      
  def _set_user(self, v, load=False):
    """
    Setter method for user, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/user (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_user is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_user() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="user", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Username'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """user must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="user", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Username'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__user = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_user(self):
    self.__user = YANGDynClass(base=unicode, is_leaf=True, yang_name="user", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Username'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_password(self):
    """
    Getter method for password, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/password (string)
    """
    return self.__password
      
  def _set_password(self, v, load=False):
    """
    Setter method for password, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/password (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_password is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_password() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Password', u'suppress-echo': u'true'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """password must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Password', u'suppress-echo': u'true'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__password = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_password(self):
    self.__password = YANGDynClass(base=unicode, is_leaf=True, yang_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Password', u'suppress-echo': u'true'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_host(self):
    """
    Getter method for host, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/host (string)
    """
    return self.__host
      
  def _set_host(self, v, load=False):
    """
    Setter method for host, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/host (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Host ipv4/ipv6 address'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Host ipv4/ipv6 address'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__host = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host(self):
    self.__host = YANGDynClass(base=unicode, is_leaf=True, yang_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Host ipv4/ipv6 address'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_directory(self):
    """
    Getter method for directory, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/directory (string)
    """
    return self.__directory
      
  def _set_directory(self, v, load=False):
    """
    Setter method for directory, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/directory (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_directory is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_directory() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="directory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Directory'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """directory must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="directory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Directory'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__directory = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_directory(self):
    self.__directory = YANGDynClass(base=unicode, is_leaf=True, yang_name="directory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Directory'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_file(self):
    """
    Getter method for file, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/file (string)
    """
    return self.__file
      
  def _set_file(self, v, load=False):
    """
    Setter method for file, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/file (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_file is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_file() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="file", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Package release file, example - release.plist'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """file must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="file", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Package release file, example - release.plist'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__file = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_file(self):
    self.__file = YANGDynClass(base=unicode, is_leaf=True, yang_name="file", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Package release file, example - release.plist'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_rbridge_id(self):
    """
    Getter method for rbridge_id, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/rbridge_id (rbridge-ids-all-type)
    """
    return self.__rbridge_id
      
  def _set_rbridge_id(self, v, load=False):
    """
    Setter method for rbridge_id, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/rbridge_id (rbridge-ids-all-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rbridge_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rbridge_id() directly.
    """
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'all'}),], is_leaf=True, yang_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"Enter 'all' for firmware download on all nodes in the \nlogical-chassis or comma seperated rbridge-ids like 'rbridge-id 3,4,7-9,20'"}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rbridge-ids-all-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rbridge_id must be of a type compatible with rbridge-ids-all-type""",
          'defined-type': "brocade-firmware:rbridge-ids-all-type",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'all'}),], is_leaf=True, yang_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"Enter 'all' for firmware download on all nodes in the \nlogical-chassis or comma seperated rbridge-ids like 'rbridge-id 3,4,7-9,20'"}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rbridge-ids-all-type', is_config=True)""",
        })

    self.__rbridge_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rbridge_id(self):
    self.__rbridge_id = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'all'}),], is_leaf=True, yang_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"Enter 'all' for firmware download on all nodes in the \nlogical-chassis or comma seperated rbridge-ids like 'rbridge-id 3,4,7-9,20'"}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='rbridge-ids-all-type', is_config=True)


  def _get_auto_activate(self):
    """
    Getter method for auto_activate, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/auto_activate (empty)
    """
    return self.__auto_activate
      
  def _set_auto_activate(self, v, load=False):
    """
    Setter method for auto_activate, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/auto_activate (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auto_activate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auto_activate() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="auto-activate", parent=self, choice=(u'cluster-options', u'auto-activate'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'To activate new firmware on all nodes'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auto_activate must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="auto-activate", parent=self, choice=(u'cluster-options', u'auto-activate'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'To activate new firmware on all nodes'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='empty', is_config=True)""",
        })

    self.__auto_activate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auto_activate(self):
    self.__auto_activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="auto-activate", parent=self, choice=(u'cluster-options', u'auto-activate'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'To activate new firmware on all nodes'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='empty', is_config=True)


  def _get_coldboot(self):
    """
    Getter method for coldboot, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/coldboot (empty)
    """
    return self.__coldboot
      
  def _set_coldboot(self, v, load=False):
    """
    Setter method for coldboot, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/coldboot (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_coldboot is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_coldboot() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="coldboot", parent=self, choice=(u'cluster-options', u'coldboot'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Perform non ISSU firmware download.'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """coldboot must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="coldboot", parent=self, choice=(u'cluster-options', u'coldboot'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Perform non ISSU firmware download.'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='empty', is_config=True)""",
        })

    self.__coldboot = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_coldboot(self):
    self.__coldboot = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="coldboot", parent=self, choice=(u'cluster-options', u'coldboot'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Perform non ISSU firmware download.'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='empty', is_config=True)


  def _get_protocol(self):
    """
    Getter method for protocol, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/protocol (enumeration)
    """
    return self.__protocol
      
  def _set_protocol(self, v, load=False):
    """
    Setter method for protocol, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/input/protocol (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ftp': {'value': 1}, u'scp': {'value': 2}, u'sftp': {'value': 3}},), is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Protocol type : ftp, scp or sftp'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol must be of a type compatible with enumeration""",
          'defined-type': "brocade-firmware:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ftp': {'value': 1}, u'scp': {'value': 2}, u'sftp': {'value': 3}},), is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Protocol type : ftp, scp or sftp'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)""",
        })

    self.__protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol(self):
    self.__protocol = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ftp': {'value': 1}, u'scp': {'value': 2}, u'sftp': {'value': 3}},), is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Protocol type : ftp, scp or sftp'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)

  user = __builtin__.property(_get_user, _set_user)
  password = __builtin__.property(_get_password, _set_password)
  host = __builtin__.property(_get_host, _set_host)
  directory = __builtin__.property(_get_directory, _set_directory)
  file = __builtin__.property(_get_file, _set_file)
  rbridge_id = __builtin__.property(_get_rbridge_id, _set_rbridge_id)
  auto_activate = __builtin__.property(_get_auto_activate, _set_auto_activate)
  coldboot = __builtin__.property(_get_coldboot, _set_coldboot)
  protocol = __builtin__.property(_get_protocol, _set_protocol)

  __choices__ = {u'cluster-options': {u'auto-activate': [u'auto_activate'], u'coldboot': [u'coldboot']}}
  _pyangbind_elements = {'user': user, 'password': password, 'host': host, 'directory': directory, 'file': file, 'rbridge_id': rbridge_id, 'auto_activate': auto_activate, 'coldboot': coldboot, 'protocol': protocol, }


