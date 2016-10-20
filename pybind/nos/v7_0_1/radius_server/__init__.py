
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import host
class radius_server(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-aaa - based on the path /radius-server. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__host',)

  _yang_name = 'radius-server'
  _rest_name = 'radius-server'

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
    self.__host = YANGDynClass(base=YANGListType("hostname use_vrf",host.host, yang_name="host", rest_name="host", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostname use-vrf', extensions={u'tailf-common': {u'info': u'Configure a RADIUS Server for AAA', u'cli-suppress-key-sort': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'radius_host_cp'}}), is_container='list', yang_name="host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a RADIUS Server for AAA', u'cli-suppress-key-sort': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'radius_host_cp'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='list', is_config=True)

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
      return [u'radius-server']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'radius-server']

  def _get_host(self):
    """
    Getter method for host, mapped from YANG variable /radius_server/host (list)
    """
    return self.__host
      
  def _set_host(self, v, load=False):
    """
    Setter method for host, mapped from YANG variable /radius_server/host (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("hostname use_vrf",host.host, yang_name="host", rest_name="host", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostname use-vrf', extensions={u'tailf-common': {u'info': u'Configure a RADIUS Server for AAA', u'cli-suppress-key-sort': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'radius_host_cp'}}), is_container='list', yang_name="host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a RADIUS Server for AAA', u'cli-suppress-key-sort': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'radius_host_cp'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("hostname use_vrf",host.host, yang_name="host", rest_name="host", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostname use-vrf', extensions={u'tailf-common': {u'info': u'Configure a RADIUS Server for AAA', u'cli-suppress-key-sort': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'radius_host_cp'}}), is_container='list', yang_name="host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a RADIUS Server for AAA', u'cli-suppress-key-sort': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'radius_host_cp'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='list', is_config=True)""",
        })

    self.__host = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host(self):
    self.__host = YANGDynClass(base=YANGListType("hostname use_vrf",host.host, yang_name="host", rest_name="host", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostname use-vrf', extensions={u'tailf-common': {u'info': u'Configure a RADIUS Server for AAA', u'cli-suppress-key-sort': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'radius_host_cp'}}), is_container='list', yang_name="host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a RADIUS Server for AAA', u'cli-suppress-key-sort': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'radius_host_cp'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='list', is_config=True)

  host = __builtin__.property(_get_host, _set_host)


  _pyangbind_elements = {'host': host, }


