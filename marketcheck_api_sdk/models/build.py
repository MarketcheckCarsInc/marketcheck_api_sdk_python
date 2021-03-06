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


class Build(object):
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
        'year': 'int',
        'make': 'str',
        'model': 'str',
        'trim': 'str',
        'short_trim': 'str',
        'body_type': 'str',
        'body_subtype': 'str',
        'vehicle_type': 'str',
        'transmission': 'str',
        'drivetrain': 'str',
        'fuel_type': 'str',
        'engine': 'str',
        'engine_size': 'float',
        'engine_block': 'str',
        'doors': 'int',
        'cylinders': 'int',
        'made_in': 'str',
        'steering_type': 'str',
        'antibrake_sys': 'str',
        'tank_size': 'str',
        'overall_height': 'str',
        'overall_length': 'str',
        'overall_width': 'str',
        'std_seating': 'str',
        'opt_seating': 'str',
        'highway_miles': 'str',
        'city_miles': 'str',
        'engine_measure': 'str',
        'engine_aspiration': 'str',
        'trim_r': 'str'
    }

    attribute_map = {
        'year': 'year',
        'make': 'make',
        'model': 'model',
        'trim': 'trim',
        'short_trim': 'short_trim',
        'body_type': 'body_type',
        'body_subtype': 'body_subtype',
        'vehicle_type': 'vehicle_type',
        'transmission': 'transmission',
        'drivetrain': 'drivetrain',
        'fuel_type': 'fuel_type',
        'engine': 'engine',
        'engine_size': 'engine_size',
        'engine_block': 'engine_block',
        'doors': 'doors',
        'cylinders': 'cylinders',
        'made_in': 'made_in',
        'steering_type': 'steering_type',
        'antibrake_sys': 'antibrake_sys',
        'tank_size': 'tank_size',
        'overall_height': 'overall_height',
        'overall_length': 'overall_length',
        'overall_width': 'overall_width',
        'std_seating': 'std_seating',
        'opt_seating': 'opt_seating',
        'highway_miles': 'highway_miles',
        'city_miles': 'city_miles',
        'engine_measure': 'engine_measure',
        'engine_aspiration': 'engine_aspiration',
        'trim_r': 'trim_r'
    }

    def __init__(self, year=None, make=None, model=None, trim=None, short_trim=None, body_type=None, body_subtype=None, vehicle_type=None, transmission=None, drivetrain=None, fuel_type=None, engine=None, engine_size=None, engine_block=None, doors=None, cylinders=None, made_in=None, steering_type=None, antibrake_sys=None, tank_size=None, overall_height=None, overall_length=None, overall_width=None, std_seating=None, opt_seating=None, highway_miles=None, city_miles=None, engine_measure=None, engine_aspiration=None, trim_r=None):  # noqa: E501
        """Build - a model defined in Swagger"""  # noqa: E501

        self._year = None
        self._make = None
        self._model = None
        self._trim = None
        self._short_trim = None
        self._body_type = None
        self._body_subtype = None
        self._vehicle_type = None
        self._transmission = None
        self._drivetrain = None
        self._fuel_type = None
        self._engine = None
        self._engine_size = None
        self._engine_block = None
        self._doors = None
        self._cylinders = None
        self._made_in = None
        self._steering_type = None
        self._antibrake_sys = None
        self._tank_size = None
        self._overall_height = None
        self._overall_length = None
        self._overall_width = None
        self._std_seating = None
        self._opt_seating = None
        self._highway_miles = None
        self._city_miles = None
        self._engine_measure = None
        self._engine_aspiration = None
        self._trim_r = None
        self.discriminator = None

        if year is not None:
            self.year = year
        if make is not None:
            self.make = make
        if model is not None:
            self.model = model
        if trim is not None:
            self.trim = trim
        if short_trim is not None:
            self.short_trim = short_trim
        if body_type is not None:
            self.body_type = body_type
        if body_subtype is not None:
            self.body_subtype = body_subtype
        if vehicle_type is not None:
            self.vehicle_type = vehicle_type
        if transmission is not None:
            self.transmission = transmission
        if drivetrain is not None:
            self.drivetrain = drivetrain
        if fuel_type is not None:
            self.fuel_type = fuel_type
        if engine is not None:
            self.engine = engine
        if engine_size is not None:
            self.engine_size = engine_size
        if engine_block is not None:
            self.engine_block = engine_block
        if doors is not None:
            self.doors = doors
        if cylinders is not None:
            self.cylinders = cylinders
        if made_in is not None:
            self.made_in = made_in
        if steering_type is not None:
            self.steering_type = steering_type
        if antibrake_sys is not None:
            self.antibrake_sys = antibrake_sys
        if tank_size is not None:
            self.tank_size = tank_size
        if overall_height is not None:
            self.overall_height = overall_height
        if overall_length is not None:
            self.overall_length = overall_length
        if overall_width is not None:
            self.overall_width = overall_width
        if std_seating is not None:
            self.std_seating = std_seating
        if opt_seating is not None:
            self.opt_seating = opt_seating
        if highway_miles is not None:
            self.highway_miles = highway_miles
        if city_miles is not None:
            self.city_miles = city_miles
        if engine_measure is not None:
            self.engine_measure = engine_measure
        if engine_aspiration is not None:
            self.engine_aspiration = engine_aspiration
        if trim_r is not None:
            self.trim_r = trim_r

    @property
    def year(self):
        """Gets the year of this Build.  # noqa: E501

        Year of the Car  # noqa: E501

        :return: The year of this Build.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Build.

        Year of the Car  # noqa: E501

        :param year: The year of this Build.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def make(self):
        """Gets the make of this Build.  # noqa: E501

        Car Make  # noqa: E501

        :return: The make of this Build.  # noqa: E501
        :rtype: str
        """
        return self._make

    @make.setter
    def make(self, make):
        """Sets the make of this Build.

        Car Make  # noqa: E501

        :param make: The make of this Build.  # noqa: E501
        :type: str
        """

        self._make = make

    @property
    def model(self):
        """Gets the model of this Build.  # noqa: E501

        Car model  # noqa: E501

        :return: The model of this Build.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Build.

        Car model  # noqa: E501

        :param model: The model of this Build.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def trim(self):
        """Gets the trim of this Build.  # noqa: E501

        Trim of the car  # noqa: E501

        :return: The trim of this Build.  # noqa: E501
        :rtype: str
        """
        return self._trim

    @trim.setter
    def trim(self, trim):
        """Sets the trim of this Build.

        Trim of the car  # noqa: E501

        :param trim: The trim of this Build.  # noqa: E501
        :type: str
        """

        self._trim = trim

    @property
    def short_trim(self):
        """Gets the short_trim of this Build.  # noqa: E501

        Short trim of the car  # noqa: E501

        :return: The short_trim of this Build.  # noqa: E501
        :rtype: str
        """
        return self._short_trim

    @short_trim.setter
    def short_trim(self, short_trim):
        """Sets the short_trim of this Build.

        Short trim of the car  # noqa: E501

        :param short_trim: The short_trim of this Build.  # noqa: E501
        :type: str
        """

        self._short_trim = short_trim

    @property
    def body_type(self):
        """Gets the body_type of this Build.  # noqa: E501

        Body type of the car  # noqa: E501

        :return: The body_type of this Build.  # noqa: E501
        :rtype: str
        """
        return self._body_type

    @body_type.setter
    def body_type(self, body_type):
        """Sets the body_type of this Build.

        Body type of the car  # noqa: E501

        :param body_type: The body_type of this Build.  # noqa: E501
        :type: str
        """

        self._body_type = body_type

    @property
    def body_subtype(self):
        """Gets the body_subtype of this Build.  # noqa: E501

        Body subtype of the car  # noqa: E501

        :return: The body_subtype of this Build.  # noqa: E501
        :rtype: str
        """
        return self._body_subtype

    @body_subtype.setter
    def body_subtype(self, body_subtype):
        """Sets the body_subtype of this Build.

        Body subtype of the car  # noqa: E501

        :param body_subtype: The body_subtype of this Build.  # noqa: E501
        :type: str
        """

        self._body_subtype = body_subtype

    @property
    def vehicle_type(self):
        """Gets the vehicle_type of this Build.  # noqa: E501

        Vehicle type of the car  # noqa: E501

        :return: The vehicle_type of this Build.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        """Sets the vehicle_type of this Build.

        Vehicle type of the car  # noqa: E501

        :param vehicle_type: The vehicle_type of this Build.  # noqa: E501
        :type: str
        """

        self._vehicle_type = vehicle_type

    @property
    def transmission(self):
        """Gets the transmission of this Build.  # noqa: E501

        Transmission of the car  # noqa: E501

        :return: The transmission of this Build.  # noqa: E501
        :rtype: str
        """
        return self._transmission

    @transmission.setter
    def transmission(self, transmission):
        """Sets the transmission of this Build.

        Transmission of the car  # noqa: E501

        :param transmission: The transmission of this Build.  # noqa: E501
        :type: str
        """

        self._transmission = transmission

    @property
    def drivetrain(self):
        """Gets the drivetrain of this Build.  # noqa: E501

        Drivetrain of the car  # noqa: E501

        :return: The drivetrain of this Build.  # noqa: E501
        :rtype: str
        """
        return self._drivetrain

    @drivetrain.setter
    def drivetrain(self, drivetrain):
        """Sets the drivetrain of this Build.

        Drivetrain of the car  # noqa: E501

        :param drivetrain: The drivetrain of this Build.  # noqa: E501
        :type: str
        """

        self._drivetrain = drivetrain

    @property
    def fuel_type(self):
        """Gets the fuel_type of this Build.  # noqa: E501

        Fuel type of the car  # noqa: E501

        :return: The fuel_type of this Build.  # noqa: E501
        :rtype: str
        """
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type):
        """Sets the fuel_type of this Build.

        Fuel type of the car  # noqa: E501

        :param fuel_type: The fuel_type of this Build.  # noqa: E501
        :type: str
        """

        self._fuel_type = fuel_type

    @property
    def engine(self):
        """Gets the engine of this Build.  # noqa: E501

        Engine of the car  # noqa: E501

        :return: The engine of this Build.  # noqa: E501
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this Build.

        Engine of the car  # noqa: E501

        :param engine: The engine of this Build.  # noqa: E501
        :type: str
        """

        self._engine = engine

    @property
    def engine_size(self):
        """Gets the engine_size of this Build.  # noqa: E501

        Engine size of the car  # noqa: E501

        :return: The engine_size of this Build.  # noqa: E501
        :rtype: float
        """
        return self._engine_size

    @engine_size.setter
    def engine_size(self, engine_size):
        """Sets the engine_size of this Build.

        Engine size of the car  # noqa: E501

        :param engine_size: The engine_size of this Build.  # noqa: E501
        :type: float
        """

        self._engine_size = engine_size

    @property
    def engine_block(self):
        """Gets the engine_block of this Build.  # noqa: E501

        Engine block of the car  # noqa: E501

        :return: The engine_block of this Build.  # noqa: E501
        :rtype: str
        """
        return self._engine_block

    @engine_block.setter
    def engine_block(self, engine_block):
        """Sets the engine_block of this Build.

        Engine block of the car  # noqa: E501

        :param engine_block: The engine_block of this Build.  # noqa: E501
        :type: str
        """

        self._engine_block = engine_block

    @property
    def doors(self):
        """Gets the doors of this Build.  # noqa: E501

        No of doors of the car  # noqa: E501

        :return: The doors of this Build.  # noqa: E501
        :rtype: int
        """
        return self._doors

    @doors.setter
    def doors(self, doors):
        """Sets the doors of this Build.

        No of doors of the car  # noqa: E501

        :param doors: The doors of this Build.  # noqa: E501
        :type: int
        """

        self._doors = doors

    @property
    def cylinders(self):
        """Gets the cylinders of this Build.  # noqa: E501

        No of cylinders of the car  # noqa: E501

        :return: The cylinders of this Build.  # noqa: E501
        :rtype: int
        """
        return self._cylinders

    @cylinders.setter
    def cylinders(self, cylinders):
        """Sets the cylinders of this Build.

        No of cylinders of the car  # noqa: E501

        :param cylinders: The cylinders of this Build.  # noqa: E501
        :type: int
        """

        self._cylinders = cylinders

    @property
    def made_in(self):
        """Gets the made_in of this Build.  # noqa: E501

        Made in of the car  # noqa: E501

        :return: The made_in of this Build.  # noqa: E501
        :rtype: str
        """
        return self._made_in

    @made_in.setter
    def made_in(self, made_in):
        """Sets the made_in of this Build.

        Made in of the car  # noqa: E501

        :param made_in: The made_in of this Build.  # noqa: E501
        :type: str
        """

        self._made_in = made_in

    @property
    def steering_type(self):
        """Gets the steering_type of this Build.  # noqa: E501

        Steering type of the car  # noqa: E501

        :return: The steering_type of this Build.  # noqa: E501
        :rtype: str
        """
        return self._steering_type

    @steering_type.setter
    def steering_type(self, steering_type):
        """Sets the steering_type of this Build.

        Steering type of the car  # noqa: E501

        :param steering_type: The steering_type of this Build.  # noqa: E501
        :type: str
        """

        self._steering_type = steering_type

    @property
    def antibrake_sys(self):
        """Gets the antibrake_sys of this Build.  # noqa: E501

        Antibrake system of the car  # noqa: E501

        :return: The antibrake_sys of this Build.  # noqa: E501
        :rtype: str
        """
        return self._antibrake_sys

    @antibrake_sys.setter
    def antibrake_sys(self, antibrake_sys):
        """Sets the antibrake_sys of this Build.

        Antibrake system of the car  # noqa: E501

        :param antibrake_sys: The antibrake_sys of this Build.  # noqa: E501
        :type: str
        """

        self._antibrake_sys = antibrake_sys

    @property
    def tank_size(self):
        """Gets the tank_size of this Build.  # noqa: E501

        Tank size of the car  # noqa: E501

        :return: The tank_size of this Build.  # noqa: E501
        :rtype: str
        """
        return self._tank_size

    @tank_size.setter
    def tank_size(self, tank_size):
        """Sets the tank_size of this Build.

        Tank size of the car  # noqa: E501

        :param tank_size: The tank_size of this Build.  # noqa: E501
        :type: str
        """

        self._tank_size = tank_size

    @property
    def overall_height(self):
        """Gets the overall_height of this Build.  # noqa: E501

        Overall height of the car  # noqa: E501

        :return: The overall_height of this Build.  # noqa: E501
        :rtype: str
        """
        return self._overall_height

    @overall_height.setter
    def overall_height(self, overall_height):
        """Sets the overall_height of this Build.

        Overall height of the car  # noqa: E501

        :param overall_height: The overall_height of this Build.  # noqa: E501
        :type: str
        """

        self._overall_height = overall_height

    @property
    def overall_length(self):
        """Gets the overall_length of this Build.  # noqa: E501

        Overall length of the car  # noqa: E501

        :return: The overall_length of this Build.  # noqa: E501
        :rtype: str
        """
        return self._overall_length

    @overall_length.setter
    def overall_length(self, overall_length):
        """Sets the overall_length of this Build.

        Overall length of the car  # noqa: E501

        :param overall_length: The overall_length of this Build.  # noqa: E501
        :type: str
        """

        self._overall_length = overall_length

    @property
    def overall_width(self):
        """Gets the overall_width of this Build.  # noqa: E501

        Overall width of the car  # noqa: E501

        :return: The overall_width of this Build.  # noqa: E501
        :rtype: str
        """
        return self._overall_width

    @overall_width.setter
    def overall_width(self, overall_width):
        """Sets the overall_width of this Build.

        Overall width of the car  # noqa: E501

        :param overall_width: The overall_width of this Build.  # noqa: E501
        :type: str
        """

        self._overall_width = overall_width

    @property
    def std_seating(self):
        """Gets the std_seating of this Build.  # noqa: E501

        Std seating of the car  # noqa: E501

        :return: The std_seating of this Build.  # noqa: E501
        :rtype: str
        """
        return self._std_seating

    @std_seating.setter
    def std_seating(self, std_seating):
        """Sets the std_seating of this Build.

        Std seating of the car  # noqa: E501

        :param std_seating: The std_seating of this Build.  # noqa: E501
        :type: str
        """

        self._std_seating = std_seating

    @property
    def opt_seating(self):
        """Gets the opt_seating of this Build.  # noqa: E501

        opt seating of the car  # noqa: E501

        :return: The opt_seating of this Build.  # noqa: E501
        :rtype: str
        """
        return self._opt_seating

    @opt_seating.setter
    def opt_seating(self, opt_seating):
        """Sets the opt_seating of this Build.

        opt seating of the car  # noqa: E501

        :param opt_seating: The opt_seating of this Build.  # noqa: E501
        :type: str
        """

        self._opt_seating = opt_seating

    @property
    def highway_miles(self):
        """Gets the highway_miles of this Build.  # noqa: E501

        Highway miles of the car  # noqa: E501

        :return: The highway_miles of this Build.  # noqa: E501
        :rtype: str
        """
        return self._highway_miles

    @highway_miles.setter
    def highway_miles(self, highway_miles):
        """Sets the highway_miles of this Build.

        Highway miles of the car  # noqa: E501

        :param highway_miles: The highway_miles of this Build.  # noqa: E501
        :type: str
        """

        self._highway_miles = highway_miles

    @property
    def city_miles(self):
        """Gets the city_miles of this Build.  # noqa: E501

        City miles of the car  # noqa: E501

        :return: The city_miles of this Build.  # noqa: E501
        :rtype: str
        """
        return self._city_miles

    @city_miles.setter
    def city_miles(self, city_miles):
        """Sets the city_miles of this Build.

        City miles of the car  # noqa: E501

        :param city_miles: The city_miles of this Build.  # noqa: E501
        :type: str
        """

        self._city_miles = city_miles

    @property
    def engine_measure(self):
        """Gets the engine_measure of this Build.  # noqa: E501

        Engine block of the car  # noqa: E501

        :return: The engine_measure of this Build.  # noqa: E501
        :rtype: str
        """
        return self._engine_measure

    @engine_measure.setter
    def engine_measure(self, engine_measure):
        """Sets the engine_measure of this Build.

        Engine block of the car  # noqa: E501

        :param engine_measure: The engine_measure of this Build.  # noqa: E501
        :type: str
        """

        self._engine_measure = engine_measure

    @property
    def engine_aspiration(self):
        """Gets the engine_aspiration of this Build.  # noqa: E501

        Engine aspiration of the car  # noqa: E501

        :return: The engine_aspiration of this Build.  # noqa: E501
        :rtype: str
        """
        return self._engine_aspiration

    @engine_aspiration.setter
    def engine_aspiration(self, engine_aspiration):
        """Sets the engine_aspiration of this Build.

        Engine aspiration of the car  # noqa: E501

        :param engine_aspiration: The engine_aspiration of this Build.  # noqa: E501
        :type: str
        """

        self._engine_aspiration = engine_aspiration

    @property
    def trim_r(self):
        """Gets the trim_r of this Build.  # noqa: E501

        Trim_r of the car  # noqa: E501

        :return: The trim_r of this Build.  # noqa: E501
        :rtype: str
        """
        return self._trim_r

    @trim_r.setter
    def trim_r(self, trim_r):
        """Sets the trim_r of this Build.

        Trim_r of the car  # noqa: E501

        :param trim_r: The trim_r of this Build.  # noqa: E501
        :type: str
        """

        self._trim_r = trim_r

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
        if not isinstance(other, Build):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
