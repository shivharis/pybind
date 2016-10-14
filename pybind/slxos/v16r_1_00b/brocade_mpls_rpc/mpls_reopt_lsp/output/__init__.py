
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/mpls-reopt-lsp/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__reopt_lsp_ret_msg',)

  _yang_name = 'output'

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
    self.__reopt_lsp_ret_msg = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..128']}), is_leaf=True, yang_name="reopt-lsp-ret-msg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)

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
      return [u'brocade_mpls_rpc', u'mpls-reopt-lsp', u'output']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'mpls-reopt-lsp', u'output']

  def _get_reopt_lsp_ret_msg(self):
    """
    Getter method for reopt_lsp_ret_msg, mapped from YANG variable /brocade_mpls_rpc/mpls_reopt_lsp/output/reopt_lsp_ret_msg (string)

    YANG Description: Reoptimize all LSPs
    """
    return self.__reopt_lsp_ret_msg
      
  def _set_reopt_lsp_ret_msg(self, v, load=False):
    """
    Setter method for reopt_lsp_ret_msg, mapped from YANG variable /brocade_mpls_rpc/mpls_reopt_lsp/output/reopt_lsp_ret_msg (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reopt_lsp_ret_msg is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reopt_lsp_ret_msg() directly.

    YANG Description: Reoptimize all LSPs
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..128']}), is_leaf=True, yang_name="reopt-lsp-ret-msg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reopt_lsp_ret_msg must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..128']}), is_leaf=True, yang_name="reopt-lsp-ret-msg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__reopt_lsp_ret_msg = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reopt_lsp_ret_msg(self):
    self.__reopt_lsp_ret_msg = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..128']}), is_leaf=True, yang_name="reopt-lsp-ret-msg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)

  reopt_lsp_ret_msg = __builtin__.property(_get_reopt_lsp_ret_msg, _set_reopt_lsp_ret_msg)


  _pyangbind_elements = {'reopt_lsp_ret_msg': reopt_lsp_ret_msg, }


