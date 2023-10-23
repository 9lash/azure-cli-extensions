# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "eventgrid namespace list",
    is_preview=True,
)
class List(AAZCommand):
    """List all the namespaces under an Azure subscription.

    :example: List namespace
        az eventgrid namespace list -g rg
    """

    _aaz_info = {
        "version": "2023-06-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.eventgrid/namespaces", "2023-06-01-preview"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.eventgrid/namespaces", "2023-06-01-preview"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.",
        )
        _args_schema.top = AAZIntArg(
            options=["--top"],
            help="The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        condition_1 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        if condition_0:
            self.NamespacesListByResourceGroup(ctx=self.ctx)()
        if condition_1:
            self.NamespacesListBySubscription(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class NamespacesListByResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/namespaces",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "$top", self.ctx.args.top,
                ),
                **self.serialize_query_param(
                    "api-version", "2023-06-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZObjectType()
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.sku = AAZObjectType()
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
            )
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.inbound_ip_rules = AAZListType(
                serialized_name="inboundIpRules",
            )
            properties.is_zone_redundant = AAZBoolType(
                serialized_name="isZoneRedundant",
            )
            properties.minimum_tls_version_allowed = AAZStrType(
                serialized_name="minimumTlsVersionAllowed",
            )
            properties.private_endpoint_connections = AAZListType(
                serialized_name="privateEndpointConnections",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_network_access = AAZStrType(
                serialized_name="publicNetworkAccess",
            )
            properties.topic_spaces_configuration = AAZObjectType(
                serialized_name="topicSpacesConfiguration",
            )
            properties.topics_configuration = AAZObjectType(
                serialized_name="topicsConfiguration",
            )

            inbound_ip_rules = cls._schema_on_200.value.Element.properties.inbound_ip_rules
            inbound_ip_rules.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.inbound_ip_rules.Element
            _element.action = AAZStrType()
            _element.ip_mask = AAZStrType(
                serialized_name="ipMask",
            )

            private_endpoint_connections = cls._schema_on_200.value.Element.properties.private_endpoint_connections
            private_endpoint_connections.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties
            properties.group_ids = AAZListType(
                serialized_name="groupIds",
            )
            properties.private_endpoint = AAZObjectType(
                serialized_name="privateEndpoint",
            )
            properties.private_link_service_connection_state = AAZObjectType(
                serialized_name="privateLinkServiceConnectionState",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )

            group_ids = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties.group_ids
            group_ids.Element = AAZStrType()

            private_endpoint = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties.private_endpoint
            private_endpoint.id = AAZStrType()

            private_link_service_connection_state = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties.private_link_service_connection_state
            private_link_service_connection_state.actions_required = AAZStrType(
                serialized_name="actionsRequired",
            )
            private_link_service_connection_state.description = AAZStrType()
            private_link_service_connection_state.status = AAZStrType()

            topic_spaces_configuration = cls._schema_on_200.value.Element.properties.topic_spaces_configuration
            topic_spaces_configuration.client_authentication = AAZObjectType(
                serialized_name="clientAuthentication",
            )
            topic_spaces_configuration.hostname = AAZStrType(
                flags={"read_only": True},
            )
            topic_spaces_configuration.maximum_client_sessions_per_authentication_name = AAZIntType(
                serialized_name="maximumClientSessionsPerAuthenticationName",
            )
            topic_spaces_configuration.maximum_session_expiry_in_hours = AAZIntType(
                serialized_name="maximumSessionExpiryInHours",
            )
            topic_spaces_configuration.route_topic_resource_id = AAZStrType(
                serialized_name="routeTopicResourceId",
            )
            topic_spaces_configuration.routing_enrichments = AAZObjectType(
                serialized_name="routingEnrichments",
            )
            topic_spaces_configuration.routing_identity_info = AAZObjectType(
                serialized_name="routingIdentityInfo",
            )
            topic_spaces_configuration.state = AAZStrType()

            client_authentication = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.client_authentication
            client_authentication.alternative_authentication_name_sources = AAZListType(
                serialized_name="alternativeAuthenticationNameSources",
            )

            alternative_authentication_name_sources = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.client_authentication.alternative_authentication_name_sources
            alternative_authentication_name_sources.Element = AAZStrType()

            routing_enrichments = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.routing_enrichments
            routing_enrichments.dynamic = AAZListType()
            routing_enrichments.static = AAZListType()

            dynamic = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.routing_enrichments.dynamic
            dynamic.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.routing_enrichments.dynamic.Element
            _element.key = AAZStrType()
            _element.value = AAZStrType()

            static = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.routing_enrichments.static
            static.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.routing_enrichments.static.Element
            _element.key = AAZStrType()
            _element.value_type = AAZStrType(
                serialized_name="valueType",
            )

            routing_identity_info = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.routing_identity_info
            routing_identity_info.type = AAZStrType()
            routing_identity_info.user_assigned_identity = AAZStrType(
                serialized_name="userAssignedIdentity",
            )

            topics_configuration = cls._schema_on_200.value.Element.properties.topics_configuration
            topics_configuration.hostname = AAZStrType(
                flags={"read_only": True},
            )

            sku = cls._schema_on_200.value.Element.sku
            sku.capacity = AAZIntType()
            sku.name = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class NamespacesListBySubscription(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.EventGrid/namespaces",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "$top", self.ctx.args.top,
                ),
                **self.serialize_query_param(
                    "api-version", "2023-06-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZObjectType()
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.sku = AAZObjectType()
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
            )
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.inbound_ip_rules = AAZListType(
                serialized_name="inboundIpRules",
            )
            properties.is_zone_redundant = AAZBoolType(
                serialized_name="isZoneRedundant",
            )
            properties.minimum_tls_version_allowed = AAZStrType(
                serialized_name="minimumTlsVersionAllowed",
            )
            properties.private_endpoint_connections = AAZListType(
                serialized_name="privateEndpointConnections",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_network_access = AAZStrType(
                serialized_name="publicNetworkAccess",
            )
            properties.topic_spaces_configuration = AAZObjectType(
                serialized_name="topicSpacesConfiguration",
            )
            properties.topics_configuration = AAZObjectType(
                serialized_name="topicsConfiguration",
            )

            inbound_ip_rules = cls._schema_on_200.value.Element.properties.inbound_ip_rules
            inbound_ip_rules.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.inbound_ip_rules.Element
            _element.action = AAZStrType()
            _element.ip_mask = AAZStrType(
                serialized_name="ipMask",
            )

            private_endpoint_connections = cls._schema_on_200.value.Element.properties.private_endpoint_connections
            private_endpoint_connections.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties
            properties.group_ids = AAZListType(
                serialized_name="groupIds",
            )
            properties.private_endpoint = AAZObjectType(
                serialized_name="privateEndpoint",
            )
            properties.private_link_service_connection_state = AAZObjectType(
                serialized_name="privateLinkServiceConnectionState",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )

            group_ids = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties.group_ids
            group_ids.Element = AAZStrType()

            private_endpoint = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties.private_endpoint
            private_endpoint.id = AAZStrType()

            private_link_service_connection_state = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties.private_link_service_connection_state
            private_link_service_connection_state.actions_required = AAZStrType(
                serialized_name="actionsRequired",
            )
            private_link_service_connection_state.description = AAZStrType()
            private_link_service_connection_state.status = AAZStrType()

            topic_spaces_configuration = cls._schema_on_200.value.Element.properties.topic_spaces_configuration
            topic_spaces_configuration.client_authentication = AAZObjectType(
                serialized_name="clientAuthentication",
            )
            topic_spaces_configuration.hostname = AAZStrType(
                flags={"read_only": True},
            )
            topic_spaces_configuration.maximum_client_sessions_per_authentication_name = AAZIntType(
                serialized_name="maximumClientSessionsPerAuthenticationName",
            )
            topic_spaces_configuration.maximum_session_expiry_in_hours = AAZIntType(
                serialized_name="maximumSessionExpiryInHours",
            )
            topic_spaces_configuration.route_topic_resource_id = AAZStrType(
                serialized_name="routeTopicResourceId",
            )
            topic_spaces_configuration.routing_enrichments = AAZObjectType(
                serialized_name="routingEnrichments",
            )
            topic_spaces_configuration.routing_identity_info = AAZObjectType(
                serialized_name="routingIdentityInfo",
            )
            topic_spaces_configuration.state = AAZStrType()

            client_authentication = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.client_authentication
            client_authentication.alternative_authentication_name_sources = AAZListType(
                serialized_name="alternativeAuthenticationNameSources",
            )

            alternative_authentication_name_sources = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.client_authentication.alternative_authentication_name_sources
            alternative_authentication_name_sources.Element = AAZStrType()

            routing_enrichments = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.routing_enrichments
            routing_enrichments.dynamic = AAZListType()
            routing_enrichments.static = AAZListType()

            dynamic = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.routing_enrichments.dynamic
            dynamic.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.routing_enrichments.dynamic.Element
            _element.key = AAZStrType()
            _element.value = AAZStrType()

            static = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.routing_enrichments.static
            static.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.routing_enrichments.static.Element
            _element.key = AAZStrType()
            _element.value_type = AAZStrType(
                serialized_name="valueType",
            )

            routing_identity_info = cls._schema_on_200.value.Element.properties.topic_spaces_configuration.routing_identity_info
            routing_identity_info.type = AAZStrType()
            routing_identity_info.user_assigned_identity = AAZStrType(
                serialized_name="userAssignedIdentity",
            )

            topics_configuration = cls._schema_on_200.value.Element.properties.topics_configuration
            topics_configuration.hostname = AAZStrType(
                flags={"read_only": True},
            )

            sku = cls._schema_on_200.value.Element.sku
            sku.capacity = AAZIntType()
            sku.name = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
