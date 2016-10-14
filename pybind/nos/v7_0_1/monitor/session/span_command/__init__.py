
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class span_command(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-span - based on the path /monitor/session/span-command. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__source','__src_tengigabitethernet','__src_tengigabitethernet_val','__destination','__dest_tengigabitethernet','__dest_tengigabitethernet_val','__dest_vlan_val','__direction',)

  _yang_name = 'span-command'

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
    self.__direction = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'both': {'value': 2}, u'rx': {'value': 1}, u'tx': {'value': 0}},), is_leaf=True, yang_name="direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mirror Direction:Ingress or Egress or Both', u'cli-optional-in-sequence': None, u'display-when': u"(((../dest-tengigabitethernet = 'gigabitethernet') or\n(../dest-tengigabitethernet = 'tengigabitethernet') or\n(../dest-tengigabitethernet = 'fortygigabitethernet') or\n(../dest-tengigabitethernet = 'rspan-vlan') or \n               (../dest-tengigabitethernet = 'hundredgigabitethernet')) and \n(../source))"}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)
    self.__dest_tengigabitethernet_val = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3..16']}), is_leaf=True, yang_name="dest-tengigabitethernet-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../dest-tengigabitethernet = 'gigabitethernet' or\n../dest-tengigabitethernet = 'tengigabitethernet' or\n../dest-tengigabitethernet = 'fortygigabitethernet' or\n../dest-tengigabitethernet = 'hundredgigabitethernet'"}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='span-if-type', is_config=True)
    self.__dest_vlan_val = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="dest-vlan-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../dest-tengigabitethernet = 'rspan-vlan'"}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='interface:vlan-type', is_config=True)
    self.__destination = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'destination': {'value': 0}},), is_leaf=True, yang_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)
    self.__src_tengigabitethernet = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 3}},), is_leaf=True, yang_name="src-tengigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'(../source)', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)
    self.__source = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'source': {'value': 0}},), is_leaf=True, yang_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)
    self.__dest_tengigabitethernet = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'rspan-vlan': {'value': 4}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 3}},), is_leaf=True, yang_name="dest-tengigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)
    self.__src_tengigabitethernet_val = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3..16']}), is_leaf=True, yang_name="src-tengigabitethernet-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'(../source)', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='span-if-type', is_config=True)

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
      return [u'monitor', u'session', u'span-command']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._rest_name]
    else:
      return [u'monitor', u'session']

  def _get_source(self):
    """
    Getter method for source, mapped from YANG variable /monitor/session/span_command/source (enumeration)
    """
    return self.__source
      
  def _set_source(self, v, load=False):
    """
    Setter method for source, mapped from YANG variable /monitor/session/span_command/source (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'source': {'value': 0}},), is_leaf=True, yang_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source must be of a type compatible with enumeration""",
          'defined-type': "brocade-span:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'source': {'value': 0}},), is_leaf=True, yang_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)""",
        })

    self.__source = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source(self):
    self.__source = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'source': {'value': 0}},), is_leaf=True, yang_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)


  def _get_src_tengigabitethernet(self):
    """
    Getter method for src_tengigabitethernet, mapped from YANG variable /monitor/session/span_command/src_tengigabitethernet (enumeration)
    """
    return self.__src_tengigabitethernet
      
  def _set_src_tengigabitethernet(self, v, load=False):
    """
    Setter method for src_tengigabitethernet, mapped from YANG variable /monitor/session/span_command/src_tengigabitethernet (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_tengigabitethernet is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_tengigabitethernet() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 3}},), is_leaf=True, yang_name="src-tengigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'(../source)', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_tengigabitethernet must be of a type compatible with enumeration""",
          'defined-type': "brocade-span:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 3}},), is_leaf=True, yang_name="src-tengigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'(../source)', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)""",
        })

    self.__src_tengigabitethernet = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_tengigabitethernet(self):
    self.__src_tengigabitethernet = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 3}},), is_leaf=True, yang_name="src-tengigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'(../source)', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)


  def _get_src_tengigabitethernet_val(self):
    """
    Getter method for src_tengigabitethernet_val, mapped from YANG variable /monitor/session/span_command/src_tengigabitethernet_val (span-if-type)
    """
    return self.__src_tengigabitethernet_val
      
  def _set_src_tengigabitethernet_val(self, v, load=False):
    """
    Setter method for src_tengigabitethernet_val, mapped from YANG variable /monitor/session/span_command/src_tengigabitethernet_val (span-if-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_tengigabitethernet_val is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_tengigabitethernet_val() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3..16']}), is_leaf=True, yang_name="src-tengigabitethernet-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'(../source)', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='span-if-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_tengigabitethernet_val must be of a type compatible with span-if-type""",
          'defined-type': "brocade-span:span-if-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3..16']}), is_leaf=True, yang_name="src-tengigabitethernet-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'(../source)', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='span-if-type', is_config=True)""",
        })

    self.__src_tengigabitethernet_val = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_tengigabitethernet_val(self):
    self.__src_tengigabitethernet_val = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3..16']}), is_leaf=True, yang_name="src-tengigabitethernet-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'(../source)', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='span-if-type', is_config=True)


  def _get_destination(self):
    """
    Getter method for destination, mapped from YANG variable /monitor/session/span_command/destination (enumeration)
    """
    return self.__destination
      
  def _set_destination(self, v, load=False):
    """
    Setter method for destination, mapped from YANG variable /monitor/session/span_command/destination (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'destination': {'value': 0}},), is_leaf=True, yang_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination must be of a type compatible with enumeration""",
          'defined-type': "brocade-span:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'destination': {'value': 0}},), is_leaf=True, yang_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)""",
        })

    self.__destination = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination(self):
    self.__destination = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'destination': {'value': 0}},), is_leaf=True, yang_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)


  def _get_dest_tengigabitethernet(self):
    """
    Getter method for dest_tengigabitethernet, mapped from YANG variable /monitor/session/span_command/dest_tengigabitethernet (enumeration)
    """
    return self.__dest_tengigabitethernet
      
  def _set_dest_tengigabitethernet(self, v, load=False):
    """
    Setter method for dest_tengigabitethernet, mapped from YANG variable /monitor/session/span_command/dest_tengigabitethernet (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dest_tengigabitethernet is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dest_tengigabitethernet() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'rspan-vlan': {'value': 4}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 3}},), is_leaf=True, yang_name="dest-tengigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dest_tengigabitethernet must be of a type compatible with enumeration""",
          'defined-type': "brocade-span:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'rspan-vlan': {'value': 4}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 3}},), is_leaf=True, yang_name="dest-tengigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)""",
        })

    self.__dest_tengigabitethernet = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dest_tengigabitethernet(self):
    self.__dest_tengigabitethernet = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'rspan-vlan': {'value': 4}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 3}},), is_leaf=True, yang_name="dest-tengigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)


  def _get_dest_tengigabitethernet_val(self):
    """
    Getter method for dest_tengigabitethernet_val, mapped from YANG variable /monitor/session/span_command/dest_tengigabitethernet_val (span-if-type)
    """
    return self.__dest_tengigabitethernet_val
      
  def _set_dest_tengigabitethernet_val(self, v, load=False):
    """
    Setter method for dest_tengigabitethernet_val, mapped from YANG variable /monitor/session/span_command/dest_tengigabitethernet_val (span-if-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dest_tengigabitethernet_val is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dest_tengigabitethernet_val() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3..16']}), is_leaf=True, yang_name="dest-tengigabitethernet-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../dest-tengigabitethernet = 'gigabitethernet' or\n../dest-tengigabitethernet = 'tengigabitethernet' or\n../dest-tengigabitethernet = 'fortygigabitethernet' or\n../dest-tengigabitethernet = 'hundredgigabitethernet'"}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='span-if-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dest_tengigabitethernet_val must be of a type compatible with span-if-type""",
          'defined-type': "brocade-span:span-if-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3..16']}), is_leaf=True, yang_name="dest-tengigabitethernet-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../dest-tengigabitethernet = 'gigabitethernet' or\n../dest-tengigabitethernet = 'tengigabitethernet' or\n../dest-tengigabitethernet = 'fortygigabitethernet' or\n../dest-tengigabitethernet = 'hundredgigabitethernet'"}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='span-if-type', is_config=True)""",
        })

    self.__dest_tengigabitethernet_val = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dest_tengigabitethernet_val(self):
    self.__dest_tengigabitethernet_val = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3..16']}), is_leaf=True, yang_name="dest-tengigabitethernet-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../dest-tengigabitethernet = 'gigabitethernet' or\n../dest-tengigabitethernet = 'tengigabitethernet' or\n../dest-tengigabitethernet = 'fortygigabitethernet' or\n../dest-tengigabitethernet = 'hundredgigabitethernet'"}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='span-if-type', is_config=True)


  def _get_dest_vlan_val(self):
    """
    Getter method for dest_vlan_val, mapped from YANG variable /monitor/session/span_command/dest_vlan_val (interface:vlan-type)
    """
    return self.__dest_vlan_val
      
  def _set_dest_vlan_val(self, v, load=False):
    """
    Setter method for dest_vlan_val, mapped from YANG variable /monitor/session/span_command/dest_vlan_val (interface:vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dest_vlan_val is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dest_vlan_val() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="dest-vlan-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../dest-tengigabitethernet = 'rspan-vlan'"}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='interface:vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dest_vlan_val must be of a type compatible with interface:vlan-type""",
          'defined-type': "interface:vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="dest-vlan-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../dest-tengigabitethernet = 'rspan-vlan'"}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='interface:vlan-type', is_config=True)""",
        })

    self.__dest_vlan_val = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dest_vlan_val(self):
    self.__dest_vlan_val = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="dest-vlan-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../dest-tengigabitethernet = 'rspan-vlan'"}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='interface:vlan-type', is_config=True)


  def _get_direction(self):
    """
    Getter method for direction, mapped from YANG variable /monitor/session/span_command/direction (enumeration)
    """
    return self.__direction
      
  def _set_direction(self, v, load=False):
    """
    Setter method for direction, mapped from YANG variable /monitor/session/span_command/direction (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_direction is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_direction() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'both': {'value': 2}, u'rx': {'value': 1}, u'tx': {'value': 0}},), is_leaf=True, yang_name="direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mirror Direction:Ingress or Egress or Both', u'cli-optional-in-sequence': None, u'display-when': u"(((../dest-tengigabitethernet = 'gigabitethernet') or\n(../dest-tengigabitethernet = 'tengigabitethernet') or\n(../dest-tengigabitethernet = 'fortygigabitethernet') or\n(../dest-tengigabitethernet = 'rspan-vlan') or \n               (../dest-tengigabitethernet = 'hundredgigabitethernet')) and \n(../source))"}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """direction must be of a type compatible with enumeration""",
          'defined-type': "brocade-span:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'both': {'value': 2}, u'rx': {'value': 1}, u'tx': {'value': 0}},), is_leaf=True, yang_name="direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mirror Direction:Ingress or Egress or Both', u'cli-optional-in-sequence': None, u'display-when': u"(((../dest-tengigabitethernet = 'gigabitethernet') or\n(../dest-tengigabitethernet = 'tengigabitethernet') or\n(../dest-tengigabitethernet = 'fortygigabitethernet') or\n(../dest-tengigabitethernet = 'rspan-vlan') or \n               (../dest-tengigabitethernet = 'hundredgigabitethernet')) and \n(../source))"}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)""",
        })

    self.__direction = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_direction(self):
    self.__direction = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'both': {'value': 2}, u'rx': {'value': 1}, u'tx': {'value': 0}},), is_leaf=True, yang_name="direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mirror Direction:Ingress or Egress or Both', u'cli-optional-in-sequence': None, u'display-when': u"(((../dest-tengigabitethernet = 'gigabitethernet') or\n(../dest-tengigabitethernet = 'tengigabitethernet') or\n(../dest-tengigabitethernet = 'fortygigabitethernet') or\n(../dest-tengigabitethernet = 'rspan-vlan') or \n               (../dest-tengigabitethernet = 'hundredgigabitethernet')) and \n(../source))"}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='enumeration', is_config=True)

  source = __builtin__.property(_get_source, _set_source)
  src_tengigabitethernet = __builtin__.property(_get_src_tengigabitethernet, _set_src_tengigabitethernet)
  src_tengigabitethernet_val = __builtin__.property(_get_src_tengigabitethernet_val, _set_src_tengigabitethernet_val)
  destination = __builtin__.property(_get_destination, _set_destination)
  dest_tengigabitethernet = __builtin__.property(_get_dest_tengigabitethernet, _set_dest_tengigabitethernet)
  dest_tengigabitethernet_val = __builtin__.property(_get_dest_tengigabitethernet_val, _set_dest_tengigabitethernet_val)
  dest_vlan_val = __builtin__.property(_get_dest_vlan_val, _set_dest_vlan_val)
  direction = __builtin__.property(_get_direction, _set_direction)


  _pyangbind_elements = {'source': source, 'src_tengigabitethernet': src_tengigabitethernet, 'src_tengigabitethernet_val': src_tengigabitethernet_val, 'destination': destination, 'dest_tengigabitethernet': dest_tengigabitethernet, 'dest_tengigabitethernet_val': dest_tengigabitethernet_val, 'dest_vlan_val': dest_vlan_val, 'direction': direction, }

