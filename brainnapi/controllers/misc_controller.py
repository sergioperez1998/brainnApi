# -*- coding: utf-8 -*-

"""
brainnapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from brainnapi.api_helper import APIHelper
from brainnapi.configuration import Server
from brainnapi.controllers.base_controller import BaseController
from brainnapi.http.auth.basic_auth import BasicAuth


class MiscController(BaseController):

    """A Controller to access Endpoints in the brainnapi API."""

    def __init__(self, config, call_back=None):
        super(MiscController, self).__init__(config, call_back)

    def login(self,
              content_type,
              body):
        """Does a POST request to /login/.

        TODO: type endpoint description here.

        Args:
            content_type (string): TODO: type description here.
            body (Loginrequest): TODO: type description here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/login/'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': content_type
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        BasicAuth.apply(self.config, _request)
        _response = self.execute_request(_request)
        self.validate_response(_response)

    def logout(self,
               content_type,
               authorization):
        """Does a GET request to /logout/.

        TODO: type endpoint description here.

        Args:
            content_type (string): TODO: type description here.
            authorization (string): TODO: type description here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/logout/'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': content_type,
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        _response = self.execute_request(_request)
        self.validate_response(_response)

    def users(self,
              content_type,
              authorization):
        """Does a GET request to /users/.

        TODO: type endpoint description here.

        Args:
            content_type (string): TODO: type description here.
            authorization (string): TODO: type description here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/users/'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': content_type,
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        _response = self.execute_request(_request)
        self.validate_response(_response)

    def user(self,
             content_type,
             authorization):
        """Does a GET request to /user/1.

        TODO: type endpoint description here.

        Args:
            content_type (string): TODO: type description here.
            authorization (string): TODO: type description here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/user/1'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': content_type,
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        _response = self.execute_request(_request)
        self.validate_response(_response)

    def personas(self,
                 content_type,
                 authorization):
        """Does a GET request to /personas/.

        TODO: type endpoint description here.

        Args:
            content_type (string): TODO: type description here.
            authorization (string): TODO: type description here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/personas/'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': content_type,
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        _response = self.execute_request(_request)
        self.validate_response(_response)

    def persona(self,
                content_type,
                authorization):
        """Does a GET request to /persona/1.

        TODO: type endpoint description here.

        Args:
            content_type (string): TODO: type description here.
            authorization (string): TODO: type description here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/persona/1'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': content_type,
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        _response = self.execute_request(_request)
        self.validate_response(_response)

    def create_user(self,
                    content_type,
                    authorization,
                    body):
        """Does a POST request to /users/.

        TODO: type endpoint description here.

        Args:
            content_type (string): TODO: type description here.
            authorization (string): TODO: type description here.
            body (CreateUserRequest): TODO: type description here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/users/'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': content_type,
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        _response = self.execute_request(_request)
        self.validate_response(_response)

    def create_persona(self,
                       content_type,
                       authorization,
                       body):
        """Does a POST request to /personas/.

        TODO: type endpoint description here.

        Args:
            content_type (string): TODO: type description here.
            authorization (string): TODO: type description here.
            body (CreatePersonaRequest): TODO: type description here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/personas/'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': content_type,
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        _response = self.execute_request(_request)
        self.validate_response(_response)

    def update_user(self,
                    content_type,
                    authorization,
                    body):
        """Does a PUT request to /user/53.

        TODO: type endpoint description here.

        Args:
            content_type (string): TODO: type description here.
            authorization (string): TODO: type description here.
            body (UpdateUserRequest): TODO: type description here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/user/53'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': content_type,
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        _response = self.execute_request(_request)
        self.validate_response(_response)

    def update_persona(self,
                       content_type,
                       authorization,
                       body):
        """Does a PUT request to /persona/47.

        TODO: type endpoint description here.

        Args:
            content_type (string): TODO: type description here.
            authorization (string): TODO: type description here.
            body (UpdatePersonaRequest): TODO: type description here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/persona/47'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': content_type,
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        _response = self.execute_request(_request)
        self.validate_response(_response)
