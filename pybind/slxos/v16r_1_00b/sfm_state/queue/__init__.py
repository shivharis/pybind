
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class queue(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sysmgr-operational - based on the path /sfm-state/queue. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: SFM Queue
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__queue_sfmid','__queue_feid','__queue_pipe','__queue_dch_count','__queue_dcm_count','__queue_dcl_count','__queue_dch_value','__queue_dch_linkno','__queue_dcm_value','__queue_dcm_linkno','__queue_dcl_value','__queue_dcl_linkno',)

  _yang_name = 'queue'

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
    self.__queue_dcl_linkno = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcl-linkno", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__queue_sfmid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-sfmid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__queue_feid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-feid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__queue_dcm_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-dcm-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__queue_dcl_value = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcl-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__queue_dcm_linkno = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcm-linkno", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__queue_dch_value = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dch-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__queue_dch_linkno = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dch-linkno", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__queue_dcl_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-dcl-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__queue_dcm_value = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcm-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__queue_dch_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-dch-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__queue_pipe = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-pipe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)

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
      return [u'sfm-state', u'queue']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'sfm-state', u'queue']

  def _get_queue_sfmid(self):
    """
    Getter method for queue_sfmid, mapped from YANG variable /sfm_state/queue/queue_sfmid (uint32)

    YANG Description: SFM Queue
    """
    return self.__queue_sfmid
      
  def _set_queue_sfmid(self, v, load=False):
    """
    Setter method for queue_sfmid, mapped from YANG variable /sfm_state/queue/queue_sfmid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_sfmid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_sfmid() directly.

    YANG Description: SFM Queue
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-sfmid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_sfmid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-sfmid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__queue_sfmid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_sfmid(self):
    self.__queue_sfmid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-sfmid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_queue_feid(self):
    """
    Getter method for queue_feid, mapped from YANG variable /sfm_state/queue/queue_feid (uint32)

    YANG Description: SFM Queue
    """
    return self.__queue_feid
      
  def _set_queue_feid(self, v, load=False):
    """
    Setter method for queue_feid, mapped from YANG variable /sfm_state/queue/queue_feid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_feid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_feid() directly.

    YANG Description: SFM Queue
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-feid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_feid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-feid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__queue_feid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_feid(self):
    self.__queue_feid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-feid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_queue_pipe(self):
    """
    Getter method for queue_pipe, mapped from YANG variable /sfm_state/queue/queue_pipe (uint32)

    YANG Description: SFM Queue Pipe
    """
    return self.__queue_pipe
      
  def _set_queue_pipe(self, v, load=False):
    """
    Setter method for queue_pipe, mapped from YANG variable /sfm_state/queue/queue_pipe (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_pipe is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_pipe() directly.

    YANG Description: SFM Queue Pipe
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-pipe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_pipe must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-pipe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__queue_pipe = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_pipe(self):
    self.__queue_pipe = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-pipe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_queue_dch_count(self):
    """
    Getter method for queue_dch_count, mapped from YANG variable /sfm_state/queue/queue_dch_count (uint32)

    YANG Description: SFM Queue
    """
    return self.__queue_dch_count
      
  def _set_queue_dch_count(self, v, load=False):
    """
    Setter method for queue_dch_count, mapped from YANG variable /sfm_state/queue/queue_dch_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_dch_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_dch_count() directly.

    YANG Description: SFM Queue
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-dch-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_dch_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-dch-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__queue_dch_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_dch_count(self):
    self.__queue_dch_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-dch-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_queue_dcm_count(self):
    """
    Getter method for queue_dcm_count, mapped from YANG variable /sfm_state/queue/queue_dcm_count (uint32)

    YANG Description: SFM Queue
    """
    return self.__queue_dcm_count
      
  def _set_queue_dcm_count(self, v, load=False):
    """
    Setter method for queue_dcm_count, mapped from YANG variable /sfm_state/queue/queue_dcm_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_dcm_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_dcm_count() directly.

    YANG Description: SFM Queue
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-dcm-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_dcm_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-dcm-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__queue_dcm_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_dcm_count(self):
    self.__queue_dcm_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-dcm-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_queue_dcl_count(self):
    """
    Getter method for queue_dcl_count, mapped from YANG variable /sfm_state/queue/queue_dcl_count (uint32)

    YANG Description: SFM Queue
    """
    return self.__queue_dcl_count
      
  def _set_queue_dcl_count(self, v, load=False):
    """
    Setter method for queue_dcl_count, mapped from YANG variable /sfm_state/queue/queue_dcl_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_dcl_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_dcl_count() directly.

    YANG Description: SFM Queue
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-dcl-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_dcl_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-dcl-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__queue_dcl_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_dcl_count(self):
    self.__queue_dcl_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-dcl-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_queue_dch_value(self):
    """
    Getter method for queue_dch_value, mapped from YANG variable /sfm_state/queue/queue_dch_value (uint32)

    YANG Description: SFM DCH Value
    """
    return self.__queue_dch_value
      
  def _set_queue_dch_value(self, v, load=False):
    """
    Setter method for queue_dch_value, mapped from YANG variable /sfm_state/queue/queue_dch_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_dch_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_dch_value() directly.

    YANG Description: SFM DCH Value
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dch-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_dch_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dch-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__queue_dch_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_dch_value(self):
    self.__queue_dch_value = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dch-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_queue_dch_linkno(self):
    """
    Getter method for queue_dch_linkno, mapped from YANG variable /sfm_state/queue/queue_dch_linkno (uint32)

    YANG Description: SFM DCH Link-No
    """
    return self.__queue_dch_linkno
      
  def _set_queue_dch_linkno(self, v, load=False):
    """
    Setter method for queue_dch_linkno, mapped from YANG variable /sfm_state/queue/queue_dch_linkno (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_dch_linkno is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_dch_linkno() directly.

    YANG Description: SFM DCH Link-No
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dch-linkno", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_dch_linkno must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dch-linkno", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__queue_dch_linkno = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_dch_linkno(self):
    self.__queue_dch_linkno = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dch-linkno", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_queue_dcm_value(self):
    """
    Getter method for queue_dcm_value, mapped from YANG variable /sfm_state/queue/queue_dcm_value (uint32)

    YANG Description: SFM DCM Value
    """
    return self.__queue_dcm_value
      
  def _set_queue_dcm_value(self, v, load=False):
    """
    Setter method for queue_dcm_value, mapped from YANG variable /sfm_state/queue/queue_dcm_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_dcm_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_dcm_value() directly.

    YANG Description: SFM DCM Value
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcm-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_dcm_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcm-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__queue_dcm_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_dcm_value(self):
    self.__queue_dcm_value = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcm-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_queue_dcm_linkno(self):
    """
    Getter method for queue_dcm_linkno, mapped from YANG variable /sfm_state/queue/queue_dcm_linkno (uint32)

    YANG Description: SFM DCM Link-No
    """
    return self.__queue_dcm_linkno
      
  def _set_queue_dcm_linkno(self, v, load=False):
    """
    Setter method for queue_dcm_linkno, mapped from YANG variable /sfm_state/queue/queue_dcm_linkno (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_dcm_linkno is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_dcm_linkno() directly.

    YANG Description: SFM DCM Link-No
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcm-linkno", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_dcm_linkno must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcm-linkno", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__queue_dcm_linkno = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_dcm_linkno(self):
    self.__queue_dcm_linkno = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcm-linkno", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_queue_dcl_value(self):
    """
    Getter method for queue_dcl_value, mapped from YANG variable /sfm_state/queue/queue_dcl_value (uint32)

    YANG Description: SFM DCL Value
    """
    return self.__queue_dcl_value
      
  def _set_queue_dcl_value(self, v, load=False):
    """
    Setter method for queue_dcl_value, mapped from YANG variable /sfm_state/queue/queue_dcl_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_dcl_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_dcl_value() directly.

    YANG Description: SFM DCL Value
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcl-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_dcl_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcl-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__queue_dcl_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_dcl_value(self):
    self.__queue_dcl_value = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcl-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_queue_dcl_linkno(self):
    """
    Getter method for queue_dcl_linkno, mapped from YANG variable /sfm_state/queue/queue_dcl_linkno (uint32)

    YANG Description: SFM DCL Link-No
    """
    return self.__queue_dcl_linkno
      
  def _set_queue_dcl_linkno(self, v, load=False):
    """
    Setter method for queue_dcl_linkno, mapped from YANG variable /sfm_state/queue/queue_dcl_linkno (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_dcl_linkno is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_dcl_linkno() directly.

    YANG Description: SFM DCL Link-No
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcl-linkno", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_dcl_linkno must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcl-linkno", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__queue_dcl_linkno = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_dcl_linkno(self):
    self.__queue_dcl_linkno = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="queue-dcl-linkno", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)

  queue_sfmid = __builtin__.property(_get_queue_sfmid)
  queue_feid = __builtin__.property(_get_queue_feid)
  queue_pipe = __builtin__.property(_get_queue_pipe)
  queue_dch_count = __builtin__.property(_get_queue_dch_count)
  queue_dcm_count = __builtin__.property(_get_queue_dcm_count)
  queue_dcl_count = __builtin__.property(_get_queue_dcl_count)
  queue_dch_value = __builtin__.property(_get_queue_dch_value)
  queue_dch_linkno = __builtin__.property(_get_queue_dch_linkno)
  queue_dcm_value = __builtin__.property(_get_queue_dcm_value)
  queue_dcm_linkno = __builtin__.property(_get_queue_dcm_linkno)
  queue_dcl_value = __builtin__.property(_get_queue_dcl_value)
  queue_dcl_linkno = __builtin__.property(_get_queue_dcl_linkno)


  _pyangbind_elements = {'queue_sfmid': queue_sfmid, 'queue_feid': queue_feid, 'queue_pipe': queue_pipe, 'queue_dch_count': queue_dch_count, 'queue_dcm_count': queue_dcm_count, 'queue_dcl_count': queue_dcl_count, 'queue_dch_value': queue_dch_value, 'queue_dch_linkno': queue_dch_linkno, 'queue_dcm_value': queue_dcm_value, 'queue_dcm_linkno': queue_dcm_linkno, 'queue_dcl_value': queue_dcl_value, 'queue_dcl_linkno': queue_dcl_linkno, }


