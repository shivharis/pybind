
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class raslog_entries(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ras-ext - based on the path /brocade_ras_ext_rpc/show-raslog/output/show-all-raslog/raslog-entries. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__index','__message_id','__date_and_time_info','__severity','__repeat_count','__message','__message_flag','__log_type','__switch_or_chassis_name',)

  _yang_name = 'raslog-entries'
  _rest_name = 'raslog-entries'

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
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="index", rest_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)
    self.__message_flag = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'unknown': {'value': 2}, u'other': {'value': 1}, u'vcs': {'value': 4}, u'ffdc': {'value': 3}},), is_leaf=True, yang_name="message-flag", rest_name="message-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)
    self.__severity = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'unknown': {'value': 6}, u'warning': {'value': 3}, u'critical': {'value': 1}, u'error': {'value': 2}, u'debug': {'value': 5}, u'informational': {'value': 4}},), is_leaf=True, yang_name="severity", rest_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)
    self.__date_and_time_info = YANGDynClass(base=unicode, is_leaf=True, yang_name="date-and-time-info", rest_name="date-and-time-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)
    self.__repeat_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="repeat-count", rest_name="repeat-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)
    self.__message = YANGDynClass(base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)
    self.__message_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="message-id", rest_name="message-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)
    self.__log_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dce': {'value': 1}, u'system': {'value': 0}},), is_leaf=True, yang_name="log-type", rest_name="log-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)
    self.__switch_or_chassis_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="switch-or-chassis-name", rest_name="switch-or-chassis-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)

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
      return [u'brocade_ras_ext_rpc', u'show-raslog', u'output', u'show-all-raslog', u'raslog-entries']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-raslog', u'output', u'show-all-raslog', u'raslog-entries']

  def _get_index(self):
    """
    Getter method for index, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/index (uint32)

    YANG Description: Sequence number for the message
    """
    return self.__index
      
  def _set_index(self, v, load=False):
    """
    Setter method for index, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_index() directly.

    YANG Description: Sequence number for the message
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="index", rest_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="index", rest_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)""",
        })

    self.__index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_index(self):
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="index", rest_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)


  def _get_message_id(self):
    """
    Getter method for message_id, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/message_id (string)

    YANG Description: Message identifier
    """
    return self.__message_id
      
  def _set_message_id(self, v, load=False):
    """
    Setter method for message_id, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/message_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_message_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_message_id() directly.

    YANG Description: Message identifier
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="message-id", rest_name="message-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """message_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="message-id", rest_name="message-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)""",
        })

    self.__message_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_message_id(self):
    self.__message_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="message-id", rest_name="message-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)


  def _get_date_and_time_info(self):
    """
    Getter method for date_and_time_info, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/date_and_time_info (string)

    YANG Description: Date and time of the message.
The format is: YYYY-MM-DD/HH:MM:SS.SSSS (micro seconds)
    """
    return self.__date_and_time_info
      
  def _set_date_and_time_info(self, v, load=False):
    """
    Setter method for date_and_time_info, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/date_and_time_info (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_date_and_time_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_date_and_time_info() directly.

    YANG Description: Date and time of the message.
The format is: YYYY-MM-DD/HH:MM:SS.SSSS (micro seconds)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="date-and-time-info", rest_name="date-and-time-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """date_and_time_info must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="date-and-time-info", rest_name="date-and-time-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)""",
        })

    self.__date_and_time_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_date_and_time_info(self):
    self.__date_and_time_info = YANGDynClass(base=unicode, is_leaf=True, yang_name="date-and-time-info", rest_name="date-and-time-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)


  def _get_severity(self):
    """
    Getter method for severity, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/severity (enumeration)

    YANG Description: Severity of the message. Valid values include
INFO, WARNING, ERROR, and CRITICAL.
    """
    return self.__severity
      
  def _set_severity(self, v, load=False):
    """
    Setter method for severity, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/severity (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_severity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_severity() directly.

    YANG Description: Severity of the message. Valid values include
INFO, WARNING, ERROR, and CRITICAL.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'unknown': {'value': 6}, u'warning': {'value': 3}, u'critical': {'value': 1}, u'error': {'value': 2}, u'debug': {'value': 5}, u'informational': {'value': 4}},), is_leaf=True, yang_name="severity", rest_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """severity must be of a type compatible with enumeration""",
          'defined-type': "brocade-ras-ext:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'unknown': {'value': 6}, u'warning': {'value': 3}, u'critical': {'value': 1}, u'error': {'value': 2}, u'debug': {'value': 5}, u'informational': {'value': 4}},), is_leaf=True, yang_name="severity", rest_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)""",
        })

    self.__severity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_severity(self):
    self.__severity = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'unknown': {'value': 6}, u'warning': {'value': 3}, u'critical': {'value': 1}, u'error': {'value': 2}, u'debug': {'value': 5}, u'informational': {'value': 4}},), is_leaf=True, yang_name="severity", rest_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)


  def _get_repeat_count(self):
    """
    Getter method for repeat_count, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/repeat_count (uint32)

    YANG Description: It identifies how many times this particular
event has occurred.
    """
    return self.__repeat_count
      
  def _set_repeat_count(self, v, load=False):
    """
    Setter method for repeat_count, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/repeat_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_repeat_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_repeat_count() directly.

    YANG Description: It identifies how many times this particular
event has occurred.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="repeat-count", rest_name="repeat-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """repeat_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="repeat-count", rest_name="repeat-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)""",
        })

    self.__repeat_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_repeat_count(self):
    self.__repeat_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="repeat-count", rest_name="repeat-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)


  def _get_message(self):
    """
    Getter method for message, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/message (string)

    YANG Description: It contains the textual description of the event.
    """
    return self.__message
      
  def _set_message(self, v, load=False):
    """
    Setter method for message, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/message (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_message is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_message() directly.

    YANG Description: It contains the textual description of the event.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """message must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)""",
        })

    self.__message = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_message(self):
    self.__message = YANGDynClass(base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)


  def _get_message_flag(self):
    """
    Getter method for message_flag, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/message_flag (enumeration)

    YANG Description: It specifies the type of the message.
    """
    return self.__message_flag
      
  def _set_message_flag(self, v, load=False):
    """
    Setter method for message_flag, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/message_flag (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_message_flag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_message_flag() directly.

    YANG Description: It specifies the type of the message.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'unknown': {'value': 2}, u'other': {'value': 1}, u'vcs': {'value': 4}, u'ffdc': {'value': 3}},), is_leaf=True, yang_name="message-flag", rest_name="message-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """message_flag must be of a type compatible with enumeration""",
          'defined-type': "brocade-ras-ext:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'unknown': {'value': 2}, u'other': {'value': 1}, u'vcs': {'value': 4}, u'ffdc': {'value': 3}},), is_leaf=True, yang_name="message-flag", rest_name="message-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)""",
        })

    self.__message_flag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_message_flag(self):
    self.__message_flag = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'unknown': {'value': 2}, u'other': {'value': 1}, u'vcs': {'value': 4}, u'ffdc': {'value': 3}},), is_leaf=True, yang_name="message-flag", rest_name="message-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)


  def _get_log_type(self):
    """
    Getter method for log_type, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/log_type (enumeration)

    YANG Description: It specifies if the message is a SYSTEM or DCE log
    """
    return self.__log_type
      
  def _set_log_type(self, v, load=False):
    """
    Setter method for log_type, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/log_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_type() directly.

    YANG Description: It specifies if the message is a SYSTEM or DCE log
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dce': {'value': 1}, u'system': {'value': 0}},), is_leaf=True, yang_name="log-type", rest_name="log-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-ras-ext:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dce': {'value': 1}, u'system': {'value': 0}},), is_leaf=True, yang_name="log-type", rest_name="log-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)""",
        })

    self.__log_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_type(self):
    self.__log_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dce': {'value': 1}, u'system': {'value': 0}},), is_leaf=True, yang_name="log-type", rest_name="log-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)


  def _get_switch_or_chassis_name(self):
    """
    Getter method for switch_or_chassis_name, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/switch_or_chassis_name (string)

    YANG Description: Switch name for the generator of this message, or chassis
    """
    return self.__switch_or_chassis_name
      
  def _set_switch_or_chassis_name(self, v, load=False):
    """
    Setter method for switch_or_chassis_name, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries/switch_or_chassis_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_switch_or_chassis_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_switch_or_chassis_name() directly.

    YANG Description: Switch name for the generator of this message, or chassis
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="switch-or-chassis-name", rest_name="switch-or-chassis-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """switch_or_chassis_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="switch-or-chassis-name", rest_name="switch-or-chassis-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)""",
        })

    self.__switch_or_chassis_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_switch_or_chassis_name(self):
    self.__switch_or_chassis_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="switch-or-chassis-name", rest_name="switch-or-chassis-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)

  index = __builtin__.property(_get_index, _set_index)
  message_id = __builtin__.property(_get_message_id, _set_message_id)
  date_and_time_info = __builtin__.property(_get_date_and_time_info, _set_date_and_time_info)
  severity = __builtin__.property(_get_severity, _set_severity)
  repeat_count = __builtin__.property(_get_repeat_count, _set_repeat_count)
  message = __builtin__.property(_get_message, _set_message)
  message_flag = __builtin__.property(_get_message_flag, _set_message_flag)
  log_type = __builtin__.property(_get_log_type, _set_log_type)
  switch_or_chassis_name = __builtin__.property(_get_switch_or_chassis_name, _set_switch_or_chassis_name)


  _pyangbind_elements = {'index': index, 'message_id': message_id, 'date_and_time_info': date_and_time_info, 'severity': severity, 'repeat_count': repeat_count, 'message': message, 'message_flag': message_flag, 'log_type': log_type, 'switch_or_chassis_name': switch_or_chassis_name, }


