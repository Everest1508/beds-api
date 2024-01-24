
## API Reference

#### Get all Data

```http
  GET https://bedsapi.pythonanywhere.com/beds/?format=json
```



#### Get Data

```http
  GET https://bedsapi.pythonanywhere.com/get_bed/{id}?format=json
```

| Parameter | Type     |
| :-------- | :------- |
| `bed_id` | `int` |


#### Insert Data

```http
  POST https://bedsapi.pythonanywhere.com/beds/
```

| Parameter | Type     |
| :-------- | :------- |
| `is_occuipied` | `boolean` |
| `patient_name` | `string` |
| `medication` | `string` |

#### DELETE BED

```http
  DELETE https://bedsapi.pythonanywhere.com/get_bed/{id}
```

