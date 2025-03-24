# coding: utf-8

"""
    HiddenLayer-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.edge import Edge

class TestEdge(unittest.TestCase):
    """Edge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Edge:
        """Test Edge
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Edge`
        """
        model = Edge()
        if include_optional:
            return Edge(
                id = '',
                label = hiddenlayer.sdk.rest.models.message.message(
                    text = '', 
                    markdown = '', 
                    id = '', 
                    arguments = [
                        ''
                        ], 
                    properties = { }, ),
                source_node_id = '',
                target_node_id = '',
                properties = { }
            )
        else:
            return Edge(
                id = '',
                source_node_id = '',
                target_node_id = '',
        )
        """

    def testEdge(self):
        """Test Edge"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
