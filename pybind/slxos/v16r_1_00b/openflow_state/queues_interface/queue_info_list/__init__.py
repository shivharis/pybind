
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class queue_info_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/queues-interface/queue-info-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Queue Info
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface','__num','__tx_packets','__tx_bytes',)

  _yang_name = 'queue-info-list'

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
    self.__interface = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    self.__tx_bytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)
    self.__num = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__tx_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)

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
      return [u'openflow-state', u'queues-interface', u'queue-info-list']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'openflow-state', u'queues-interface', u'queue-info-list']

  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /openflow_state/queues_interface/queue_info_list/interface (string)

    YANG Description: Port
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /openflow_state/queues_interface/queue_info_list/interface (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: Port
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)


  def _get_num(self):
    """
    Getter method for num, mapped from YANG variable /openflow_state/queues_interface/queue_info_list/num (uint32)

    YANG Description: Queue Number
    """
    return self.__num
      
  def _set_num(self, v, load=False):
    """
    Setter method for num, mapped from YANG variable /openflow_state/queues_interface/queue_info_list/num (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num() directly.

    YANG Description: Queue Number
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num(self):
    self.__num = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_tx_packets(self):
    """
    Getter method for tx_packets, mapped from YANG variable /openflow_state/queues_interface/queue_info_list/tx_packets (uint64)

    YANG Description: Tx Packets
    """
    return self.__tx_packets
      
  def _set_tx_packets(self, v, load=False):
    """
    Setter method for tx_packets, mapped from YANG variable /openflow_state/queues_interface/queue_info_list/tx_packets (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tx_packets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tx_packets() directly.

    YANG Description: Tx Packets
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tx_packets must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)""",
        })

    self.__tx_packets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tx_packets(self):
    self.__tx_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)


  def _get_tx_bytes(self):
    """
    Getter method for tx_bytes, mapped from YANG variable /openflow_state/queues_interface/queue_info_list/tx_bytes (uint64)

    YANG Description: Tx Bytes
    """
    return self.__tx_bytes
      
  def _set_tx_bytes(self, v, load=False):
    """
    Setter method for tx_bytes, mapped from YANG variable /openflow_state/queues_interface/queue_info_list/tx_bytes (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tx_bytes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tx_bytes() directly.

    YANG Description: Tx Bytes
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tx_bytes must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)""",
        })

    self.__tx_bytes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tx_bytes(self):
    self.__tx_bytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint64', is_config=False)

  interface = __builtin__.property(_get_interface)
  num = __builtin__.property(_get_num)
  tx_packets = __builtin__.property(_get_tx_packets)
  tx_bytes = __builtin__.property(_get_tx_bytes)


  _pyangbind_elements = {'interface': interface, 'num': num, 'tx_packets': tx_packets, 'tx_bytes': tx_bytes, }


