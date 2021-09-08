# -*- coding: utf-8 -*-

"""
brainnapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from enum import Enum
from brainnapi.http.requests_client import RequestsClient


class Environment(Enum):
    """An enum for SDK environments"""
    PRODUCTION = 0


class Server(Enum):
    """An enum for API servers"""
    SERVER_1 = 0


class Configuration(object):
    """A class used for configuring the SDK by a user.
    """

    @property
    def http_client(self):
        return self._http_client

    @property
    def timeout(self):
        return self._timeout

    @property
    def max_retries(self):
        return self._max_retries

    @property
    def backoff_factor(self):
        return self._backoff_factor

    @property
    def retry_statuses(self):
        return self._retry_statuses

    @property
    def retry_methods(self):
        return self._retry_methods

    @property
    def environment(self):
        return self._environment

    @property
    def basic_auth_user_name(self):
        return self._basic_auth_user_name

    @property
    def basic_auth_password(self):
        return self._basic_auth_password

    def __init__(
        self, timeout=60, max_retries=0, backoff_factor=2,
        retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
        retry_methods=['GET', 'PUT'], environment=Environment.PRODUCTION,
        basic_auth_user_name='TODO: Replace',
        basic_auth_password='TODO: Replace'
    ):
        # The value to use for connection timeout
        self._timeout = timeout

        # The number of times to retry an endpoint call if it fails
        self._max_retries = max_retries

        # A backoff factor to apply between attempts after the second try.
        # urllib3 will sleep for:
        # `{backoff factor} * (2 ** ({number of total retries} - 1))`
        self._backoff_factor = backoff_factor

        # The http statuses on which retry is to be done
        self._retry_statuses = retry_statuses

        # The http methods on which retry is to be done
        self._retry_methods = retry_methods

        # Current API environment
        self._environment = environment

        # The username to use with basic authentication
        self._basic_auth_user_name = basic_auth_user_name

        # The password to use with basic authentication
        self._basic_auth_password = basic_auth_password

        # The Http Client to use for making requests.
        self._http_client = self.create_http_client()

    def clone_with(self, timeout=None, max_retries=None, backoff_factor=None,
                   retry_statuses=None, retry_methods=None, environment=None,
                   basic_auth_user_name=None, basic_auth_password=None):
        timeout = timeout or self.timeout
        max_retries = max_retries or self.max_retries
        backoff_factor = backoff_factor or self.backoff_factor
        retry_statuses = retry_statuses or self.retry_statuses
        retry_methods = retry_methods or self.retry_methods
        environment = environment or self.environment
        basic_auth_user_name = basic_auth_user_name or self.basic_auth_user_name
        basic_auth_password = basic_auth_password or self.basic_auth_password

        return Configuration(timeout=timeout, max_retries=max_retries,
                             backoff_factor=backoff_factor,
                             retry_statuses=retry_statuses,
                             retry_methods=retry_methods,
                             environment=environment,
                             basic_auth_user_name=basic_auth_user_name,
                             basic_auth_password=basic_auth_password)

    def create_http_client(self):
        return RequestsClient(timeout=self.timeout,
                              max_retries=self.max_retries,
                              backoff_factor=self.backoff_factor,
                              retry_statuses=self.retry_statuses,
                              retry_methods=self.retry_methods)

    # All the environments the SDK can run in
    environments = {
        Environment.PRODUCTION: {
            Server.SERVER_1: 'http://localhost:8000/api'
        }
    }

    def get_base_uri(self, server=Server.SERVER_1):
        """Generates the appropriate base URI for the environment and the
        server.

        Args:
            server (Configuration.Server): The server enum for which the base
            URI is required.

        Returns:
            String: The base URI.

        """
        return self.environments[self.environment][server]
