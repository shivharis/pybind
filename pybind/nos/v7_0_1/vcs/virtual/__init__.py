
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ip
import ipv6
class virtual(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vcs - based on the path /vcs/virtual. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ip','__ipv6',)

  _yang_name = 'virtual'

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
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', yang_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)

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
      return [u'vcs', u'virtual']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'vcs', u'virtual']

  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /vcs/virtual/ip (container)
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /vcs/virtual/ip (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.
    """
    try:
      t = YANGDynClass(v,base=ip.ip, is_container='container', yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ip.ip, is_container='container', yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)


  def _get_ipv6(self):
    """
    Getter method for ipv6, mapped from YANG variable /vcs/virtual/ipv6 (container)
    """
    return self.__ipv6
      
  def _set_ipv6(self, v, load=False):
    """
    Setter method for ipv6, mapped from YANG variable /vcs/virtual/ipv6 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6() directly.
    """
    try:
      t = YANGDynClass(v,base=ipv6.ipv6, is_container='container', yang_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6.ipv6, is_container='container', yang_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)""",
        })

    self.__ipv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6(self):
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', yang_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)

  ip = __builtin__.property(_get_ip, _set_ip)
  ipv6 = __builtin__.property(_get_ipv6, _set_ipv6)


  _pyangbind_elements = {'ip': ip, 'ipv6': ipv6, }


