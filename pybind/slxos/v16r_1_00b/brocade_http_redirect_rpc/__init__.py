
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import set_http_application_url
class brocade_http_redirect(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-http-redirect - based on the path /brocade_http_redirect_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Data Model for HTTP Server configuration
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__set_http_application_url',)

  _yang_name = 'brocade-http-redirect'
  _rest_name = ''

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
    self.__set_http_application_url = YANGDynClass(base=set_http_application_url.set_http_application_url, is_leaf=True, yang_name="set-http-application-url", rest_name="set-http-application-url", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'set-http-app-url'}}, namespace='urn:brocade.com:mgmt:brocade-http-redirect', defining_module='brocade-http-redirect', yang_type='rpc', is_config=True)

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
      return [u'brocade_http_redirect_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_set_http_application_url(self):
    """
    Getter method for set_http_application_url, mapped from YANG variable /brocade_http_redirect_rpc/set_http_application_url (rpc)

    YANG Description: update http application url.
    """
    return self.__set_http_application_url
      
  def _set_set_http_application_url(self, v, load=False):
    """
    Setter method for set_http_application_url, mapped from YANG variable /brocade_http_redirect_rpc/set_http_application_url (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_http_application_url is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_http_application_url() directly.

    YANG Description: update http application url.
    """
    try:
      t = YANGDynClass(v,base=set_http_application_url.set_http_application_url, is_leaf=True, yang_name="set-http-application-url", rest_name="set-http-application-url", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'set-http-app-url'}}, namespace='urn:brocade.com:mgmt:brocade-http-redirect', defining_module='brocade-http-redirect', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_http_application_url must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=set_http_application_url.set_http_application_url, is_leaf=True, yang_name="set-http-application-url", rest_name="set-http-application-url", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'set-http-app-url'}}, namespace='urn:brocade.com:mgmt:brocade-http-redirect', defining_module='brocade-http-redirect', yang_type='rpc', is_config=True)""",
        })

    self.__set_http_application_url = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_http_application_url(self):
    self.__set_http_application_url = YANGDynClass(base=set_http_application_url.set_http_application_url, is_leaf=True, yang_name="set-http-application-url", rest_name="set-http-application-url", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'set-http-app-url'}}, namespace='urn:brocade.com:mgmt:brocade-http-redirect', defining_module='brocade-http-redirect', yang_type='rpc', is_config=True)

  set_http_application_url = __builtin__.property(_get_set_http_application_url, _set_set_http_application_url)


  _pyangbind_elements = {'set_http_application_url': set_http_application_url, }


