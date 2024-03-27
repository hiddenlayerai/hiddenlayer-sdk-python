# coding: utf-8

"""
    HiddenLayer ModelScan

    HiddenLayer ModelScan API for scanning of models

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.rest.models.model_query_response import ModelQueryResponse

class TestModelQueryResponse(unittest.TestCase):
    """ModelQueryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelQueryResponse:
        """Test ModelQueryResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelQueryResponse`
        """
        model = ModelQueryResponse()
        if include_optional:
            return ModelQueryResponse(
                total_count = 56,
                page_size = 56,
                page_number = 56,
                results = [
                    null
                    ]
            )
        else:
            return ModelQueryResponse(
                total_count = 56,
                page_size = 56,
                page_number = 56,
                results = [
                    null
                    ],
        )
        """

    def testModelQueryResponse(self):
        """Test ModelQueryResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()