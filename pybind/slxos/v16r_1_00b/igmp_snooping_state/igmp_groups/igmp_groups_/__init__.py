
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import igmpv3_sources
class igmp_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mc-hms-operational - based on the path /igmp-snooping-state/igmp-groups/igmp-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Igmp Snooping Group Information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__group_addr','__interface_name','__uptime','__expiry_time','__last_reporter','__filter_mode','__member_ship','__igmpv3_sources',)

  _yang_name = 'igmp-groups'
  _rest_name = 'igmp-groups'

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
    self.__uptime = YANGDynClass(base=unicode, is_leaf=True, yang_name="uptime", rest_name="uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__expiry_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="expiry-time", rest_name="expiry-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__group_addr = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="group-addr", rest_name="group-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    self.__igmpv3_sources = YANGDynClass(base=YANGListType("interface_name",igmpv3_sources.igmpv3_sources, yang_name="igmpv3-sources", rest_name="igmpv3-sources", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-name', extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmpv3-sources', u'cli-suppress-show-path': None}}), is_container='list', yang_name="igmpv3-sources", rest_name="igmpv3-sources", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmpv3-sources', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)
    self.__member_ship = YANGDynClass(base=unicode, is_leaf=True, yang_name="member-ship", rest_name="member-ship", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__filter_mode = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="filter-mode", rest_name="filter-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    self.__last_reporter = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-reporter", rest_name="last-reporter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)

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
      return [u'igmp-snooping-state', u'igmp-groups', u'igmp-groups']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'igmp-snooping-state', u'igmp-groups', u'igmp-groups']

  def _get_group_addr(self):
    """
    Getter method for group_addr, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/group_addr (uint32)

    YANG Description: group ip address
    """
    return self.__group_addr
      
  def _set_group_addr(self, v, load=False):
    """
    Setter method for group_addr, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/group_addr (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_addr() directly.

    YANG Description: group ip address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="group-addr", rest_name="group-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_addr must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="group-addr", rest_name="group-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__group_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_addr(self):
    self.__group_addr = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="group-addr", rest_name="group-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_interface_name(self):
    """
    Getter method for interface_name, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/interface_name (string)

    YANG Description: Igmp interface name hosting a group
    """
    return self.__interface_name
      
  def _set_interface_name(self, v, load=False):
    """
    Setter method for interface_name, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/interface_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_name() directly.

    YANG Description: Igmp interface name hosting a group
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_name(self):
    self.__interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_uptime(self):
    """
    Getter method for uptime, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/uptime (string)

    YANG Description: group up time
    """
    return self.__uptime
      
  def _set_uptime(self, v, load=False):
    """
    Setter method for uptime, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/uptime (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_uptime is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_uptime() directly.

    YANG Description: group up time
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="uptime", rest_name="uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """uptime must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="uptime", rest_name="uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__uptime = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_uptime(self):
    self.__uptime = YANGDynClass(base=unicode, is_leaf=True, yang_name="uptime", rest_name="uptime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_expiry_time(self):
    """
    Getter method for expiry_time, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/expiry_time (string)

    YANG Description: group expiry time
    """
    return self.__expiry_time
      
  def _set_expiry_time(self, v, load=False):
    """
    Setter method for expiry_time, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/expiry_time (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_expiry_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_expiry_time() directly.

    YANG Description: group expiry time
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="expiry-time", rest_name="expiry-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """expiry_time must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="expiry-time", rest_name="expiry-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__expiry_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_expiry_time(self):
    self.__expiry_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="expiry-time", rest_name="expiry-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_last_reporter(self):
    """
    Getter method for last_reporter, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/last_reporter (uint32)

    YANG Description: last reporter
    """
    return self.__last_reporter
      
  def _set_last_reporter(self, v, load=False):
    """
    Setter method for last_reporter, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/last_reporter (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_reporter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_reporter() directly.

    YANG Description: last reporter
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-reporter", rest_name="last-reporter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_reporter must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-reporter", rest_name="last-reporter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__last_reporter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_reporter(self):
    self.__last_reporter = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="last-reporter", rest_name="last-reporter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_filter_mode(self):
    """
    Getter method for filter_mode, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/filter_mode (uint8)

    YANG Description: filter mode
    """
    return self.__filter_mode
      
  def _set_filter_mode(self, v, load=False):
    """
    Setter method for filter_mode, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/filter_mode (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_filter_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_filter_mode() directly.

    YANG Description: filter mode
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="filter-mode", rest_name="filter-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """filter_mode must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="filter-mode", rest_name="filter-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)""",
        })

    self.__filter_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_filter_mode(self):
    self.__filter_mode = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="filter-mode", rest_name="filter-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)


  def _get_member_ship(self):
    """
    Getter method for member_ship, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/member_ship (string)

    YANG Description: Group interface member ship
    """
    return self.__member_ship
      
  def _set_member_ship(self, v, load=False):
    """
    Setter method for member_ship, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/member_ship (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_member_ship is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_member_ship() directly.

    YANG Description: Group interface member ship
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="member-ship", rest_name="member-ship", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """member_ship must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="member-ship", rest_name="member-ship", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__member_ship = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_member_ship(self):
    self.__member_ship = YANGDynClass(base=unicode, is_leaf=True, yang_name="member-ship", rest_name="member-ship", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_igmpv3_sources(self):
    """
    Getter method for igmpv3_sources, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/igmpv3_sources (list)

    YANG Description: Igmp Snooping version 3 include/exclude source list
    """
    return self.__igmpv3_sources
      
  def _set_igmpv3_sources(self, v, load=False):
    """
    Setter method for igmpv3_sources, mapped from YANG variable /igmp_snooping_state/igmp_groups/igmp_groups/igmpv3_sources (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmpv3_sources is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmpv3_sources() directly.

    YANG Description: Igmp Snooping version 3 include/exclude source list
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("interface_name",igmpv3_sources.igmpv3_sources, yang_name="igmpv3-sources", rest_name="igmpv3-sources", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-name', extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmpv3-sources', u'cli-suppress-show-path': None}}), is_container='list', yang_name="igmpv3-sources", rest_name="igmpv3-sources", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmpv3-sources', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmpv3_sources must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("interface_name",igmpv3_sources.igmpv3_sources, yang_name="igmpv3-sources", rest_name="igmpv3-sources", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-name', extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmpv3-sources', u'cli-suppress-show-path': None}}), is_container='list', yang_name="igmpv3-sources", rest_name="igmpv3-sources", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmpv3-sources', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)""",
        })

    self.__igmpv3_sources = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmpv3_sources(self):
    self.__igmpv3_sources = YANGDynClass(base=YANGListType("interface_name",igmpv3_sources.igmpv3_sources, yang_name="igmpv3-sources", rest_name="igmpv3-sources", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-name', extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmpv3-sources', u'cli-suppress-show-path': None}}), is_container='list', yang_name="igmpv3-sources", rest_name="igmpv3-sources", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mc-hms-igmpv3-sources', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='list', is_config=False)

  group_addr = __builtin__.property(_get_group_addr)
  interface_name = __builtin__.property(_get_interface_name)
  uptime = __builtin__.property(_get_uptime)
  expiry_time = __builtin__.property(_get_expiry_time)
  last_reporter = __builtin__.property(_get_last_reporter)
  filter_mode = __builtin__.property(_get_filter_mode)
  member_ship = __builtin__.property(_get_member_ship)
  igmpv3_sources = __builtin__.property(_get_igmpv3_sources)


  _pyangbind_elements = {'group_addr': group_addr, 'interface_name': interface_name, 'uptime': uptime, 'expiry_time': expiry_time, 'last_reporter': last_reporter, 'filter_mode': filter_mode, 'member_ship': member_ship, 'igmpv3_sources': igmpv3_sources, }


