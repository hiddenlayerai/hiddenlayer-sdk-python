# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.pagination_v3 import PaginationV3

class TestPaginationV3(unittest.TestCase):
    """PaginationV3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginationV3:
        """Test PaginationV3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginationV3`
        """
        model = PaginationV3()
        if include_optional:
            return PaginationV3(
                var_self = '',
                first = '',
                prev = '',
                next = '',
                last = ''
            )
        else:
            return PaginationV3(
                var_self = '',
                first = '',
                prev = '',
                next = '',
                last = '',
        )
        """

    def testPaginationV3(self):
        """Test PaginationV3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
