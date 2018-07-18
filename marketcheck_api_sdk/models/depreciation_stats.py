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


class DepreciationStats(object):
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
        'name': 'str',
        'current_value': 'float',
        'one_year_from_now': 'float',
        'one_year_from_now_percent': 'float',
        'two_year_from_now': 'float',
        'two_year_from_now_percent': 'float',
        'five_year_from_now': 'float',
        'five_year_from_now_percent': 'float'
    }

    attribute_map = {
        'name': 'name',
        'current_value': 'current_value',
        'one_year_from_now': 'one_year_from_now',
        'one_year_from_now_percent': 'one_year_from_now_percent',
        'two_year_from_now': 'two_year_from_now',
        'two_year_from_now_percent': 'two_year_from_now_percent',
        'five_year_from_now': 'five_year_from_now',
        'five_year_from_now_percent': 'five_year_from_now_percent'
    }

    def __init__(self, name=None, current_value=None, one_year_from_now=None, one_year_from_now_percent=None, two_year_from_now=None, two_year_from_now_percent=None, five_year_from_now=None, five_year_from_now_percent=None):  # noqa: E501
        """DepreciationStats - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._current_value = None
        self._one_year_from_now = None
        self._one_year_from_now_percent = None
        self._two_year_from_now = None
        self._two_year_from_now_percent = None
        self._five_year_from_now = None
        self._five_year_from_now_percent = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if current_value is not None:
            self.current_value = current_value
        if one_year_from_now is not None:
            self.one_year_from_now = one_year_from_now
        if one_year_from_now_percent is not None:
            self.one_year_from_now_percent = one_year_from_now_percent
        if two_year_from_now is not None:
            self.two_year_from_now = two_year_from_now
        if two_year_from_now_percent is not None:
            self.two_year_from_now_percent = two_year_from_now_percent
        if five_year_from_now is not None:
            self.five_year_from_now = five_year_from_now
        if five_year_from_now_percent is not None:
            self.five_year_from_now_percent = five_year_from_now_percent

    @property
    def name(self):
        """Gets the name of this DepreciationStats.  # noqa: E501

        ymm_comb_name  # noqa: E501

        :return: The name of this DepreciationStats.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DepreciationStats.

        ymm_comb_name  # noqa: E501

        :param name: The name of this DepreciationStats.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def current_value(self):
        """Gets the current_value of this DepreciationStats.  # noqa: E501

        Price of year make model combination  # noqa: E501

        :return: The current_value of this DepreciationStats.  # noqa: E501
        :rtype: float
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        """Sets the current_value of this DepreciationStats.

        Price of year make model combination  # noqa: E501

        :param current_value: The current_value of this DepreciationStats.  # noqa: E501
        :type: float
        """

        self._current_value = current_value

    @property
    def one_year_from_now(self):
        """Gets the one_year_from_now of this DepreciationStats.  # noqa: E501

        price after one year from now  # noqa: E501

        :return: The one_year_from_now of this DepreciationStats.  # noqa: E501
        :rtype: float
        """
        return self._one_year_from_now

    @one_year_from_now.setter
    def one_year_from_now(self, one_year_from_now):
        """Sets the one_year_from_now of this DepreciationStats.

        price after one year from now  # noqa: E501

        :param one_year_from_now: The one_year_from_now of this DepreciationStats.  # noqa: E501
        :type: float
        """

        self._one_year_from_now = one_year_from_now

    @property
    def one_year_from_now_percent(self):
        """Gets the one_year_from_now_percent of this DepreciationStats.  # noqa: E501

        price depreciation percent after one year from now  # noqa: E501

        :return: The one_year_from_now_percent of this DepreciationStats.  # noqa: E501
        :rtype: float
        """
        return self._one_year_from_now_percent

    @one_year_from_now_percent.setter
    def one_year_from_now_percent(self, one_year_from_now_percent):
        """Sets the one_year_from_now_percent of this DepreciationStats.

        price depreciation percent after one year from now  # noqa: E501

        :param one_year_from_now_percent: The one_year_from_now_percent of this DepreciationStats.  # noqa: E501
        :type: float
        """

        self._one_year_from_now_percent = one_year_from_now_percent

    @property
    def two_year_from_now(self):
        """Gets the two_year_from_now of this DepreciationStats.  # noqa: E501

        price after two year from now  # noqa: E501

        :return: The two_year_from_now of this DepreciationStats.  # noqa: E501
        :rtype: float
        """
        return self._two_year_from_now

    @two_year_from_now.setter
    def two_year_from_now(self, two_year_from_now):
        """Sets the two_year_from_now of this DepreciationStats.

        price after two year from now  # noqa: E501

        :param two_year_from_now: The two_year_from_now of this DepreciationStats.  # noqa: E501
        :type: float
        """

        self._two_year_from_now = two_year_from_now

    @property
    def two_year_from_now_percent(self):
        """Gets the two_year_from_now_percent of this DepreciationStats.  # noqa: E501

        price depreciation percent after two year from now  # noqa: E501

        :return: The two_year_from_now_percent of this DepreciationStats.  # noqa: E501
        :rtype: float
        """
        return self._two_year_from_now_percent

    @two_year_from_now_percent.setter
    def two_year_from_now_percent(self, two_year_from_now_percent):
        """Sets the two_year_from_now_percent of this DepreciationStats.

        price depreciation percent after two year from now  # noqa: E501

        :param two_year_from_now_percent: The two_year_from_now_percent of this DepreciationStats.  # noqa: E501
        :type: float
        """

        self._two_year_from_now_percent = two_year_from_now_percent

    @property
    def five_year_from_now(self):
        """Gets the five_year_from_now of this DepreciationStats.  # noqa: E501

        price after five year from now  # noqa: E501

        :return: The five_year_from_now of this DepreciationStats.  # noqa: E501
        :rtype: float
        """
        return self._five_year_from_now

    @five_year_from_now.setter
    def five_year_from_now(self, five_year_from_now):
        """Sets the five_year_from_now of this DepreciationStats.

        price after five year from now  # noqa: E501

        :param five_year_from_now: The five_year_from_now of this DepreciationStats.  # noqa: E501
        :type: float
        """

        self._five_year_from_now = five_year_from_now

    @property
    def five_year_from_now_percent(self):
        """Gets the five_year_from_now_percent of this DepreciationStats.  # noqa: E501

        price depreciation percent after five year from now  # noqa: E501

        :return: The five_year_from_now_percent of this DepreciationStats.  # noqa: E501
        :rtype: float
        """
        return self._five_year_from_now_percent

    @five_year_from_now_percent.setter
    def five_year_from_now_percent(self, five_year_from_now_percent):
        """Sets the five_year_from_now_percent of this DepreciationStats.

        price depreciation percent after five year from now  # noqa: E501

        :param five_year_from_now_percent: The five_year_from_now_percent of this DepreciationStats.  # noqa: E501
        :type: float
        """

        self._five_year_from_now_percent = five_year_from_now_percent

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
        if not isinstance(other, DepreciationStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other