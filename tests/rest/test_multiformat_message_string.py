# coding: utf-8

"""
    HiddenLayer-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.multiformat_message_string import MultiformatMessageString

class TestMultiformatMessageString(unittest.TestCase):
    """MultiformatMessageString unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MultiformatMessageString:
        """Test MultiformatMessageString
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MultiformatMessageString`
        """
        model = MultiformatMessageString()
        if include_optional:
            return MultiformatMessageString(
                text = '',
                markdown = '',
                properties = { }
            )
        else:
            return MultiformatMessageString(
                text = '',
        )
        """

    def testMultiformatMessageString(self):
        """Test MultiformatMessageString"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
