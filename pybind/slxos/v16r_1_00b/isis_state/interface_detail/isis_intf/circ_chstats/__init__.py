
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class circ_chstats(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /isis-state/interface-detail/isis-intf/circ-chstats. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: ISIS circuit change statistics
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__circ_changes','__adj_changes','__adj_rej','__l1authfail','__l2authfail','__bad_lsps','__ctrl_out','__ctrl_in',)

  _yang_name = 'circ-chstats'

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
    self.__l1authfail = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l1authfail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__adj_rej = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adj-rej", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__bad_lsps = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bad-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__ctrl_out = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ctrl-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__l2authfail = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l2authfail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__ctrl_in = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ctrl-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__circ_changes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="circ-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__adj_changes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adj-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)

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
      return [u'isis-state', u'interface-detail', u'isis-intf', u'circ-chstats']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'isis-state', u'interface-detail', u'isis-intf', u'circ-chstats']

  def _get_circ_changes(self):
    """
    Getter method for circ_changes, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/circ_changes (uint32)

    YANG Description: Number of circuit state changes
    """
    return self.__circ_changes
      
  def _set_circ_changes(self, v, load=False):
    """
    Setter method for circ_changes, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/circ_changes (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_circ_changes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_circ_changes() directly.

    YANG Description: Number of circuit state changes
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="circ-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """circ_changes must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="circ-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__circ_changes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_circ_changes(self):
    self.__circ_changes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="circ-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_adj_changes(self):
    """
    Getter method for adj_changes, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/adj_changes (uint32)

    YANG Description: Number of adjacency changes
    """
    return self.__adj_changes
      
  def _set_adj_changes(self, v, load=False):
    """
    Setter method for adj_changes, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/adj_changes (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_adj_changes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_adj_changes() directly.

    YANG Description: Number of adjacency changes
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adj-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """adj_changes must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adj-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__adj_changes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_adj_changes(self):
    self.__adj_changes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adj-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_adj_rej(self):
    """
    Getter method for adj_rej, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/adj_rej (uint32)

    YANG Description: Number of rejected adjacencies
    """
    return self.__adj_rej
      
  def _set_adj_rej(self, v, load=False):
    """
    Setter method for adj_rej, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/adj_rej (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_adj_rej is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_adj_rej() directly.

    YANG Description: Number of rejected adjacencies
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adj-rej", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """adj_rej must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adj-rej", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__adj_rej = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_adj_rej(self):
    self.__adj_rej = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adj-rej", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_l1authfail(self):
    """
    Getter method for l1authfail, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/l1authfail (uint32)

    YANG Description: Number of L1 authentication failures
    """
    return self.__l1authfail
      
  def _set_l1authfail(self, v, load=False):
    """
    Setter method for l1authfail, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/l1authfail (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l1authfail is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l1authfail() directly.

    YANG Description: Number of L1 authentication failures
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l1authfail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l1authfail must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l1authfail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__l1authfail = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l1authfail(self):
    self.__l1authfail = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l1authfail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_l2authfail(self):
    """
    Getter method for l2authfail, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/l2authfail (uint32)

    YANG Description: Number of L2 authentication failures
    """
    return self.__l2authfail
      
  def _set_l2authfail(self, v, load=False):
    """
    Setter method for l2authfail, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/l2authfail (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l2authfail is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l2authfail() directly.

    YANG Description: Number of L2 authentication failures
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l2authfail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l2authfail must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l2authfail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__l2authfail = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l2authfail(self):
    self.__l2authfail = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="l2authfail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_bad_lsps(self):
    """
    Getter method for bad_lsps, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/bad_lsps (uint32)

    YANG Description: Number of Bad LSPs received by the circuit
    """
    return self.__bad_lsps
      
  def _set_bad_lsps(self, v, load=False):
    """
    Setter method for bad_lsps, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/bad_lsps (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bad_lsps is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bad_lsps() directly.

    YANG Description: Number of Bad LSPs received by the circuit
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bad-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bad_lsps must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bad-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__bad_lsps = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bad_lsps(self):
    self.__bad_lsps = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bad-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_ctrl_out(self):
    """
    Getter method for ctrl_out, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/ctrl_out (uint32)

    YANG Description: Control messages sent
    """
    return self.__ctrl_out
      
  def _set_ctrl_out(self, v, load=False):
    """
    Setter method for ctrl_out, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/ctrl_out (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ctrl_out is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ctrl_out() directly.

    YANG Description: Control messages sent
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ctrl-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ctrl_out must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ctrl-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__ctrl_out = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ctrl_out(self):
    self.__ctrl_out = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ctrl-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_ctrl_in(self):
    """
    Getter method for ctrl_in, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/ctrl_in (uint32)

    YANG Description: Control messages received
    """
    return self.__ctrl_in
      
  def _set_ctrl_in(self, v, load=False):
    """
    Setter method for ctrl_in, mapped from YANG variable /isis_state/interface_detail/isis_intf/circ_chstats/ctrl_in (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ctrl_in is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ctrl_in() directly.

    YANG Description: Control messages received
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ctrl-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ctrl_in must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ctrl-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__ctrl_in = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ctrl_in(self):
    self.__ctrl_in = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ctrl-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)

  circ_changes = __builtin__.property(_get_circ_changes)
  adj_changes = __builtin__.property(_get_adj_changes)
  adj_rej = __builtin__.property(_get_adj_rej)
  l1authfail = __builtin__.property(_get_l1authfail)
  l2authfail = __builtin__.property(_get_l2authfail)
  bad_lsps = __builtin__.property(_get_bad_lsps)
  ctrl_out = __builtin__.property(_get_ctrl_out)
  ctrl_in = __builtin__.property(_get_ctrl_in)


  _pyangbind_elements = {'circ_changes': circ_changes, 'adj_changes': adj_changes, 'adj_rej': adj_rej, 'l1authfail': l1authfail, 'l2authfail': l2authfail, 'bad_lsps': bad_lsps, 'ctrl_out': ctrl_out, 'ctrl_in': ctrl_in, }


