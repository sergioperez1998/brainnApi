
# Update User Request

## Structure

`UpdateUserRequest`

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
  "password": "probando123",
  "is_superuser": false,
  "username": "insinnoBrainn99",
  "first_name": "insinno",
  "email": "probando@probando.es",
  "is_staff": true,
  "is_active": false,
  "groups": [
    8
  ],
  "user_permissions": [
    9
  ]
}
```

