1. Развернуть Mongodb

через docker

```
version: '3.7'

services:
  mongodb:
    image: mongo:latest
    container_name: mongodb
    ports:
      - 27017:27017
    volumes:
      - ./mongodata:/data/db
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: admin
    restart: always
```

```
$ docker compose up mongodb
```
```
$ docker exec -it mongodb bash
root@bc7ffdbe0ba8:/#
```
```
root@bc7ffdbe0ba8:/# mongod --version
db version v8.0.14
Build Info: {
    "version": "8.0.14",
    "gitVersion": "bbdb887c2ac94424af0ee8fcaad39203bdf98671",
    "openSSLVersion": "OpenSSL 3.0.13 30 Jan 2024",
    "modules": [],
    "allocator": "tcmalloc-google",
    "environment": {
        "distmod": "ubuntu2404",
        "distarch": "aarch64",
        "target_arch": "aarch64"
    }
}
```
```
root@bc7ffdbe0ba8:/# mongosh --port 27017 -u "admin" -p "admin"
Current Mongosh Log ID: 68dbad916ac062a70b4f87fd
Connecting to:          mongodb://<credentials>@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.8
Using MongoDB:          8.0.14
Using Mongosh:          2.5.8

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

------
   The server generated these startup warnings when booting
   2025-09-30T09:57:23.331+00:00: For customers running the current memory allocator, we suggest changing the contents of the following sysfsFile
   2025-09-30T09:57:23.331+00:00: We suggest setting the contents of sysfsFile to 0.
   2025-09-30T09:57:23.331+00:00: vm.max_map_count is too low
   2025-09-30T09:57:23.331+00:00: We suggest setting swappiness to 0 or 1, as swapping can cause performance problems.
------

test> 
```
2. Создать коллекцию со случайным количеством элементов
```
test> for ( i = 0; i < Math.random()*100; ++i ) {
      db.mydocs.insertOne( { key: i, random_point: [Math.random(), Math.random()] } );
}
{
  acknowledged: true,
  insertedId: ObjectId('68dbb0426ac062a70b4f8824')
}
```
3. Посчитать количество элементов
```
test> db.mydocs.countDocuments({});
10
```

```
test> db.mydocs.find()
[
  {
    _id: ObjectId('68dbb0426ac062a70b4f881b'),
    key: 0,
    random_point: [ 0.394096590361412, 0.5490916098273382 ]
  },
  {
    _id: ObjectId('68dbb0426ac062a70b4f881c'),
    key: 1,
    random_point: [ 0.0431320865956526, 0.5841926577117365 ]
  },
  {
    _id: ObjectId('68dbb0426ac062a70b4f881d'),
    key: 2,
    random_point: [ 0.20328091520720637, 0.14541570559892603 ]
  },
  {
    _id: ObjectId('68dbb0426ac062a70b4f881e'),
    key: 3,
    random_point: [ 0.06044001355632522, 0.195463003583779 ]
  },
  {
    _id: ObjectId('68dbb0426ac062a70b4f881f'),
    key: 4,
    random_point: [ 0.4344204584739302, 0.24577711618465092 ]
  },
  {
    _id: ObjectId('68dbb0426ac062a70b4f8820'),
    key: 5,
    random_point: [ 0.2063962156199901, 0.28028590006301957 ]
  },
  {
    _id: ObjectId('68dbb0426ac062a70b4f8821'),
    key: 6,
    random_point: [ 0.4549441366647409, 0.005796224123790772 ]
  },
  {
    _id: ObjectId('68dbb0426ac062a70b4f8822'),
    key: 7,
    random_point: [ 0.9273398007398166, 0.6584268490832403 ]
  },
  {
    _id: ObjectId('68dbb0426ac062a70b4f8823'),
    key: 8,
    random_point: [ 0.34204669613942484, 0.30038026098323733 ]
  },
  {
    _id: ObjectId('68dbb0426ac062a70b4f8824'),
    key: 9,
    random_point: [ 0.44071525511865706, 0.8451042284577561 ]
  }
]
```
4. Не забываем ВМ остановить/удалить
```
$ docker compose stop mongodb
WARN[0000] /Users/korotkova.a34/Documents/lessons/mongodb/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Stopping 1/1
 ✔ Container mongodb  Stopped
```
   
