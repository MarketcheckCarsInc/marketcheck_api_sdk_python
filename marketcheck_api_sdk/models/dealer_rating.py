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

from marketcheck_api_sdk.models.rating_components import RatingComponents  # noqa: F401,E501


class DealerRating(object):
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
        'street': 'str',
        'city': 'str',
        'state': 'str',
        'zip': 'str',
        'latitude': 'str',
        'longitude': 'str',
        'overall_rating': 'float',
        'rating_components': 'list[RatingComponents]'
    }

    attribute_map = {
        'name': 'name',
        'street': 'street',
        'city': 'city',
        'state': 'state',
        'zip': 'zip',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'overall_rating': 'overall_rating',
        'rating_components': 'rating_components'
    }

    def __init__(self, name=None, street=None, city=None, state=None, zip=None, latitude=None, longitude=None, overall_rating=None, rating_components=None):  # noqa: E501
        """DealerRating - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._street = None
        self._city = None
        self._state = None
        self._zip = None
        self._latitude = None
        self._longitude = None
        self._overall_rating = None
        self._rating_components = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if street is not None:
            self.street = street
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if zip is not None:
            self.zip = zip
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if overall_rating is not None:
            self.overall_rating = overall_rating
        if rating_components is not None:
            self.rating_components = rating_components

    @property
    def name(self):
        """Gets the name of this DealerRating.  # noqa: E501

        Name of the dealer  # noqa: E501

        :return: The name of this DealerRating.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DealerRating.

        Name of the dealer  # noqa: E501

        :param name: The name of this DealerRating.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def street(self):
        """Gets the street of this DealerRating.  # noqa: E501

        Street of the dealer  # noqa: E501

        :return: The street of this DealerRating.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this DealerRating.

        Street of the dealer  # noqa: E501

        :param street: The street of this DealerRating.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def city(self):
        """Gets the city of this DealerRating.  # noqa: E501

        City of the dealer  # noqa: E501

        :return: The city of this DealerRating.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this DealerRating.

        City of the dealer  # noqa: E501

        :param city: The city of this DealerRating.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this DealerRating.  # noqa: E501

        State of the dealer  # noqa: E501

        :return: The state of this DealerRating.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DealerRating.

        State of the dealer  # noqa: E501

        :param state: The state of this DealerRating.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this DealerRating.  # noqa: E501

        Zip of the dealer  # noqa: E501

        :return: The zip of this DealerRating.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this DealerRating.

        Zip of the dealer  # noqa: E501

        :param zip: The zip of this DealerRating.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def latitude(self):
        """Gets the latitude of this DealerRating.  # noqa: E501

        Latutide for the dealer location  # noqa: E501

        :return: The latitude of this DealerRating.  # noqa: E501
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this DealerRating.

        Latutide for the dealer location  # noqa: E501

        :param latitude: The latitude of this DealerRating.  # noqa: E501
        :type: str
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this DealerRating.  # noqa: E501

        Longitude for the dealer location  # noqa: E501

        :return: The longitude of this DealerRating.  # noqa: E501
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this DealerRating.

        Longitude for the dealer location  # noqa: E501

        :param longitude: The longitude of this DealerRating.  # noqa: E501
        :type: str
        """

        self._longitude = longitude

    @property
    def overall_rating(self):
        """Gets the overall_rating of this DealerRating.  # noqa: E501

        Overall rating of the dealership on scale 1-5  # noqa: E501

        :return: The overall_rating of this DealerRating.  # noqa: E501
        :rtype: float
        """
        return self._overall_rating

    @overall_rating.setter
    def overall_rating(self, overall_rating):
        """Sets the overall_rating of this DealerRating.

        Overall rating of the dealership on scale 1-5  # noqa: E501

        :param overall_rating: The overall_rating of this DealerRating.  # noqa: E501
        :type: float
        """

        self._overall_rating = overall_rating

    @property
    def rating_components(self):
        """Gets the rating_components of this DealerRating.  # noqa: E501


        :return: The rating_components of this DealerRating.  # noqa: E501
        :rtype: list[RatingComponents]
        """
        return self._rating_components

    @rating_components.setter
    def rating_components(self, rating_components):
        """Sets the rating_components of this DealerRating.


        :param rating_components: The rating_components of this DealerRating.  # noqa: E501
        :type: list[RatingComponents]
        """

        self._rating_components = rating_components

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
        if not isinstance(other, DealerRating):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other