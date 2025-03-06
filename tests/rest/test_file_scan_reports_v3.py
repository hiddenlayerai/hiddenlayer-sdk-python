# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.file_scan_reports_v3 import FileScanReportsV3

class TestFileScanReportsV3(unittest.TestCase):
    """FileScanReportsV3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileScanReportsV3:
        """Test FileScanReportsV3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileScanReportsV3`
        """
        model = FileScanReportsV3()
        if include_optional:
            return FileScanReportsV3(
                file_results = [
                    hiddenlayer.sdk.rest.models.file_scan_report_v3.FileScanReportV3(
                        file_instance_id = '', 
                        file_location = '', 
                        start_time = '2024-10-16T23:38:32.278Z', 
                        end_time = '2024-10-16T23:38:32.354Z', 
                        details = hiddenlayer.sdk.rest.models.file_details_v3.FileDetailsV3(
                            estimated_time = '', 
                            md5 = 'ce114e4501d2f4e2dcea3e17b546f339', 
                            sha256 = 'a54d88e06612d820bc3be72877c74f257b561b19', 
                            tlsh = 'T1C50757F93C74D00C05B70C0793A1D5A9DF3F6D3A2F7AD940F3BFBF07B3BDF5A1D293', 
                            file_size = '9 GB', 
                            file_size_bytes = 9663676416, 
                            file_type = 'safetensors', 
                            file_type_details = { }, ), 
                        status = 'skipped', 
                        seen = '2024-10-22T17:59:12.431Z', 
                        detections = [
                            hiddenlayer.sdk.rest.models.scan_detection_v3.ScanDetectionV3(
                                description = 'Found lambda embedded in keras model allowing custom layers that support  arbitrary expression execution', 
                                risk = 'MALICIOUS', 
                                severity = 'low', 
                                detection_id = '00000000-0000-0000-0000-000000000000', 
                                impact = 'critical', 
                                likelihood = 'medium', 
                                rule_details = [
                                    hiddenlayer.sdk.rest.models.rule_details_inner.Rule_Details_inner(
                                        status = 'created', 
                                        status_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        description = '', )
                                    ], 
                                rule_id = 'PICKLE_0055_202408', 
                                category = 'Arbitrary Code Execution', 
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
                                technical_blog_href = '', )
                            ], 
                        file_results = [
                            hiddenlayer.sdk.rest.models.file_scan_report_v3.FileScanReportV3(
                                file_instance_id = '', 
                                file_location = '', 
                                start_time = '2024-10-16T23:38:32.278Z', 
                                end_time = '2024-10-16T23:38:32.354Z', 
                                details = hiddenlayer.sdk.rest.models.file_details_v3.FileDetailsV3(
                                    estimated_time = '', 
                                    md5 = 'ce114e4501d2f4e2dcea3e17b546f339', 
                                    sha256 = 'a54d88e06612d820bc3be72877c74f257b561b19', 
                                    tlsh = 'T1C50757F93C74D00C05B70C0793A1D5A9DF3F6D3A2F7AD940F3BFBF07B3BDF5A1D293', 
                                    file_size = '9 GB', 
                                    file_size_bytes = 9663676416, 
                                    file_type = 'safetensors', 
                                    file_type_details = { }, ), 
                                status = 'skipped', 
                                seen = '2024-10-22T17:59:12.431Z', 
                                detections = [
                                    hiddenlayer.sdk.rest.models.scan_detection_v3.ScanDetectionV3(
                                        description = 'Found lambda embedded in keras model allowing custom layers that support  arbitrary expression execution', 
                                        risk = 'MALICIOUS', 
                                        severity = 'low', 
                                        detection_id = '00000000-0000-0000-0000-000000000000', 
                                        impact = 'critical', 
                                        likelihood = 'medium', 
                                        rule_details = [
                                            hiddenlayer.sdk.rest.models.rule_details_inner.Rule_Details_inner(
                                                status = 'created', 
                                                status_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                description = '', )
                                            ], 
                                        rule_id = 'PICKLE_0055_202408', 
                                        category = 'Arbitrary Code Execution', 
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
                                        technical_blog_href = '', )
                                    ], 
                                file_results = , )
                            ], )
                    ]
            )
        else:
            return FileScanReportsV3(
        )
        """

    def testFileScanReportsV3(self):
        """Test FileScanReportsV3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
