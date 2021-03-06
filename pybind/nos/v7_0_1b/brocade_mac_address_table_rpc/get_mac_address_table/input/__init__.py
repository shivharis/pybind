
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import last_mac_address_details
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mac-address-table - based on the path /brocade_mac_address_table_rpc/get-mac-address-table/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mac_address','__last_mac_address_details',)

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
    self.__last_mac_address_details = YANGDynClass(base=last_mac_address_details.last_mac_address_details, is_container='container', presence=False, yang_name="last-mac-address-details", rest_name="last-mac-address-details", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)
    self.__mac_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, choice=(u'request-type', u'get-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='yang:mac-address', is_config=True)

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
      return [u'brocade_mac_address_table_rpc', u'get-mac-address-table', u'input']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-mac-address-table', u'input']

  def _get_mac_address(self):
    """
    Getter method for mac_address, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/mac_address (yang:mac-address)

    YANG Description: The Mac Address for which the
corresponding mac entry will be
fetched. The i/p should be in 
xx:xx:xx:xx:xx:xx format.
    """
    return self.__mac_address
      
  def _set_mac_address(self, v, load=False):
    """
    Setter method for mac_address, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/mac_address (yang:mac-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_address() directly.

    YANG Description: The Mac Address for which the
corresponding mac entry will be
fetched. The i/p should be in 
xx:xx:xx:xx:xx:xx format.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, choice=(u'request-type', u'get-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='yang:mac-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_address must be of a type compatible with yang:mac-address""",
          'defined-type': "yang:mac-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, choice=(u'request-type', u'get-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='yang:mac-address', is_config=True)""",
        })

    self.__mac_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_address(self):
    self.__mac_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, choice=(u'request-type', u'get-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='yang:mac-address', is_config=True)


  def _get_last_mac_address_details(self):
    """
    Getter method for last_mac_address_details, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/last_mac_address_details (container)
    """
    return self.__last_mac_address_details
      
  def _set_last_mac_address_details(self, v, load=False):
    """
    Setter method for last_mac_address_details, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/last_mac_address_details (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_mac_address_details is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_mac_address_details() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=last_mac_address_details.last_mac_address_details, is_container='container', presence=False, yang_name="last-mac-address-details", rest_name="last-mac-address-details", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_mac_address_details must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=last_mac_address_details.last_mac_address_details, is_container='container', presence=False, yang_name="last-mac-address-details", rest_name="last-mac-address-details", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)""",
        })

    self.__last_mac_address_details = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_mac_address_details(self):
    self.__last_mac_address_details = YANGDynClass(base=last_mac_address_details.last_mac_address_details, is_container='container', presence=False, yang_name="last-mac-address-details", rest_name="last-mac-address-details", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)

  mac_address = __builtin__.property(_get_mac_address, _set_mac_address)
  last_mac_address_details = __builtin__.property(_get_last_mac_address_details, _set_last_mac_address_details)

  __choices__ = {u'request-type': {u'get-next-request': [u'last_mac_address_details'], u'get-request': [u'mac_address']}}
  _pyangbind_elements = {'mac_address': mac_address, 'last_mac_address_details': last_mac_address_details, }


