
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class banner(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-aaa - based on the path /banner. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__login','__motd','__incoming',)

  _yang_name = 'banner'

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
    self.__incoming = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..2048']}), default=unicode(""), is_leaf=True, yang_name="incoming", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set incoming terminal line banner', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    self.__login = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..2048']}), default=unicode(""), is_leaf=True, yang_name="login", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Banner text displayed after user logs into the switch', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    self.__motd = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..2048']}), default=unicode(""), is_leaf=True, yang_name="motd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Banner text displayed before user logs into\n the switch', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)

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
      return [u'banner']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'banner']

  def _get_login(self):
    """
    Getter method for login, mapped from YANG variable /banner/login (string)
    """
    return self.__login
      
  def _set_login(self, v, load=False):
    """
    Setter method for login, mapped from YANG variable /banner/login (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_login is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_login() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..2048']}), default=unicode(""), is_leaf=True, yang_name="login", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Banner text displayed after user logs into the switch', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """login must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..2048']}), default=unicode(""), is_leaf=True, yang_name="login", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Banner text displayed after user logs into the switch', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)""",
        })

    self.__login = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_login(self):
    self.__login = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..2048']}), default=unicode(""), is_leaf=True, yang_name="login", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Banner text displayed after user logs into the switch', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)


  def _get_motd(self):
    """
    Getter method for motd, mapped from YANG variable /banner/motd (string)
    """
    return self.__motd
      
  def _set_motd(self, v, load=False):
    """
    Setter method for motd, mapped from YANG variable /banner/motd (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_motd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_motd() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..2048']}), default=unicode(""), is_leaf=True, yang_name="motd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Banner text displayed before user logs into\n the switch', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """motd must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..2048']}), default=unicode(""), is_leaf=True, yang_name="motd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Banner text displayed before user logs into\n the switch', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)""",
        })

    self.__motd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_motd(self):
    self.__motd = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..2048']}), default=unicode(""), is_leaf=True, yang_name="motd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Banner text displayed before user logs into\n the switch', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)


  def _get_incoming(self):
    """
    Getter method for incoming, mapped from YANG variable /banner/incoming (string)
    """
    return self.__incoming
      
  def _set_incoming(self, v, load=False):
    """
    Setter method for incoming, mapped from YANG variable /banner/incoming (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_incoming is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_incoming() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..2048']}), default=unicode(""), is_leaf=True, yang_name="incoming", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set incoming terminal line banner', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """incoming must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..2048']}), default=unicode(""), is_leaf=True, yang_name="incoming", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set incoming terminal line banner', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)""",
        })

    self.__incoming = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_incoming(self):
    self.__incoming = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..2048']}), default=unicode(""), is_leaf=True, yang_name="incoming", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set incoming terminal line banner', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)

  login = __builtin__.property(_get_login, _set_login)
  motd = __builtin__.property(_get_motd, _set_motd)
  incoming = __builtin__.property(_get_incoming, _set_incoming)


  _pyangbind_elements = {'login': login, 'motd': motd, 'incoming': incoming, }


