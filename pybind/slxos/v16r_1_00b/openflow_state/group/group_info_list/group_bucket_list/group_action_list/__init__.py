
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class group_action_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/group/group-info-list/group-bucket-list/group-action-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: group action info
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__action_id','__out_port','__vlan_id','__out_vlan_tag','__out_vlan_etype',)

  _yang_name = 'group-action-list'
  _rest_name = 'group-action-list'

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
    self.__out_vlan_etype = YANGDynClass(base=unicode, is_leaf=True, yang_name="out-vlan-etype", rest_name="out-vlan-etype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    self.__out_vlan_tag = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-vlan-action-pop': {'value': 2}, u'dcm-vlan-action-push': {'value': 1}, u'dcm-vlan-action-set': {'value': 0}},), is_leaf=True, yang_name="out-vlan-tag", rest_name="out-vlan-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='vlan-action', is_config=False)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__out_port = YANGDynClass(base=unicode, is_leaf=True, yang_name="out-port", rest_name="out-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    self.__action_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="action-id", rest_name="action-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)

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
      return [u'openflow-state', u'group', u'group-info-list', u'group-bucket-list', u'group-action-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow-state', u'group', u'group-info-list', u'group-bucket-list', u'group-action-list']

  def _get_action_id(self):
    """
    Getter method for action_id, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/group_action_list/action_id (uint32)

    YANG Description: action id
    """
    return self.__action_id
      
  def _set_action_id(self, v, load=False):
    """
    Setter method for action_id, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/group_action_list/action_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action_id() directly.

    YANG Description: action id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="action-id", rest_name="action-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="action-id", rest_name="action-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__action_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action_id(self):
    self.__action_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="action-id", rest_name="action-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_out_port(self):
    """
    Getter method for out_port, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/group_action_list/out_port (string)

    YANG Description: out port
    """
    return self.__out_port
      
  def _set_out_port(self, v, load=False):
    """
    Setter method for out_port, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/group_action_list/out_port (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_port() directly.

    YANG Description: out port
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="out-port", rest_name="out-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_port must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="out-port", rest_name="out-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__out_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_port(self):
    self.__out_port = YANGDynClass(base=unicode, is_leaf=True, yang_name="out-port", rest_name="out-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)


  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/group_action_list/vlan_id (uint32)

    YANG Description: Vlan
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/group_action_list/vlan_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: Vlan
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_out_vlan_tag(self):
    """
    Getter method for out_vlan_tag, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/group_action_list/out_vlan_tag (vlan-action)

    YANG Description: Vlan tag
    """
    return self.__out_vlan_tag
      
  def _set_out_vlan_tag(self, v, load=False):
    """
    Setter method for out_vlan_tag, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/group_action_list/out_vlan_tag (vlan-action)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_vlan_tag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_vlan_tag() directly.

    YANG Description: Vlan tag
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-vlan-action-pop': {'value': 2}, u'dcm-vlan-action-push': {'value': 1}, u'dcm-vlan-action-set': {'value': 0}},), is_leaf=True, yang_name="out-vlan-tag", rest_name="out-vlan-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='vlan-action', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_vlan_tag must be of a type compatible with vlan-action""",
          'defined-type': "brocade-openflow-operational:vlan-action",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-vlan-action-pop': {'value': 2}, u'dcm-vlan-action-push': {'value': 1}, u'dcm-vlan-action-set': {'value': 0}},), is_leaf=True, yang_name="out-vlan-tag", rest_name="out-vlan-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='vlan-action', is_config=False)""",
        })

    self.__out_vlan_tag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_vlan_tag(self):
    self.__out_vlan_tag = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-vlan-action-pop': {'value': 2}, u'dcm-vlan-action-push': {'value': 1}, u'dcm-vlan-action-set': {'value': 0}},), is_leaf=True, yang_name="out-vlan-tag", rest_name="out-vlan-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='vlan-action', is_config=False)


  def _get_out_vlan_etype(self):
    """
    Getter method for out_vlan_etype, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/group_action_list/out_vlan_etype (string)

    YANG Description: Vlan etype
    """
    return self.__out_vlan_etype
      
  def _set_out_vlan_etype(self, v, load=False):
    """
    Setter method for out_vlan_etype, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/group_action_list/out_vlan_etype (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_vlan_etype is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_vlan_etype() directly.

    YANG Description: Vlan etype
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="out-vlan-etype", rest_name="out-vlan-etype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_vlan_etype must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="out-vlan-etype", rest_name="out-vlan-etype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__out_vlan_etype = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_vlan_etype(self):
    self.__out_vlan_etype = YANGDynClass(base=unicode, is_leaf=True, yang_name="out-vlan-etype", rest_name="out-vlan-etype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)

  action_id = __builtin__.property(_get_action_id)
  out_port = __builtin__.property(_get_out_port)
  vlan_id = __builtin__.property(_get_vlan_id)
  out_vlan_tag = __builtin__.property(_get_out_vlan_tag)
  out_vlan_etype = __builtin__.property(_get_out_vlan_etype)


  _pyangbind_elements = {'action_id': action_id, 'out_port': out_port, 'vlan_id': vlan_id, 'out_vlan_tag': out_vlan_tag, 'out_vlan_etype': out_vlan_etype, }


