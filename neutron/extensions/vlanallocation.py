from neutron.api.v2 import base
from neutron.common import exceptions as nexception
from neutron.api import extensions
from neutron import manager


RESOURCE_NAME = 'vlan-allocation'
RESOURCE_ATTRIBUTE_MAP = {
    RESOURCE_NAME + 's': {
        'physical_network': {'allow_post': False, 'allow_put': False,
                             'is_visible': True},
        'vlan_id': {'allow_post': False, 'allow_put': False,
                    'is_visible': True, 'primary_key': True},
        'allocated': {'allow_post': False, 'allow_put': False,
                      'is_visible': True}
    }
}


class Vlanallocation(extensions.ExtensionDescriptor):

    @classmethod
    def get_name(cls):
        return "Neutron VLAN"

    @classmethod
    def get_alias(cls):
        return "vlan-allocation"

    @classmethod
    def get_description(cls):
        return _("Create VLAN resource.")

    @classmethod
    def get_namespace(cls):
        return ""

    @classmethod
    def get_updated(cls):
        return "2015-05-25T10:00:00-00:00"

    @classmethod
    def get_resources(cls):
        """Returns vlan Resources."""
        plugin = manager.NeutronManager.get_plugin()
        params = RESOURCE_ATTRIBUTE_MAP.get(RESOURCE_NAME + 's')
        controller = base.create_resource(RESOURCE_NAME + 's',
                                          RESOURCE_NAME,
                                          plugin, params,
                                          allow_pagination=True
                                          )
        ex = extensions.ResourceExtension(RESOURCE_NAME + 's',
                                          controller)

        return [ex]
