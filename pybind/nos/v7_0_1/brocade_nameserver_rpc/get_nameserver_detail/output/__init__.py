
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import show_nameserver
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-nameserver - based on the path /brocade_nameserver_rpc/get-nameserver-detail/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__show_nameserver',)

  _yang_name = 'output'
  _rest_name = 'output'

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
    self.__show_nameserver = YANGDynClass(base=YANGListType("nameserver_portid",show_nameserver.show_nameserver, yang_name="show-nameserver", rest_name="show-nameserver", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='nameserver-portid', extensions=None), is_container='list', yang_name="show-nameserver", rest_name="show-nameserver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nameserver', defining_module='brocade-nameserver', yang_type='list', is_config=True)

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
      return [u'brocade_nameserver_rpc', u'get-nameserver-detail', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-nameserver-detail', u'output']

  def _get_show_nameserver(self):
    """
    Getter method for show_nameserver, mapped from YANG variable /brocade_nameserver_rpc/get_nameserver_detail/output/show_nameserver (list)

    YANG Description: The list of all Nx_Ports registered in the
Name Server database of this managed
device. Each row represents a FC device
(Nx_Port) logged in and registered with the
Name Server.
    """
    return self.__show_nameserver
      
  def _set_show_nameserver(self, v, load=False):
    """
    Setter method for show_nameserver, mapped from YANG variable /brocade_nameserver_rpc/get_nameserver_detail/output/show_nameserver (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_nameserver is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_nameserver() directly.

    YANG Description: The list of all Nx_Ports registered in the
Name Server database of this managed
device. Each row represents a FC device
(Nx_Port) logged in and registered with the
Name Server.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("nameserver_portid",show_nameserver.show_nameserver, yang_name="show-nameserver", rest_name="show-nameserver", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='nameserver-portid', extensions=None), is_container='list', yang_name="show-nameserver", rest_name="show-nameserver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nameserver', defining_module='brocade-nameserver', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_nameserver must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("nameserver_portid",show_nameserver.show_nameserver, yang_name="show-nameserver", rest_name="show-nameserver", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='nameserver-portid', extensions=None), is_container='list', yang_name="show-nameserver", rest_name="show-nameserver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nameserver', defining_module='brocade-nameserver', yang_type='list', is_config=True)""",
        })

    self.__show_nameserver = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_nameserver(self):
    self.__show_nameserver = YANGDynClass(base=YANGListType("nameserver_portid",show_nameserver.show_nameserver, yang_name="show-nameserver", rest_name="show-nameserver", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='nameserver-portid', extensions=None), is_container='list', yang_name="show-nameserver", rest_name="show-nameserver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nameserver', defining_module='brocade-nameserver', yang_type='list', is_config=True)

  show_nameserver = __builtin__.property(_get_show_nameserver, _set_show_nameserver)


  _pyangbind_elements = {'show_nameserver': show_nameserver, }


