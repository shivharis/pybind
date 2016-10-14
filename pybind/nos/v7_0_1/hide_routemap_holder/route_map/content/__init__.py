
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import match
import set_
import continue_holder
class content(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ip-policy - based on the path /hide-routemap-holder/route-map/content. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__match','__set_','__continue_holder',)

  _yang_name = 'content'

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
    self.__set_ = YANGDynClass(base=set_.set_, is_container='container', yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set values.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__match = YANGDynClass(base=match.match, is_container='container', yang_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Matches conditions.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__continue_holder = YANGDynClass(base=continue_holder.continue_holder, is_container='container', yang_name="continue-holder", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)

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
      return [u'hide-routemap-holder', u'route-map', u'content']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'route-map']

  def _get_match(self):
    """
    Getter method for match, mapped from YANG variable /hide_routemap_holder/route_map/content/match (container)

    YANG Description: Matches conditions.
    """
    return self.__match
      
  def _set_match(self, v, load=False):
    """
    Setter method for match, mapped from YANG variable /hide_routemap_holder/route_map/content/match (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match() directly.

    YANG Description: Matches conditions.
    """
    try:
      t = YANGDynClass(v,base=match.match, is_container='container', yang_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Matches conditions.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=match.match, is_container='container', yang_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Matches conditions.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__match = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match(self):
    self.__match = YANGDynClass(base=match.match, is_container='container', yang_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Matches conditions.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_set_(self):
    """
    Getter method for set_, mapped from YANG variable /hide_routemap_holder/route_map/content/set (container)

    YANG Description: Set values.
    """
    return self.__set_
      
  def _set_set_(self, v, load=False):
    """
    Setter method for set_, mapped from YANG variable /hide_routemap_holder/route_map/content/set (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_() directly.

    YANG Description: Set values.
    """
    try:
      t = YANGDynClass(v,base=set_.set_, is_container='container', yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set values.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=set_.set_, is_container='container', yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set values.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__set_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_(self):
    self.__set_ = YANGDynClass(base=set_.set_, is_container='container', yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set values.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_continue_holder(self):
    """
    Getter method for continue_holder, mapped from YANG variable /hide_routemap_holder/route_map/content/continue_holder (container)
    """
    return self.__continue_holder
      
  def _set_continue_holder(self, v, load=False):
    """
    Setter method for continue_holder, mapped from YANG variable /hide_routemap_holder/route_map/content/continue_holder (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_continue_holder is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_continue_holder() directly.
    """
    try:
      t = YANGDynClass(v,base=continue_holder.continue_holder, is_container='container', yang_name="continue-holder", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """continue_holder must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=continue_holder.continue_holder, is_container='container', yang_name="continue-holder", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__continue_holder = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_continue_holder(self):
    self.__continue_holder = YANGDynClass(base=continue_holder.continue_holder, is_container='container', yang_name="continue-holder", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)

  match = __builtin__.property(_get_match, _set_match)
  set_ = __builtin__.property(_get_set_, _set_set_)
  continue_holder = __builtin__.property(_get_continue_holder, _set_continue_holder)


  _pyangbind_elements = {'match': match, 'set_': set_, 'continue_holder': continue_holder, }


