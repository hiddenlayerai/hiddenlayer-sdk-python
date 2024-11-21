# coding: utf-8

"""
    HiddenLayer ModelScan V2

    HiddenLayer ModelScan API for scanning of models

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.location_relationship import LocationRelationship

class TestLocationRelationship(unittest.TestCase):
    """LocationRelationship unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LocationRelationship:
        """Test LocationRelationship
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LocationRelationship`
        """
        model = LocationRelationship()
        if include_optional:
            return LocationRelationship(
                target = 0,
                kinds = [
                    ''
                    ],
                description = hiddenlayer.sdk.rest.models.message.message(
                    text = '', 
                    markdown = '', 
                    id = '', 
                    arguments = [
                        ''
                        ], 
                    properties = { }, ),
                properties = { }
            )
        else:
            return LocationRelationship(
                target = 0,
        )
        """

    def testLocationRelationship(self):
        """Test LocationRelationship"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
