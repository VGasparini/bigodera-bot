# Alterações necessárias

## Formatação de resposta
Em todos os endpoints que atualmente usam a chave `'1'`, a resposta deverá vir na chave `data`
```diff
{
-    '1': 'abc...'
+    'data': 'abc...'
}
```

### Rota `/probleminha`
Agora será enviado sempre o seguinte payload
```json
{
    "id_telegram" = user_id,
    "rating": rating,
    "tags": tags
}
```
* Todos os campos serão do tipo `string`
* `rating` e `tags` poderão ser `null`, caso onde o usuário não informou esses dados

### Rota `/contador_cagada_pau++`
Endpoint agora deverá ser `/mais_uma_cagada` e deverá esperar um `POST`
Payload enviado será
```json
{
    "amount" = 1,
}
```
`amount` será um número inteiro. No momento será fixo 1

### Rota `/roll`
* Payload se mantém o mesmo
* Quando é excedido o limite de dados rolados, retornar um **STATUS_CODE - 403**
* A resposta quando sucedida deverá vir nesse formato
```json
{
    "dices": [
        "1": 5
        "2": 12
        ...
    ]
}

```

### Rota `/calculadora`
* Quando não for possível realizar o cálculo, devemos retornar um **STATUS_CODE - 403** informando a seguinte resposta
```json
{
    "msg": "Não foi possível computar"
}
```

Caso o cálculo seja efetuado, retornar no seguinte formato
```json
{
    "data": 42
}
```


