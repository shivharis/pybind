
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class lsp_frr_bandwidth(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/lsp/lsp-frr/lsp-frr-bandwidth. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__lsp_frr_bandwidth','__lsp_frr_bandwidth_inherit',)

  _yang_name = 'lsp-frr-bandwidth'
  _rest_name = 'bandwidth'

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
    self.__lsp_frr_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="lsp-frr-bandwidth", rest_name="", parent=self, choice=(u'lsp-frr-bandwidth-options', u'lsp-frr-bandwidth-case-exact'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__lsp_frr_bandwidth_inherit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-frr-bandwidth-inherit", rest_name="inherit", parent=self, choice=(u'lsp-frr-bandwidth-options', u'lsp-frr-bandwidth-case-inherit'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Inherit the bandwidth for Detour/Backup LSP from the Protected LSP', u'cli-full-command': None, u'alt-name': u'inherit'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'lsp', u'lsp-frr', u'lsp-frr-bandwidth']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'mpls', u'lsp', u'frr', u'bandwidth']

  def _get_lsp_frr_bandwidth(self):
    """
    Getter method for lsp_frr_bandwidth, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_bandwidth/lsp_frr_bandwidth (uint32)
    """
    return self.__lsp_frr_bandwidth
      
  def _set_lsp_frr_bandwidth(self, v, load=False):
    """
    Setter method for lsp_frr_bandwidth, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_bandwidth/lsp_frr_bandwidth (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_frr_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_frr_bandwidth() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="lsp-frr-bandwidth", rest_name="", parent=self, choice=(u'lsp-frr-bandwidth-options', u'lsp-frr-bandwidth-case-exact'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_frr_bandwidth must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="lsp-frr-bandwidth", rest_name="", parent=self, choice=(u'lsp-frr-bandwidth-options', u'lsp-frr-bandwidth-case-exact'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__lsp_frr_bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_frr_bandwidth(self):
    self.__lsp_frr_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="lsp-frr-bandwidth", rest_name="", parent=self, choice=(u'lsp-frr-bandwidth-options', u'lsp-frr-bandwidth-case-exact'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_lsp_frr_bandwidth_inherit(self):
    """
    Getter method for lsp_frr_bandwidth_inherit, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_bandwidth/lsp_frr_bandwidth_inherit (empty)
    """
    return self.__lsp_frr_bandwidth_inherit
      
  def _set_lsp_frr_bandwidth_inherit(self, v, load=False):
    """
    Setter method for lsp_frr_bandwidth_inherit, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_bandwidth/lsp_frr_bandwidth_inherit (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_frr_bandwidth_inherit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_frr_bandwidth_inherit() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-frr-bandwidth-inherit", rest_name="inherit", parent=self, choice=(u'lsp-frr-bandwidth-options', u'lsp-frr-bandwidth-case-inherit'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Inherit the bandwidth for Detour/Backup LSP from the Protected LSP', u'cli-full-command': None, u'alt-name': u'inherit'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_frr_bandwidth_inherit must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-frr-bandwidth-inherit", rest_name="inherit", parent=self, choice=(u'lsp-frr-bandwidth-options', u'lsp-frr-bandwidth-case-inherit'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Inherit the bandwidth for Detour/Backup LSP from the Protected LSP', u'cli-full-command': None, u'alt-name': u'inherit'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__lsp_frr_bandwidth_inherit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_frr_bandwidth_inherit(self):
    self.__lsp_frr_bandwidth_inherit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-frr-bandwidth-inherit", rest_name="inherit", parent=self, choice=(u'lsp-frr-bandwidth-options', u'lsp-frr-bandwidth-case-inherit'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Inherit the bandwidth for Detour/Backup LSP from the Protected LSP', u'cli-full-command': None, u'alt-name': u'inherit'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)

  lsp_frr_bandwidth = __builtin__.property(_get_lsp_frr_bandwidth, _set_lsp_frr_bandwidth)
  lsp_frr_bandwidth_inherit = __builtin__.property(_get_lsp_frr_bandwidth_inherit, _set_lsp_frr_bandwidth_inherit)

  __choices__ = {u'lsp-frr-bandwidth-options': {u'lsp-frr-bandwidth-case-exact': [u'lsp_frr_bandwidth'], u'lsp-frr-bandwidth-case-inherit': [u'lsp_frr_bandwidth_inherit']}}
  _pyangbind_elements = {'lsp_frr_bandwidth': lsp_frr_bandwidth, 'lsp_frr_bandwidth_inherit': lsp_frr_bandwidth_inherit, }


