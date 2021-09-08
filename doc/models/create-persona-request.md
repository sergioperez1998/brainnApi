
# Create Persona Request

## Structure

`CreatePersonaRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `codigo` | `int` | Required | - |
| `nombre` | `string` | Required | - |
| `apellido_1` | `string` | Required | - |
| `apellido_2` | `string` | Required | - |
| `activo` | `bool` | Required | - |
| `externo` | `bool` | Required | - |
| `advance` | `bool` | Required | - |
| `fecha_nacimiento` | `string` | Required | - |
| `foto` | `string` | Optional | - |
| `tipo_eval` | `string` | Required | - |
| `disponible` | `bool` | Required | - |
| `organizacion` | `int` | Required | - |
| `usuario` | `int` | Required | - |
| `centro_fisico` | `int` | Required | - |
| `movilidad` | `List of int` | Required | - |

## Example (as JSON)

```json
{
  "codigo": 117,
  "nombre": "brainn_persona2",
  "apellido1": "apellido1",
  "apellido2": "apellido2",
  "activo": true,
  "externo": false,
  "advance": false,
  "fecha_nacimiento": "1073-09-01",
  "foto": null,
  "tipo_eval": "B",
  "disponible": false,
  "organizacion": 1,
  "usuario": 2,
  "centro_fisico": 1,
  "movilidad": [
    4
  ]
}
```

