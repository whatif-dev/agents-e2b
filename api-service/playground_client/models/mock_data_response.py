# coding: utf-8

"""
    playground

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field
from playground_client.models.mock_data_response_body_data import MockDataResponseBodyData

class MockDataResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    body_data: MockDataResponseBodyData = Field(..., alias="bodyData")
    __properties = ["bodyData"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MockDataResponse:
        """Create an instance of MockDataResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of body_data
        if self.body_data:
            _dict['bodyData'] = self.body_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MockDataResponse:
        """Create an instance of MockDataResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MockDataResponse.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in MockDataResponse) in the input: " + obj)

        _obj = MockDataResponse.parse_obj({
            "body_data": MockDataResponseBodyData.from_dict(obj.get("bodyData")) if obj.get("bodyData") is not None else None
        })
        return _obj
