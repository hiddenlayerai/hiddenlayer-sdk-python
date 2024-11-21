# coding: utf-8

"""
    HiddenLayer ModelScan V2

    HiddenLayer ModelScan API for scanning of models

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.web_request import WebRequest

class TestWebRequest(unittest.TestCase):
    """WebRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebRequest:
        """Test WebRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebRequest`
        """
        model = WebRequest()
        if include_optional:
            return WebRequest(
                index = -1,
                protocol = '',
                version = '',
                target = '',
                method = '',
                headers = {
                    'key' : ''
                    },
                parameters = {
                    'key' : ''
                    },
                body = hiddenlayer.sdk.rest.models.artifact_content.artifactContent(
                    text = '', 
                    binary = '', 
                    rendered = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                        text = '', 
                        markdown = '', 
                        properties = { }, ), 
                    properties = { }, ),
                properties = { }
            )
        else:
            return WebRequest(
        )
        """

    def testWebRequest(self):
        """Test WebRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
