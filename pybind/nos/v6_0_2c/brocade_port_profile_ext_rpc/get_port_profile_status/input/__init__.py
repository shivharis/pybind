
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import last_received_port_profile_info
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-port-profile-ext - based on the path /brocade_port_profile_ext_rpc/get-port-profile-status/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rbridge_id','__port_profile_name','__port_profile_status','__last_received_port_profile_info',)

  _yang_name = 'input'
  _rest_name = 'input'

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
    self.__port_profile_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="port-profile-name", rest_name="port-profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='common-def:name-string64', is_config=True)
    self.__last_received_port_profile_info = YANGDynClass(base=last_received_port_profile_info.last_received_port_profile_info, is_container='container', presence=False, yang_name="last-received-port-profile-info", rest_name="last-received-port-profile-info", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='container', is_config=True)
    self.__rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='uint32', is_config=True)
    self.__port_profile_status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'applied': {'value': 3}, u'associated': {'value': 2}, u'activated': {'value': 1}},), is_leaf=True, yang_name="port-profile-status", rest_name="port-profile-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='enumeration', is_config=True)

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
      return [u'brocade_port_profile_ext_rpc', u'get-port-profile-status', u'input']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-port-profile-status', u'input']

  def _get_rbridge_id(self):
    """
    Getter method for rbridge_id, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_status/input/rbridge_id (uint32)

    YANG Description: rbridge id of the node from which the data needs
to be fetched. When no rbridge id is given, data is fetched
from all rbridges
    """
    return self.__rbridge_id
      
  def _set_rbridge_id(self, v, load=False):
    """
    Setter method for rbridge_id, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_status/input/rbridge_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rbridge_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rbridge_id() directly.

    YANG Description: rbridge id of the node from which the data needs
to be fetched. When no rbridge id is given, data is fetched
from all rbridges
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rbridge_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='uint32', is_config=True)""",
        })

    self.__rbridge_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rbridge_id(self):
    self.__rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='uint32', is_config=True)


  def _get_port_profile_name(self):
    """
    Getter method for port_profile_name, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_status/input/port_profile_name (common-def:name-string64)

    YANG Description: This indicates the optional port profile name to
query.It returns status of all profiles if no
profile name is specified
    """
    return self.__port_profile_name
      
  def _set_port_profile_name(self, v, load=False):
    """
    Setter method for port_profile_name, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_status/input/port_profile_name (common-def:name-string64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_profile_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_profile_name() directly.

    YANG Description: This indicates the optional port profile name to
query.It returns status of all profiles if no
profile name is specified
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="port-profile-name", rest_name="port-profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='common-def:name-string64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_profile_name must be of a type compatible with common-def:name-string64""",
          'defined-type': "common-def:name-string64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="port-profile-name", rest_name="port-profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='common-def:name-string64', is_config=True)""",
        })

    self.__port_profile_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_profile_name(self):
    self.__port_profile_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="port-profile-name", rest_name="port-profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='common-def:name-string64', is_config=True)


  def _get_port_profile_status(self):
    """
    Getter method for port_profile_status, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_status/input/port_profile_status (enumeration)

    YANG Description: This indicates query is based on the port profile 
status. Profiles are not filtered based on the
status when this parameter is not specified
    """
    return self.__port_profile_status
      
  def _set_port_profile_status(self, v, load=False):
    """
    Setter method for port_profile_status, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_status/input/port_profile_status (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_profile_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_profile_status() directly.

    YANG Description: This indicates query is based on the port profile 
status. Profiles are not filtered based on the
status when this parameter is not specified
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'applied': {'value': 3}, u'associated': {'value': 2}, u'activated': {'value': 1}},), is_leaf=True, yang_name="port-profile-status", rest_name="port-profile-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_profile_status must be of a type compatible with enumeration""",
          'defined-type': "brocade-port-profile-ext:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'applied': {'value': 3}, u'associated': {'value': 2}, u'activated': {'value': 1}},), is_leaf=True, yang_name="port-profile-status", rest_name="port-profile-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='enumeration', is_config=True)""",
        })

    self.__port_profile_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_profile_status(self):
    self.__port_profile_status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'applied': {'value': 3}, u'associated': {'value': 2}, u'activated': {'value': 1}},), is_leaf=True, yang_name="port-profile-status", rest_name="port-profile-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='enumeration', is_config=True)


  def _get_last_received_port_profile_info(self):
    """
    Getter method for last_received_port_profile_info, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_status/input/last_received_port_profile_info (container)

    YANG Description: get request : 
