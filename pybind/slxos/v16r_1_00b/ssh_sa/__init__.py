
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ssh
class ssh_sa(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sec-services - based on the path /ssh-sa. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ssh',)

  _yang_name = 'ssh-sa'
  _rest_name = ''

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    path_helper_ = kwargs.pop("path_helper", None)
    if path_helper_ is False:
      self._path_helper = False
    elif path_helper_ is not None and isinstance(path_helper_, xpathhelper.YANGPathHelper):
      self._path_helper = path_helper_
    elif hasattr(self, "_parent"):
      path_helper_ = getattr(self._parent, "_path_helper", False)
      self._path_helper = path_helper_
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
    self.__ssh = YANGDynClass(base=ssh.ssh, is_container='container', presence=False, yang_name="ssh", rest_name="ssh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure SSH', u'sort-priority': u'RUNNCFG_LEVEL_SYSTEM_SSH_SERVER'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)

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
      return [u'ssh-sa']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_ssh(self):
    """
    Getter method for ssh, mapped from YANG variable /ssh_sa/ssh (container)
    """
    return self.__ssh
      
  def _set_ssh(self, v, load=False):
    """
    Setter method for ssh, mapped from YANG variable /ssh_sa/ssh (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ssh is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ssh() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ssh.ssh, is_container='container', presence=False, yang_name="ssh", rest_name="ssh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure SSH', u'sort-priority': u'RUNNCFG_LEVEL_SYSTEM_SSH_SERVER'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ssh must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ssh.ssh, is_container='container', presence=False, yang_name="ssh", rest_name="ssh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure SSH', u'sort-priority': u'RUNNCFG_LEVEL_SYSTEM_SSH_SERVER'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)""",
        })

    self.__ssh = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ssh(self):
    self.__ssh = YANGDynClass(base=ssh.ssh, is_container='container', presence=False, yang_name="ssh", rest_name="ssh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure SSH', u'sort-priority': u'RUNNCFG_LEVEL_SYSTEM_SSH_SERVER'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)

  ssh = __builtin__.property(_get_ssh, _set_ssh)


  _pyangbind_elements = {'ssh': ssh, }


