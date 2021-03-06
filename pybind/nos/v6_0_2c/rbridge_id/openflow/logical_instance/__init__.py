
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import version
import controller
import passive
class logical_instance(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/openflow/logical-instance. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: OpenFlow logical instance configuration. There can be multiple
logical instances under a physical switch.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__instance_id','__version','__controller','__passive','__default_forwarding_action','__activate',)

  _yang_name = 'logical-instance'
  _rest_name = 'logical-instance'

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
    self.__passive = YANGDynClass(base=passive.passive, is_container='container', presence=False, yang_name="passive", rest_name="passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Passive controller connection', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)
    self.__activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Activate this logical instance', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='empty', is_config=True)
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='uint32', is_config=True)
    self.__controller = YANGDynClass(base=YANGListType("controller_name",controller.controller, yang_name="controller", rest_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='controller-name', extensions={u'tailf-common': {u'callpoint': u'OpenFlowAttachedControllers', u'info': u'OpenFlow controller name', u'cli-suppress-mode': None}}), is_container='list', yang_name="controller", rest_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'OpenFlowAttachedControllers', u'info': u'OpenFlow controller name', u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='list', is_config=True)
    self.__version = YANGDynClass(base=YANGListType("version_name",version.version, yang_name="version", rest_name="version", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='version-name', extensions={u'tailf-common': {u'callpoint': u'OpenFlowSupportedVersions', u'info': u'OpenFlow version', u'cli-suppress-mode': None}}), is_container='list', yang_name="version", rest_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'OpenFlowSupportedVersions', u'info': u'OpenFlow version', u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='list', is_config=True)
    self.__default_forwarding_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'drop': {'value': 2}, u'send-to-controller': {'value': 1}},), default=unicode("drop"), is_leaf=True, yang_name="default-forwarding-action", rest_name="default-behavior", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Default MISS behavior for this logical instance', u'cli-full-command': None, u'alt-name': u'default-behavior'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='enumeration', is_config=True)

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
      return [u'rbridge-id', u'openflow', u'logical-instance']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'openflow', u'logical-instance']

  def _get_instance_id(self):
    """
    Getter method for instance_id, mapped from YANG variable /rbridge_id/openflow/logical_instance/instance_id (uint32)

    YANG Description: OpenFlow logical instance id
    """
    return self.__instance_id
      
  def _set_instance_id(self, v, load=False):
    """
    Setter method for instance_id, mapped from YANG variable /rbridge_id/openflow/logical_instance/instance_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance_id() directly.

    YANG Description: OpenFlow logical instance id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='uint32', is_config=True)""",
        })

    self.__instance_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance_id(self):
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='uint32', is_config=True)


  def _get_version(self):
    """
    Getter method for version, mapped from YANG variable /rbridge_id/openflow/logical_instance/version (list)

    YANG Description: OpenFlow version
    """
    return self.__version
      
  def _set_version(self, v, load=False):
    """
    Setter method for version, mapped from YANG variable /rbridge_id/openflow/logical_instance/version (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_version() directly.

    YANG Description: OpenFlow version
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("version_name",version.version, yang_name="version", rest_name="version", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='version-name', extensions={u'tailf-common': {u'callpoint': u'OpenFlowSupportedVersions', u'info': u'OpenFlow version', u'cli-suppress-mode': None}}), is_container='list', yang_name="version", rest_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'OpenFlowSupportedVersions', u'info': u'OpenFlow version', u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """version must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("version_name",version.version, yang_name="version", rest_name="version", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='version-name', extensions={u'tailf-common': {u'callpoint': u'OpenFlowSupportedVersions', u'info': u'OpenFlow version', u'cli-suppress-mode': None}}), is_container='list', yang_name="version", rest_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'OpenFlowSupportedVersions', u'info': u'OpenFlow version', u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='list', is_config=True)""",
        })

    self.__version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_version(self):
    self.__version = YANGDynClass(base=YANGListType("version_name",version.version, yang_name="version", rest_name="version", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='version-name', extensions={u'tailf-common': {u'callpoint': u'OpenFlowSupportedVersions', u'info': u'OpenFlow version', u'cli-suppress-mode': None}}), is_container='list', yang_name="version", rest_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'OpenFlowSupportedVersions', u'info': u'OpenFlow version', u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='list', is_config=True)


  def _get_controller(self):
    """
    Getter method for controller, mapped from YANG variable /rbridge_id/openflow/logical_instance/controller (list)

    YANG Description: OpenFlow controller name
    """
    return self.__controller
      
  def _set_controller(self, v, load=False):
    """
    Setter method for controller, mapped from YANG variable /rbridge_id/openflow/logical_instance/controller (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_controller is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_controller() directly.

    YANG Description: OpenFlow controller name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("controller_name",controller.controller, yang_name="controller", rest_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='controller-name', extensions={u'tailf-common': {u'callpoint': u'OpenFlowAttachedControllers', u'info': u'OpenFlow controller name', u'cli-suppress-mode': None}}), is_container='list', yang_name="controller", rest_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'OpenFlowAttachedControllers', u'info': u'OpenFlow controller name', u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """controller must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("controller_name",controller.controller, yang_name="controller", rest_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='controller-name', extensions={u'tailf-common': {u'callpoint': u'OpenFlowAttachedControllers', u'info': u'OpenFlow controller name', u'cli-suppress-mode': None}}), is_container='list', yang_name="controller", rest_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'OpenFlowAttachedControllers', u'info': u'OpenFlow controller name', u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='list', is_config=True)""",
        })

    self.__controller = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_controller(self):
    self.__controller = YANGDynClass(base=YANGListType("controller_name",controller.controller, yang_name="controller", rest_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='controller-name', extensions={u'tailf-common': {u'callpoint': u'OpenFlowAttachedControllers', u'info': u'OpenFlow controller name', u'cli-suppress-mode': None}}), is_container='list', yang_name="controller", rest_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'OpenFlowAttachedControllers', u'info': u'OpenFlow controller name', u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='list', is_config=True)


  def _get_passive(self):
    """
    Getter method for passive, mapped from YANG variable /rbridge_id/openflow/logical_instance/passive (container)

    YANG Description: Passive controller connection
    """
    return self.__passive
      
  def _set_passive(self, v, load=False):
    """
    Setter method for passive, mapped from YANG variable /rbridge_id/openflow/logical_instance/passive (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_passive is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_passive() directly.

    YANG Description: Passive controller connection
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=passive.passive, is_container='container', presence=False, yang_name="passive", rest_name="passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Passive controller connection', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """passive must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=passive.passive, is_container='container', presence=False, yang_name="passive", rest_name="passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Passive controller connection', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)""",
        })

    self.__passive = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_passive(self):
    self.__passive = YANGDynClass(base=passive.passive, is_container='container', presence=False, yang_name="passive", rest_name="passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Passive controller connection', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)


  def _get_default_forwarding_action(self):
    """
    Getter method for default_forwarding_action, mapped from YANG variable /rbridge_id/openflow/logical_instance/default_forwarding_action (enumeration)

    YANG Description: Default MISS behavior for this logical instance
    """
    return self.__default_forwarding_action
      
  def _set_default_forwarding_action(self, v, load=False):
    """
    Setter method for default_forwarding_action, mapped from YANG variable /rbridge_id/openflow/logical_instance/default_forwarding_action (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_forwarding_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_forwarding_action() directly.

    YANG Description: Default MISS behavior for this logical instance
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'drop': {'value': 2}, u'send-to-controller': {'value': 1}},), default=unicode("drop"), is_leaf=True, yang_name="default-forwarding-action", rest_name="default-behavior", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Default MISS behavior for this logical instance', u'cli-full-command': None, u'alt-name': u'default-behavior'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_forwarding_action must be of a type compatible with enumeration""",
          'defined-type': "brocade-openflow:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'drop': {'value': 2}, u'send-to-controller': {'value': 1}},), default=unicode("drop"), is_leaf=True, yang_name="default-forwarding-action", rest_name="default-behavior", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Default MISS behavior for this logical instance', u'cli-full-command': None, u'alt-name': u'default-behavior'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='enumeration', is_config=True)""",
        })

    self.__default_forwarding_action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_forwarding_action(self):
    self.__default_forwarding_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'drop': {'value': 2}, u'send-to-controller': {'value': 1}},), default=unicode("drop"), is_leaf=True, yang_name="default-forwarding-action", rest_name="default-behavior", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Default MISS behavior for this logical instance', u'cli-full-command': None, u'alt-name': u'default-behavior'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='enumeration', is_config=True)


  def _get_activate(self):
    """
    Getter method for activate, mapped from YANG variable /rbridge_id/openflow/logical_instance/activate (empty)

    YANG Description: Activate this logical instance
    """
    return self.__activate
      
  def _set_activate(self, v, load=False):
    """
    Setter method for activate, mapped from YANG variable /rbridge_id/openflow/logical_instance/activate (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_activate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_activate() directly.

    YANG Description: Activate this logical instance
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Activate this logical instance', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """activate must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Activate this logical instance', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='empty', is_config=True)""",
        })

    self.__activate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_activate(self):
    self.__activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Activate this logical instance', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='empty', is_config=True)

  instance_id = __builtin__.property(_get_instance_id, _set_instance_id)
  version = __builtin__.property(_get_version, _set_version)
  controller = __builtin__.property(_get_controller, _set_controller)
  passive = __builtin__.property(_get_passive, _set_passive)
  default_forwarding_action = __builtin__.property(_get_default_forwarding_action, _set_default_forwarding_action)
  activate = __builtin__.property(_get_activate, _set_activate)


  _pyangbind_elements = {'instance_id': instance_id, 'version': version, 'controller': controller, 'passive': passive, 'default_forwarding_action': default_forwarding_action, 'activate': activate, }


