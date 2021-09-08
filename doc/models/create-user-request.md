
# Create User Request

## Structure

`CreateUserRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `password` | `string` | Required | - |
| `is_superuser` | `bool` | Required | - |
| `username` | `string` | Required | - |
| `first_name` | `string` | Required | - |
| `email` | `string` | Required | - |
| `is_staff` | `bool` | Required | - |
| `is_active` | `bool` | Required | - |
| `groups` | `List of int` | Required | - |
| `user_permissions` | `List of int` | Required | - |

## Example (as JSON)

```json
{
  "password": "probando1234",
  "is_superuser": false,
  "username": "insinnoBrainn12",
  "first_name": "brainn",
  "email": "probando@probando.es",
  "is_staff": true,
  "is_active": true,
  "groups": [
    3
  ],
  "user_permissions": [
    1,
    3
  ]
}
```

