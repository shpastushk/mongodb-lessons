1. Развернуть ВМ (Linux) с MongoDB (у вас ест ВМ в ВБ, лбой другой способ, в т.. докер)
через docker

```
$ docker compose up mongodb
```
```
$ docker exec -it mongodb bash
root@bc7ffdbe0ba8:/# 

root@bc7ffdbe0ba8:/# mongosh --port 27017 -u "admin" -p "admin"
Current Mongosh Log ID: 68ed27dfc108b3449d4f87fd
Connecting to:          mongodb://<credentials>@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.8
Using MongoDB:          8.0.14
Using Mongosh:          2.5.8

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

------
   The server generated these startup warnings when booting
   2025-10-13T16:20:33.586+00:00: For customers running the current memory allocator, we suggest changing the contents of the following sysfsFile
   2025-10-13T16:20:33.586+00:00: We suggest setting the contents of sysfsFile to 0.
   2025-10-13T16:20:33.586+00:00: vm.max_map_count is too low
   2025-10-13T16:20:33.586+00:00: We suggest setting swappiness to 0 or 1, as swapping can cause performance problems.
------

test> 
```

2. Создать 2 коллекии (10-20 строк) с товарами и складами их наличием
```
test> db.products.insertMany([
...    { "_id" : 1, "item" : "apples", "price" : 12 },
...    { "_id" : 2, "item" : "oranges", "price" : 20 },
...    { "_id" : 3, "item" : "mangos", "price" : 30 },
...    { "_id" : 5, "item" : "lemons", "price" : 10 },
...    { "_id" : 6, "item" : "pineapples", "price" : 14 },
...    { "_id" : 7, "item" : "potatoes", "price" : 60 },
...    { "_id" : 8, "item" : "limes", "price" : 21 },
...    { "_id" : 9, "item" : "cucumbers", "price" : 45 },
...    { "_id" : 10, "item" : "pecans", "price" : 33 },
... ])
{
  acknowledged: true,
  insertedIds: {
    '0': 1,
    '1': 2,
    '2': 3,
    '3': 5,
    '4': 6,
    '5': 7,
    '6': 8,
    '7': 9,
    '8': 10
  }
}
```

```
test> db.inventory.insertMany([
...    { "_id" : 1, "sku" : "apples", "instock" : 120 },
...    { "_id" : 2, "sku" : "oranges", "instock" : 80 },
...    { "_id" : 3, "sku" : "mangos", "instock" : 60 },
...    { "_id" : 4, "sku" : "lemons", "instock" : 70 },
...    { "_id" : 5, "sku" : "pineapples", "instock" : 120 },
...    { "_id" : 6, "sku" : "potatoes", "instock" : 80 },
...    { "_id" : 7, "sku" : "limes", "instock" : 60 },
...    { "_id" : 8, "sku" : "cucumbers", "instock" : 20 },
...    { "_id" : 9, "sku" : "cucumbers", "instock" : 30 },
...    { "_id" : 10, "sku" : "cucumbers", "instock" : 40 },
... ])
{
  acknowledged: true,
  insertedIds: {
    '0': 1,
    '1': 2,
    '2': 3,
    '3': 4,
    '4': 5,
    '5': 6,
    '6': 7,
    '7': 8,
    '8': 9,
    '9': 10
  }
}
```
3. Или написать Map Reduce по подсчёту количества товаров по наименованиям
(просуммировать с разных складов)

```
test> var mapProduct = function () {
...     emit(this.item, 0)
... };

test> var mapInventory= function () {
...     emit(this.sku, this.instock)
... };

test> var r = function(key, values) {
...     var total = 0
...     values.forEach(function(value) {
...         total+=value
...     });
...     return total;
... }

test> db.products.mapReduce(mapProduct, r, {out: {reduce: 'joined'}})
DeprecationWarning: Collection.mapReduce() is deprecated. Use an aggregation instead.
See https://mongodb.com/docs/manual/core/map-reduce for details.
{ result: 'joined', ok: 1 }
test> db.joined.find()
[
  { _id: 'pecans', value: 0 },
  { _id: 'pineapples', value: 0 },
  { _id: 'limes', value: 0 },
  { _id: 'oranges', value: 0 },
  { _id: 'apples', value: 0 },
  { _id: 'lemons', value: 0 },
  { _id: 'mangos', value: 0 },
  { _id: 'cucumbers', value: 0 },
  { _id: 'potatoes', value: 0 }
]
test> db.inventory.mapReduce(mapInventory, r, {out: {reduce: 'joined'}})
{ result: 'joined', ok: 1 }
test> db.joined.find()
[
  { _id: 'pecans', value: 0 },
  { _id: 'pineapples', value: 120 },
  { _id: 'limes', value: 60 },
  { _id: 'oranges', value: 80 },
  { _id: 'apples', value: 120 },
  { _id: 'lemons', value: 70 },
  { _id: 'mangos', value: 60 },
  { _id: 'cucumbers', value: 90 },
  { _id: 'potatoes', value: 80 }
]
```

4. Или реализовать на aggregation framework
```
test> db.products.aggregate([
    {
      $lookup:
        {
          localField: "item",
          from: "inventory",
          foreignField: "sku",
          as: "totals",
          pipeline : [
             {
             $group: {  
                 _id: 100, 
                 total: { $sum: "$instock"}              
               },
             },
            ],
        } 
    },
     { 
     $project: { _id: 0, product: "$item", all_count: "$totals.total" }
     }
 ])
[
  { product: 'apples', all_count: [ 120 ] },
  { product: 'oranges', all_count: [ 80 ] },
  { product: 'mangos', all_count: [ 60 ] },
  { product: 'lemons', all_count: [ 70 ] },
  { product: 'pineapples', all_count: [ 120 ] },
  { product: 'potatoes', all_count: [ 80 ] },
  { product: 'limes', all_count: [ 60 ] },
  { product: 'cucumbers', all_count: [ 90 ] },
  { product: 'pecans', all_count: [] }
]
```
5. Не забываем ВМ остановить/удалить
```
$ docker compose stop mongodb
WARN[0000] /lessons/mongodb/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Stopping 1/1
 ✔ Container mongodb  Stopped 
 ```
