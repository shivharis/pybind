
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import mqc
import l2
import ipv6
import ssm
import lag
class capabilities(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-system-capabilities - based on the path /capabilities. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mqc','__l2','__ipv6','__ssm','__lag',)

  _yang_name = 'capabilities'
  _rest_name = 'capabilities'

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
    self.__ssm = YANGDynClass(base=ssm.ssm, is_container='container', presence=False, yang_name="ssm", rest_name="ssm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)
    self.__mqc = YANGDynClass(base=mqc.mqc, is_container='container', presence=False, yang_name="mqc", rest_name="mqc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)
    self.__lag = YANGDynClass(base=lag.lag, is_container='container', presence=False, yang_name="lag", rest_name="lag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)
    self.__l2 = YANGDynClass(base=l2.l2, is_container='container', presence=False, yang_name="l2", rest_name="l2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)

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
      return [u'capabilities']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'capabilities']

  def _get_mqc(self):
    """
    Getter method for mqc, mapped from YANG variable /capabilities/mqc (container)
    """
    return self.__mqc
      
  def _set_mqc(self, v, load=False):
    """
    Setter method for mqc, mapped from YANG variable /capabilities/mqc (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mqc is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mqc() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=mqc.mqc, is_container='container', presence=False, yang_name="mqc", rest_name="mqc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mqc must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mqc.mqc, is_container='container', presence=False, yang_name="mqc", rest_name="mqc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)""",
        })

    self.__mqc = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mqc(self):
    self.__mqc = YANGDynClass(base=mqc.mqc, is_container='container', presence=False, yang_name="mqc", rest_name="mqc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)


  def _get_l2(self):
    """
    Getter method for l2, mapped from YANG variable /capabilities/l2 (container)
    """
    return self.__l2
      
  def _set_l2(self, v, load=False):
    """
    Setter method for l2, mapped from YANG variable /capabilities/l2 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l2() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=l2.l2, is_container='container', presence=False, yang_name="l2", rest_name="l2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l2 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=l2.l2, is_container='container', presence=False, yang_name="l2", rest_name="l2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)""",
        })

    self.__l2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l2(self):
    self.__l2 = YANGDynClass(base=l2.l2, is_container='container', presence=False, yang_name="l2", rest_name="l2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)


  def _get_ipv6(self):
    """
    Getter method for ipv6, mapped from YANG variable /capabilities/ipv6 (container)
    """
    return self.__ipv6
      
  def _set_ipv6(self, v, load=False):
    """
    Setter method for ipv6, mapped from YANG variable /capabilities/ipv6 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)""",
        })

    self.__ipv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6(self):
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)


  def _get_ssm(self):
    """
    Getter method for ssm, mapped from YANG variable /capabilities/ssm (container)
    """
    return self.__ssm
      
  def _set_ssm(self, v, load=False):
    """
    Setter method for ssm, mapped from YANG variable /capabilities/ssm (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ssm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ssm() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ssm.ssm, is_container='container', presence=False, yang_name="ssm", rest_name="ssm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ssm must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ssm.ssm, is_container='container', presence=False, yang_name="ssm", rest_name="ssm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)""",
        })

    self.__ssm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ssm(self):
    self.__ssm = YANGDynClass(base=ssm.ssm, is_container='container', presence=False, yang_name="ssm", rest_name="ssm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)


  def _get_lag(self):
    """
    Getter method for lag, mapped from YANG variable /capabilities/lag (container)
    """
    return self.__lag
      
  def _set_lag(self, v, load=False):
    """
    Setter method for lag, mapped from YANG variable /capabilities/lag (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lag() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=lag.lag, is_container='container', presence=False, yang_name="lag", rest_name="lag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lag must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=lag.lag, is_container='container', presence=False, yang_name="lag", rest_name="lag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)""",
        })

    self.__lag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lag(self):
    self.__lag = YANGDynClass(base=lag.lag, is_container='container', presence=False, yang_name="lag", rest_name="lag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='container', is_config=False)

  mqc = __builtin__.property(_get_mqc)
  l2 = __builtin__.property(_get_l2)
  ipv6 = __builtin__.property(_get_ipv6)
  ssm = __builtin__.property(_get_ssm)
  lag = __builtin__.property(_get_lag)


  _pyangbind_elements = {'mqc': mqc, 'l2': l2, 'ipv6': ipv6, 'ssm': ssm, 'lag': lag, }


