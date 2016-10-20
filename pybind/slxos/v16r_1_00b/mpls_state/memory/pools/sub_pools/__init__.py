
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class sub_pools(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/memory/pools/sub-pools. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Memory sub pools
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__sub_pool_index','__gen_size','__block_size','__gen_blocks','__current_gens','__current_blocks','__free_blocks',)

  _yang_name = 'sub-pools'
  _rest_name = 'sub-pools'

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
    self.__current_gens = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="current-gens", rest_name="current-gens", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__gen_blocks = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="gen-blocks", rest_name="gen-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__gen_size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="gen-size", rest_name="gen-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__sub_pool_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sub-pool-index", rest_name="sub-pool-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__free_blocks = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free-blocks", rest_name="free-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__current_blocks = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="current-blocks", rest_name="current-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__block_size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="block-size", rest_name="block-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

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
      return [u'mpls-state', u'memory', u'pools', u'sub-pools']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'memory', u'pools', u'sub-pools']

  def _get_sub_pool_index(self):
    """
    Getter method for sub_pool_index, mapped from YANG variable /mpls_state/memory/pools/sub_pools/sub_pool_index (uint32)

    YANG Description: Sub-pool index
    """
    return self.__sub_pool_index
      
  def _set_sub_pool_index(self, v, load=False):
    """
    Setter method for sub_pool_index, mapped from YANG variable /mpls_state/memory/pools/sub_pools/sub_pool_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sub_pool_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sub_pool_index() directly.

    YANG Description: Sub-pool index
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sub-pool-index", rest_name="sub-pool-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sub_pool_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sub-pool-index", rest_name="sub-pool-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__sub_pool_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sub_pool_index(self):
    self.__sub_pool_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sub-pool-index", rest_name="sub-pool-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_gen_size(self):
    """
    Getter method for gen_size, mapped from YANG variable /mpls_state/memory/pools/sub_pools/gen_size (uint32)

    YANG Description: Generation size
    """
    return self.__gen_size
      
  def _set_gen_size(self, v, load=False):
    """
    Setter method for gen_size, mapped from YANG variable /mpls_state/memory/pools/sub_pools/gen_size (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gen_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gen_size() directly.

    YANG Description: Generation size
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="gen-size", rest_name="gen-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gen_size must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="gen-size", rest_name="gen-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__gen_size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gen_size(self):
    self.__gen_size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="gen-size", rest_name="gen-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_block_size(self):
    """
    Getter method for block_size, mapped from YANG variable /mpls_state/memory/pools/sub_pools/block_size (uint32)

    YANG Description: Block size
    """
    return self.__block_size
      
  def _set_block_size(self, v, load=False):
    """
    Setter method for block_size, mapped from YANG variable /mpls_state/memory/pools/sub_pools/block_size (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_block_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_block_size() directly.

    YANG Description: Block size
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="block-size", rest_name="block-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """block_size must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="block-size", rest_name="block-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__block_size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_block_size(self):
    self.__block_size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="block-size", rest_name="block-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_gen_blocks(self):
    """
    Getter method for gen_blocks, mapped from YANG variable /mpls_state/memory/pools/sub_pools/gen_blocks (uint32)

    YANG Description: Generation blocks
    """
    return self.__gen_blocks
      
  def _set_gen_blocks(self, v, load=False):
    """
    Setter method for gen_blocks, mapped from YANG variable /mpls_state/memory/pools/sub_pools/gen_blocks (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gen_blocks is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gen_blocks() directly.

    YANG Description: Generation blocks
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="gen-blocks", rest_name="gen-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gen_blocks must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="gen-blocks", rest_name="gen-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__gen_blocks = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gen_blocks(self):
    self.__gen_blocks = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="gen-blocks", rest_name="gen-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_current_gens(self):
    """
    Getter method for current_gens, mapped from YANG variable /mpls_state/memory/pools/sub_pools/current_gens (uint32)

    YANG Description: Current generations
    """
    return self.__current_gens
      
  def _set_current_gens(self, v, load=False):
    """
    Setter method for current_gens, mapped from YANG variable /mpls_state/memory/pools/sub_pools/current_gens (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_current_gens is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_current_gens() directly.

    YANG Description: Current generations
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="current-gens", rest_name="current-gens", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """current_gens must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="current-gens", rest_name="current-gens", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__current_gens = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_current_gens(self):
    self.__current_gens = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="current-gens", rest_name="current-gens", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_current_blocks(self):
    """
    Getter method for current_blocks, mapped from YANG variable /mpls_state/memory/pools/sub_pools/current_blocks (uint32)

    YANG Description: Current blocks
    """
    return self.__current_blocks
      
  def _set_current_blocks(self, v, load=False):
    """
    Setter method for current_blocks, mapped from YANG variable /mpls_state/memory/pools/sub_pools/current_blocks (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_current_blocks is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_current_blocks() directly.

    YANG Description: Current blocks
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="current-blocks", rest_name="current-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """current_blocks must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="current-blocks", rest_name="current-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__current_blocks = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_current_blocks(self):
    self.__current_blocks = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="current-blocks", rest_name="current-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_free_blocks(self):
    """
    Getter method for free_blocks, mapped from YANG variable /mpls_state/memory/pools/sub_pools/free_blocks (uint32)

    YANG Description: Free blocks
    """
    return self.__free_blocks
      
  def _set_free_blocks(self, v, load=False):
    """
    Setter method for free_blocks, mapped from YANG variable /mpls_state/memory/pools/sub_pools/free_blocks (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_free_blocks is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_free_blocks() directly.

    YANG Description: Free blocks
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free-blocks", rest_name="free-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """free_blocks must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free-blocks", rest_name="free-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__free_blocks = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_free_blocks(self):
    self.__free_blocks = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free-blocks", rest_name="free-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

  sub_pool_index = __builtin__.property(_get_sub_pool_index)
  gen_size = __builtin__.property(_get_gen_size)
  block_size = __builtin__.property(_get_block_size)
  gen_blocks = __builtin__.property(_get_gen_blocks)
  current_gens = __builtin__.property(_get_current_gens)
  current_blocks = __builtin__.property(_get_current_blocks)
  free_blocks = __builtin__.property(_get_free_blocks)


  _pyangbind_elements = {'sub_pool_index': sub_pool_index, 'gen_size': gen_size, 'block_size': block_size, 'gen_blocks': gen_blocks, 'current_gens': current_gens, 'current_blocks': current_blocks, 'free_blocks': free_blocks, }


