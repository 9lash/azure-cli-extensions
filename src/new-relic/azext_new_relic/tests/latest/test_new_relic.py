# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)


class NewRelicScenario(ScenarioTest):

    @AllowLargeResponse(size_kb=10240)
    @ResourceGroupPreparer(name_prefix='cli_test_new_relic_monitor')
    def test_new_relic_monitor(self, resource_group):
        self.kwargs.update({
            'new_relic_monitor_name': 'test-new-relic-monitor',
            'user_email': 'dipeshbhakat@microsoft.com',
            'loc': 'eastus'
        })

        self.cmd('az new-relic monitor create '
                 '--resource-group {rg} '
                 '--name {new_relic_monitor_name} '
                 '--location {loc} '
                 '--user-info {{"first-name":"Dipesh","last-name":"Bhakat","email-address":{user_email},"phone-number":"123456"}} '
                 '--plan-data {{"billing-cycle":"MONTHLY","effective-date":"\'2023-10-25T15:14:33+02:00\'","plan-details":"newrelic-pay-as-you-go-free-live@TIDgmz7xq9ge3py@PUBIDnewrelicinc1635200720692.newrelic_liftr_payg","usage-type":"PAYG"}} '
                 '--account-creation-source "LIFTR" '
                 '--org-creation-source "LIFTR" '
                 '--tags {{"key6976":"oaxfhf"}}',
                 checks=[self.check('name', '{new_relic_monitor_name}'),
                         self.check('accountCreationSource', 'LIFTR'),
                         self.check('orgCreationSource', 'LIFTR'),
                         self.check('location', '{loc}'),
                         self.check('planData.billingCycle', 'MONTHLY'),
                         self.check('planData.effectiveDate', '2023-10-25T13:14:33Z'),
                         self.check('planData.planDetails', 'newrelic-pay-as-you-go-free-live@TIDgmz7xq9ge3py@PUBIDnewrelicinc1635200720692.newrelic_liftr_payg'),
                         self.check('planData.usageType', 'PAYG'),
                         self.check('userInfo.emailAddress', '{user_email}'),
                         self.check('userInfo.firstName', 'Dipesh'),
                         self.check('userInfo.lastName', 'Bhakat'),
                         self.check('userInfo.phoneNumber', '123456'),
                         self.check('tags.key6976', 'oaxfhf')])

        self.cmd('az new-relic monitor tag-rule create --resource-group {rg} --monitor-name {new_relic_monitor_name} --name default '
                 '--log-rules {{"send-aad-logs":"Enabled","send-subscription-logs":"Enabled","send-activity-logs":"Enabled","filtering-tags":[]}} '
                 '--metric-rules {{"user-email":"{user_email}","filtering-tags":[{{"name":"Environment","value":"Prod","action":"Include"}}]}}',
                 checks=[self.check('name', 'default'),
                         self.check('logRules.sendAadLogs', 'Enabled'),
                         self.check('logRules.sendActivityLogs', 'Enabled'),
                         self.check('logRules.sendSubscriptionLogs', 'Enabled'),
                         self.check('metricRules.filteringTags[0].action', 'Include'),
                         self.check('metricRules.filteringTags[0].name', 'Environment'),
                         self.check('metricRules.filteringTags[0].value', 'Prod')])
        self.cmd('az new-relic monitor tag-rule update --resource-group {rg} --monitor-name {new_relic_monitor_name} --name default '
                 '--log-rules {{"send-aad-logs":"Enabled","send-subscription-logs":"Enabled","send-activity-logs":"Disabled","filtering-tags":[]}}',
                 self.check('logRules.sendActivityLogs', 'Disabled'))
        self.cmd('az new-relic monitor tag-rule list --resource-group {rg} --monitor-name {new_relic_monitor_name}',
                 self.check('length(@)', 1))
        self.cmd('az new-relic monitor tag-rule show --resource-group {rg} --monitor-name {new_relic_monitor_name} --name default',
                 checks=[self.check('name', 'default'),
                         self.check('length(metricRules.filteringTags)', 1),
                         self.check('length(logRules.filteringTags)', 0)])
        self.cmd('az new-relic monitor get-metric-rule --monitor-name {new_relic_monitor_name} --resource-group {rg} --user-email {user_email}',
                 checks=[self.check('length(filteringTags)', 0),
                         self.check('sendMetrics', 'Disabled')])
        self.cmd('az new-relic monitor monitored-subscription create --resource-group {rg} --monitor-name {new_relic_monitor_name} --configuration-name default --patch-operation AddBegin --subscriptions [{{subscription-id:"8503bb5b-d6ad-4293-bf3d-c996bf639d9b",status:"InProgress"}}]')
        self.cmd('az new-relic monitor monitored-subscription create --resource-group {rg} --monitor-name {new_relic_monitor_name} --configuration-name default --patch-operation AddComplete --subscriptions [{{status:"Active",subscription-id:"8503bb5b-d6ad-4293-bf3d-c996bf639d9b"}}]',
                 checks=[self.check('name', 'default'),
                         self.check('length(properties.monitoredSubscriptionList)', 1),
                         self.check('properties.monitoredSubscriptionList[0].subscriptionId', '8503bb5b-d6ad-4293-bf3d-c996bf639d9b'),
                         self.check('properties.monitoredSubscriptionList[0].status', 'Active')])
        self.cmd('az new-relic monitor monitored-subscription show --resource-group {rg} --monitor-name {new_relic_monitor_name} --configuration-name default',
                 self.check('name', 'default'))
        self.cmd('az new-relic monitor monitored-subscription update --resource-group {rg} --monitor-name {new_relic_monitor_name} --configuration-name default --patch-operation AddBegin --subscriptions [{{subscription-id:"8503bb5b-d6ad-4293-bf3d-c996bf639d9b",status:"InProgress"}}]')
        self.cmd('az new-relic monitor monitored-subscription update --resource-group {rg} --monitor-name {new_relic_monitor_name} --configuration-name default --patch-operation AddComplete --subscriptions [{{status:"Active",subscription-id:"8503bb5b-d6ad-4293-bf3d-c996bf639d9b"}}]',
                 checks=[self.check('name', 'default'),
                         self.check('length(properties.monitoredSubscriptionList)', 1),
                         self.check('properties.monitoredSubscriptionList[0].subscriptionId', '8503bb5b-d6ad-4293-bf3d-c996bf639d9b'),
                         self.check('properties.monitoredSubscriptionList[0].status', 'Active')])
        self.cmd('az new-relic monitor get-metric-statu --resource-group {rg} --monitor-name {new_relic_monitor_name} --user-email {user_email} --azure-resource-ids abcdefg',
                 self.check('length(azureResourceIds)', 0))
        self.cmd('az new-relic monitor list', self.check('type(@)', 'array'))
        self.cmd('az new-relic monitor list-app-service --resource-group {rg} --monitor-name {new_relic_monitor_name} --user-email {user_email} --azure-resource-ids abcdefg',
                 self.check('type(@)', 'array'))
        self.cmd('az new-relic monitor list-host --resource-group {rg} --monitor-name {new_relic_monitor_name} --user-email {user_email} --vm-ids test-vm',
                 self.check('type(@)', 'array'))
        self.cmd('az new-relic monitor monitored-resource --monitor-name {new_relic_monitor_name} --resource-group {rg}',
                 self.check('type(@)', 'array'))
        self.cmd('az new-relic monitor list-linked-resource --monitor-name {new_relic_monitor_name} --resource-group {rg}',
                 self.check('type(@)', 'array'))
        self.cmd('az new-relic monitor list-connected-partner-resource --monitor-name {new_relic_monitor_name} --resource-group {rg}',
                 self.check('type(@)', 'array'))
        self.cmd('az new-relic monitor get-billing-info --monitor-name {new_relic_monitor_name} --resource-group {rg}',
                 self.check('length(marketplaceSaasInfo)', 5))
        self.cmd('az new-relic monitor show --resource-group {rg} --monitor-name {new_relic_monitor_name}',
                 self.check('name', '{new_relic_monitor_name}'))
        self.cmd('az new-relic monitor vm-host-payload --monitor-name {new_relic_monitor_name} --resource-group {rg}',
                 self.check('length(@)', 1))
        self.cmd('az new-relic account list --location {loc} --user-email rheahooda@microsoft.com',
                 self.check('type(@)', 'array'))
        self.cmd('az new-relic organization list --location {loc} --user-email rheahooda@microsoft.com',
                 self.check('type(@)', 'array'))
        self.cmd('az new-relic plan list --account-id test-account --organization-id test-organization',
                 self.check('type(@)', 'array'))
        self.cmd('az new-relic monitor monitored-subscription delete --resource-group {rg} --monitor-name {new_relic_monitor_name} --configuration-name default')
        self.cmd('az new-relic monitor tag-rule delete --resource-group {rg} --monitor-name {new_relic_monitor_name} --name default')
        self.cmd('az new-relic monitor delete --resource-group {rg} --monitor-name {new_relic_monitor_name} --user-email {user_email}')
