# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.web_response import WebResponse

class TestWebResponse(unittest.TestCase):
    """WebResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebResponse:
        """Test WebResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebResponse`
        """
        model = WebResponse()
        if include_optional:
            return WebResponse(
                index = -1,
                protocol = '',
                version = '',
                status_code = 56,
                reason_phrase = '',
                headers = {
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
                no_response_received = True,
                properties = { }
            )
        else:
            return WebResponse(
        )
        """

    def testWebResponse(self):
        """Test WebResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
