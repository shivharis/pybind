
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import show_linkinfo
import show_portindex_interface_info
import show_fibrechannel_interface_info
import show_fabric_trunk_info
class brocade_fabric_service(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fabric-service - based on the path /brocade_fabric_service_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This management module gives Virtual Cluster Switching (VCS)
FABRIC related information. VCS refers to the ability of
a group of physical Ethernet switches, inter-connected
in arbitrary fashion via the regular front-end
data ports, to present themselves as one unified and
transparent Ethernet switching service to the external network.
The inter-connecting network that glues all these individual
switches is refered as 'fabric', and the group of physical
Ethernet switches in the fabric is refered to as 'cluster'.

Glossary of the terms used:
---------------------------
RBridge     - A Routing Bridge or RBridge is a network device
              that implements the TRILL protocol, as defined
              by the IETF.

RBridge-ID  - RBridge-ID is the unique identifier of a node
              in the fabric. It can take values from 1 - 239.

ISL         - A inter switch link (ISL) is the link directly
              connecting a fabric port of one switch to fabric
              port of another switch. For an ISL to come up
              both side of the link need to have
              compatible configurations.

Trunk       - Brocade trunk is a hardware based LAG (link
              aggregation group) that is formed dynamically.
              It is a technology that allows to combine up to
              8 ISLs into a single logical trunk that provides
              up to 80 Gigabits per second (Gbps) data
              transfers.
              Trunking uses a simple algorithm to optimally
              distribute frames across a set of available paths
              that link two adjacent switches. Such a set of
              links is called trunking group.
              In a trunk group one of the trunk ports is
              used to set up all routing paths for the entire
              trunk group. This port is called the 'trunk
              master'.

WWN         - World Wide Name (WWN) is a unique 64 bit
              identifier that is assigned to a manufacturer
              by the Institute of Electrical and Electronic
              Engineers(IEEE) and hard-coded into a Fibre
              Channel (FC) device.

Principle   - In a fabric one switch is elected to manage
Switch        RBridge-ID assignments within the fabric.
              This switch is called the Principal Switch.
              Each fabric has its own Principal Switch. If the
              fabric configuration changes, a different switch
              could become principal.
              Note: In case of a single switch fabric, the same
              switch acts as the Principal Switch.

ECMP        - Equal cost multiple path (ECMP) is a routing
              strategy where next-hop packet forwarding to a
              single destination can occur over multiple
              'best paths' which tie for top place in routing
              metric calculations.

BUM         - Broadcast, Unknown Unicast & Multicast (BUM)
              traffic.

FSPF        - Fabric Shortest Path First (FSPF) is a routing
              protocol used in Fibre Channel networks.
              It calculates the best path between switches,
              establishes routes across the fabric and
              calculates alternate routes in event of a
              failure or topology change. FSPF guarantees
              in-order delivery of frames, even if the
              routing topology has changed during a failure,
              by enforcing a 'hold down' time before a new
              path is activated.

Port ID(PID)- The Fibre Channel address ID in DDAAPP
              hexadecimal format.

VID         - VLAN identifier (VID).

PISL        - Physical inter switch link (PISL).

Note:
The terms node and switch have been used interchangeably
in this document. Both refer to the same.

  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__show_linkinfo','__show_portindex_interface_info','__show_fibrechannel_interface_info','__show_fabric_trunk_info',)

  _yang_name = 'brocade-fabric-service'
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
    self.__show_portindex_interface_info = YANGDynClass(base=show_portindex_interface_info.show_portindex_interface_info, is_leaf=True, yang_name="show-portindex-interface-info", rest_name="show-portindex-interface-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_portindex_interface_all'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)
    self.__show_linkinfo = YANGDynClass(base=show_linkinfo.show_linkinfo, is_leaf=True, yang_name="show-linkinfo", rest_name="show-linkinfo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_linkinfo_all'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)
    self.__show_fibrechannel_interface_info = YANGDynClass(base=show_fibrechannel_interface_info.show_fibrechannel_interface_info, is_leaf=True, yang_name="show-fibrechannel-interface-info", rest_name="show-fibrechannel-interface-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_fi_interface_info'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)
    self.__show_fabric_trunk_info = YANGDynClass(base=show_fabric_trunk_info.show_fabric_trunk_info, is_leaf=True, yang_name="show-fabric-trunk-info", rest_name="show-fabric-trunk-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_fabric_trunk'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)

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
      return [u'brocade_fabric_service_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_show_linkinfo(self):
    """
    Getter method for show_linkinfo, mapped from YANG variable /brocade_fabric_service_rpc/show_linkinfo (rpc)

    YANG Description: Provides details of all the links connected in
the fabric. This information is given in groups
for all the RBridges in the fabric.
    """
    return self.__show_linkinfo
      
  def _set_show_linkinfo(self, v, load=False):
    """
    Setter method for show_linkinfo, mapped from YANG variable /brocade_fabric_service_rpc/show_linkinfo (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_linkinfo is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_linkinfo() directly.

    YANG Description: Provides details of all the links connected in
the fabric. This information is given in groups
for all the RBridges in the fabric.
    """
    try:
      t = YANGDynClass(v,base=show_linkinfo.show_linkinfo, is_leaf=True, yang_name="show-linkinfo", rest_name="show-linkinfo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_linkinfo_all'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_linkinfo must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=show_linkinfo.show_linkinfo, is_leaf=True, yang_name="show-linkinfo", rest_name="show-linkinfo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_linkinfo_all'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)""",
        })

    self.__show_linkinfo = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_linkinfo(self):
    self.__show_linkinfo = YANGDynClass(base=show_linkinfo.show_linkinfo, is_leaf=True, yang_name="show-linkinfo", rest_name="show-linkinfo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_linkinfo_all'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)


  def _get_show_portindex_interface_info(self):
    """
    Getter method for show_portindex_interface_info, mapped from YANG variable /brocade_fabric_service_rpc/show_portindex_interface_info (rpc)

    YANG Description: Provides the details of 10G Ethernet and fibrechannel
over ethernet ports. It consists of port index of the
RBridge, port type (Te or FCOE) and port interface.
Port interface is in the format
rbridge-id/slot/port for Te ports and
vlan-id/rbridge-id/port for FCOE ports.
    """
    return self.__show_portindex_interface_info
      
  def _set_show_portindex_interface_info(self, v, load=False):
    """
    Setter method for show_portindex_interface_info, mapped from YANG variable /brocade_fabric_service_rpc/show_portindex_interface_info (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_portindex_interface_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_portindex_interface_info() directly.

    YANG Description: Provides the details of 10G Ethernet and fibrechannel
over ethernet ports. It consists of port index of the
RBridge, port type (Te or FCOE) and port interface.
Port interface is in the format
rbridge-id/slot/port for Te ports and
vlan-id/rbridge-id/port for FCOE ports.
    """
    try:
      t = YANGDynClass(v,base=show_portindex_interface_info.show_portindex_interface_info, is_leaf=True, yang_name="show-portindex-interface-info", rest_name="show-portindex-interface-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_portindex_interface_all'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_portindex_interface_info must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=show_portindex_interface_info.show_portindex_interface_info, is_leaf=True, yang_name="show-portindex-interface-info", rest_name="show-portindex-interface-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_portindex_interface_all'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)""",
        })

    self.__show_portindex_interface_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_portindex_interface_info(self):
    self.__show_portindex_interface_info = YANGDynClass(base=show_portindex_interface_info.show_portindex_interface_info, is_leaf=True, yang_name="show-portindex-interface-info", rest_name="show-portindex-interface-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_portindex_interface_all'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)


  def _get_show_fibrechannel_interface_info(self):
    """
    Getter method for show_fibrechannel_interface_info, mapped from YANG variable /brocade_fabric_service_rpc/show_fibrechannel_interface_info (rpc)

    YANG Description: Provides all detailed information of fibrechannel ports
in the RBridge. It consists of port index of the RBridge,
port type (E-port/F-port/G-port/U-port), port interface, port
address, port WWN, remote port WWN, remote node WWN,
port state, port status, port status message, port health,
trunk details, licence details etc.
    """
    return self.__show_fibrechannel_interface_info
      
  def _set_show_fibrechannel_interface_info(self, v, load=False):
    """
    Setter method for show_fibrechannel_interface_info, mapped from YANG variable /brocade_fabric_service_rpc/show_fibrechannel_interface_info (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_fibrechannel_interface_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_fibrechannel_interface_info() directly.

    YANG Description: Provides all detailed information of fibrechannel ports
in the RBridge. It consists of port index of the RBridge,
port type (E-port/F-port/G-port/U-port), port interface, port
address, port WWN, remote port WWN, remote node WWN,
port state, port status, port status message, port health,
trunk details, licence details etc.
    """
    try:
      t = YANGDynClass(v,base=show_fibrechannel_interface_info.show_fibrechannel_interface_info, is_leaf=True, yang_name="show-fibrechannel-interface-info", rest_name="show-fibrechannel-interface-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_fi_interface_info'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_fibrechannel_interface_info must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=show_fibrechannel_interface_info.show_fibrechannel_interface_info, is_leaf=True, yang_name="show-fibrechannel-interface-info", rest_name="show-fibrechannel-interface-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_fi_interface_info'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)""",
        })

    self.__show_fibrechannel_interface_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_fibrechannel_interface_info(self):
    self.__show_fibrechannel_interface_info = YANGDynClass(base=show_fibrechannel_interface_info.show_fibrechannel_interface_info, is_leaf=True, yang_name="show-fibrechannel-interface-info", rest_name="show-fibrechannel-interface-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_fi_interface_info'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)


  def _get_show_fabric_trunk_info(self):
    """
    Getter method for show_fabric_trunk_info, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info (rpc)

    YANG Description:  This rpc provides all ISL trunk
information in a fabric
    """
    return self.__show_fabric_trunk_info
      
  def _set_show_fabric_trunk_info(self, v, load=False):
    """
    Setter method for show_fabric_trunk_info, mapped from YANG variable /brocade_fabric_service_rpc/show_fabric_trunk_info (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_fabric_trunk_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_fabric_trunk_info() directly.

    YANG Description:  This rpc provides all ISL trunk
information in a fabric
    """
    try:
      t = YANGDynClass(v,base=show_fabric_trunk_info.show_fabric_trunk_info, is_leaf=True, yang_name="show-fabric-trunk-info", rest_name="show-fabric-trunk-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_fabric_trunk'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_fabric_trunk_info must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=show_fabric_trunk_info.show_fabric_trunk_info, is_leaf=True, yang_name="show-fabric-trunk-info", rest_name="show-fabric-trunk-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_fabric_trunk'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)""",
        })

    self.__show_fabric_trunk_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_fabric_trunk_info(self):
    self.__show_fabric_trunk_info = YANGDynClass(base=show_fabric_trunk_info.show_fabric_trunk_info, is_leaf=True, yang_name="show-fabric-trunk-info", rest_name="show-fabric-trunk-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'show_fabric_trunk'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='rpc', is_config=True)

  show_linkinfo = __builtin__.property(_get_show_linkinfo, _set_show_linkinfo)
  show_portindex_interface_info = __builtin__.property(_get_show_portindex_interface_info, _set_show_portindex_interface_info)
  show_fibrechannel_interface_info = __builtin__.property(_get_show_fibrechannel_interface_info, _set_show_fibrechannel_interface_info)
  show_fabric_trunk_info = __builtin__.property(_get_show_fabric_trunk_info, _set_show_fabric_trunk_info)


  _pyangbind_elements = {'show_linkinfo': show_linkinfo, 'show_portindex_interface_info': show_portindex_interface_info, 'show_fibrechannel_interface_info': show_fibrechannel_interface_info, 'show_fabric_trunk_info': show_fabric_trunk_info, }


