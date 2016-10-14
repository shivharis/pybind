
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class tmvoqstatistics(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sysdiag-operational - based on the path /tm-state/tmvoqstatistics. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Get TM VOQ statistics
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ing_slot','__ing_tower','__egr_voqid','__priority','__enquepkt','__enqueubytes','__discardpkt','__discardbytes','__currdepth','__maxdepth',)

  _yang_name = 'tmvoqstatistics'

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
    self.__discardpkt = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardpkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__egr_voqid = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="egr-voqid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    self.__enqueubytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enqueubytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__discardbytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardbytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    self.__ing_slot = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="ing-slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    self.__maxdepth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="maxdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__enquepkt = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enquepkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__currdepth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="currdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__ing_tower = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="ing-tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)

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
      return [u'tm-state', u'tmvoqstatistics']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'tm-state', u'tmvoqstatistics']

  def _get_ing_slot(self):
    """
    Getter method for ing_slot, mapped from YANG variable /tm_state/tmvoqstatistics/ing_slot (uint16)

    YANG Description: ingress slot to get tm voq statistics
    """
    return self.__ing_slot
      
  def _set_ing_slot(self, v, load=False):
    """
    Setter method for ing_slot, mapped from YANG variable /tm_state/tmvoqstatistics/ing_slot (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ing_slot is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ing_slot() directly.

    YANG Description: ingress slot to get tm voq statistics
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="ing-slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ing_slot must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="ing-slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)""",
        })

    self.__ing_slot = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ing_slot(self):
    self.__ing_slot = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="ing-slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)


  def _get_ing_tower(self):
    """
    Getter method for ing_tower, mapped from YANG variable /tm_state/tmvoqstatistics/ing_tower (uint16)

    YANG Description: ingress tpwer to get tm voq statistics
    """
    return self.__ing_tower
      
  def _set_ing_tower(self, v, load=False):
    """
    Setter method for ing_tower, mapped from YANG variable /tm_state/tmvoqstatistics/ing_tower (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ing_tower is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ing_tower() directly.

    YANG Description: ingress tpwer to get tm voq statistics
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="ing-tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ing_tower must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="ing-tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)""",
        })

    self.__ing_tower = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ing_tower(self):
    self.__ing_tower = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="ing-tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)


  def _get_egr_voqid(self):
    """
    Getter method for egr_voqid, mapped from YANG variable /tm_state/tmvoqstatistics/egr_voqid (uint16)

    YANG Description: egress voq-id to get tm voq statistics
    """
    return self.__egr_voqid
      
  def _set_egr_voqid(self, v, load=False):
    """
    Setter method for egr_voqid, mapped from YANG variable /tm_state/tmvoqstatistics/egr_voqid (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_egr_voqid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_egr_voqid() directly.

    YANG Description: egress voq-id to get tm voq statistics
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="egr-voqid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """egr_voqid must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="egr-voqid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)""",
        })

    self.__egr_voqid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_egr_voqid(self):
    self.__egr_voqid = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="egr-voqid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)


  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /tm_state/tmvoqstatistics/priority (uint16)

    YANG Description: Traffic class priority for TM VOQ statistics
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /tm_state/tmvoqstatistics/priority (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: Traffic class priority for TM VOQ statistics
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)


  def _get_enquepkt(self):
    """
    Getter method for enquepkt, mapped from YANG variable /tm_state/tmvoqstatistics/enquepkt (uint64)

    YANG Description: Count of packets enqueued in TM VOQ
    """
    return self.__enquepkt
      
  def _set_enquepkt(self, v, load=False):
    """
    Setter method for enquepkt, mapped from YANG variable /tm_state/tmvoqstatistics/enquepkt (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enquepkt is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enquepkt() directly.

    YANG Description: Count of packets enqueued in TM VOQ
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enquepkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enquepkt must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enquepkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__enquepkt = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enquepkt(self):
    self.__enquepkt = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enquepkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)


  def _get_enqueubytes(self):
    """
    Getter method for enqueubytes, mapped from YANG variable /tm_state/tmvoqstatistics/enqueubytes (uint64)

    YANG Description: Count of bytes enqueued in TM VOQ
    """
    return self.__enqueubytes
      
  def _set_enqueubytes(self, v, load=False):
    """
    Setter method for enqueubytes, mapped from YANG variable /tm_state/tmvoqstatistics/enqueubytes (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enqueubytes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enqueubytes() directly.

    YANG Description: Count of bytes enqueued in TM VOQ
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enqueubytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enqueubytes must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enqueubytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__enqueubytes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enqueubytes(self):
    self.__enqueubytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enqueubytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)


  def _get_discardpkt(self):
    """
    Getter method for discardpkt, mapped from YANG variable /tm_state/tmvoqstatistics/discardpkt (uint64)

    YANG Description: Count of packets discarded for respective TM VOQ
    """
    return self.__discardpkt
      
  def _set_discardpkt(self, v, load=False):
    """
    Setter method for discardpkt, mapped from YANG variable /tm_state/tmvoqstatistics/discardpkt (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_discardpkt is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_discardpkt() directly.

    YANG Description: Count of packets discarded for respective TM VOQ
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardpkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """discardpkt must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardpkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__discardpkt = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_discardpkt(self):
    self.__discardpkt = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardpkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)


  def _get_discardbytes(self):
    """
    Getter method for discardbytes, mapped from YANG variable /tm_state/tmvoqstatistics/discardbytes (uint64)

    YANG Description: Count of bytes discarded for respective TM VOQ
    """
    return self.__discardbytes
      
  def _set_discardbytes(self, v, load=False):
    """
    Setter method for discardbytes, mapped from YANG variable /tm_state/tmvoqstatistics/discardbytes (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_discardbytes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_discardbytes() directly.

    YANG Description: Count of bytes discarded for respective TM VOQ
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardbytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """discardbytes must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardbytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__discardbytes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_discardbytes(self):
    self.__discardbytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardbytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)


  def _get_currdepth(self):
    """
    Getter method for currdepth, mapped from YANG variable /tm_state/tmvoqstatistics/currdepth (uint64)

    YANG Description: Current queue depth size of respective TM VOQ
    """
    return self.__currdepth
      
  def _set_currdepth(self, v, load=False):
    """
    Setter method for currdepth, mapped from YANG variable /tm_state/tmvoqstatistics/currdepth (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_currdepth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_currdepth() directly.

    YANG Description: Current queue depth size of respective TM VOQ
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="currdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """currdepth must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="currdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__currdepth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_currdepth(self):
    self.__currdepth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="currdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)


  def _get_maxdepth(self):
    """
    Getter method for maxdepth, mapped from YANG variable /tm_state/tmvoqstatistics/maxdepth (uint64)

    YANG Description: Maxixum depth reached for respective TM VOQ
    """
    return self.__maxdepth
      
  def _set_maxdepth(self, v, load=False):
    """
    Setter method for maxdepth, mapped from YANG variable /tm_state/tmvoqstatistics/maxdepth (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maxdepth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maxdepth() directly.

    YANG Description: Maxixum depth reached for respective TM VOQ
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="maxdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maxdepth must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="maxdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__maxdepth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maxdepth(self):
    self.__maxdepth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="maxdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)

  ing_slot = __builtin__.property(_get_ing_slot)
  ing_tower = __builtin__.property(_get_ing_tower)
  egr_voqid = __builtin__.property(_get_egr_voqid)
  priority = __builtin__.property(_get_priority)
  enquepkt = __builtin__.property(_get_enquepkt)
  enqueubytes = __builtin__.property(_get_enqueubytes)
  discardpkt = __builtin__.property(_get_discardpkt)
  discardbytes = __builtin__.property(_get_discardbytes)
  currdepth = __builtin__.property(_get_currdepth)
  maxdepth = __builtin__.property(_get_maxdepth)


  _pyangbind_elements = {'ing_slot': ing_slot, 'ing_tower': ing_tower, 'egr_voqid': egr_voqid, 'priority': priority, 'enquepkt': enquepkt, 'enqueubytes': enqueubytes, 'discardpkt': discardpkt, 'discardbytes': discardbytes, 'currdepth': currdepth, 'maxdepth': maxdepth, }


