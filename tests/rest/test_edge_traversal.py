# coding: utf-8

"""
    HiddenLayer ModelScan V2

    HiddenLayer ModelScan API for scanning of models

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.edge_traversal import EdgeTraversal

class TestEdgeTraversal(unittest.TestCase):
    """EdgeTraversal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EdgeTraversal:
        """Test EdgeTraversal
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EdgeTraversal`
        """
        model = EdgeTraversal()
        if include_optional:
            return EdgeTraversal(
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
                        markdown = '', 
                        properties = { }, )
                    },
                step_over_edge_count = 0,
                properties = { }
            )
        else:
            return EdgeTraversal(
                edge_id = '',
        )
        """

    def testEdgeTraversal(self):
        """Test EdgeTraversal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
