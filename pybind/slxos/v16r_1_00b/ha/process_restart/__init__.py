
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import disable_res
class process_restart(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ha - based on the path /ha/process-restart. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__disable_res',)

  _yang_name = 'process-restart'
  _rest_name = 'process-restart'

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
    self.__disable_res = YANGDynClass(base=disable_res.disable_res, is_container='container', yang_name="disable-res", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable process restart for fault recovery', u'cli-compact-syntax': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-ha', defining_module='brocade-ha', yang_type='container', is_config=True)

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
      return [u'ha', u'process-restart']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ha', u'process-restart']

  def _get_disable_res(self):
    """
    Getter method for disable_res, mapped from YANG variable /ha/process_restart/disable_res (container)
    """
    return self.__disable_res
      
  def _set_disable_res(self, v, load=False):
    """
    Setter method for disable_res, mapped from YANG variable /ha/process_restart/disable_res (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_disable_res is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_disable_res() directly.
    """
    try:
      t = YANGDynClass(v,base=disable_res.disable_res, is_container='container', yang_name="disable-res", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable process restart for fault recovery', u'cli-compact-syntax': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-ha', defining_module='brocade-ha', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """disable_res must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=disable_res.disable_res, is_container='container', yang_name="disable-res", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable process restart for fault recovery', u'cli-compact-syntax': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-ha', defining_module='brocade-ha', yang_type='container', is_config=True)""",
        })

    self.__disable_res = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_disable_res(self):
    self.__disable_res = YANGDynClass(base=disable_res.disable_res, is_container='container', yang_name="disable-res", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable process restart for fault recovery', u'cli-compact-syntax': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-ha', defining_module='brocade-ha', yang_type='container', is_config=True)

  disable_res = __builtin__.property(_get_disable_res, _set_disable_res)


  _pyangbind_elements = {'disable_res': disable_res, }


