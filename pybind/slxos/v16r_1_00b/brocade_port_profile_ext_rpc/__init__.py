
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import get_port_profile_for_intf
import get_port_profile_status
class brocade_port_profile_ext(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-port-profile-ext - based on the path /brocade_port_profile_ext_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This management module is an extension to the port-profile
model for 
   - Defining RPCs to retrieve port-profile related operational
     data in the managed device.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__get_port_profile_for_intf','__get_port_profile_status',)

  _yang_name = 'brocade-port-profile-ext'

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
    self.__get_port_profile_for_intf = YANGDynClass(base=get_port_profile_for_intf.get_port_profile_for_intf, is_leaf=True, yang_name="get-port-profile-for-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'appm-port-profile'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='rpc', is_config=True)
    self.__get_port_profile_status = YANGDynClass(base=get_port_profile_status.get_port_profile_status, is_leaf=True, yang_name="get-port-profile-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'appm-port-profile'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='rpc', is_config=True)

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
      return [u'brocade_port_profile_ext_rpc']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return []

  def _get_get_port_profile_for_intf(self):
    """
    Getter method for get_port_profile_for_intf, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_for_intf (rpc)

    YANG Description: This is a function that returns the port profiles applied 
on port(s) and port-channels.
    """
    return self.__get_port_profile_for_intf
      
  def _set_get_port_profile_for_intf(self, v, load=False):
    """
    Setter method for get_port_profile_for_intf, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_for_intf (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_port_profile_for_intf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_port_profile_for_intf() directly.

    YANG Description: This is a function that returns the port profiles applied 
on port(s) and port-channels.
    """
    try:
      t = YANGDynClass(v,base=get_port_profile_for_intf.get_port_profile_for_intf, is_leaf=True, yang_name="get-port-profile-for-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'appm-port-profile'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_port_profile_for_intf must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_port_profile_for_intf.get_port_profile_for_intf, is_leaf=True, yang_name="get-port-profile-for-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'appm-port-profile'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='rpc', is_config=True)""",
        })

    self.__get_port_profile_for_intf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_port_profile_for_intf(self):
    self.__get_port_profile_for_intf = YANGDynClass(base=get_port_profile_for_intf.get_port_profile_for_intf, is_leaf=True, yang_name="get-port-profile-for-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'appm-port-profile'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='rpc', is_config=True)


  def _get_get_port_profile_status(self):
    """
    Getter method for get_port_profile_status, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_status (rpc)

    YANG Description: This is a function that returns the status of a port 
profile or all the port profiles.
    """
    return self.__get_port_profile_status
      
  def _set_get_port_profile_status(self, v, load=False):
    """
    Setter method for get_port_profile_status, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_status (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_port_profile_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_port_profile_status() directly.

    YANG Description: This is a function that returns the status of a port 
profile or all the port profiles.
    """
    try:
      t = YANGDynClass(v,base=get_port_profile_status.get_port_profile_status, is_leaf=True, yang_name="get-port-profile-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'appm-port-profile'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_port_profile_status must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_port_profile_status.get_port_profile_status, is_leaf=True, yang_name="get-port-profile-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'appm-port-profile'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='rpc', is_config=True)""",
        })

    self.__get_port_profile_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_port_profile_status(self):
    self.__get_port_profile_status = YANGDynClass(base=get_port_profile_status.get_port_profile_status, is_leaf=True, yang_name="get-port-profile-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'appm-port-profile'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='rpc', is_config=True)

  get_port_profile_for_intf = __builtin__.property(_get_get_port_profile_for_intf, _set_get_port_profile_for_intf)
  get_port_profile_status = __builtin__.property(_get_get_port_profile_status, _set_get_port_profile_status)


  _pyangbind_elements = {'get_port_profile_for_intf': get_port_profile_for_intf, 'get_port_profile_status': get_port_profile_status, }


