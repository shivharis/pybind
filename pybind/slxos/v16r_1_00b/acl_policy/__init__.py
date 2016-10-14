
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import global_acl_policy_conf_cmds
class acl_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-acl-policy - based on the path /acl-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__global_acl_policy_conf_cmds',)

  _yang_name = 'acl-policy'

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
    self.__global_acl_policy_conf_cmds = YANGDynClass(base=global_acl_policy_conf_cmds.global_acl_policy_conf_cmds, is_container='container', yang_name="global-acl-policy-conf-cmds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-acl-policy', defining_module='brocade-acl-policy', yang_type='container', is_config=True)

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
      return [u'acl-policy']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'acl-policy']

  def _get_global_acl_policy_conf_cmds(self):
    """
    Getter method for global_acl_policy_conf_cmds, mapped from YANG variable /acl_policy/global_acl_policy_conf_cmds (container)
    """
    return self.__global_acl_policy_conf_cmds
      
  def _set_global_acl_policy_conf_cmds(self, v, load=False):
    """
    Setter method for global_acl_policy_conf_cmds, mapped from YANG variable /acl_policy/global_acl_policy_conf_cmds (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_acl_policy_conf_cmds is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_acl_policy_conf_cmds() directly.
    """
    try:
      t = YANGDynClass(v,base=global_acl_policy_conf_cmds.global_acl_policy_conf_cmds, is_container='container', yang_name="global-acl-policy-conf-cmds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-acl-policy', defining_module='brocade-acl-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_acl_policy_conf_cmds must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=global_acl_policy_conf_cmds.global_acl_policy_conf_cmds, is_container='container', yang_name="global-acl-policy-conf-cmds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-acl-policy', defining_module='brocade-acl-policy', yang_type='container', is_config=True)""",
        })

    self.__global_acl_policy_conf_cmds = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_acl_policy_conf_cmds(self):
    self.__global_acl_policy_conf_cmds = YANGDynClass(base=global_acl_policy_conf_cmds.global_acl_policy_conf_cmds, is_container='container', yang_name="global-acl-policy-conf-cmds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-acl-policy', defining_module='brocade-acl-policy', yang_type='container', is_config=True)

  global_acl_policy_conf_cmds = __builtin__.property(_get_global_acl_policy_conf_cmds, _set_global_acl_policy_conf_cmds)


  _pyangbind_elements = {'global_acl_policy_conf_cmds': global_acl_policy_conf_cmds, }


