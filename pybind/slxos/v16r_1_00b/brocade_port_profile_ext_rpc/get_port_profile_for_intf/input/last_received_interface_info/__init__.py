
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class last_received_interface_info(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-port-profile-ext - based on the path /brocade_port_profile_ext_rpc/get-port-profile-for-intf/input/last-received-interface-info. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The rpc returns the list of
port-profiles associated with the next set of 
interfaces.

The rpc request would look as below:
get-port-profile-for-intf
last-received-interface-info/interface-type=
fortygigabitethernet
last-received-interface-info/interface-name=
1/0/1.

The rpc response will contain the list of 
port-profiles applied on the interface fo 1/0/2,
1/0/3 and so on till the page limit is reached.

The rpc response has an attribute is-more, which 
will be false, when all the interfaces are 
exhausted.

The getnext-request model can be used to retrieve
the port-profiles applied on all the interfaces.

The rpc returns the list of port-profiles applied 
on the first set of interfaces when interface name 
and interface type are not specified.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface_type','__interface_name',)

  _yang_name = 'last-received-interface-info'

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
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loopback': {'value': 7}, u'unknown': {'value': 1}, u'port-channel': {'value': 5}, u'fibrechannel': {'value': 8}, u'ethernet': {'value': 10}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='enumeration', is_config=True)
    self.__interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}),], is_leaf=True, yang_name="interface-name", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='union', is_config=True)

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
      return [u'brocade_port_profile_ext_rpc', u'get-port-profile-for-intf', u'input', u'last-received-interface-info']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'get-port-profile-for-intf', u'input', u'last-received-interface-info']

  def _get_interface_type(self):
    """
    Getter method for interface_type, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_for_intf/input/last_received_interface_info/interface_type (enumeration)

    YANG Description: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
    """
    return self.__interface_type
      
  def _set_interface_type(self, v, load=False):
    """
    Setter method for interface_type, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_for_intf/input/last_received_interface_info/interface_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_type() directly.

    YANG Description: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loopback': {'value': 7}, u'unknown': {'value': 1}, u'port-channel': {'value': 5}, u'fibrechannel': {'value': 8}, u'ethernet': {'value': 10}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-port-profile-ext:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loopback': {'value': 7}, u'unknown': {'value': 1}, u'port-channel': {'value': 5}, u'fibrechannel': {'value': 8}, u'ethernet': {'value': 10}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='enumeration', is_config=True)""",
        })

    self.__interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_type(self):
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loopback': {'value': 7}, u'unknown': {'value': 1}, u'port-channel': {'value': 5}, u'fibrechannel': {'value': 8}, u'ethernet': {'value': 10}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='enumeration', is_config=True)


  def _get_interface_name(self):
    """
    Getter method for interface_name, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_for_intf/input/last_received_interface_info/interface_name (union)

    YANG Description: The Interface value. The interface value is always 
interpreted within the context of the value of 
'interface-type' leaf:

interface-type         interface-name
-----------------      --------------------
ethernet               slot/port
port-channel           Port channel ID
l2vlan                 Vlan ID
unknown                Zero-length string.

The value of an 'interface-name' must always be 
consistent with the value of the associated 
'interface-type'.  Attempts to set an interface-name
to a value inconsistent with the associated 
'interface-type' must fail with an error.
    """
    return self.__interface_name
      
  def _set_interface_name(self, v, load=False):
    """
    Setter method for interface_name, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_for_intf/input/last_received_interface_info/interface_name (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_name() directly.

    YANG Description: The Interface value. The interface value is always 
interpreted within the context of the value of 
'interface-type' leaf:

interface-type         interface-name
-----------------      --------------------
ethernet               slot/port
port-channel           Port channel ID
l2vlan                 Vlan ID
unknown                Zero-length string.

The value of an 'interface-name' must always be 
consistent with the value of the associated 
'interface-type'.  Attempts to set an interface-name
to a value inconsistent with the associated 
'interface-type' must fail with an error.
    """
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}),], is_leaf=True, yang_name="interface-name", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_name must be of a type compatible with union""",
          'defined-type': "brocade-port-profile-ext:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}),], is_leaf=True, yang_name="interface-name", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='union', is_config=True)""",
        })

    self.__interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_name(self):
    self.__interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}),], is_leaf=True, yang_name="interface-name", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='union', is_config=True)

  interface_type = __builtin__.property(_get_interface_type, _set_interface_type)
  interface_name = __builtin__.property(_get_interface_name, _set_interface_name)

  __choices__ = {u'request-type': {u'getnext-request': [u'interface_type', u'interface_name']}}
  _pyangbind_elements = {'interface_type': interface_type, 'interface_name': interface_name, }

