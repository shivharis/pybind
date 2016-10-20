
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import node_info
class show_firmware_version(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-firmware-ext - based on the path /brocade_firmware_ext_rpc/show-firmware-version/output/show-firmware-version. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__os_name','__os_version','__copy_right_info','__build_time','__firmware_full_version','__control_processor_vendor','__control_processor_chipset','__control_processor_memory','__node_info',)

  _yang_name = 'show-firmware-version'
  _rest_name = 'show-firmware-version'

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
    self.__os_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="os-name", rest_name="os-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)
    self.__copy_right_info = YANGDynClass(base=unicode, is_leaf=True, yang_name="copy-right-info", rest_name="copy-right-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)
    self.__build_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="build-time", rest_name="build-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)
    self.__control_processor_chipset = YANGDynClass(base=unicode, is_leaf=True, yang_name="control-processor-chipset", rest_name="control-processor-chipset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)
    self.__os_version = YANGDynClass(base=unicode, is_leaf=True, yang_name="os-version", rest_name="os-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)
    self.__node_info = YANGDynClass(base=YANGListType(False,node_info.node_info, yang_name="node-info", rest_name="node-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="node-info", rest_name="node-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='list', is_config=True)
    self.__firmware_full_version = YANGDynClass(base=unicode, is_leaf=True, yang_name="firmware-full-version", rest_name="firmware-full-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)
    self.__control_processor_vendor = YANGDynClass(base=unicode, is_leaf=True, yang_name="control-processor-vendor", rest_name="control-processor-vendor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)
    self.__control_processor_memory = YANGDynClass(base=unicode, is_leaf=True, yang_name="control-processor-memory", rest_name="control-processor-memory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)

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
      return [u'brocade_firmware_ext_rpc', u'show-firmware-version', u'output', u'show-firmware-version']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-firmware-version', u'output', u'show-firmware-version']

  def _get_os_name(self):
    """
    Getter method for os_name, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/os_name (string)

    YANG Description: Name of the Firmware version. Example: NOS, FOS etc.
    """
    return self.__os_name
      
  def _set_os_name(self, v, load=False):
    """
    Setter method for os_name, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/os_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_os_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_os_name() directly.

    YANG Description: Name of the Firmware version. Example: NOS, FOS etc.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="os-name", rest_name="os-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """os_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="os-name", rest_name="os-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)""",
        })

    self.__os_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_os_name(self):
    self.__os_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="os-name", rest_name="os-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)


  def _get_os_version(self):
    """
    Getter method for os_version, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/os_version (string)

    YANG Description: Version of the Firmware.
    """
    return self.__os_version
      
  def _set_os_version(self, v, load=False):
    """
    Setter method for os_version, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/os_version (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_os_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_os_version() directly.

    YANG Description: Version of the Firmware.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="os-version", rest_name="os-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """os_version must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="os-version", rest_name="os-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)""",
        })

    self.__os_version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_os_version(self):
    self.__os_version = YANGDynClass(base=unicode, is_leaf=True, yang_name="os-version", rest_name="os-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)


  def _get_copy_right_info(self):
    """
    Getter method for copy_right_info, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/copy_right_info (string)

    YANG Description: Copy right information of the Firmware.
    """
    return self.__copy_right_info
      
  def _set_copy_right_info(self, v, load=False):
    """
    Setter method for copy_right_info, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/copy_right_info (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_copy_right_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_copy_right_info() directly.

    YANG Description: Copy right information of the Firmware.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="copy-right-info", rest_name="copy-right-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """copy_right_info must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="copy-right-info", rest_name="copy-right-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)""",
        })

    self.__copy_right_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_copy_right_info(self):
    self.__copy_right_info = YANGDynClass(base=unicode, is_leaf=True, yang_name="copy-right-info", rest_name="copy-right-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)


  def _get_build_time(self):
    """
    Getter method for build_time, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/build_time (string)

    YANG Description: Time information on the build of Firmware.
    """
    return self.__build_time
      
  def _set_build_time(self, v, load=False):
    """
    Setter method for build_time, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/build_time (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_build_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_build_time() directly.

    YANG Description: Time information on the build of Firmware.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="build-time", rest_name="build-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """build_time must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="build-time", rest_name="build-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)""",
        })

    self.__build_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_build_time(self):
    self.__build_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="build-time", rest_name="build-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)


  def _get_firmware_full_version(self):
    """
    Getter method for firmware_full_version, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/firmware_full_version (string)

    YANG Description: Full version string of Firmware.
    """
    return self.__firmware_full_version
      
  def _set_firmware_full_version(self, v, load=False):
    """
    Setter method for firmware_full_version, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/firmware_full_version (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_firmware_full_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_firmware_full_version() directly.

    YANG Description: Full version string of Firmware.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="firmware-full-version", rest_name="firmware-full-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """firmware_full_version must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="firmware-full-version", rest_name="firmware-full-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)""",
        })

    self.__firmware_full_version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_firmware_full_version(self):
    self.__firmware_full_version = YANGDynClass(base=unicode, is_leaf=True, yang_name="firmware-full-version", rest_name="firmware-full-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)


  def _get_control_processor_vendor(self):
    """
    Getter method for control_processor_vendor, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/control_processor_vendor (string)

    YANG Description: Information on the control processor.
    """
    return self.__control_processor_vendor
      
  def _set_control_processor_vendor(self, v, load=False):
    """
    Setter method for control_processor_vendor, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/control_processor_vendor (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_control_processor_vendor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_control_processor_vendor() directly.

    YANG Description: Information on the control processor.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="control-processor-vendor", rest_name="control-processor-vendor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """control_processor_vendor must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="control-processor-vendor", rest_name="control-processor-vendor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)""",
        })

    self.__control_processor_vendor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_control_processor_vendor(self):
    self.__control_processor_vendor = YANGDynClass(base=unicode, is_leaf=True, yang_name="control-processor-vendor", rest_name="control-processor-vendor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)


  def _get_control_processor_chipset(self):
    """
    Getter method for control_processor_chipset, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/control_processor_chipset (string)

    YANG Description: Information on the control processor.
    """
    return self.__control_processor_chipset
      
  def _set_control_processor_chipset(self, v, load=False):
    """
    Setter method for control_processor_chipset, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/control_processor_chipset (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_control_processor_chipset is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_control_processor_chipset() directly.

    YANG Description: Information on the control processor.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="control-processor-chipset", rest_name="control-processor-chipset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """control_processor_chipset must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="control-processor-chipset", rest_name="control-processor-chipset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)""",
        })

    self.__control_processor_chipset = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_control_processor_chipset(self):
    self.__control_processor_chipset = YANGDynClass(base=unicode, is_leaf=True, yang_name="control-processor-chipset", rest_name="control-processor-chipset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)


  def _get_control_processor_memory(self):
    """
    Getter method for control_processor_memory, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/control_processor_memory (string)

    YANG Description: Memory of the control processor.
    """
    return self.__control_processor_memory
      
  def _set_control_processor_memory(self, v, load=False):
    """
    Setter method for control_processor_memory, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/control_processor_memory (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_control_processor_memory is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_control_processor_memory() directly.

    YANG Description: Memory of the control processor.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="control-processor-memory", rest_name="control-processor-memory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """control_processor_memory must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="control-processor-memory", rest_name="control-processor-memory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)""",
        })

    self.__control_processor_memory = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_control_processor_memory(self):
    self.__control_processor_memory = YANGDynClass(base=unicode, is_leaf=True, yang_name="control-processor-memory", rest_name="control-processor-memory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='string', is_config=True)


  def _get_node_info(self):
    """
    Getter method for node_info, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/node_info (list)
    """
    return self.__node_info
      
  def _set_node_info(self, v, load=False):
    """
    Setter method for node_info, mapped from YANG variable /brocade_firmware_ext_rpc/show_firmware_version/output/show_firmware_version/node_info (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_node_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_node_info() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType(False,node_info.node_info, yang_name="node-info", rest_name="node-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="node-info", rest_name="node-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """node_info must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,node_info.node_info, yang_name="node-info", rest_name="node-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="node-info", rest_name="node-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='list', is_config=True)""",
        })

    self.__node_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_node_info(self):
    self.__node_info = YANGDynClass(base=YANGListType(False,node_info.node_info, yang_name="node-info", rest_name="node-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="node-info", rest_name="node-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware-ext', defining_module='brocade-firmware-ext', yang_type='list', is_config=True)

  os_name = __builtin__.property(_get_os_name, _set_os_name)
  os_version = __builtin__.property(_get_os_version, _set_os_version)
  copy_right_info = __builtin__.property(_get_copy_right_info, _set_copy_right_info)
  build_time = __builtin__.property(_get_build_time, _set_build_time)
  firmware_full_version = __builtin__.property(_get_firmware_full_version, _set_firmware_full_version)
  control_processor_vendor = __builtin__.property(_get_control_processor_vendor, _set_control_processor_vendor)
  control_processor_chipset = __builtin__.property(_get_control_processor_chipset, _set_control_processor_chipset)
  control_processor_memory = __builtin__.property(_get_control_processor_memory, _set_control_processor_memory)
  node_info = __builtin__.property(_get_node_info, _set_node_info)


  _pyangbind_elements = {'os_name': os_name, 'os_version': os_version, 'copy_right_info': copy_right_info, 'build_time': build_time, 'firmware_full_version': firmware_full_version, 'control_processor_vendor': control_processor_vendor, 'control_processor_chipset': control_processor_chipset, 'control_processor_memory': control_processor_memory, 'node_info': node_info, }


