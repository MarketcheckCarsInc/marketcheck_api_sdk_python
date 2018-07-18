# coding: utf-8

"""
    Marketcheck Cars API

    <b>Access the New, Used and Certified cars inventories for all Car Dealers in US.</b> <br/>The data is sourced from online listings by over 44,000 Car dealers in US. At any time, there are about 6.2M searchable listings (about 1.9M unique VINs) for Used & Certified cars and about 6.6M (about 3.9M unique VINs) New Car listings from all over US. We use this API at the back for our website <a href='https://www.marketcheck.com' target='_blank'>www.marketcheck.com</a> and our Android and iOS mobile apps too.<br/><h5> Few useful links : </h5><ul><li>A quick view of the API and the use cases is depicated <a href='https://portals.marketcheck.com/mcapi/' target='_blank'>here</a></li><li>The Postman collection with various usages of the API is shared here https://www.getpostman.com/collections/2752684ff636cdd7bac2</li></ul>  # noqa: E501

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from marketcheck_api_sdk.models.depreciation_stats import DepreciationStats  # noqa: F401,E501


class DepreciationPoint(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'similar_models': 'list[DepreciationStats]'
    }

    attribute_map = {
        'similar_models': 'similar_models'
    }

    def __init__(self, similar_models=None):  # noqa: E501
        """DepreciationPoint - a model defined in Swagger"""  # noqa: E501

        self._similar_models = None
        self.discriminator = None

        if similar_models is not None:
            self.similar_models = similar_models

    @property
    def similar_models(self):
        """Gets the similar_models of this DepreciationPoint.  # noqa: E501


        :return: The similar_models of this DepreciationPoint.  # noqa: E501
        :rtype: list[DepreciationStats]
        """
        return self._similar_models

    @similar_models.setter
    def similar_models(self, similar_models):
        """Sets the similar_models of this DepreciationPoint.


        :param similar_models: The similar_models of this DepreciationPoint.  # noqa: E501
        :type: list[DepreciationStats]
        """

        self._similar_models = similar_models

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DepreciationPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other