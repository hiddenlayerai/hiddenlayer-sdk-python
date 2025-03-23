# coding: utf-8

"""
    HiddenLayer Sensor SOR

    HiddenLayer Sensor SOR API for operations to sensor data storage

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.graph_traversal import GraphTraversal

class TestGraphTraversal(unittest.TestCase):
    """GraphTraversal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GraphTraversal:
        """Test GraphTraversal
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GraphTraversal`
        """
        model = GraphTraversal()
        if include_optional:
            return GraphTraversal(
                run_graph_index = -1,
                result_graph_index = -1,
                description = hiddenlayer.sdk.rest.models.message.message(
                    text = '', 
                    markdown = '', 
                    id = '', 
                    arguments = [
                        ''
                        ], 
                    properties = { }, ),
                initial_state = {
                    'key' : hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                        text = '', 
                        markdown = '', 
                        properties = { }, )
                    },
                immutable_state = {
                    'key' : hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                        text = '', 
                        markdown = '', 
                        properties = { }, )
                    },
                edge_traversals = [
                    hiddenlayer.sdk.rest.models.edge_traversal.edgeTraversal(
                        edge_id = '', 
                        message = hiddenlayer.sdk.rest.models.message.message(
                            text = '', 
                            markdown = '', 
                            id = '', 
                            arguments = [
                                ''
                                ], 
                            properties = { }, ), 
                        final_state = {
                            'key' : hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                                text = '', 
                                markdown = '', )
                            }, 
                        step_over_edge_count = 0, 
                        properties = { }, )
                    ],
                properties = { }
            )
        else:
            return GraphTraversal(
        )
        """

    def testGraphTraversal(self):
        """Test GraphTraversal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
