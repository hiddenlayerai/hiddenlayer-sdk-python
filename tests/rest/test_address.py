# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.address import Address

class TestAddress(unittest.TestCase):
    """Address unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Address:
        """Test Address
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Address`
        """
        model = Address()
        if include_optional:
            return Address(
                absolute_address = -1,
                relative_address = 56,
                length = 56,
                kind = '',
                name = '',
                fully_qualified_name = '',
                offset_from_parent = 56,
                index = -1,
                parent_index = -1,
                properties = { }
            )
        else:
            return Address(
        )
        """

    def testAddress(self):
        """Test Address"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
