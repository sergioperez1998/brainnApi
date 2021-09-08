# -*- coding: utf-8 -*-

"""
brainnapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from tests.http_response_catcher import HttpResponseCatcher
from brainnapi.api_helper import APIHelper
from brainnapi.controllers.misc_controller import MiscController
from brainnapi.models.loginrequest import Loginrequest
from brainnapi.models.create_user_request import CreateUserRequest
from brainnapi.models.create_persona_request import CreatePersonaRequest
from brainnapi.models.update_user_request import UpdateUserRequest
from brainnapi.models.update_persona_request import UpdatePersonaRequest


class MiscControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(MiscControllerTests, cls).setUpClass()
        cls.response_catcher = HttpResponseCatcher()
        cls.controller = MiscController(cls.config, cls.response_catcher)

    # Todo: Add description for test test_login
    def test_login(self):
        # Parameters for the API call
        content_type = 'application/json'
        body = APIHelper.json_deserialize('{"username":"admin_brainn","password":"insinno123"}', Loginrequest.from_dictionary)

        # Perform the API call through the SDK function
        self.controller.login(content_type, body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # Todo: Add description for test test_logout
    def test_logout(self):
        # Parameters for the API call
        content_type = 'application/json'
        authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'

        # Perform the API call through the SDK function
        self.controller.logout(content_type, authorization)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # Todo: Add description for test test_users
    def test_users(self):
        # Parameters for the API call
        content_type = 'application/json'
        authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'

        # Perform the API call through the SDK function
        self.controller.users(content_type, authorization)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # Todo: Add description for test test_user
    def test_user(self):
        # Parameters for the API call
        content_type = 'application/json'
        authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'

        # Perform the API call through the SDK function
        self.controller.user(content_type, authorization)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # Todo: Add description for test test_personas
    def test_personas(self):
        # Parameters for the API call
        content_type = 'application/json'
        authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'

        # Perform the API call through the SDK function
        self.controller.personas(content_type, authorization)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # Todo: Add description for test test_persona
    def test_persona(self):
        # Parameters for the API call
        content_type = 'application/json'
        authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'

        # Perform the API call through the SDK function
        self.controller.persona(content_type, authorization)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # Todo: Add description for test test_create_user
    def test_create_user(self):
        # Parameters for the API call
        content_type = 'application/json'
        authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'
        body = APIHelper.json_deserialize('{"password":"probando1234","is_superuser":false,"username":"insinn'
            'oBrainn12","first_name":"brainn","email":"probando@probando.es","i'
            's_staff":true,"is_active":true,"groups":[3],"user_permissions":[1,'
            '3]}', CreateUserRequest.from_dictionary)

        # Perform the API call through the SDK function
        self.controller.create_user(content_type, authorization, body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # Todo: Add description for test test_create_persona
    def test_create_persona(self):
        # Parameters for the API call
        content_type = 'application/json'
        authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'
        body = APIHelper.json_deserialize('{"codigo":117,"nombre":"brainn_persona2","apellido1":"apellido1","'
            'apellido2":"apellido2","activo":true,"externo":false,"advance":fal'
            'se,"fecha_nacimiento":"1073-09-01","foto":null,"tipo_eval":"B","di'
            'sponible":false,"organizacion":1,"usuario":2,"centro_fisico":1,"mo'
            'vilidad":[4]}', CreatePersonaRequest.from_dictionary)

        # Perform the API call through the SDK function
        self.controller.create_persona(content_type, authorization, body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # Todo: Add description for test test_update_user
    def test_update_user(self):
        # Parameters for the API call
        content_type = 'application/json'
        authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'
        body = APIHelper.json_deserialize('{"password":"probando123","is_superuser":false,"username":"insinno'
            'Brainn99","first_name":"insinno","email":"probando@probando.es","i'
            's_staff":true,"is_active":false,"groups":[8],"user_permissions":[9'
            ']}', UpdateUserRequest.from_dictionary)

        # Perform the API call through the SDK function
        self.controller.update_user(content_type, authorization, body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # Todo: Add description for test test_update_persona
    def test_update_persona(self):
        # Parameters for the API call
        content_type = 'application/json'
        authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'
        body = APIHelper.json_deserialize('{"codigo":"60","nombre":"brainn","apellido1":"probando","apellido2'
            '":"apellido","activo":false}', UpdatePersonaRequest.from_dictionary)

        # Perform the API call through the SDK function
        self.controller.update_persona(content_type, authorization, body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

