
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import g_refresh_reduction
import g_reliable_messaging
import global_rsvp_hello
class rsvp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/rsvp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__refresh_interval','__refresh_multiple','__g_refresh_reduction','__g_reliable_messaging','__global_rsvp_hello','__global_rsvp_hello_acknowledgements','__global_rsvp_hello_unprioritize','__g_rsvp_backup_bw_guarantee',)

  _yang_name = 'rsvp'
  _rest_name = 'rsvp'

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
    self.__g_refresh_reduction = YANGDynClass(base=g_refresh_reduction.g_refresh_reduction, is_container='container', yang_name="g-refresh-reduction", rest_name="refresh-reduction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RSVP Refresh reduction globally', u'alt-name': u'refresh-reduction'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__global_rsvp_hello_acknowledgements = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="global-rsvp-hello-acknowledgements", rest_name="hello-acknowledgements", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Acknowledge RSVP Hellos on interfaces supporting RSVP Hello and not having RSVP sessions', u'alt-name': u'hello-acknowledgements'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    self.__g_rsvp_backup_bw_guarantee = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="g-rsvp-backup-bw-guarantee", rest_name="backup-bw-guarantee", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Setup a backup path requesting bandwidth only if bandwidth is available', u'alt-name': u'backup-bw-guarantee', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    self.__global_rsvp_hello_unprioritize = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="global-rsvp-hello-unprioritize", rest_name="hello-unprioritize", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Stop prioritizing RSVP Hello messages', u'hidden': u'full', u'alt-name': u'hello-unprioritize'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    self.__refresh_multiple = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="refresh-multiple", rest_name="refresh-multiple", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure RSVP Refresh multiple', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__g_reliable_messaging = YANGDynClass(base=g_reliable_messaging.g_reliable_messaging, is_container='container', yang_name="g-reliable-messaging", rest_name="reliable-messaging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RSVP Reliable messaging globally', u'alt-name': u'reliable-messaging'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__refresh_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..360']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="refresh-interval", rest_name="refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure RSVP Refresh interval', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__global_rsvp_hello = YANGDynClass(base=global_rsvp_hello.global_rsvp_hello, is_container='container', yang_name="global-rsvp-hello", rest_name="hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable RSVP Hello on all RSVP interfaces', u'cli-compact-syntax': None, u'alt-name': u'hello'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'rsvp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'mpls', u'rsvp']

  def _get_refresh_interval(self):
    """
    Getter method for refresh_interval, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/refresh_interval (uint32)
    """
    return self.__refresh_interval
      
  def _set_refresh_interval(self, v, load=False):
    """
    Setter method for refresh_interval, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/refresh_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_refresh_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_refresh_interval() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..360']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="refresh-interval", rest_name="refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure RSVP Refresh interval', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """refresh_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..360']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="refresh-interval", rest_name="refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure RSVP Refresh interval', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__refresh_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_refresh_interval(self):
    self.__refresh_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..360']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="refresh-interval", rest_name="refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure RSVP Refresh interval', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_refresh_multiple(self):
    """
    Getter method for refresh_multiple, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/refresh_multiple (uint32)
    """
    return self.__refresh_multiple
      
  def _set_refresh_multiple(self, v, load=False):
    """
    Setter method for refresh_multiple, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/refresh_multiple (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_refresh_multiple is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_refresh_multiple() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="refresh-multiple", rest_name="refresh-multiple", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure RSVP Refresh multiple', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """refresh_multiple must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="refresh-multiple", rest_name="refresh-multiple", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure RSVP Refresh multiple', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__refresh_multiple = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_refresh_multiple(self):
    self.__refresh_multiple = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="refresh-multiple", rest_name="refresh-multiple", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure RSVP Refresh multiple', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_g_refresh_reduction(self):
    """
    Getter method for g_refresh_reduction, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/g_refresh_reduction (container)
    """
    return self.__g_refresh_reduction
      
  def _set_g_refresh_reduction(self, v, load=False):
    """
    Setter method for g_refresh_reduction, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/g_refresh_reduction (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_g_refresh_reduction is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_g_refresh_reduction() directly.
    """
    try:
      t = YANGDynClass(v,base=g_refresh_reduction.g_refresh_reduction, is_container='container', yang_name="g-refresh-reduction", rest_name="refresh-reduction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RSVP Refresh reduction globally', u'alt-name': u'refresh-reduction'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """g_refresh_reduction must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=g_refresh_reduction.g_refresh_reduction, is_container='container', yang_name="g-refresh-reduction", rest_name="refresh-reduction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RSVP Refresh reduction globally', u'alt-name': u'refresh-reduction'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__g_refresh_reduction = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_g_refresh_reduction(self):
    self.__g_refresh_reduction = YANGDynClass(base=g_refresh_reduction.g_refresh_reduction, is_container='container', yang_name="g-refresh-reduction", rest_name="refresh-reduction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RSVP Refresh reduction globally', u'alt-name': u'refresh-reduction'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_g_reliable_messaging(self):
    """
    Getter method for g_reliable_messaging, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/g_reliable_messaging (container)
    """
    return self.__g_reliable_messaging
      
  def _set_g_reliable_messaging(self, v, load=False):
    """
    Setter method for g_reliable_messaging, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/g_reliable_messaging (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_g_reliable_messaging is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_g_reliable_messaging() directly.
    """
    try:
      t = YANGDynClass(v,base=g_reliable_messaging.g_reliable_messaging, is_container='container', yang_name="g-reliable-messaging", rest_name="reliable-messaging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RSVP Reliable messaging globally', u'alt-name': u'reliable-messaging'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """g_reliable_messaging must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=g_reliable_messaging.g_reliable_messaging, is_container='container', yang_name="g-reliable-messaging", rest_name="reliable-messaging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RSVP Reliable messaging globally', u'alt-name': u'reliable-messaging'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__g_reliable_messaging = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_g_reliable_messaging(self):
    self.__g_reliable_messaging = YANGDynClass(base=g_reliable_messaging.g_reliable_messaging, is_container='container', yang_name="g-reliable-messaging", rest_name="reliable-messaging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RSVP Reliable messaging globally', u'alt-name': u'reliable-messaging'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_global_rsvp_hello(self):
    """
    Getter method for global_rsvp_hello, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/global_rsvp_hello (container)
    """
    return self.__global_rsvp_hello
      
  def _set_global_rsvp_hello(self, v, load=False):
    """
    Setter method for global_rsvp_hello, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/global_rsvp_hello (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_rsvp_hello is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_rsvp_hello() directly.
    """
    try:
      t = YANGDynClass(v,base=global_rsvp_hello.global_rsvp_hello, is_container='container', yang_name="global-rsvp-hello", rest_name="hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable RSVP Hello on all RSVP interfaces', u'cli-compact-syntax': None, u'alt-name': u'hello'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_rsvp_hello must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=global_rsvp_hello.global_rsvp_hello, is_container='container', yang_name="global-rsvp-hello", rest_name="hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable RSVP Hello on all RSVP interfaces', u'cli-compact-syntax': None, u'alt-name': u'hello'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__global_rsvp_hello = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_rsvp_hello(self):
    self.__global_rsvp_hello = YANGDynClass(base=global_rsvp_hello.global_rsvp_hello, is_container='container', yang_name="global-rsvp-hello", rest_name="hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable RSVP Hello on all RSVP interfaces', u'cli-compact-syntax': None, u'alt-name': u'hello'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_global_rsvp_hello_acknowledgements(self):
    """
    Getter method for global_rsvp_hello_acknowledgements, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/global_rsvp_hello_acknowledgements (empty)
    """
    return self.__global_rsvp_hello_acknowledgements
      
  def _set_global_rsvp_hello_acknowledgements(self, v, load=False):
    """
    Setter method for global_rsvp_hello_acknowledgements, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/global_rsvp_hello_acknowledgements (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_rsvp_hello_acknowledgements is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_rsvp_hello_acknowledgements() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="global-rsvp-hello-acknowledgements", rest_name="hello-acknowledgements", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Acknowledge RSVP Hellos on interfaces supporting RSVP Hello and not having RSVP sessions', u'alt-name': u'hello-acknowledgements'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_rsvp_hello_acknowledgements must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="global-rsvp-hello-acknowledgements", rest_name="hello-acknowledgements", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Acknowledge RSVP Hellos on interfaces supporting RSVP Hello and not having RSVP sessions', u'alt-name': u'hello-acknowledgements'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__global_rsvp_hello_acknowledgements = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_rsvp_hello_acknowledgements(self):
    self.__global_rsvp_hello_acknowledgements = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="global-rsvp-hello-acknowledgements", rest_name="hello-acknowledgements", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Acknowledge RSVP Hellos on interfaces supporting RSVP Hello and not having RSVP sessions', u'alt-name': u'hello-acknowledgements'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)


  def _get_global_rsvp_hello_unprioritize(self):
    """
    Getter method for global_rsvp_hello_unprioritize, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/global_rsvp_hello_unprioritize (empty)
    """
    return self.__global_rsvp_hello_unprioritize
      
  def _set_global_rsvp_hello_unprioritize(self, v, load=False):
    """
    Setter method for global_rsvp_hello_unprioritize, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/global_rsvp_hello_unprioritize (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_rsvp_hello_unprioritize is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_rsvp_hello_unprioritize() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="global-rsvp-hello-unprioritize", rest_name="hello-unprioritize", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Stop prioritizing RSVP Hello messages', u'hidden': u'full', u'alt-name': u'hello-unprioritize'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_rsvp_hello_unprioritize must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="global-rsvp-hello-unprioritize", rest_name="hello-unprioritize", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Stop prioritizing RSVP Hello messages', u'hidden': u'full', u'alt-name': u'hello-unprioritize'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__global_rsvp_hello_unprioritize = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_rsvp_hello_unprioritize(self):
    self.__global_rsvp_hello_unprioritize = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="global-rsvp-hello-unprioritize", rest_name="hello-unprioritize", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Stop prioritizing RSVP Hello messages', u'hidden': u'full', u'alt-name': u'hello-unprioritize'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)


  def _get_g_rsvp_backup_bw_guarantee(self):
    """
    Getter method for g_rsvp_backup_bw_guarantee, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/g_rsvp_backup_bw_guarantee (empty)
    """
    return self.__g_rsvp_backup_bw_guarantee
      
  def _set_g_rsvp_backup_bw_guarantee(self, v, load=False):
    """
    Setter method for g_rsvp_backup_bw_guarantee, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/rsvp/g_rsvp_backup_bw_guarantee (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_g_rsvp_backup_bw_guarantee is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_g_rsvp_backup_bw_guarantee() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="g-rsvp-backup-bw-guarantee", rest_name="backup-bw-guarantee", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Setup a backup path requesting bandwidth only if bandwidth is available', u'alt-name': u'backup-bw-guarantee', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """g_rsvp_backup_bw_guarantee must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="g-rsvp-backup-bw-guarantee", rest_name="backup-bw-guarantee", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Setup a backup path requesting bandwidth only if bandwidth is available', u'alt-name': u'backup-bw-guarantee', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__g_rsvp_backup_bw_guarantee = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_g_rsvp_backup_bw_guarantee(self):
    self.__g_rsvp_backup_bw_guarantee = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="g-rsvp-backup-bw-guarantee", rest_name="backup-bw-guarantee", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Setup a backup path requesting bandwidth only if bandwidth is available', u'alt-name': u'backup-bw-guarantee', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)

  refresh_interval = __builtin__.property(_get_refresh_interval, _set_refresh_interval)
  refresh_multiple = __builtin__.property(_get_refresh_multiple, _set_refresh_multiple)
  g_refresh_reduction = __builtin__.property(_get_g_refresh_reduction, _set_g_refresh_reduction)
  g_reliable_messaging = __builtin__.property(_get_g_reliable_messaging, _set_g_reliable_messaging)
  global_rsvp_hello = __builtin__.property(_get_global_rsvp_hello, _set_global_rsvp_hello)
  global_rsvp_hello_acknowledgements = __builtin__.property(_get_global_rsvp_hello_acknowledgements, _set_global_rsvp_hello_acknowledgements)
  global_rsvp_hello_unprioritize = __builtin__.property(_get_global_rsvp_hello_unprioritize, _set_global_rsvp_hello_unprioritize)
  g_rsvp_backup_bw_guarantee = __builtin__.property(_get_g_rsvp_backup_bw_guarantee, _set_g_rsvp_backup_bw_guarantee)


  _pyangbind_elements = {'refresh_interval': refresh_interval, 'refresh_multiple': refresh_multiple, 'g_refresh_reduction': g_refresh_reduction, 'g_reliable_messaging': g_reliable_messaging, 'global_rsvp_hello': global_rsvp_hello, 'global_rsvp_hello_acknowledgements': global_rsvp_hello_acknowledgements, 'global_rsvp_hello_unprioritize': global_rsvp_hello_unprioritize, 'g_rsvp_backup_bw_guarantee': g_rsvp_backup_bw_guarantee, }


