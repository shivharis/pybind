
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import queue_info_list
class queues_interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/queues-interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface_value','__queue_info_list',)

  _yang_name = 'queues-interface'

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
    self.__interface_value = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    self.__queue_info_list = YANGDynClass(base=YANGListType("interface num",queue_info_list.queue_info_list, yang_name="queue-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface num', extensions={u'tailf-common': {u'callpoint': u'openflow-queue-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="queue-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-queue-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)

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
      return [u'openflow-state', u'queues-interface']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'openflow-state', u'queues-interface']

  def _get_interface_value(self):
    """
    Getter method for interface_value, mapped from YANG variable /openflow_state/queues_interface/interface_value (string)

    YANG Description: Port
    """
    return self.__interface_value
      
  def _set_interface_value(self, v, load=False):
    """
    Setter method for interface_value, mapped from YANG variable /openflow_state/queues_interface/interface_value (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_value() directly.

    YANG Description: Port
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_value must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__interface_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_value(self):
    self.__interface_value = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)


  def _get_queue_info_list(self):
    """
    Getter method for queue_info_list, mapped from YANG variable /openflow_state/queues_interface/queue_info_list (list)

    YANG Description: Queue Info
    """
    return self.__queue_info_list
      
  def _set_queue_info_list(self, v, load=False):
    """
    Setter method for queue_info_list, mapped from YANG variable /openflow_state/queues_interface/queue_info_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_info_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_info_list() directly.

    YANG Description: Queue Info
    """
    try:
      t = YANGDynClass(v,base=YANGListType("interface num",queue_info_list.queue_info_list, yang_name="queue-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface num', extensions={u'tailf-common': {u'callpoint': u'openflow-queue-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="queue-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-queue-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_info_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("interface num",queue_info_list.queue_info_list, yang_name="queue-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface num', extensions={u'tailf-common': {u'callpoint': u'openflow-queue-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="queue-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-queue-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)""",
        })

    self.__queue_info_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_info_list(self):
    self.__queue_info_list = YANGDynClass(base=YANGListType("interface num",queue_info_list.queue_info_list, yang_name="queue-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface num', extensions={u'tailf-common': {u'callpoint': u'openflow-queue-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="queue-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-queue-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)

  interface_value = __builtin__.property(_get_interface_value)
  queue_info_list = __builtin__.property(_get_queue_info_list)


  _pyangbind_elements = {'interface_value': interface_value, 'queue_info_list': queue_info_list, }


