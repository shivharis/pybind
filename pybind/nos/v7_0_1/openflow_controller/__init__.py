
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import connection_address
class openflow_controller(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow - based on the path /openflow-controller. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: OpenFlow controller configuration
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__controller_name','__connection_address',)

  _yang_name = 'openflow-controller'

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
    self.__connection_address = YANGDynClass(base=connection_address.connection_address, is_container='container', yang_name="connection-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'IP address configuration', u'cli-sequence-commands': None, u'alt-name': u'ip', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)
    self.__controller_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,32}'}), is_leaf=True, yang_name="controller-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='openflow-controller-name-type', is_config=True)

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
      return [u'openflow-controller']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'openflow-controller']

  def _get_controller_name(self):
    """
    Getter method for controller_name, mapped from YANG variable /openflow_controller/controller_name (openflow-controller-name-type)

    YANG Description: OpenFlow controller name
    """
    return self.__controller_name
      
  def _set_controller_name(self, v, load=False):
    """
    Setter method for controller_name, mapped from YANG variable /openflow_controller/controller_name (openflow-controller-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_controller_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_controller_name() directly.

    YANG Description: OpenFlow controller name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,32}'}), is_leaf=True, yang_name="controller-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='openflow-controller-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """controller_name must be of a type compatible with openflow-controller-name-type""",
          'defined-type': "brocade-openflow:openflow-controller-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,32}'}), is_leaf=True, yang_name="controller-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='openflow-controller-name-type', is_config=True)""",
        })

    self.__controller_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_controller_name(self):
    self.__controller_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,32}'}), is_leaf=True, yang_name="controller-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='openflow-controller-name-type', is_config=True)


  def _get_connection_address(self):
    """
    Getter method for connection_address, mapped from YANG variable /openflow_controller/connection_address (container)

    YANG Description: IP address configuration
    """
    return self.__connection_address
      
  def _set_connection_address(self, v, load=False):
    """
    Setter method for connection_address, mapped from YANG variable /openflow_controller/connection_address (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connection_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connection_address() directly.

    YANG Description: IP address configuration
    """
    try:
      t = YANGDynClass(v,base=connection_address.connection_address, is_container='container', yang_name="connection-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'IP address configuration', u'cli-sequence-commands': None, u'alt-name': u'ip', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connection_address must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=connection_address.connection_address, is_container='container', yang_name="connection-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'IP address configuration', u'cli-sequence-commands': None, u'alt-name': u'ip', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)""",
        })

    self.__connection_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connection_address(self):
    self.__connection_address = YANGDynClass(base=connection_address.connection_address, is_container='container', yang_name="connection-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'IP address configuration', u'cli-sequence-commands': None, u'alt-name': u'ip', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)

  controller_name = __builtin__.property(_get_controller_name, _set_controller_name)
  connection_address = __builtin__.property(_get_connection_address, _set_connection_address)


  _pyangbind_elements = {'controller_name': controller_name, 'connection_address': connection_address, }


