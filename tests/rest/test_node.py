# coding: utf-8

"""
    HiddenLayer ModelScan V2

    HiddenLayer ModelScan API for scanning of models

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.node import Node

class TestNode(unittest.TestCase):
    """Node unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Node:
        """Test Node
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Node`
        """
        model = Node()
        if include_optional:
            return Node(
                id = '',
                label = hiddenlayer.sdk.rest.models.message.message(
                    text = '', 
                    markdown = '', 
                    id = '', 
                    arguments = [
                        ''
                        ], 
                    properties = { }, ),
                location = hiddenlayer.sdk.rest.models.location.location(
                    id = -1, 
                    physical_location = hiddenlayer.sdk.rest.models.physical_location.physicalLocation(
                        address = hiddenlayer.sdk.rest.models.address.address(
                            absolute_address = -1, 
                            relative_address = 56, 
                            length = 56, 
                            kind = '', 
                            name = '', 
                            fully_qualified_name = '', 
                            offset_from_parent = 56, 
                            index = -1, 
                            parent_index = -1, 
                            properties = { }, ), 
                        artifact_location = hiddenlayer.sdk.rest.models.artifact_location.artifactLocation(
                            uri = '', 
                            uri_base_id = '', 
                            index = -1, 
                            description = hiddenlayer.sdk.rest.models.message.message(
                                text = '', 
                                markdown = '', 
                                id = '', 
                                arguments = [
                                    ''
                                    ], ), ), 
                        region = hiddenlayer.sdk.rest.models.region.region(
                            start_line = 1, 
                            start_column = 1, 
                            end_line = 1, 
                            end_column = 1, 
                            char_offset = -1, 
                            char_length = 0, 
                            byte_offset = -1, 
                            byte_length = 0, 
                            snippet = hiddenlayer.sdk.rest.models.artifact_content.artifactContent(
                                text = '', 
                                binary = '', 
                                rendered = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                                    text = '', 
                                    markdown = '', ), ), 
                            source_language = '', ), 
                        context_region = hiddenlayer.sdk.rest.models.region.region(
                            start_line = 1, 
                            start_column = 1, 
                            end_line = 1, 
                            end_column = 1, 
                            char_offset = -1, 
                            char_length = 0, 
                            byte_offset = -1, 
                            byte_length = 0, 
                            source_language = '', ), 
                        properties = { }, ), 
                    logical_locations = [
                        hiddenlayer.sdk.rest.models.logical_location.logicalLocation(
                            name = '', 
                            index = -1, 
                            fully_qualified_name = '', 
                            decorated_name = '', 
                            parent_index = -1, 
                            kind = '', )
                        ], 
                    message = hiddenlayer.sdk.rest.models.message.message(
                        text = '', 
                        markdown = '', 
                        id = '', ), 
                    annotations = [
                        
                        ], 
                    relationships = [
                        hiddenlayer.sdk.rest.models.location_relationship.locationRelationship(
                            target = 0, 
                            kinds = [
                                ''
                                ], )
                        ], 
                    properties = , ),
                children = [
                    hiddenlayer.sdk.rest.models.node.node(
                        id = '', 
                        label = hiddenlayer.sdk.rest.models.message.message(
                            text = '', 
                            markdown = '', 
                            id = '', 
                            arguments = [
                                ''
                                ], 
                            properties = { }, ), 
                        location = hiddenlayer.sdk.rest.models.location.location(
                            id = -1, 
                            physical_location = hiddenlayer.sdk.rest.models.physical_location.physicalLocation(
                                address = hiddenlayer.sdk.rest.models.address.address(
                                    absolute_address = -1, 
                                    relative_address = 56, 
                                    length = 56, 
                                    kind = '', 
                                    name = '', 
                                    fully_qualified_name = '', 
                                    offset_from_parent = 56, 
                                    index = -1, 
                                    parent_index = -1, ), 
                                artifact_location = hiddenlayer.sdk.rest.models.artifact_location.artifactLocation(
                                    uri = '', 
                                    uri_base_id = '', 
                                    index = -1, 
                                    description = hiddenlayer.sdk.rest.models.message.message(
                                        text = '', 
                                        markdown = '', 
                                        id = '', ), ), 
                                region = hiddenlayer.sdk.rest.models.region.region(
                                    start_line = 1, 
                                    start_column = 1, 
                                    end_line = 1, 
                                    end_column = 1, 
                                    char_offset = -1, 
                                    char_length = 0, 
                                    byte_offset = -1, 
                                    byte_length = 0, 
                                    snippet = hiddenlayer.sdk.rest.models.artifact_content.artifactContent(
                                        text = '', 
                                        binary = '', 
                                        rendered = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                                            text = '', 
                                            markdown = '', ), ), 
                                    source_language = '', ), 
                                context_region = hiddenlayer.sdk.rest.models.region.region(
                                    start_line = 1, 
                                    start_column = 1, 
                                    end_line = 1, 
                                    end_column = 1, 
                                    char_offset = -1, 
                                    char_length = 0, 
                                    byte_offset = -1, 
                                    byte_length = 0, 
                                    source_language = '', ), ), 
                            logical_locations = [
                                hiddenlayer.sdk.rest.models.logical_location.logicalLocation(
                                    name = '', 
                                    index = -1, 
                                    fully_qualified_name = '', 
                                    decorated_name = '', 
                                    parent_index = -1, 
                                    kind = '', )
                                ], 
                            annotations = [
                                
                                ], 
                            relationships = [
                                hiddenlayer.sdk.rest.models.location_relationship.locationRelationship(
                                    target = 0, 
                                    kinds = [
                                        ''
                                        ], )
                                ], ), 
                        properties = { }, )
                    ],
                properties = { }
            )
        else:
            return Node(
                id = '',
        )
        """

    def testNode(self):
        """Test Node"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
