
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import show_cfm
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-dot1ag - based on the path /brocade_dot1ag_rpc/get-show-cfm/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__show_cfm',)

  _yang_name = 'output'
  _rest_name = 'output'

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
    self.__show_cfm = YANGDynClass(base=show_cfm.show_cfm, is_container='container', presence=False, yang_name="show-cfm", rest_name="show-cfm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)

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
      return [u'brocade_dot1ag_rpc', u'get-show-cfm', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-show-cfm', u'output']

  def _get_show_cfm(self):
    """
    Getter method for show_cfm, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm (container)
    """
    return self.__show_cfm
      
  def _set_show_cfm(self, v, load=False):
    """
    Setter method for show_cfm, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_cfm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_cfm() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=show_cfm.show_cfm, is_container='container', presence=False, yang_name="show-cfm", rest_name="show-cfm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_cfm must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=show_cfm.show_cfm, is_container='container', presence=False, yang_name="show-cfm", rest_name="show-cfm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)""",
        })

    self.__show_cfm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_cfm(self):
    self.__show_cfm = YANGDynClass(base=show_cfm.show_cfm, is_container='container', presence=False, yang_name="show-cfm", rest_name="show-cfm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='container', is_config=True)

  show_cfm = __builtin__.property(_get_show_cfm, _set_show_cfm)


  _pyangbind_elements = {'show_cfm': show_cfm, }


