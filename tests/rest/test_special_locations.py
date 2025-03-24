# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.special_locations import SpecialLocations

class TestSpecialLocations(unittest.TestCase):
    """SpecialLocations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpecialLocations:
        """Test SpecialLocations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpecialLocations`
        """
        model = SpecialLocations()
        if include_optional:
            return SpecialLocations(
                display_base = hiddenlayer.sdk.rest.models.artifact_location.artifactLocation(
                    uri = '', 
                    uri_base_id = '', 
                    index = -1, 
                    description = hiddenlayer.sdk.rest.models.message.message(
                        text = '', 
                        markdown = '', 
                        id = '', 
                        arguments = [
                            ''
                            ], 
                        properties = { }, ), 
                    properties = { }, ),
                properties = { }
            )
        else:
            return SpecialLocations(
        )
        """

    def testSpecialLocations(self):
        """Test SpecialLocations"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
