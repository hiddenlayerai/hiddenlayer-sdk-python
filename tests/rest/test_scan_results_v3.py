# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.scan_results_v3 import ScanResultsV3

class TestScanResultsV3(unittest.TestCase):
    """ScanResultsV3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScanResultsV3:
        """Test ScanResultsV3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScanResultsV3`
        """
        model = ScanResultsV3()
        if include_optional:
            return ScanResultsV3(
                scan_id = '',
                start_time = 56,
                end_time = 56,
                status = 'done',
                version = '',
                inventory = hiddenlayer.sdk.rest.models.inventory_v3.Inventory V3(
                    requested_scan_location = '', 
                    model_name = '', 
                    model_source = '', 
                    model_version = '', 
                    model_version_id = '', 
                    requesting_entity = '', ),
                file_results = [
                    hiddenlayer.sdk.rest.models.file_result_v3.File Result V3(
                        file_location = '', 
                        status = 'done', 
                        start_time = 56, 
                        end_time = 56, 
                        details = hiddenlayer.sdk.rest.models.file_details_v3.FileDetailsV3(
                            estimated_time = '', 
                            md5 = 'ce114e4501d2f4e2dcea3e17b546f339', 
                            sha256 = 'a54d88e06612d820bc3be72877c74f257b561b19', 
                            tlsh = 'T1C50757F93C74D00C05B70C0793A1D5A9DF3F6D3A2F7AD940F3BFBF07B3BDF5A1D293', 
                            file_size = '9 GB', 
                            file_size_bytes = 9663676416, 
                            file_type = 'safetensors', 
                            file_type_details = { }, ), 
                        seen = 56, 
                        detections = [
                            hiddenlayer.sdk.rest.models.scan_detection_v3.ScanDetectionV3(
                                detection_id = '00000000-0000-0000-0000-000000000000', 
                                rule_id = 'PICKLE_0055_202408', 
                                risk = 'MALICIOUS', 
                                category = 'Arbitrary Code Execution', 
                                description = 'Found lambda embedded in keras model allowing custom layers that support  arbitrary expression execution', 
                                likelihood = 'medium', 
                                impact = 'critical', 
                                severity = 'low', 
                                rule_details = [
                                    hiddenlayer.sdk.rest.models.rule_details_inner.Rule_Details_inner(
                                        status = 'created', 
                                        status_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        description = '', )
                                    ], 
                                mitre_atlas = [
                                    hiddenlayer.sdk.rest.models.mitre_atlas_inner.MITRE_Atlas_inner(
                                        technique = 'AML.T0480Z#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mGL,i&z5[', 
                                        tactic = 'AML.TA4807', )
                                    ], 
                                owasp = [
                                    'LLM8072'
                                    ], 
                                cve = [
                                    'CVE-0480-288800152'
                                    ], 
                                cwe = '', 
                                cwe_href = '', 
                                technical_blog_hrefs = [
                                    ''
                                    ], 
                                technical_blog_href = '', )
                            ], )
                    ]
            )
        else:
            return ScanResultsV3(
                file_results = [
                    hiddenlayer.sdk.rest.models.file_result_v3.File Result V3(
                        file_location = '', 
                        status = 'done', 
                        start_time = 56, 
                        end_time = 56, 
                        details = hiddenlayer.sdk.rest.models.file_details_v3.FileDetailsV3(
                            estimated_time = '', 
                            md5 = 'ce114e4501d2f4e2dcea3e17b546f339', 
                            sha256 = 'a54d88e06612d820bc3be72877c74f257b561b19', 
                            tlsh = 'T1C50757F93C74D00C05B70C0793A1D5A9DF3F6D3A2F7AD940F3BFBF07B3BDF5A1D293', 
                            file_size = '9 GB', 
                            file_size_bytes = 9663676416, 
                            file_type = 'safetensors', 
                            file_type_details = { }, ), 
                        seen = 56, 
                        detections = [
                            hiddenlayer.sdk.rest.models.scan_detection_v3.ScanDetectionV3(
                                detection_id = '00000000-0000-0000-0000-000000000000', 
                                rule_id = 'PICKLE_0055_202408', 
                                risk = 'MALICIOUS', 
                                category = 'Arbitrary Code Execution', 
                                description = 'Found lambda embedded in keras model allowing custom layers that support  arbitrary expression execution', 
                                likelihood = 'medium', 
                                impact = 'critical', 
                                severity = 'low', 
                                rule_details = [
                                    hiddenlayer.sdk.rest.models.rule_details_inner.Rule_Details_inner(
                                        status = 'created', 
                                        status_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        description = '', )
                                    ], 
                                mitre_atlas = [
                                    hiddenlayer.sdk.rest.models.mitre_atlas_inner.MITRE_Atlas_inner(
                                        technique = 'AML.T0480Z#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mGL,i&z5[', 
                                        tactic = 'AML.TA4807', )
                                    ], 
                                owasp = [
                                    'LLM8072'
                                    ], 
                                cve = [
                                    'CVE-0480-288800152'
                                    ], 
                                cwe = '', 
                                cwe_href = '', 
                                technical_blog_hrefs = [
                                    ''
                                    ], 
                                technical_blog_href = '', )
                            ], )
                    ],
        )
        """

    def testScanResultsV3(self):
        """Test ScanResultsV3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