provides data only for a given
port profile based on the input attribute 
port-profile-name.

To begin with, user should provide 
port-profile-name attribute and optional
profile-mac value as 00:00:00:00:00:00.
The response will contain the initial set of
macs associated with the given port profile.

For subsequent calls, user should provide 
port-profile-name along with the 
profile-mac value.
Response will contain the next set of
associated macs for the given port profile.

Response has an attribute is-more, which
will be false, when all the macs associated
with a given port-profile are exhausted.

getnext request : 
To get the next record,
provide both profile-name and profile-mac.

To begin with, user can invoke the rpc 
without providing profile-name and profile-mac
attributes.
The response will contain the initial set of 
macs associated with the first port profile.

For subsequent calls, user should provide 
profile-name along with the profile-mac.

If the user provides profile-name and last 
profile mac associated with the profile, 
the response will contain the next port profile
info.

Response has an attribute is-more, which will
be false, when all the macs associated with all
the port-profiles are exhausted.
    """
    return self.__last_received_port_profile_info
      
  def _set_last_received_port_profile_info(self, v, load=False):
    """
    Setter method for last_received_port_profile_info, mapped from YANG variable /brocade_port_profile_ext_rpc/get_port_profile_status/input/last_received_port_profile_info (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_received_port_profile_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_received_port_profile_info() directly.

    YANG Description: get request : 
provides data only for a given
port profile based on the input attribute 
port-profile-name.

To begin with, user should provide 
port-profile-name attribute and optional
profile-mac value as 00:00:00:00:00:00.
The response will contain the initial set of
macs associated with the given port profile.

For subsequent calls, user should provide 
port-profile-name along with the 
profile-mac value.
Response will contain the next set of
associated macs for the given port profile.

Response has an attribute is-more, which
will be false, when all the macs associated
with a given port-profile are exhausted.

getnext request : 
To get the next record,
provide both profile-name and profile-mac.

To begin with, user can invoke the rpc 
without providing profile-name and profile-mac
attributes.
The response will contain the initial set of 
macs associated with the first port profile.

For subsequent calls, user should provide 
profile-name along with the profile-mac.

If the user provides profile-name and last 
profile mac associated with the profile, 
the response will contain the next port profile
info.

Response has an attribute is-more, which will
be false, when all the macs associated with all
the port-profiles are exhausted.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=last_received_port_profile_info.last_received_port_profile_info, is_container='container', presence=False, yang_name="last-received-port-profile-info", rest_name="last-received-port-profile-info", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_received_port_profile_info must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=last_received_port_profile_info.last_received_port_profile_info, is_container='container', presence=False, yang_name="last-received-port-profile-info", rest_name="last-received-port-profile-info", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='container', is_config=True)""",
        })

    self.__last_received_port_profile_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_received_port_profile_info(self):
    self.__last_received_port_profile_info = YANGDynClass(base=last_received_port_profile_info.last_received_port_profile_info, is_container='container', presence=False, yang_name="last-received-port-profile-info", rest_name="last-received-port-profile-info", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-port-profile-ext', defining_module='brocade-port-profile-ext', yang_type='container', is_config=True)

  rbridge_id = __builtin__.property(_get_rbridge_id, _set_rbridge_id)
  port_profile_name = __builtin__.property(_get_port_profile_name, _set_port_profile_name)
  port_profile_status = __builtin__.property(_get_port_profile_status, _set_port_profile_status)
  last_received_port_profile_info = __builtin__.property(_get_last_received_port_profile_info, _set_last_received_port_profile_info)

  __choices__ = {u'request-type': {u'getnext-request': [u'last_received_port_profile_info']}}
  _pyangbind_elements = {'rbridge_id': rbridge_id, 'port_profile_name': port_profile_name, 'port_profile_status': port_profile_status, 'last_received_port_profile_info': last_received_port_profile_info, }


