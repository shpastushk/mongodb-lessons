1. Развернуть ВМ (Linux) с MongoDB (у вас есть ВМ в ВБ, любой другой способ, в т.ч. докер)

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
$ docker exec -it mongodb bash
root@86ae5c6295fe:/# mongosh --port 27017 -u "admin" -p "admin"
Current Mongosh Log ID: 68fa5aba61a40331ac4f87fd
Connecting to:          mongodb://<credentials>@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.8
Using MongoDB:          8.0.14
Using Mongosh:          2.5.8

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

------
   The server generated these startup warnings when booting
   2025-10-23T16:40:26.920+00:00: For customers running the current memory allocator, we suggest changing the contents of the following sysfsFile
   2025-10-23T16:40:26.920+00:00: We suggest setting the contents of sysfsFile to 0.
   2025-10-23T16:40:26.920+00:00: vm.max_map_count is too low
   2025-10-23T16:40:26.920+00:00: We suggest setting swappiness to 0 or 1, as swapping can cause performance problems.
------

test>
```
2. Настроить аутентификацию и валидацию

Аутентификация

```
test> use history
switched to db history
history> db.createUser({      
...      user: "user1",      
...      pwd: "password1",      
...      roles: [{role: "readWrite",db: "history"}] 
... })
{ ok: 1 }
history> exit

root@86ae5c6295fe:/# mongosh history --port 27017 -u user1 -p password1 --authenticationDatabase "admin"
Current Mongosh Log ID: 68fa5bf1400e508eff4f87fd
Connecting to:          mongodb://<credentials>@127.0.0.1:27017/history?directConnection=true&serverSelectionTimeoutMS=2000&authSource=admin&appName=mongosh+2.5.8
MongoServerError: Authentication failed.

root@86ae5c6295fe:/# mongosh history --port 27017 -u user1 -p password1 --authenticationDatabase "history"
Current Mongosh Log ID: 68fa5bf7ee035f91374f87fd
Connecting to:          mongodb://<credentials>@127.0.0.1:27017/history?directConnection=true&serverSelectionTimeoutMS=2000&authSource=history&appName=mongosh+2.5.8
Using MongoDB:          8.0.14
Using Mongosh:          2.5.8

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

history> exit

root@86ae5c6295fe:/# mongosh admin --port 27017 -u user1 -p password1 --authenticationDatabase "history"
Current Mongosh Log ID: 68fa5c07ace98fa7054f87fd
Connecting to:          mongodb://<credentials>@127.0.0.1:27017/admin?directConnection=true&serverSelectionTimeoutMS=2000&authSource=history&appName=mongosh+2.5.8
Using MongoDB:          8.0.14
Using Mongosh:          2.5.8

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

admin> show collections
MongoServerError[Unauthorized]: not authorized on admin to execute command { listCollections: 1, filter: {}, cursor: {}, nameOnly: true, authorizedCollections: false, lsid: { id: UUID("862f7d1d-1ead-424d-a4a7-ad38aa62ee30") }, $db: "admin" }
```

3. Проверить как работает при экспорте/импорте данных
    a. список датасетов для загрузки (выбрать 1) - https://github.com/jdorfman/awesome-json-datasets

Загружаем https://api.github.com/events
```
root@5557b0132efc:/# mongoimport --port 27017 -d history -u user1 -p password1 -c github  --jsonArray --file /data/examples/github.bjson 
2025-10-23T17:24:25.235+0000    connected to: mongodb://localhost:27017/
2025-10-23T17:24:25.248+0000    30 document(s) imported successfully. 0 document(s) failed to import.
```

Смотрим что загрузили
```
history> db.github.find().count()
30
history> db.github.find().limit(1)
[
  {
    _id: ObjectId('68fa64c9e6a76ece6da14d39'),
    id: '5420214781',
    type: 'PushEvent',
    actor: {
      id: 46170177,
      login: 'macneale4',
      display_login: 'macneale4',
      gravatar_id: '',
      url: 'https://api.github.com/users/macneale4',
      avatar_url: 'https://avatars.githubusercontent.com/u/46170177?'
    },
    repo: {
      id: 198683574,
      name: 'dolthub/dolt',
      url: 'https://api.github.com/repos/dolthub/dolt'
    },
    payload: {
      repository_id: 198683574,
      push_id: Long('27710448373'),
      ref: 'refs/heads/macneale4/branch-activity-table',
      head: '05da38260b27e3d974b3d2ce570dae5c3590fbb0',
      before: 'b51c7b72c377215162aa60f1536f3e8972b615cd'
    },
    public: true,
    created_at: '2025-10-23T17:15:23Z',
    org: {
      id: 42156961,
      login: 'dolthub',
      gravatar_id: '',
      url: 'https://api.github.com/orgs/dolthub',
      avatar_url: 'https://avatars.githubusercontent.com/u/42156961?'
    }
  }
]
history> 
```

Добавляем валидацию

Есть два типа событий в коллекции

```
history> db.github.find({type: "PushEvent"}).count()
26
history> db.github.find({type: "CreateEvent"}).count()
4
history> db.github.find().count()
30
```

Добавим права
```
root@5557b0132efc:/# mongosh --port 27017 -u "admin" -p "admin"
Current Mongosh Log ID: 68fa6b5b711411f9814f87fd
Connecting to:          mongodb://<credentials>@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.8
Using MongoDB:          8.0.14
Using Mongosh:          2.5.8

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

