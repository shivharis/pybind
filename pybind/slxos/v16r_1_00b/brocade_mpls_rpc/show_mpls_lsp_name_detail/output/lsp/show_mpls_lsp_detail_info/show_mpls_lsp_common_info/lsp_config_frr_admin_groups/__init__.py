
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import lsp_admin_group
class lsp_config_frr_admin_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-lsp-name-detail/output/lsp/show-mpls-lsp-detail-info/show-mpls-lsp-common-info/lsp-config-frr-admin-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__lsp_admin_group',)

  _yang_name = 'lsp-config-frr-admin-groups'
  _rest_name = 'lsp-config-frr-admin-groups'

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
    self.__lsp_admin_group = YANGDynClass(base=lsp_admin_group.lsp_admin_group, is_container='container', yang_name="lsp-admin-group", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-lsp-name-detail', u'output', u'lsp', u'show-mpls-lsp-detail-info', u'show-mpls-lsp-common-info', u'lsp-config-frr-admin-groups']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-lsp-name-detail', u'output', u'lsp', u'lsp-config-frr-admin-groups']

  def _get_lsp_admin_group(self):
    """
    Getter method for lsp_admin_group, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_common_info/lsp_config_frr_admin_groups/lsp_admin_group (container)
    """
    return self.__lsp_admin_group
      
  def _set_lsp_admin_group(self, v, load=False):
    """
    Setter method for lsp_admin_group, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_common_info/lsp_config_frr_admin_groups/lsp_admin_group (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_admin_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_admin_group() directly.
    """
    try:
      t = YANGDynClass(v,base=lsp_admin_group.lsp_admin_group, is_container='container', yang_name="lsp-admin-group", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_admin_group must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=lsp_admin_group.lsp_admin_group, is_container='container', yang_name="lsp-admin-group", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__lsp_admin_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_admin_group(self):
    self.__lsp_admin_group = YANGDynClass(base=lsp_admin_group.lsp_admin_group, is_container='container', yang_name="lsp-admin-group", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

  lsp_admin_group = __builtin__.property(_get_lsp_admin_group, _set_lsp_admin_group)


  _pyangbind_elements = {'lsp_admin_group': lsp_admin_group, }


