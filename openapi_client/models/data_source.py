# coding: utf-8

"""
    Chemically Peculiar Stars Database OpenAPI definitions

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class DataSource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'name': 'str',
        'full_name': 'str',
        'year': 'int',
        'bibcode': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'full_name': 'fullName',
        'year': 'year',
        'bibcode': 'bibcode',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, full_name=None, year=None, bibcode=None, description=None, local_vars_configuration=None):  # noqa: E501
        """DataSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._full_name = None
        self._year = None
        self._bibcode = None
        self._description = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.full_name = full_name
        self.year = year
        self.bibcode = bibcode
        self.description = description

    @property
    def id(self):
        """Gets the id of this DataSource.  # noqa: E501


        :return: The id of this DataSource.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataSource.


        :param id: The id of this DataSource.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this DataSource.  # noqa: E501


        :return: The name of this DataSource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataSource.


        :param name: The name of this DataSource.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 30):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `30`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def full_name(self):
        """Gets the full_name of this DataSource.  # noqa: E501


        :return: The full_name of this DataSource.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this DataSource.


        :param full_name: The full_name of this DataSource.  # noqa: E501
        :type full_name: str
        """
        if self.local_vars_configuration.client_side_validation and full_name is None:  # noqa: E501
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                full_name is not None and len(full_name) > 100):
            raise ValueError("Invalid value for `full_name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                full_name is not None and len(full_name) < 0):
            raise ValueError("Invalid value for `full_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._full_name = full_name

    @property
    def year(self):
        """Gets the year of this DataSource.  # noqa: E501


        :return: The year of this DataSource.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this DataSource.


        :param year: The year of this DataSource.  # noqa: E501
        :type year: int
        """
        if self.local_vars_configuration.client_side_validation and year is None:  # noqa: E501
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

    @property
    def bibcode(self):
        """Gets the bibcode of this DataSource.  # noqa: E501


        :return: The bibcode of this DataSource.  # noqa: E501
        :rtype: str
        """
        return self._bibcode

    @bibcode.setter
    def bibcode(self, bibcode):
        """Sets the bibcode of this DataSource.


        :param bibcode: The bibcode of this DataSource.  # noqa: E501
        :type bibcode: str
        """
        if self.local_vars_configuration.client_side_validation and bibcode is None:  # noqa: E501
            raise ValueError("Invalid value for `bibcode`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                bibcode is not None and len(bibcode) > 19):
            raise ValueError("Invalid value for `bibcode`, length must be less than or equal to `19`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                bibcode is not None and len(bibcode) < 0):
            raise ValueError("Invalid value for `bibcode`, length must be greater than or equal to `0`")  # noqa: E501

        self._bibcode = bibcode

    @property
    def description(self):
        """Gets the description of this DataSource.  # noqa: E501


        :return: The description of this DataSource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataSource.


        :param description: The description of this DataSource.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 16384):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `16384`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DataSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataSource):
            return True

        return self.to_dict() != other.to_dict()