------
   The server generated these startup warnings when booting
   2025-10-23T17:21:13.798+00:00: For customers running the current memory allocator, we suggest changing the contents of the following sysfsFile
   2025-10-23T17:21:13.798+00:00: We suggest setting the contents of sysfsFile to 0.
   2025-10-23T17:21:13.798+00:00: vm.max_map_count is too low
   2025-10-23T17:21:13.798+00:00: We suggest setting swappiness to 0 or 1, as swapping can cause performance problems.
------

test> use history
switched to db history
history>     db.grantRolesToUser(
...         "user1",
...         [
...             {role: "readWrite",db: "history"},
...             { role: "dbAdmin", db: "history" }
...         ]
...     );
{ ok: 1 }
```

Добавляем валидацию
```
history> db.runCommand( { collMod: "github",
...    validator: {
...       $jsonSchema : {
...          bsonType: "object",
...          properties: {
...             type: {
...                enum: [ "PushEvent"],
...                description: "required and must be PushEvent" }
...          }
...        }
... },
... validationLevel: "strict",
... validationAction: "error"
... })
{ ok: 1 }
  
```

При экспорте выгружаются все документы
```
root@5557b0132efc:/# mongoexport --port 27017 -d history -u user1 -p password1 -c github -o export.json
2025-10-23T17:55:57.545+0000    connected to: mongodb://localhost:27017/
2025-10-23T17:55:57.549+0000    exported 30 records
```

Удаляем все документы
```
history> db.github.deleteMany({})
{ acknowledged: true, deletedCount: 30 }
```

Выполняем импорт <br>
4 документа где type = CreateEvent не загрузились
```
root@5557b0132efc:/# mongoimport --port 27017 -d history -u user1 -p password1 -c github  --jsonArray --file /data/examples/github.bjson 
2025-10-23T17:58:08.329+0000    connected to: mongodb://localhost:27017/
2025-10-23T17:58:08.334+0000    continuing through error: Document failed validation
2025-10-23T17:58:08.334+0000    continuing through error: Document failed validation
2025-10-23T17:58:08.334+0000    continuing through error: Document failed validation
2025-10-23T17:58:08.334+0000    continuing through error: Document failed validation
2025-10-23T17:58:08.334+0000    26 document(s) imported successfully. 4 document(s) failed to import.
```

Проверяем

```
root@5557b0132efc:/# mongoimport --port 27017 -d history -u user1 -p password1 -c github  --jsonArray --file /data/examples/github.bjson 
2025-10-23T17:58:08.329+0000    connected to: mongodb://localhost:27017/
2025-10-23T17:58:08.334+0000    continuing through error: Document failed validation
2025-10-23T17:58:08.334+0000    continuing through error: Document failed validation
2025-10-23T17:58:08.334+0000    continuing through error: Document failed validation
2025-10-23T17:58:08.334+0000    continuing through error: Document failed validation
2025-10-23T17:58:08.334+0000    26 document(s) imported successfully. 4 document(s) failed to import.
root@5557b0132efc:/# mongosh history --port 27017 -u user1 -p password1 --authenticationDatabase "history"
Current Mongosh Log ID: 68fa6cf24b0773c7474f87fd
Connecting to:          mongodb://<credentials>@127.0.0.1:27017/history?directConnection=true&serverSelectionTimeoutMS=2000&authSource=history&appName=mongosh+2.5.8
Using MongoDB:          8.0.14
Using Mongosh:          2.5.8

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

history> db.github.find({type: {$ne: "PushEvent"}})

history> db.github.find({type: {$ne: "PushEvent"}}).count()
0
history> db.github.find({type: "PushEvent"}).count()
26
history> db.github.find().count()
26
history> 
```

4. Не забываем ВМ остановить/удалить
```
$ docker compose stop mongodb
WARN[0000] /lessons/mongodb/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Stopping 1/1
 ✔ Container mongodb  Stopped 
```
