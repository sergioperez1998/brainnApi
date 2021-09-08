# Misc

```python
misc_controller = client.misc
```

## Class Name

`MiscController`

## Methods

* [Login](/doc/controllers/misc.md#login)
* [Logout](/doc/controllers/misc.md#logout)
* [Users](/doc/controllers/misc.md#users)
* [User](/doc/controllers/misc.md#user)
* [Personas](/doc/controllers/misc.md#personas)
* [Persona](/doc/controllers/misc.md#persona)
* [Create User](/doc/controllers/misc.md#create-user)
* [Create Persona](/doc/controllers/misc.md#create-persona)
* [Update User](/doc/controllers/misc.md#update-user)
* [Update Persona](/doc/controllers/misc.md#update-persona)


# Login

```python
def login(self,
         content_type,
         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | `string` | Header, Required | - |
| `body` | [`Loginrequest`](/doc/models/loginrequest.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
content_type = 'application/json'
body = Loginrequest()
body.username = 'admin_brainn'
body.password = 'insinno123'

result = misc_controller.login(content_type, body)
```


# Logout

:information_source: **Note** This endpoint does not require authentication.

```python
def logout(self,
          content_type,
          authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |

## Response Type

`void`

## Example Usage

```python
content_type = 'application/json'
authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'

result = misc_controller.logout(content_type, authorization)
```


# Users

:information_source: **Note** This endpoint does not require authentication.

```python
def users(self,
         content_type,
         authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |

## Response Type

`void`

## Example Usage

```python
content_type = 'application/json'
authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'

result = misc_controller.users(content_type, authorization)
```


# User

:information_source: **Note** This endpoint does not require authentication.

```python
def user(self,
        content_type,
        authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |

## Response Type

`void`

## Example Usage

```python
content_type = 'application/json'
authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'

result = misc_controller.user(content_type, authorization)
```


# Personas

:information_source: **Note** This endpoint does not require authentication.

```python
def personas(self,
            content_type,
            authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |

## Response Type

`void`

## Example Usage

```python
content_type = 'application/json'
authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'

result = misc_controller.personas(content_type, authorization)
```


# Persona

:information_source: **Note** This endpoint does not require authentication.

```python
def persona(self,
           content_type,
           authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |

## Response Type

`void`

## Example Usage

```python
content_type = 'application/json'
authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'

result = misc_controller.persona(content_type, authorization)
```


# Create User

:information_source: **Note** This endpoint does not require authentication.

```python
def create_user(self,
               content_type,
               authorization,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `body` | [`CreateUserRequest`](/doc/models/create-user-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
content_type = 'application/json'
authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'
body = CreateUserRequest()
body.password = 'probando1234'
body.is_superuser = False
body.username = 'insinnoBrainn12'
body.first_name = 'brainn'
body.email = 'probando@probando.es'
body.is_staff = True
body.is_active = True
body.groups = [3]
body.user_permissions = [1, 3]

result = misc_controller.create_user(content_type, authorization, body)
```


# Create Persona

:information_source: **Note** This endpoint does not require authentication.

```python
def create_persona(self,
                  content_type,
                  authorization,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `body` | [`CreatePersonaRequest`](/doc/models/create-persona-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
content_type = 'application/json'
authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'
body = CreatePersonaRequest()
body.codigo = 117
body.nombre = 'brainn_persona2'
body.apellido_1 = 'apellido1'
body.apellido_2 = 'apellido2'
body.activo = True
body.externo = False
body.advance = False
body.fecha_nacimiento = '1073-09-01'
body.tipo_eval = 'B'
body.disponible = False
body.organizacion = 1
body.usuario = 2
body.centro_fisico = 1
body.movilidad = [4]

result = misc_controller.create_persona(content_type, authorization, body)
```


# Update User

:information_source: **Note** This endpoint does not require authentication.

```python
def update_user(self,
               content_type,
               authorization,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `body` | [`UpdateUserRequest`](/doc/models/update-user-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
content_type = 'application/json'
authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'
body = UpdateUserRequest()
body.password = 'probando123'
body.is_superuser = False
body.username = 'insinnoBrainn99'
body.first_name = 'insinno'
body.email = 'probando@probando.es'
body.is_staff = True
body.is_active = False
body.groups = [8]
body.user_permissions = [9]

result = misc_controller.update_user(content_type, authorization, body)
```


# Update Persona

:information_source: **Note** This endpoint does not require authentication.

```python
def update_persona(self,
                  content_type,
                  authorization,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `body` | [`UpdatePersonaRequest`](/doc/models/update-persona-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
content_type = 'application/json'
authorization = 'Token 043b548b673ce9748ffc10bca03872a92e13aaae'
body = UpdatePersonaRequest()
body.codigo = '60'
body.nombre = 'brainn'
body.apellido_1 = 'probando'
body.apellido_2 = 'apellido'
body.activo = False

result = misc_controller.update_persona(content_type, authorization, body)
```

