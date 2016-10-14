
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class mcast(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sysmgr-operational - based on the path /sfm-state/mcast. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MCAST Operational Information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__mcastid','__mcast_count','__mcast_sfmid','__mcast_feid','__mcast_sfmcount','__mcast_out',)

  _yang_name = 'mcast'

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
    self.__mcast_sfmid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-sfmid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__mcast_out = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mcast-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__mcastid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcastid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__mcast_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__mcast_sfmcount = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-sfmcount", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    self.__mcast_feid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-feid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)

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
      return [u'sfm-state', u'mcast']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'sfm-state', u'mcast']

  def _get_mcastid(self):
    """
    Getter method for mcastid, mapped from YANG variable /sfm_state/mcast/mcastid (uint32)

    YANG Description: MCAST-ID
    """
    return self.__mcastid
      
  def _set_mcastid(self, v, load=False):
    """
    Setter method for mcastid, mapped from YANG variable /sfm_state/mcast/mcastid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mcastid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mcastid() directly.

    YANG Description: MCAST-ID
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcastid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mcastid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcastid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__mcastid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mcastid(self):
    self.__mcastid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcastid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_mcast_count(self):
    """
    Getter method for mcast_count, mapped from YANG variable /sfm_state/mcast/mcast_count (uint32)

    YANG Description: MCAST-Count
    """
    return self.__mcast_count
      
  def _set_mcast_count(self, v, load=False):
    """
    Setter method for mcast_count, mapped from YANG variable /sfm_state/mcast/mcast_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mcast_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mcast_count() directly.

    YANG Description: MCAST-Count
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mcast_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__mcast_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mcast_count(self):
    self.__mcast_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_mcast_sfmid(self):
    """
    Getter method for mcast_sfmid, mapped from YANG variable /sfm_state/mcast/mcast_sfmid (uint32)

    YANG Description: MCAST-SFMID
    """
    return self.__mcast_sfmid
      
  def _set_mcast_sfmid(self, v, load=False):
    """
    Setter method for mcast_sfmid, mapped from YANG variable /sfm_state/mcast/mcast_sfmid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mcast_sfmid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mcast_sfmid() directly.

    YANG Description: MCAST-SFMID
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-sfmid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mcast_sfmid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-sfmid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__mcast_sfmid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mcast_sfmid(self):
    self.__mcast_sfmid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-sfmid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_mcast_feid(self):
    """
    Getter method for mcast_feid, mapped from YANG variable /sfm_state/mcast/mcast_feid (uint32)

    YANG Description: MCAST-FEID
    """
    return self.__mcast_feid
      
  def _set_mcast_feid(self, v, load=False):
    """
    Setter method for mcast_feid, mapped from YANG variable /sfm_state/mcast/mcast_feid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mcast_feid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mcast_feid() directly.

    YANG Description: MCAST-FEID
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-feid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mcast_feid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-feid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__mcast_feid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mcast_feid(self):
    self.__mcast_feid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-feid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_mcast_sfmcount(self):
    """
    Getter method for mcast_sfmcount, mapped from YANG variable /sfm_state/mcast/mcast_sfmcount (uint32)

    YANG Description: MCAST-SFMCount
    """
    return self.__mcast_sfmcount
      
  def _set_mcast_sfmcount(self, v, load=False):
    """
    Setter method for mcast_sfmcount, mapped from YANG variable /sfm_state/mcast/mcast_sfmcount (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mcast_sfmcount is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mcast_sfmcount() directly.

    YANG Description: MCAST-SFMCount
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-sfmcount", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mcast_sfmcount must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-sfmcount", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__mcast_sfmcount = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mcast_sfmcount(self):
    self.__mcast_sfmcount = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mcast-sfmcount", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)


  def _get_mcast_out(self):
    """
    Getter method for mcast_out, mapped from YANG variable /sfm_state/mcast/mcast_out (uint32)

    YANG Description: MCAST-ID
    """
    return self.__mcast_out
      
  def _set_mcast_out(self, v, load=False):
    """
    Setter method for mcast_out, mapped from YANG variable /sfm_state/mcast/mcast_out (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mcast_out is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mcast_out() directly.

    YANG Description: MCAST-ID
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mcast-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mcast_out must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mcast-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)""",
        })

    self.__mcast_out = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mcast_out(self):
    self.__mcast_out = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mcast-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysmgr-operational', defining_module='brocade-sysmgr-operational', yang_type='uint32', is_config=False)

  mcastid = __builtin__.property(_get_mcastid)
  mcast_count = __builtin__.property(_get_mcast_count)
  mcast_sfmid = __builtin__.property(_get_mcast_sfmid)
  mcast_feid = __builtin__.property(_get_mcast_feid)
  mcast_sfmcount = __builtin__.property(_get_mcast_sfmcount)
  mcast_out = __builtin__.property(_get_mcast_out)


  _pyangbind_elements = {'mcastid': mcastid, 'mcast_count': mcast_count, 'mcast_sfmid': mcast_sfmid, 'mcast_feid': mcast_feid, 'mcast_sfmcount': mcast_sfmcount, 'mcast_out': mcast_out, }


