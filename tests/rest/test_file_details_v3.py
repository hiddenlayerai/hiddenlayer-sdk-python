# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.file_details_v3 import FileDetailsV3

class TestFileDetailsV3(unittest.TestCase):
    """FileDetailsV3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileDetailsV3:
        """Test FileDetailsV3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileDetailsV3`
        """
        model = FileDetailsV3()
        if include_optional:
            return FileDetailsV3(
                estimated_time = '',
                md5 = 'ce114e4501d2f4e2dcea3e17b546f339',
                sha256 = 'a54d88e06612d820bc3be72877c74f257b561b19',
                tlsh = 'T1C50757F93C74D00C05B70C0793A1D5A9DF3F6D3A2F7AD940F3BFBF07B3BDF5A1D293',
                file_size = '9 GB',
                file_size_bytes = 9663676416,
                file_type = 'safetensors',
                file_type_details = { }
            )
        else:
            return FileDetailsV3(
                estimated_time = '',
                sha256 = 'a54d88e06612d820bc3be72877c74f257b561b19',
                file_type = 'safetensors',
        )
        """

    def testFileDetailsV3(self):
        """Test FileDetailsV3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
