
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class shape(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mqc - based on the path /policy-map/class/shape. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__shaping_rate',)

  _yang_name = 'shape'
  _rest_name = 'shape'

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
    self.__shaping_rate = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'28000 .. 100000000']}), is_leaf=True, yang_name="shaping_rate", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shaping rate', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='shaping-rate-limit', is_config=True)

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
      return [u'policy-map', u'class', u'shape']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'policy-map', u'class', u'shape']

  def _get_shaping_rate(self):
    """
    Getter method for shaping_rate, mapped from YANG variable /policy_map/class/shape/shaping_rate (shaping-rate-limit)
    """
    return self.__shaping_rate
      
  def _set_shaping_rate(self, v, load=False):
    """
    Setter method for shaping_rate, mapped from YANG variable /policy_map/class/shape/shaping_rate (shaping-rate-limit)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_shaping_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_shaping_rate() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'28000 .. 100000000']}), is_leaf=True, yang_name="shaping_rate", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shaping rate', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='shaping-rate-limit', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """shaping_rate must be of a type compatible with shaping-rate-limit""",
          'defined-type': "brocade-qos-mqc:shaping-rate-limit",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'28000 .. 100000000']}), is_leaf=True, yang_name="shaping_rate", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shaping rate', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='shaping-rate-limit', is_config=True)""",
        })

    self.__shaping_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_shaping_rate(self):
    self.__shaping_rate = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'28000 .. 100000000']}), is_leaf=True, yang_name="shaping_rate", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shaping rate', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='shaping-rate-limit', is_config=True)

  shaping_rate = __builtin__.property(_get_shaping_rate, _set_shaping_rate)


  _pyangbind_elements = {'shaping_rate': shaping_rate, }


