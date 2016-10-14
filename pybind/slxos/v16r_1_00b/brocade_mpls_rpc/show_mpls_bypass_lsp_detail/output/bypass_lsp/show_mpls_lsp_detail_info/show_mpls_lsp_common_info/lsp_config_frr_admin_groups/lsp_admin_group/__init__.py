
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import lsp_admin_group_exclude_any
import lsp_admin_group_include_any
import lsp_admin_group_include_all
class lsp_admin_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-bypass-lsp-detail/output/bypass-lsp/show-mpls-lsp-detail-info/show-mpls-lsp-common-info/lsp-config-frr-admin-groups/lsp-admin-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__lsp_admin_group_exclude_any','__lsp_admin_group_include_any','__lsp_admin_group_include_all',)

  _yang_name = 'lsp-admin-group'

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
    self.__lsp_admin_group_exclude_any = YANGDynClass(base=YANGListType("lsp_admin_group_exclude_any_group_id",lsp_admin_group_exclude_any.lsp_admin_group_exclude_any, yang_name="lsp-admin-group-exclude-any", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-admin-group-exclude-any-group-id', extensions=None), is_container='list', yang_name="lsp-admin-group-exclude-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    self.__lsp_admin_group_include_any = YANGDynClass(base=YANGListType("lsp_admin_group_include_any_group_id",lsp_admin_group_include_any.lsp_admin_group_include_any, yang_name="lsp-admin-group-include-any", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-admin-group-include-any-group-id', extensions=None), is_container='list', yang_name="lsp-admin-group-include-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    self.__lsp_admin_group_include_all = YANGDynClass(base=YANGListType("lsp_admin_group_include_all_group_id",lsp_admin_group_include_all.lsp_admin_group_include_all, yang_name="lsp-admin-group-include-all", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-admin-group-include-all-group-id', extensions=None), is_container='list', yang_name="lsp-admin-group-include-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-bypass-lsp-detail', u'output', u'bypass-lsp', u'show-mpls-lsp-detail-info', u'show-mpls-lsp-common-info', u'lsp-config-frr-admin-groups', u'lsp-admin-group']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'show-mpls-bypass-lsp-detail', u'output', u'bypass-lsp', u'lsp-config-frr-admin-groups']

  def _get_lsp_admin_group_exclude_any(self):
    """
    Getter method for lsp_admin_group_exclude_any, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_detail/output/bypass_lsp/show_mpls_lsp_detail_info/show_mpls_lsp_common_info/lsp_config_frr_admin_groups/lsp_admin_group/lsp_admin_group_exclude_any (list)
    """
    return self.__lsp_admin_group_exclude_any
      
  def _set_lsp_admin_group_exclude_any(self, v, load=False):
    """
    Setter method for lsp_admin_group_exclude_any, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_detail/output/bypass_lsp/show_mpls_lsp_detail_info/show_mpls_lsp_common_info/lsp_config_frr_admin_groups/lsp_admin_group/lsp_admin_group_exclude_any (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_admin_group_exclude_any is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_admin_group_exclude_any() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("lsp_admin_group_exclude_any_group_id",lsp_admin_group_exclude_any.lsp_admin_group_exclude_any, yang_name="lsp-admin-group-exclude-any", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-admin-group-exclude-any-group-id', extensions=None), is_container='list', yang_name="lsp-admin-group-exclude-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_admin_group_exclude_any must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("lsp_admin_group_exclude_any_group_id",lsp_admin_group_exclude_any.lsp_admin_group_exclude_any, yang_name="lsp-admin-group-exclude-any", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-admin-group-exclude-any-group-id', extensions=None), is_container='list', yang_name="lsp-admin-group-exclude-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)""",
        })

    self.__lsp_admin_group_exclude_any = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_admin_group_exclude_any(self):
    self.__lsp_admin_group_exclude_any = YANGDynClass(base=YANGListType("lsp_admin_group_exclude_any_group_id",lsp_admin_group_exclude_any.lsp_admin_group_exclude_any, yang_name="lsp-admin-group-exclude-any", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-admin-group-exclude-any-group-id', extensions=None), is_container='list', yang_name="lsp-admin-group-exclude-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)


  def _get_lsp_admin_group_include_any(self):
    """
    Getter method for lsp_admin_group_include_any, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_detail/output/bypass_lsp/show_mpls_lsp_detail_info/show_mpls_lsp_common_info/lsp_config_frr_admin_groups/lsp_admin_group/lsp_admin_group_include_any (list)
    """
    return self.__lsp_admin_group_include_any
      
  def _set_lsp_admin_group_include_any(self, v, load=False):
    """
    Setter method for lsp_admin_group_include_any, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_detail/output/bypass_lsp/show_mpls_lsp_detail_info/show_mpls_lsp_common_info/lsp_config_frr_admin_groups/lsp_admin_group/lsp_admin_group_include_any (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_admin_group_include_any is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_admin_group_include_any() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("lsp_admin_group_include_any_group_id",lsp_admin_group_include_any.lsp_admin_group_include_any, yang_name="lsp-admin-group-include-any", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-admin-group-include-any-group-id', extensions=None), is_container='list', yang_name="lsp-admin-group-include-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_admin_group_include_any must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("lsp_admin_group_include_any_group_id",lsp_admin_group_include_any.lsp_admin_group_include_any, yang_name="lsp-admin-group-include-any", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-admin-group-include-any-group-id', extensions=None), is_container='list', yang_name="lsp-admin-group-include-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)""",
        })

    self.__lsp_admin_group_include_any = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_admin_group_include_any(self):
    self.__lsp_admin_group_include_any = YANGDynClass(base=YANGListType("lsp_admin_group_include_any_group_id",lsp_admin_group_include_any.lsp_admin_group_include_any, yang_name="lsp-admin-group-include-any", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-admin-group-include-any-group-id', extensions=None), is_container='list', yang_name="lsp-admin-group-include-any", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)


  def _get_lsp_admin_group_include_all(self):
    """
    Getter method for lsp_admin_group_include_all, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_detail/output/bypass_lsp/show_mpls_lsp_detail_info/show_mpls_lsp_common_info/lsp_config_frr_admin_groups/lsp_admin_group/lsp_admin_group_include_all (list)
    """
    return self.__lsp_admin_group_include_all
      
  def _set_lsp_admin_group_include_all(self, v, load=False):
    """
    Setter method for lsp_admin_group_include_all, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_detail/output/bypass_lsp/show_mpls_lsp_detail_info/show_mpls_lsp_common_info/lsp_config_frr_admin_groups/lsp_admin_group/lsp_admin_group_include_all (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_admin_group_include_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_admin_group_include_all() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("lsp_admin_group_include_all_group_id",lsp_admin_group_include_all.lsp_admin_group_include_all, yang_name="lsp-admin-group-include-all", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-admin-group-include-all-group-id', extensions=None), is_container='list', yang_name="lsp-admin-group-include-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_admin_group_include_all must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("lsp_admin_group_include_all_group_id",lsp_admin_group_include_all.lsp_admin_group_include_all, yang_name="lsp-admin-group-include-all", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-admin-group-include-all-group-id', extensions=None), is_container='list', yang_name="lsp-admin-group-include-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)""",
        })

    self.__lsp_admin_group_include_all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_admin_group_include_all(self):
    self.__lsp_admin_group_include_all = YANGDynClass(base=YANGListType("lsp_admin_group_include_all_group_id",lsp_admin_group_include_all.lsp_admin_group_include_all, yang_name="lsp-admin-group-include-all", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-admin-group-include-all-group-id', extensions=None), is_container='list', yang_name="lsp-admin-group-include-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)

  lsp_admin_group_exclude_any = __builtin__.property(_get_lsp_admin_group_exclude_any, _set_lsp_admin_group_exclude_any)
  lsp_admin_group_include_any = __builtin__.property(_get_lsp_admin_group_include_any, _set_lsp_admin_group_include_any)
  lsp_admin_group_include_all = __builtin__.property(_get_lsp_admin_group_include_all, _set_lsp_admin_group_include_all)


  _pyangbind_elements = {'lsp_admin_group_exclude_any': lsp_admin_group_exclude_any, 'lsp_admin_group_include_any': lsp_admin_group_include_any, 'lsp_admin_group_include_all': lsp_admin_group_include_all, }


