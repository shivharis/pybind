
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class comm_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ip-policy - based on the path /hide-routemap-holder/route-map/content/set/comm-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: BGP community list for deletion
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__comm_list_name','__match_comm_delete',)

  _yang_name = 'comm-list'

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
    self.__comm_list_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="comm-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-community-list-name-t', is_config=True)
    self.__match_comm_delete = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="match-comm-delete", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'delete', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)

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
      return [u'hide-routemap-holder', u'route-map', u'content', u'set', u'comm-list']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'route-map', u'set', u'comm-list']

  def _get_comm_list_name(self):
    """
    Getter method for comm_list_name, mapped from YANG variable /hide_routemap_holder/route_map/content/set/comm_list/comm_list_name (ip-community-list-name-t)
    """
    return self.__comm_list_name
      
  def _set_comm_list_name(self, v, load=False):
    """
    Setter method for comm_list_name, mapped from YANG variable /hide_routemap_holder/route_map/content/set/comm_list/comm_list_name (ip-community-list-name-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_comm_list_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_comm_list_name() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="comm-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-community-list-name-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """comm_list_name must be of a type compatible with ip-community-list-name-t""",
          'defined-type': "brocade-ip-policy:ip-community-list-name-t",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="comm-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-community-list-name-t', is_config=True)""",
        })

    self.__comm_list_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_comm_list_name(self):
    self.__comm_list_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="comm-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-community-list-name-t', is_config=True)


  def _get_match_comm_delete(self):
    """
    Getter method for match_comm_delete, mapped from YANG variable /hide_routemap_holder/route_map/content/set/comm_list/match_comm_delete (empty)
    """
    return self.__match_comm_delete
      
  def _set_match_comm_delete(self, v, load=False):
    """
    Setter method for match_comm_delete, mapped from YANG variable /hide_routemap_holder/route_map/content/set/comm_list/match_comm_delete (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match_comm_delete is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match_comm_delete() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="match-comm-delete", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'delete', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match_comm_delete must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="match-comm-delete", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'delete', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)""",
        })

    self.__match_comm_delete = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match_comm_delete(self):
    self.__match_comm_delete = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="match-comm-delete", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'delete', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)

  comm_list_name = __builtin__.property(_get_comm_list_name, _set_comm_list_name)
  match_comm_delete = __builtin__.property(_get_match_comm_delete, _set_match_comm_delete)


  _pyangbind_elements = {'comm_list_name': comm_list_name, 'match_comm_delete': match_comm_delete, }


