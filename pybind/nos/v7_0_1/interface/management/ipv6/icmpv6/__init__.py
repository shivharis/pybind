
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class icmpv6(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/management/ipv6/icmpv6. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The ICMPv6 control for this management interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__v6_unreachable','__v6_echo_reply','__v6_rate_limiting',)

  _yang_name = 'icmpv6'
  _rest_name = 'icmpv6'

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
    self.__v6_echo_reply = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="v6_echo_reply", rest_name="echo-reply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'To enable sending ICMPv6 Echo Reply in response Echo Request.', u'alt-name': u'echo-reply', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__v6_unreachable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="v6_unreachable", rest_name="unreachable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'To enable generating ICMPv6 Destination Unreachable message.', u'alt-name': u'unreachable'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__v6_rate_limiting = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="v6_rate_limiting", rest_name="rate-limiting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'To enable ICMPv6 incoming rate limiting', u'alt-name': u'rate-limiting'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)

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
      return [u'interface', u'management', u'ipv6', u'icmpv6']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Management', u'ipv6', u'icmpv6']

  def _get_v6_unreachable(self):
    """
    Getter method for v6_unreachable, mapped from YANG variable /interface/management/ipv6/icmpv6/v6_unreachable (empty)

    YANG Description: To enable generating ICMPv6 Destination Unreachable message.
    """
    return self.__v6_unreachable
      
  def _set_v6_unreachable(self, v, load=False):
    """
    Setter method for v6_unreachable, mapped from YANG variable /interface/management/ipv6/icmpv6/v6_unreachable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_v6_unreachable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_v6_unreachable() directly.

    YANG Description: To enable generating ICMPv6 Destination Unreachable message.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="v6_unreachable", rest_name="unreachable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'To enable generating ICMPv6 Destination Unreachable message.', u'alt-name': u'unreachable'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """v6_unreachable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="v6_unreachable", rest_name="unreachable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'To enable generating ICMPv6 Destination Unreachable message.', u'alt-name': u'unreachable'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__v6_unreachable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_v6_unreachable(self):
    self.__v6_unreachable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="v6_unreachable", rest_name="unreachable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'To enable generating ICMPv6 Destination Unreachable message.', u'alt-name': u'unreachable'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_v6_echo_reply(self):
    """
    Getter method for v6_echo_reply, mapped from YANG variable /interface/management/ipv6/icmpv6/v6_echo_reply (empty)

    YANG Description: To enable sending ICMPv6 Echo Reply in response Echo Request.
    """
    return self.__v6_echo_reply
      
  def _set_v6_echo_reply(self, v, load=False):
    """
    Setter method for v6_echo_reply, mapped from YANG variable /interface/management/ipv6/icmpv6/v6_echo_reply (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_v6_echo_reply is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_v6_echo_reply() directly.

    YANG Description: To enable sending ICMPv6 Echo Reply in response Echo Request.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="v6_echo_reply", rest_name="echo-reply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'To enable sending ICMPv6 Echo Reply in response Echo Request.', u'alt-name': u'echo-reply', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """v6_echo_reply must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="v6_echo_reply", rest_name="echo-reply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'To enable sending ICMPv6 Echo Reply in response Echo Request.', u'alt-name': u'echo-reply', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__v6_echo_reply = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_v6_echo_reply(self):
    self.__v6_echo_reply = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="v6_echo_reply", rest_name="echo-reply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'To enable sending ICMPv6 Echo Reply in response Echo Request.', u'alt-name': u'echo-reply', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_v6_rate_limiting(self):
    """
    Getter method for v6_rate_limiting, mapped from YANG variable /interface/management/ipv6/icmpv6/v6_rate_limiting (uint32)

    YANG Description: To enable ICMPv6 incoming rate limiting
    """
    return self.__v6_rate_limiting
      
  def _set_v6_rate_limiting(self, v, load=False):
    """
    Setter method for v6_rate_limiting, mapped from YANG variable /interface/management/ipv6/icmpv6/v6_rate_limiting (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_v6_rate_limiting is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_v6_rate_limiting() directly.

    YANG Description: To enable ICMPv6 incoming rate limiting
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="v6_rate_limiting", rest_name="rate-limiting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'To enable ICMPv6 incoming rate limiting', u'alt-name': u'rate-limiting'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """v6_rate_limiting must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="v6_rate_limiting", rest_name="rate-limiting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'To enable ICMPv6 incoming rate limiting', u'alt-name': u'rate-limiting'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)""",
        })

    self.__v6_rate_limiting = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_v6_rate_limiting(self):
    self.__v6_rate_limiting = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="v6_rate_limiting", rest_name="rate-limiting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'To enable ICMPv6 incoming rate limiting', u'alt-name': u'rate-limiting'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)

  v6_unreachable = __builtin__.property(_get_v6_unreachable, _set_v6_unreachable)
  v6_echo_reply = __builtin__.property(_get_v6_echo_reply, _set_v6_echo_reply)
  v6_rate_limiting = __builtin__.property(_get_v6_rate_limiting, _set_v6_rate_limiting)


  _pyangbind_elements = {'v6_unreachable': v6_unreachable, 'v6_echo_reply': v6_echo_reply, 'v6_rate_limiting': v6_rate_limiting, }


