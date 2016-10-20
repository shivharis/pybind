
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import get_tunnel_info
import get_tunnel_statistics
class brocade_tunnels_ext(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tunnels-ext - based on the path /brocade_tunnels_ext_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This management module is an instrumentation to manage the IP
tunnels. It is a extension of brocade-tunnels module.

Glossary of the terms used:
---------------------------
VXLAN       Virtual eXtensible Local Area Network (RFC 7348)
VXLAN Gateway
           Software module in Brocade VCS switch which forwards
           traffic between VXLAN and non-VXLAN environments.
NSX         NSX is a network virtualization platform solution
           by Vmware. Refer - www.vmware.com/in/products/nsx
NSX Controller
           NSX Controller is the cluster of x86 systems which
           manage the virtual networks.
TCP         Transmission Control Protocol (RFC 793)
SSL         Secure Sockets Layer Protocol (RFC 6101)
BFD         Bidirectional Forwarding Detection (RFC 5880)
BGP-EVPN    Border Gateway Protocol, Ethernet VPN (RFC 7432)


  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__get_tunnel_info','__get_tunnel_statistics',)

  _yang_name = 'brocade-tunnels-ext'
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
    self.__get_tunnel_statistics = YANGDynClass(base=get_tunnel_statistics.get_tunnel_statistics, is_leaf=True, yang_name="get-tunnel-statistics", rest_name="get-tunnel-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tnl-actionpt'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='rpc', is_config=True)
    self.__get_tunnel_info = YANGDynClass(base=get_tunnel_info.get_tunnel_info, is_leaf=True, yang_name="get-tunnel-info", rest_name="get-tunnel-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tnl-actionpt'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='rpc', is_config=True)

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
      return [u'brocade_tunnels_ext_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_get_tunnel_info(self):
    """
    Getter method for get_tunnel_info, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_info (rpc)

    YANG Description: Retrieves summary of one or more tunnles from the switch.
Output contains tunnel records sorted in the ascending order
of tunnel id.

Input filters can be used to select specific set of
tunnels matching a criteria. See rpc input section for
details of input filters. Only one filter can be specified.
RPC returns data about all tunnels if no filters are
specified.

Data is aggregated from all rbridges of cluster. Client can
use 'rbridge-id' filter to retrieve data from specific
rbridges.

When output contains large number of records, they are sent
in multiple pages. Page size is implementation specific.
Output contains an opaque data 'next-page-cursor' when more
pages exist. Client is expected to invoke the RPC again
with same filters and pass this opaque data as 'page-cursor'
paramater. This cycle should be repeated until the output
does not include 'next-page-cursor' value, indicating there
are no more data. Client should not pass 'page-cursor'
paramater to retrieve first page.

This RPC is equivalent of 'show tunnel brief' CLI.
    """
    return self.__get_tunnel_info
      
  def _set_get_tunnel_info(self, v, load=False):
    """
    Setter method for get_tunnel_info, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_info (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_tunnel_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_tunnel_info() directly.

    YANG Description: Retrieves summary of one or more tunnles from the switch.
Output contains tunnel records sorted in the ascending order
of tunnel id.

Input filters can be used to select specific set of
tunnels matching a criteria. See rpc input section for
details of input filters. Only one filter can be specified.
RPC returns data about all tunnels if no filters are
specified.

Data is aggregated from all rbridges of cluster. Client can
use 'rbridge-id' filter to retrieve data from specific
rbridges.

When output contains large number of records, they are sent
in multiple pages. Page size is implementation specific.
Output contains an opaque data 'next-page-cursor' when more
pages exist. Client is expected to invoke the RPC again
with same filters and pass this opaque data as 'page-cursor'
paramater. This cycle should be repeated until the output
does not include 'next-page-cursor' value, indicating there
are no more data. Client should not pass 'page-cursor'
paramater to retrieve first page.

This RPC is equivalent of 'show tunnel brief' CLI.
    """
    try:
      t = YANGDynClass(v,base=get_tunnel_info.get_tunnel_info, is_leaf=True, yang_name="get-tunnel-info", rest_name="get-tunnel-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tnl-actionpt'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_tunnel_info must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_tunnel_info.get_tunnel_info, is_leaf=True, yang_name="get-tunnel-info", rest_name="get-tunnel-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tnl-actionpt'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='rpc', is_config=True)""",
        })

    self.__get_tunnel_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_tunnel_info(self):
    self.__get_tunnel_info = YANGDynClass(base=get_tunnel_info.get_tunnel_info, is_leaf=True, yang_name="get-tunnel-info", rest_name="get-tunnel-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tnl-actionpt'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='rpc', is_config=True)


  def _get_get_tunnel_statistics(self):
    """
    Getter method for get_tunnel_statistics, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics (rpc)

    YANG Description: Retrieves tunnel statistics - count of bytes & frames
transmitted and received. Output records are sorted in
ascending order of tunnel id.

Data is aggregated from all rbridges of cluster. Clients can
use 'rbridge-id' filter to retrieve statistics from specific
rbridges.

When output contains large number of records, they are sent
in multiple pages. Page size is implementation specific.
Output contains an opaque data 'next-page-cursor' when more
pages exist. Client is expected to invoke the RPC again
with same filters and pass this opaque data as 'page-cursor'
paramater. This cycle should be repeated until the output
does not include 'next-page-cursor' value, indicating there
are no more data. Client should not pass 'page-cursor'
paramater to retrieve first page.

This RPC is equivalent of 'show tunnel statistics' CLI.
    """
    return self.__get_tunnel_statistics
      
  def _set_get_tunnel_statistics(self, v, load=False):
    """
    Setter method for get_tunnel_statistics, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_tunnel_statistics is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_tunnel_statistics() directly.

    YANG Description: Retrieves tunnel statistics - count of bytes & frames
transmitted and received. Output records are sorted in
ascending order of tunnel id.

Data is aggregated from all rbridges of cluster. Clients can
use 'rbridge-id' filter to retrieve statistics from specific
rbridges.

When output contains large number of records, they are sent
in multiple pages. Page size is implementation specific.
Output contains an opaque data 'next-page-cursor' when more
pages exist. Client is expected to invoke the RPC again
with same filters and pass this opaque data as 'page-cursor'
paramater. This cycle should be repeated until the output
does not include 'next-page-cursor' value, indicating there
are no more data. Client should not pass 'page-cursor'
paramater to retrieve first page.

This RPC is equivalent of 'show tunnel statistics' CLI.
    """
    try:
      t = YANGDynClass(v,base=get_tunnel_statistics.get_tunnel_statistics, is_leaf=True, yang_name="get-tunnel-statistics", rest_name="get-tunnel-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tnl-actionpt'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_tunnel_statistics must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_tunnel_statistics.get_tunnel_statistics, is_leaf=True, yang_name="get-tunnel-statistics", rest_name="get-tunnel-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tnl-actionpt'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='rpc', is_config=True)""",
        })

    self.__get_tunnel_statistics = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_tunnel_statistics(self):
    self.__get_tunnel_statistics = YANGDynClass(base=get_tunnel_statistics.get_tunnel_statistics, is_leaf=True, yang_name="get-tunnel-statistics", rest_name="get-tunnel-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tnl-actionpt'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='rpc', is_config=True)

  get_tunnel_info = __builtin__.property(_get_get_tunnel_info, _set_get_tunnel_info)
  get_tunnel_statistics = __builtin__.property(_get_get_tunnel_statistics, _set_get_tunnel_statistics)


  _pyangbind_elements = {'get_tunnel_info': get_tunnel_info, 'get_tunnel_statistics': get_tunnel_statistics, }


