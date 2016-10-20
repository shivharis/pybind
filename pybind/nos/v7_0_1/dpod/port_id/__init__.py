
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class port_id(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-license - based on the path /dpod/port-id. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__port_id','__operation',)

  _yang_name = 'port-id'
  _rest_name = ''

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
    self.__operation = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'release': {'value': 1}, u'reserve': {'value': 2}},), is_leaf=True, yang_name="operation", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'release/reserve a DPOD license', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-license', defining_module='brocade-license', yang_type='license-dpod-operation-type', is_config=True)
    self.__port_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="port-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Syntax: [rbridge-id/slot/port]', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-license', defining_module='brocade-license', yang_type='interface:interface-type', is_config=True)

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
      return [u'dpod', u'port-id']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'dpod']

  def _get_port_id(self):
    """
    Getter method for port_id, mapped from YANG variable /dpod/port_id/port_id (interface:interface-type)

    YANG Description: Port details for identification
[rbridge-id/slot/port].
    """
    return self.__port_id
      
  def _set_port_id(self, v, load=False):
    """
    Setter method for port_id, mapped from YANG variable /dpod/port_id/port_id (interface:interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_id() directly.

    YANG Description: Port details for identification
[rbridge-id/slot/port].
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="port-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Syntax: [rbridge-id/slot/port]', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-license', defining_module='brocade-license', yang_type='interface:interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_id must be of a type compatible with interface:interface-type""",
          'defined-type': "interface:interface-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="port-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Syntax: [rbridge-id/slot/port]', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-license', defining_module='brocade-license', yang_type='interface:interface-type', is_config=True)""",
        })

    self.__port_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_id(self):
    self.__port_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="port-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Syntax: [rbridge-id/slot/port]', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-license', defining_module='brocade-license', yang_type='interface:interface-type', is_config=True)


  def _get_operation(self):
    """
    Getter method for operation, mapped from YANG variable /dpod/port_id/operation (license-dpod-operation-type)

    YANG Description: Operation to release or reserve a DPOD
license for this port.
    """
    return self.__operation
      
  def _set_operation(self, v, load=False):
    """
    Setter method for operation, mapped from YANG variable /dpod/port_id/operation (license-dpod-operation-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_operation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_operation() directly.

    YANG Description: Operation to release or reserve a DPOD
license for this port.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'release': {'value': 1}, u'reserve': {'value': 2}},), is_leaf=True, yang_name="operation", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'release/reserve a DPOD license', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-license', defining_module='brocade-license', yang_type='license-dpod-operation-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """operation must be of a type compatible with license-dpod-operation-type""",
          'defined-type': "brocade-license:license-dpod-operation-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'release': {'value': 1}, u'reserve': {'value': 2}},), is_leaf=True, yang_name="operation", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'release/reserve a DPOD license', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-license', defining_module='brocade-license', yang_type='license-dpod-operation-type', is_config=True)""",
        })

    self.__operation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_operation(self):
    self.__operation = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'release': {'value': 1}, u'reserve': {'value': 2}},), is_leaf=True, yang_name="operation", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'release/reserve a DPOD license', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-license', defining_module='brocade-license', yang_type='license-dpod-operation-type', is_config=True)

  port_id = __builtin__.property(_get_port_id, _set_port_id)
  operation = __builtin__.property(_get_operation, _set_operation)


  _pyangbind_elements = {'port_id': port_id, 'operation': operation, }


