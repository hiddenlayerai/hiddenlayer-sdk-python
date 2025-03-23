# coding: utf-8

"""
    HiddenLayer Sensor SOR

    HiddenLayer Sensor SOR API for operations to sensor data storage

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.problem_details import ProblemDetails

class TestProblemDetails(unittest.TestCase):
    """ProblemDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProblemDetails:
        """Test ProblemDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProblemDetails`
        """
        model = ProblemDetails()
        if include_optional:
            return ProblemDetails(
                type = 'https://example.net/validation-error',
                title = 'Your request is not valid',
                detail = '',
                instance = '',
                errors = [
                    hiddenlayer.sdk.rest.models.errors_inner.Errors_inner(
                        code = '', 
                        detail = '', 
                        pointer = [
                            ''
                            ], )
                    ]
            )
        else:
            return ProblemDetails(
                errors = [
                    hiddenlayer.sdk.rest.models.errors_inner.Errors_inner(
                        code = '', 
                        detail = '', 
                        pointer = [
                            ''
                            ], )
                    ],
        )
        """

    def testProblemDetails(self):
        """Test ProblemDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
