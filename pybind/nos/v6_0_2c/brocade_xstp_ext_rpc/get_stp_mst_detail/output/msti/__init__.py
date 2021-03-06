
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vlans
import port
class msti(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-xstp-ext - based on the path /brocade_xstp_ext_rpc/get-stp-mst-detail/output/msti. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__instance_id','__msti_root_id','__msti_bridge_id','__msti_bridge_priority','__vlans','__port',)

  _yang_name = 'msti'
  _rest_name = 'msti'

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
    self.__msti_root_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="msti-root-id", rest_name="msti-root-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='bridge-id-type', is_config=True)
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)
    self.__msti_bridge_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="msti-bridge-id", rest_name="msti-bridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='bridge-id-type', is_config=True)
    self.__vlans = YANGDynClass(base=vlans.vlans, is_container='container', presence=False, yang_name="vlans", rest_name="vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    self.__port = YANGDynClass(base=YANGListType(False,port.port, yang_name="port", rest_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)
    self.__msti_bridge_priority = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="msti-bridge-priority", rest_name="msti-bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)

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
      return [u'brocade_xstp_ext_rpc', u'get-stp-mst-detail', u'output', u'msti']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-stp-mst-detail', u'output', u'msti']

  def _get_instance_id(self):
    """
    Getter method for instance_id, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/msti/instance_id (uint32)

    YANG Description: MSTI Instance
    """
    return self.__instance_id
      
  def _set_instance_id(self, v, load=False):
    """
    Setter method for instance_id, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/msti/instance_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance_id() directly.

    YANG Description: MSTI Instance
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)""",
        })

    self.__instance_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance_id(self):
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)


  def _get_msti_root_id(self):
    """
    Getter method for msti_root_id, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/msti/msti_root_id (bridge-id-type)

    YANG Description: MSTI Root Id
    """
    return self.__msti_root_id
      
  def _set_msti_root_id(self, v, load=False):
    """
    Setter method for msti_root_id, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/msti/msti_root_id (bridge-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_msti_root_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_msti_root_id() directly.

    YANG Description: MSTI Root Id
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="msti-root-id", rest_name="msti-root-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='bridge-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """msti_root_id must be of a type compatible with bridge-id-type""",
          'defined-type': "brocade-xstp-ext:bridge-id-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="msti-root-id", rest_name="msti-root-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='bridge-id-type', is_config=True)""",
        })

    self.__msti_root_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_msti_root_id(self):
    self.__msti_root_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="msti-root-id", rest_name="msti-root-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='bridge-id-type', is_config=True)


  def _get_msti_bridge_id(self):
    """
    Getter method for msti_bridge_id, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/msti/msti_bridge_id (bridge-id-type)

    YANG Description: MSTI bridge Id
    """
    return self.__msti_bridge_id
      
  def _set_msti_bridge_id(self, v, load=False):
    """
    Setter method for msti_bridge_id, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/msti/msti_bridge_id (bridge-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_msti_bridge_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_msti_bridge_id() directly.

    YANG Description: MSTI bridge Id
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="msti-bridge-id", rest_name="msti-bridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='bridge-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """msti_bridge_id must be of a type compatible with bridge-id-type""",
          'defined-type': "brocade-xstp-ext:bridge-id-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="msti-bridge-id", rest_name="msti-bridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='bridge-id-type', is_config=True)""",
        })

    self.__msti_bridge_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_msti_bridge_id(self):
    self.__msti_bridge_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="msti-bridge-id", rest_name="msti-bridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='bridge-id-type', is_config=True)


  def _get_msti_bridge_priority(self):
    """
    Getter method for msti_bridge_priority, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/msti/msti_bridge_priority (uint32)

    YANG Description: MSTI Bridge priority
    """
    return self.__msti_bridge_priority
      
  def _set_msti_bridge_priority(self, v, load=False):
    """
    Setter method for msti_bridge_priority, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/msti/msti_bridge_priority (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_msti_bridge_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_msti_bridge_priority() directly.

    YANG Description: MSTI Bridge priority
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="msti-bridge-priority", rest_name="msti-bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """msti_bridge_priority must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="msti-bridge-priority", rest_name="msti-bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)""",
        })

    self.__msti_bridge_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_msti_bridge_priority(self):
    self.__msti_bridge_priority = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="msti-bridge-priority", rest_name="msti-bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)


  def _get_vlans(self):
    """
    Getter method for vlans, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/msti/vlans (container)

    YANG Description: VLANs associated with this instance..
    """
    return self.__vlans
      
  def _set_vlans(self, v, load=False):
    """
    Setter method for vlans, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/msti/vlans (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlans is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlans() directly.

    YANG Description: VLANs associated with this instance..
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=vlans.vlans, is_container='container', presence=False, yang_name="vlans", rest_name="vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlans must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vlans.vlans, is_container='container', presence=False, yang_name="vlans", rest_name="vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)""",
        })

    self.__vlans = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlans(self):
    self.__vlans = YANGDynClass(base=vlans.vlans, is_container='container', presence=False, yang_name="vlans", rest_name="vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)


  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/msti/port (list)
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/msti/port (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType(False,port.port, yang_name="port", rest_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,port.port, yang_name="port", rest_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=YANGListType(False,port.port, yang_name="port", rest_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)

  instance_id = __builtin__.property(_get_instance_id, _set_instance_id)
  msti_root_id = __builtin__.property(_get_msti_root_id, _set_msti_root_id)
  msti_bridge_id = __builtin__.property(_get_msti_bridge_id, _set_msti_bridge_id)
  msti_bridge_priority = __builtin__.property(_get_msti_bridge_priority, _set_msti_bridge_priority)
  vlans = __builtin__.property(_get_vlans, _set_vlans)
  port = __builtin__.property(_get_port, _set_port)


  _pyangbind_elements = {'instance_id': instance_id, 'msti_root_id': msti_root_id, 'msti_bridge_id': msti_bridge_id, 'msti_bridge_priority': msti_bridge_priority, 'vlans': vlans, 'port': port, }


