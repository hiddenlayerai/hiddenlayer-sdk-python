# coding: utf-8

"""
    HiddenLayer-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.errors_inner import ErrorsInner

class TestErrorsInner(unittest.TestCase):
    """ErrorsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorsInner:
        """Test ErrorsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorsInner`
        """
        model = ErrorsInner()
        if include_optional:
            return ErrorsInner(
                code = '',
                detail = '',
                pointer = [
                    ''
                    ]
            )
        else:
            return ErrorsInner(
        )
        """

    def testErrorsInner(self):
        """Test ErrorsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
