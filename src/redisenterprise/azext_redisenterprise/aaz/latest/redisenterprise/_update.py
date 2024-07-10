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
    "redisenterprise update",
)
class Update(AAZCommand):
    """Update an existing (overwrite/recreate, with potential downtime) cache cluster
    """

    _aaz_info = {
        "version": "2023-03-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.cache/redisenterprise/{}", "2023-03-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_name = AAZStrArg(
            options=["-n", "--name", "--cluster-name"],
            help="The name of the RedisEnterprise cluster.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Encryption"

        _args_schema = cls._args_schema
        _args_schema.key_encryption_key_url = AAZStrArg(
            options=["--key-encryption-key-url"],
            arg_group="Encryption",
            help="Key encryption key Url, versioned only. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78",
            nullable=True,
        )

        # define Arg Group "Identity"

        _args_schema = cls._args_schema
        _args_schema.identity_type = AAZStrArg(
            options=["--identity-type"],
            arg_group="Identity",
            help="Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).",
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned, UserAssigned": "SystemAssigned, UserAssigned", "UserAssigned": "UserAssigned"},
        )
        _args_schema.user_assigned_identities = AAZDictArg(
            options=["--assigned-identities", "--user-assigned-identities"],
            arg_group="Identity",
            help="The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.",
            nullable=True,
        )

        user_assigned_identities = cls._args_schema.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            nullable=True,
            blank={},
        )

        # define Arg Group "KeyEncryptionKeyIdentity"

        _args_schema = cls._args_schema
        _args_schema.key_encryption_identity_type = AAZStrArg(
            options=["--key-identity-type", "--key-encryption-identity-type"],
            arg_group="KeyEncryptionKeyIdentity",
            help="Only userAssignedIdentity is supported in this API version; other types may be supported in the future",
            nullable=True,
            enum={"systemAssignedIdentity": "systemAssignedIdentity", "userAssignedIdentity": "userAssignedIdentity"},
        )
        _args_schema.user_assigned_identity_resource_id = AAZStrArg(
            options=["--identity-resource-id", "--user-assigned-identity-resource-id"],
            arg_group="KeyEncryptionKeyIdentity",
            help="User assigned identity to use for accessing key encryption key Url. Ex: /subscriptions/<sub uuid>/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId.",
            nullable=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Resource tags.",
            nullable=True,
        )
        _args_schema.zones = AAZListArg(
            options=["--zones"],
            arg_group="Parameters",
            help="The Availability Zones where this cluster will be deployed.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        zones = cls._args_schema.zones
        zones.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.minimum_tls_version = AAZStrArg(
            options=["--minimum-tls-version"],
            arg_group="Properties",
            help="The minimum TLS version for the cluster to support, e.g. '1.2'",
            nullable=True,
            enum={"1.0": "1.0", "1.1": "1.1", "1.2": "1.2"},
        )

        # define Arg Group "Sku"

        _args_schema = cls._args_schema
        _args_schema.capacity = AAZIntArg(
            options=["--capacity"],
            arg_group="Sku",
            help="The size of the RedisEnterprise cluster. Defaults to 2 or 3 depending on SKU. Valid values are (2, 4, 6, ...) for Enterprise SKUs and (3, 9, 15, ...) for Flash SKUs.",
            nullable=True,
        )
        _args_schema.sku = AAZStrArg(
            options=["--sku"],
            arg_group="Sku",
            help="The type of RedisEnterprise cluster to deploy. Possible values: (Enterprise_E10, EnterpriseFlash_F300 etc.)",
            enum={"EnterpriseFlash_F1500": "EnterpriseFlash_F1500", "EnterpriseFlash_F300": "EnterpriseFlash_F300", "EnterpriseFlash_F700": "EnterpriseFlash_F700", "Enterprise_E1": "Enterprise_E1", "Enterprise_E10": "Enterprise_E10", "Enterprise_E100": "Enterprise_E100", "Enterprise_E20": "Enterprise_E20", "Enterprise_E200": "Enterprise_E200", "Enterprise_E400": "Enterprise_E400", "Enterprise_E5": "Enterprise_E5", "Enterprise_E50": "Enterprise_E50"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.RedisEnterpriseGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.RedisEnterpriseCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class RedisEnterpriseGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/redisEnterprise/{clusterName}",
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
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
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
                    "api-version", "2023-03-01-preview",
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
            _UpdateHelper._build_schema_cluster_read(cls._schema_on_200)

            return cls._schema_on_200

    class RedisEnterpriseCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "original-uri"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "original-uri"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/redisEnterprise/{clusterName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
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
                    "api-version", "2023-03-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_cluster_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("identity", AAZObjectType)
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("sku", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")
            _builder.set_prop("zones", AAZListType, ".zones")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".identity_type", typ_kwargs={"flags": {"required": True}})
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("encryption", AAZObjectType)
                properties.set_prop("minimumTlsVersion", AAZStrType, ".minimum_tls_version")

            encryption = _builder.get(".properties.encryption")
            if encryption is not None:
                encryption.set_prop("customerManagedKeyEncryption", AAZObjectType)

            customer_managed_key_encryption = _builder.get(".properties.encryption.customerManagedKeyEncryption")
            if customer_managed_key_encryption is not None:
                customer_managed_key_encryption.set_prop("keyEncryptionKeyIdentity", AAZObjectType)
                customer_managed_key_encryption.set_prop("keyEncryptionKeyUrl", AAZStrType, ".key_encryption_key_url")

            key_encryption_key_identity = _builder.get(".properties.encryption.customerManagedKeyEncryption.keyEncryptionKeyIdentity")
            if key_encryption_key_identity is not None:
                key_encryption_key_identity.set_prop("identityType", AAZStrType, ".key_encryption_identity_type")
                key_encryption_key_identity.set_prop("userAssignedIdentityResourceId", AAZStrType, ".user_assigned_identity_resource_id")

            sku = _builder.get(".sku")
            if sku is not None:
                sku.set_prop("capacity", AAZIntType, ".capacity")
                sku.set_prop("name", AAZStrType, ".sku", typ_kwargs={"flags": {"required": True}})

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            zones = _builder.get(".zones")
            if zones is not None:
                zones.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_cluster_read = None

    @classmethod
    def _build_schema_cluster_read(cls, _schema):
        if cls._schema_cluster_read is not None:
            _schema.id = cls._schema_cluster_read.id
            _schema.identity = cls._schema_cluster_read.identity
            _schema.location = cls._schema_cluster_read.location
            _schema.name = cls._schema_cluster_read.name
            _schema.properties = cls._schema_cluster_read.properties
            _schema.sku = cls._schema_cluster_read.sku
            _schema.system_data = cls._schema_cluster_read.system_data
            _schema.tags = cls._schema_cluster_read.tags
            _schema.type = cls._schema_cluster_read.type
            _schema.zones = cls._schema_cluster_read.zones
            return

        cls._schema_cluster_read = _schema_cluster_read = AAZObjectType()

        cluster_read = _schema_cluster_read
        cluster_read.id = AAZStrType(
            flags={"read_only": True},
        )
        cluster_read.identity = AAZObjectType()
        cluster_read.location = AAZStrType(
            flags={"required": True},
        )
        cluster_read.name = AAZStrType(
            flags={"read_only": True},
        )
        cluster_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        cluster_read.sku = AAZObjectType(
            flags={"required": True},
        )
        cluster_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        cls._build_schema_system_data_read(cluster_read.system_data)
        cluster_read.tags = AAZDictType()
        cluster_read.type = AAZStrType(
            flags={"read_only": True},
        )
        cluster_read.zones = AAZListType()

        identity = _schema_cluster_read.identity
        identity.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )
        identity.tenant_id = AAZStrType(
            serialized_name="tenantId",
            flags={"read_only": True},
        )
        identity.type = AAZStrType(
            flags={"required": True},
        )
        identity.user_assigned_identities = AAZDictType(
            serialized_name="userAssignedIdentities",
        )

        user_assigned_identities = _schema_cluster_read.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectType()

        _element = _schema_cluster_read.identity.user_assigned_identities.Element
        _element.client_id = AAZStrType(
            serialized_name="clientId",
            flags={"read_only": True},
        )
        _element.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )

        properties = _schema_cluster_read.properties
        properties.encryption = AAZObjectType()
        properties.host_name = AAZStrType(
            serialized_name="hostName",
            flags={"read_only": True},
        )
        properties.minimum_tls_version = AAZStrType(
            serialized_name="minimumTlsVersion",
        )
        properties.private_endpoint_connections = AAZListType(
            serialized_name="privateEndpointConnections",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.redis_version = AAZStrType(
            serialized_name="redisVersion",
            flags={"read_only": True},
        )
        properties.resource_state = AAZStrType(
            serialized_name="resourceState",
            flags={"read_only": True},
        )

        encryption = _schema_cluster_read.properties.encryption
        encryption.customer_managed_key_encryption = AAZObjectType(
            serialized_name="customerManagedKeyEncryption",
        )

        customer_managed_key_encryption = _schema_cluster_read.properties.encryption.customer_managed_key_encryption
        customer_managed_key_encryption.key_encryption_key_identity = AAZObjectType(
            serialized_name="keyEncryptionKeyIdentity",
        )
        customer_managed_key_encryption.key_encryption_key_url = AAZStrType(
            serialized_name="keyEncryptionKeyUrl",
        )

        key_encryption_key_identity = _schema_cluster_read.properties.encryption.customer_managed_key_encryption.key_encryption_key_identity
        key_encryption_key_identity.identity_type = AAZStrType(
            serialized_name="identityType",
        )
        key_encryption_key_identity.user_assigned_identity_resource_id = AAZStrType(
            serialized_name="userAssignedIdentityResourceId",
        )

        private_endpoint_connections = _schema_cluster_read.properties.private_endpoint_connections
        private_endpoint_connections.Element = AAZObjectType()

        _element = _schema_cluster_read.properties.private_endpoint_connections.Element
        _element.id = AAZStrType(
            flags={"read_only": True},
        )
        _element.name = AAZStrType(
            flags={"read_only": True},
        )
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        _element.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        cls._build_schema_system_data_read(_element.system_data)
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_cluster_read.properties.private_endpoint_connections.Element.properties
        properties.private_endpoint = AAZObjectType(
            serialized_name="privateEndpoint",
        )
        properties.private_link_service_connection_state = AAZObjectType(
            serialized_name="privateLinkServiceConnectionState",
            flags={"required": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        private_endpoint = _schema_cluster_read.properties.private_endpoint_connections.Element.properties.private_endpoint
        private_endpoint.id = AAZStrType(
            flags={"read_only": True},
        )

        private_link_service_connection_state = _schema_cluster_read.properties.private_endpoint_connections.Element.properties.private_link_service_connection_state
        private_link_service_connection_state.actions_required = AAZStrType(
            serialized_name="actionsRequired",
        )
        private_link_service_connection_state.description = AAZStrType()
        private_link_service_connection_state.status = AAZStrType()

        sku = _schema_cluster_read.sku
        sku.capacity = AAZIntType()
        sku.name = AAZStrType(
            flags={"required": True},
        )

        tags = _schema_cluster_read.tags
        tags.Element = AAZStrType()

        zones = _schema_cluster_read.zones
        zones.Element = AAZStrType()

        _schema.id = cls._schema_cluster_read.id
        _schema.identity = cls._schema_cluster_read.identity
        _schema.location = cls._schema_cluster_read.location
        _schema.name = cls._schema_cluster_read.name
        _schema.properties = cls._schema_cluster_read.properties
        _schema.sku = cls._schema_cluster_read.sku
        _schema.system_data = cls._schema_cluster_read.system_data
        _schema.tags = cls._schema_cluster_read.tags
        _schema.type = cls._schema_cluster_read.type
        _schema.zones = cls._schema_cluster_read.zones

    _schema_system_data_read = None

    @classmethod
    def _build_schema_system_data_read(cls, _schema):
        if cls._schema_system_data_read is not None:
            _schema.created_at = cls._schema_system_data_read.created_at
            _schema.created_by = cls._schema_system_data_read.created_by
            _schema.created_by_type = cls._schema_system_data_read.created_by_type
            _schema.last_modified_at = cls._schema_system_data_read.last_modified_at
            _schema.last_modified_by = cls._schema_system_data_read.last_modified_by
            _schema.last_modified_by_type = cls._schema_system_data_read.last_modified_by_type
            return

        cls._schema_system_data_read = _schema_system_data_read = AAZObjectType(
            flags={"read_only": True}
        )

        system_data_read = _schema_system_data_read
        system_data_read.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data_read.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data_read.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data_read.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data_read.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data_read.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.created_at = cls._schema_system_data_read.created_at
        _schema.created_by = cls._schema_system_data_read.created_by
        _schema.created_by_type = cls._schema_system_data_read.created_by_type
        _schema.last_modified_at = cls._schema_system_data_read.last_modified_at
        _schema.last_modified_by = cls._schema_system_data_read.last_modified_by
        _schema.last_modified_by_type = cls._schema_system_data_read.last_modified_by_type


__all__ = ["Update"]
