1. Развернуть ВМ (Linux) с MongoDB (у вас ест ВМ в ВБ, лбой другой способ, в т.ч. докер)
```
$ docker compose up mongodb
```

```
$ docker exec -it mongodb bash
root@bc7ffdbe0ba8:/# mongosh --port 27017 -u "admin" -p "admin"
Current Mongosh Log ID: 68f3936c33319e774b4f87fd
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
2. Построить шардированный кластер из 3(2) кластерных нод (по 3 инстанса с репликацией
(мб арбитр)) и с кластером конфига(3 инстанса);

запуск репликсета 1
```
docker compose up mongodb-rs-1-init
WARN[0000] /lessons/mongodb/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] Found orphan containers ([mongodb]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up. 
[+] Running 4/4
 ✔ Container mongodb-rs103  Created                                                                                                                       0.0s 
 ✔ Container mongodb-rs101  Created                                                                                                                       0.1s 
 ✔ Container mongodb-rs102  Created                                                                                                                       0.1s 
 ✔ Container rs-1-init      Created                                                                                                                       0.1s 
Attaching to rs-1-init
rs-1-init  | MongoNetworkError: connect ECONNREFUSED 172.20.0.3:27017
rs-1-init  | waited for connection
rs-1-init  | {
rs-1-init  |   ok: 1,
rs-1-init  |   '$clusterTime': {
rs-1-init  |     clusterTime: Timestamp({ t: 1760810715, i: 1 }),
rs-1-init  |     signature: {
rs-1-init  |       hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
rs-1-init  |       keyId: Long('0')
rs-1-init  |     }
rs-1-init  |   },
rs-1-init  |   operationTime: Timestamp({ t: 1760810715, i: 1 })
rs-1-init  | }
rs-1-init exited with code 0
```

запуск репликсета 2
```
$ docker compose up mongodb-rs-2-init
WARN[0000] /lessons/mongodb/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] Found orphan containers ([mongodb]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up. 
[+] Running 4/4
 ✔ Container mongodb-rs203  Created                                                                                                                       0.1s 
 ✔ Container mongodb-rs201  Created                                                                                                                       0.0s 
 ✔ Container mongodb-rs202  Created                                                                                                                       0.1s 
 ✔ Container rs-2-init      Created                                                                                                                       0.1s 
Attaching to rs-2-init
rs-2-init  | MongoNetworkError: connect ECONNREFUSED 172.20.0.6:27027
rs-2-init  | waited for connection
rs-2-init  | {
rs-2-init  |   ok: 1,
rs-2-init  |   '$clusterTime': {
rs-2-init  |     clusterTime: Timestamp({ t: 1760810846, i: 1 }),
rs-2-init  |     signature: {
rs-2-init  |       hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
rs-2-init  |       keyId: Long('0')
rs-2-init  |     }
rs-2-init  |   },
rs-2-init  |   operationTime: Timestamp({ t: 1760810846, i: 1 })
rs-2-init  | }
rs-2-init exited with code 0
```

запуск конфигсета
```
$ docker compose up mongodb-cs-init
WARN[0000] /lessons/mongodb/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] Found orphan containers ([mongodb]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up. 
[+] Running 3/3
 ✔ Container mongodb-cs103  Created                                                                                                                       0.0s 
 ✔ Container mongodb-cs102  Created                                                                                                                       0.0s 
 ✔ Container cs-init        Created                                                                                                                       0.1s 
Attaching to cs-init
cs-init  | MongoNetworkError: connect ECONNREFUSED 172.20.0.9:27037
cs-init  | waited for connection
cs-init  | {
cs-init  |   ok: 1,
cs-init  |   '$clusterTime': {
cs-init  |     clusterTime: Timestamp({ t: 1760811544, i: 1 }),
cs-init  |     signature: {
cs-init  |       hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
cs-init  |       keyId: Long('0')
cs-init  |     }
cs-init  |   },
cs-init  |   operationTime: Timestamp({ t: 1760811544, i: 1 })
cs-init  | }
cs-init exited with code 0
```

Смотрим что получилось

```
$ docker exec -it mongodb-rs101 bash
root@cb0c2ef01efb:/# mongosh --port 27017                      
Current Mongosh Log ID: 68f7b5b4786e312d634f87fd
Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.8
Using MongoDB:          8.0.14
Using Mongosh:          2.5.8

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.

------
   The server generated these startup warnings when booting
   2025-10-18T18:05:09.938+00:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
   2025-10-18T18:05:09.938+00:00: For customers running the current memory allocator, we suggest changing the contents of the following sysfsFile
   2025-10-18T18:05:09.938+00:00: We suggest setting the contents of sysfsFile to 0.
   2025-10-18T18:05:09.938+00:00: vm.max_map_count is too low
   2025-10-18T18:05:09.938+00:00: We suggest setting swappiness to 0 or 1, as swapping can cause performance problems.
------

RS1 [direct: secondary] test>rs.status()
{
  set: 'RS1',
  date: ISODate('2025-10-21T16:33:44.999Z'),
  myState: 2,
  term: Long('20'),
  syncSourceHost: 'mongodb-rs102:28017',
  syncSourceId: 1,
  heartbeatIntervalMillis: Long('2000'),
  majorityVoteCount: 2,
  writeMajorityCount: 2,
  votingMembersCount: 3,
  writableVotingMembersCount: 3,
  optimes: {
    lastCommittedOpTime: { ts: Timestamp({ t: 1761064415, i: 1 }), t: Long('20') },
    lastCommittedWallTime: ISODate('2025-10-21T16:33:35.044Z'),
    readConcernMajorityOpTime: { ts: Timestamp({ t: 1761064415, i: 1 }), t: Long('20') },
    appliedOpTime: { ts: Timestamp({ t: 1761064415, i: 1 }), t: Long('20') },
    durableOpTime: { ts: Timestamp({ t: 1761064415, i: 1 }), t: Long('20') },
    writtenOpTime: { ts: Timestamp({ t: 1761064415, i: 1 }), t: Long('20') },
    lastAppliedWallTime: ISODate('2025-10-21T16:33:35.044Z'),
    lastDurableWallTime: ISODate('2025-10-21T16:33:35.044Z'),
    lastWrittenWallTime: ISODate('2025-10-21T16:33:35.044Z')
  },
  lastStableRecoveryTimestamp: Timestamp({ t: 1761064395, i: 1 }),
  electionParticipantMetrics: {
    votedForCandidate: true,
    electionTerm: Long('20'),
    lastVoteDate: ISODate('2025-10-21T07:22:18.231Z'),
    electionCandidateMemberId: 1,
    voteReason: '',
    lastWrittenOpTimeAtElection: { ts: Timestamp({ t: 1761029495, i: 1 }), t: Long('19') },
    maxWrittenOpTimeInSet: { ts: Timestamp({ t: 1761029495, i: 1 }), t: Long('19') },
    lastAppliedOpTimeAtElection: { ts: Timestamp({ t: 1761029495, i: 1 }), t: Long('19') },
    maxAppliedOpTimeInSet: { ts: Timestamp({ t: 1761029495, i: 1 }), t: Long('19') },
    priorityAtElection: 1,
    newTermStartDate: ISODate('2025-10-21T07:22:18.234Z'),
    newTermAppliedDate: ISODate('2025-10-21T07:22:18.239Z')
  },
  members: [
    {
      _id: 0,
      name: 'mongodb-rs101:27017',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 253715,
      optime: { ts: Timestamp({ t: 1761064415, i: 1 }), t: Long('20') },
      optimeDate: ISODate('2025-10-21T16:33:35.000Z'),
      optimeWritten: { ts: Timestamp({ t: 1761064415, i: 1 }), t: Long('20') },
      optimeWrittenDate: ISODate('2025-10-21T16:33:35.000Z'),
      lastAppliedWallTime: ISODate('2025-10-21T16:33:35.044Z'),
      lastDurableWallTime: ISODate('2025-10-21T16:33:35.044Z'),
      lastWrittenWallTime: ISODate('2025-10-21T16:33:35.044Z'),
      syncSourceHost: 'mongodb-rs102:28017',
      syncSourceId: 1,
      infoMessage: '',
      configVersion: 1,
      configTerm: 20,
      self: true,
      lastHeartbeatMessage: ''
    },
    {
      _id: 1,
      name: 'mongodb-rs102:28017',
      health: 1,
      state: 1,
      stateStr: 'PRIMARY',
      uptime: 90102,
      optime: { ts: Timestamp({ t: 1761064415, i: 1 }), t: Long('20') },
      optimeDurable: { ts: Timestamp({ t: 1761064415, i: 1 }), t: Long('20') },
      optimeWritten: { ts: Timestamp({ t: 1761064415, i: 1 }), t: Long('20') },
      optimeDate: ISODate('2025-10-21T16:33:35.000Z'),
      optimeDurableDate: ISODate('2025-10-21T16:33:35.000Z'),
      optimeWrittenDate: ISODate('2025-10-21T16:33:35.000Z'),
      lastAppliedWallTime: ISODate('2025-10-21T16:33:35.044Z'),
      lastDurableWallTime: ISODate('2025-10-21T16:33:35.044Z'),
      lastWrittenWallTime: ISODate('2025-10-21T16:33:35.044Z'),
      lastHeartbeat: ISODate('2025-10-21T16:33:43.548Z'),
      lastHeartbeatRecv: ISODate('2025-10-21T16:33:44.485Z'),
      pingMs: Long('0'),
      lastHeartbeatMessage: '',
      syncSourceHost: '',
      syncSourceId: -1,
      infoMessage: '',
      electionTime: Timestamp({ t: 1761031338, i: 1 }),
      electionDate: ISODate('2025-10-21T07:22:18.000Z'),
      configVersion: 1,
      configTerm: 20
    },
    {
      _id: 2,
      name: 'mongodb-rs103:29017',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 90102,
      optime: { ts: Timestamp({ t: 1761064415, i: 1 }), t: Long('20') },
      optimeDurable: { ts: Timestamp({ t: 1761064415, i: 1 }), t: Long('20') },
      optimeWritten: { ts: Timestamp({ t: 1761064415, i: 1 }), t: Long('20') },
      optimeDate: ISODate('2025-10-21T16:33:35.000Z'),
      optimeDurableDate: ISODate('2025-10-21T16:33:35.000Z'),
      optimeWrittenDate: ISODate('2025-10-21T16:33:35.000Z'),
      lastAppliedWallTime: ISODate('2025-10-21T16:33:35.044Z'),
      lastDurableWallTime: ISODate('2025-10-21T16:33:35.044Z'),
      lastWrittenWallTime: ISODate('2025-10-21T16:33:35.044Z'),
      lastHeartbeat: ISODate('2025-10-21T16:33:43.549Z'),
      lastHeartbeatRecv: ISODate('2025-10-21T16:33:43.939Z'),
      pingMs: Long('0'),
      lastHeartbeatMessage: '',
      syncSourceHost: 'mongodb-rs102:28017',
      syncSourceId: 1,
      infoMessage: '',
      configVersion: 1,
      configTerm: 20
    }
  ],
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761064415, i: 1 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761064415, i: 1 })
}
RS1 [direct: secondary] test >
```

3. Добавить балансировку, нагрузить данными, выбрать хороший ключ шардирования, посмотреть как данные перебалансирутся между шардами (stocks.zip)

Запуск mongosh

```
$ docker compose up mongodb-mongosh

$ docker exec -it mongodb-mongos bash
root@a0ba48608d9b:/# mongosh --port 27000 
Current Mongosh Log ID: 68f3dc833efcd1f4fb4f87fd
Connecting to:          mongodb://127.0.0.1:27000/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.8
Using MongoDB:          8.0.14
Using Mongosh:          2.5.8

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.

------
   The server generated these startup warnings when booting
   2025-10-18T18:27:26.225+00:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
   2025-10-18T18:27:26.225+00:00: This server is bound to localhost. Remote systems will be unable to connect to this server. Start the server with --bind_ip <address> to specify which IP addresses it should serve responses from, or with --bind_ip_all to bind to all interfaces. If this behavior is desired, start the server with --bind_ip 127.0.0.1 to disable this warning
------

[direct: mongos] test>
```

Добавляем два шарда

```
[direct: mongos] test> sh.addShard("RS1/mongodb-rs101:27017,mongodb-rs102:28017,mongodb-rs103:29017")
{
  shardAdded: 'RS1',
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761065025, i: 21 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761065025, i: 21 })
}

[direct: mongos] test> sh.addShard("RS2/mongodb-rs201:27027,mongodb-rs202:28027,mongodb-rs203:29027")
{
  shardAdded: 'RS2',
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761065143, i: 24 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761065143, i: 18 })
}
```

Проверяем статус

```
[direct: mongos] test> sh.status()
shardingVersion
{ _id: 1, clusterId: ObjectId('68f3da232623ffcc1464440b') }
---
shards
[
  {
    _id: 'RS1',
    host: 'RS1/mongodb-rs101:27017,mongodb-rs102:28017,mongodb-rs103:29017',
    state: 1,
    topologyTime: Timestamp({ t: 1761065025, i: 11 }),
    replSetConfigVersion: Long('-1')
  },
  {
    _id: 'RS2',
    host: 'RS2/mongodb-rs201:27027,mongodb-rs202:28027,mongodb-rs203:29027',
    state: 1,
    topologyTime: Timestamp({ t: 1761065143, i: 9 }),
    replSetConfigVersion: Long('-1')
  }
]
---
active mongoses
[ { '8.0.14': 1 } ]
---
autosplit
{ 'Currently enabled': 'yes' }
---
balancer
{
  'Currently enabled': 'yes',
  'Failed balancer rounds in last 5 attempts': 0,
  'Currently running': 'no',
  'Migration Results for the last 24 hours': 'No recent migrations'
}
---
shardedDataDistribution
[]
---
databases
[
  {
    database: { _id: 'config', primary: 'config', partitioned: true },
    collections: {}
  }
]
```

Включаем шардирование на бд

```
[direct: mongos] test> use bank
switched to db bank
[direct: mongos] bank> sh.enableSharding("bank")
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761065920, i: 9 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761065920, i: 6 })
}
[direct: mongos] bank>
```

Загружаем данные 

```
[direct: mongos] test> exit
root@ae92008ef076:/# ls /data/stocks
system.indexes.bson  values.bson
root@ae92008ef076:/# mongorestore --port 27000 /data/stocks/values.bson
2025-10-21T17:15:14.795+0000    checking for collection data in /data/stocks/values.bson
2025-10-21T17:15:14.835+0000    restoring stocks.values from /data/stocks/values.bson
2025-10-21T17:15:17.795+0000    [####....................]  stocks.values  123MB/715MB  (17.1%)
2025-10-21T17:15:20.795+0000    [#######.................]  stocks.values  225MB/715MB  (31.4%)
2025-10-21T17:15:23.795+0000    [##########..............]  stocks.values  320MB/715MB  (44.8%)
2025-10-21T17:15:26.798+0000    [#############...........]  stocks.values  406MB/715MB  (56.7%)
2025-10-21T17:15:29.796+0000    [################........]  stocks.values  500MB/715MB  (69.9%)
2025-10-21T17:15:32.794+0000    [###################.....]  stocks.values  596MB/715MB  (83.3%)
2025-10-21T17:15:35.794+0000    [######################..]  stocks.values  685MB/715MB  (95.8%)
2025-10-21T17:15:36.705+0000    [########################]  stocks.values  715MB/715MB  (100.0%)
2025-10-21T17:15:36.706+0000    finished restoring stocks.values (4308303 documents, 0 failures)
2025-10-21T17:15:36.707+0000    4308303 document(s) restored successfully. 0 document(s) failed to restore.
```

Проверяем что загрузили

```
[direct: mongos] test> show dbs
admin   144.00 KiB
config    2.41 MiB
stocks  290.78 MiB
[direct: mongos] test> use stocks
switched to db stocks
[direct: mongos] stocks> show collections
values
[direct: mongos] stocks> db.values.find().limit(1)
[
  {
    _id: ObjectId('4d094f58c96767d7a0099d49'),
    exchange: 'NASDAQ',
    stock_symbol: 'AACC',
    date: '2008-03-07',
    open: 8.4,
    high: 8.75,
    low: 8.08,
    close: 8.55,
    volume: 275800,
    'adj close': 8.55
  }
]
[direct: mongos] stocks> 
```

Ключом шардирования выбрала поле date

```
[direct: mongos] stocks> db.values.createIndex({date: 1})
date_1
[direct: mongos] stocks> sh.enableSharding("stocks")
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761067674, i: 1 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761067674, i: 1 })
}
[direct: mongos] stocks> sh.shardCollection("stocks.values",{ date: 1 })
{
  collectionsharded: 'stocks.values',
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761067715, i: 12 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761067715, i: 12 })
}
[direct: mongos] stocks>
```

Смотрим как данные разъехались

```
[direct: mongos] stocks> sh.status()
shardingVersion
{ _id: 1, clusterId: ObjectId('68f3da232623ffcc1464440b') }
---
shards
[
  {
    _id: 'RS1',
    host: 'RS1/mongodb-rs101:27017,mongodb-rs102:28017,mongodb-rs103:29017',
    state: 1,
    topologyTime: Timestamp({ t: 1761065025, i: 11 }),
    replSetConfigVersion: Long('-1')
  },
  {
    _id: 'RS2',
    host: 'RS2/mongodb-rs201:27027,mongodb-rs202:28027,mongodb-rs203:29027',
    state: 1,
    topologyTime: Timestamp({ t: 1761065143, i: 9 }),
    replSetConfigVersion: Long('-1')
  }
]
---
active mongoses
[ { '8.0.14': 1 } ]
---
autosplit
{ 'Currently enabled': 'yes' }
---
balancer
{
  'Currently enabled': 'yes',
  'Currently running': 'no',
  'Failed balancer rounds in last 5 attempts': 0,
  'Migration Results for the last 24 hours': { '2': 'Success' }
}
---
shardedDataDistribution
[
  {
    ns: 'config.system.sessions',
    shards: [
      {
        shardName: 'RS1',
        numOrphanedDocs: 0,
        numOwnedDocuments: 14,
        ownedSizeBytes: 1386,
        orphanedSizeBytes: 0
      }
    ]
  },
  {
    ns: 'stocks.values',
    shards: [
      {
        shardName: 'RS1',
        numOrphanedDocs: 0,
        numOwnedDocuments: 1541467,
        ownedSizeBytes: 268215258,
        orphanedSizeBytes: 0
      },
      {
        shardName: 'RS2',
        numOrphanedDocs: 1541467,
        numOwnedDocuments: 2766836,
        ownedSizeBytes: 481429464,
        orphanedSizeBytes: 268215258
      }
    ]
  }
]
---
databases
[
  {
    database: {
      _id: 'bank',
      primary: 'RS2',
      version: {
        uuid: UUID('3740ac2e-941b-402e-bbc9-07cd606c7929'),
        timestamp: Timestamp({ t: 1761065920, i: 3 }),
        lastMod: 1
      }
    },
    collections: {}
  },
  {
    database: { _id: 'config', primary: 'config', partitioned: true },
    collections: {
      'config.system.sessions': {
        shardKey: { _id: 1 },
        unique: false,
        balancing: true,
        chunkMetadata: [ { shard: 'RS1', nChunks: 1 } ],
        chunks: [
          { min: { _id: MinKey() }, max: { _id: MaxKey() }, 'on shard': 'RS1', 'last modified': Timestamp({ t: 1, i: 0 }) }
        ],
        tags: []
      }
    }
  },
  {
    database: {
      _id: 'stocks',
      primary: 'RS2',
      version: {
        uuid: UUID('2eac6d3e-a4c3-4bfa-9760-639b6ff9dc9f'),
        timestamp: Timestamp({ t: 1761066914, i: 3 }),
        lastMod: 1
      }
    },
    collections: {
      'stocks.values': {
        shardKey: { date: 1 },
        unique: false,
        balancing: true,
        chunkMetadata: [ { shard: 'RS1', nChunks: 2 }, { shard: 'RS2', nChunks: 1 } ],
        chunks: [
          { min: { date: MinKey() }, max: { date: '1996-08-06' }, 'on shard': 'RS1', 'last modified': Timestamp({ t: 2, i: 0 }) },
          { min: { date: '1996-08-06' }, max: { date: '2000-03-21' }, 'on shard': 'RS1', 'last modified': Timestamp({ t: 3, i: 0 }) },
          { min: { date: '2000-03-21' }, max: { date: MaxKey() }, 'on shard': 'RS2', 'last modified': Timestamp({ t: 3, i: 1 }) }
        ],
        tags: []
      }
    }
  }
]
```

4. Написат Map Reduce на ваше усмотрение для подсчёта агрегированных данных (Например аналог db.values.find({$where: '(this.open - this.close >
100)'},{"stock_symbol":1,"open":1,"close":1}) - заодно проверьте и скорость стандартного агрегатного запроса)

Считаем количество записей по дате через aggregate
```
[direct: mongos] stocks> db.values.aggregate([
   {
     $group: {
       _id: "$date",
       count: { $sum: 1 }
     },
   },
   {
       $out:  "dateAggregate1"      
   }
])
[direct: mongos] stocks> db.dateAggregate1.countDocuments({})
6290
[direct: mongos] stocks> db.dateAggregate1.find({_id: "1988-08-24"})
[ { _id: '1988-08-24', count: 106 } ]
[direct: mongos] stocks> db.dateAggregate1.find({_id: "1991-07-10"})
[ { _id: '1991-07-10', count: 251 } ]
```
Посмотрим план выполнения
```

[direct: mongos] stocks> db.values.explain("executionStats").aggregate([
   {
     $group: {
       _id: "$date",
       count: { $sum: 1 }
     },
   },
   {
       $out:  "dateAggregate1"      
   }
])

{
  serverInfo: {
    host: 'ae92008ef076',
    port: 27000,
    version: '8.0.14',
    gitVersion: 'bbdb887c2ac94424af0ee8fcaad39203bdf98671'
  },
  serverParameters: {
    internalQueryFacetBufferSizeBytes: 104857600,
    internalQueryFacetMaxOutputDocSizeBytes: 104857600,
    internalLookupStageIntermediateDocumentMaxSizeBytes: 104857600,
    internalDocumentSourceGroupMaxMemoryBytes: 104857600,
    internalQueryMaxBlockingSortMemoryUsageBytes: 104857600,
    internalQueryProhibitBlockingMergeOnMongoS: 0,
    internalQueryMaxAddToSetBytes: 104857600,
    internalDocumentSourceSetWindowFieldsMaxMemoryBytes: 104857600,
    internalQueryFrameworkControl: 'trySbeRestricted',
    internalQueryPlannerIgnoreIndexWithCollationForRegex: 1
  },
  mergeType: 'specificShard',
  mergeShardId: 'RS2',
  splitPipeline: {
    shardsPart: [
      {
        '$group': { _id: '$date', count: { '$sum': { '$const': 1 } } }
      }
    ],
    mergerPart: [
      {
        '$mergeCursors': {
          lsid: {
            id: UUID('137796e7-0657-4def-a1dc-f20f3b4e6c3d'),
            uid: Binary.createFromBase64('47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=', 0)
          },
          compareWholeSortKey: false,
          tailableMode: 'normal',
          nss: 'stocks.values',
          allowPartialResults: false,
          recordRemoteOpWaitTime: false,
          requestQueryStatsFromRemotes: false
        }
      },
      {
        '$group': {
          _id: '$$ROOT._id',
          count: { '$sum': '$$ROOT.count' },
          '$doingMerge': true
        }
      },
      { '$out': { coll: 'dateAggregate1', db: 'stocks' } }
    ]
  },
  shards: {
    RS1: {
      host: 'mongodb-rs102:28017',
      explainVersion: '2',
      queryPlanner: {
        namespace: 'stocks.values',
        parsedQuery: {},
        indexFilterSet: false,
        queryHash: '96AB8260',
        planCacheShapeHash: '96AB8260',
        planCacheKey: '77433B40',
        optimizationTimeMillis: 1,
        optimizedPipeline: true,
        maxIndexedOrSolutionsReached: false,
        maxIndexedAndSolutionsReached: false,
        maxScansToExplodeReached: false,
        prunedSimilarIndexes: false,
        winningPlan: {
          isCached: false,
          queryPlan: {
            stage: 'GROUP',
            planNodeId: 4,
            inputStage: {
              stage: 'SHARDING_FILTER',
              planNodeId: 2,
              inputStage: {
                stage: 'COLLSCAN',
                planNodeId: 1,
                filter: {},
                direction: 'forward'
              }
            }
          },
          slotBasedPlan: {
            slots: '$$RESULT=s9 env: { s1 = ShardFilterer (shardFilterer) }',
            stages: '[4] project [s9 = newBsonObj("_id", s6, "count", s8)] \n' +
              '[4] project [s8 = doubleDoublePartialSumFinalize(convertSimpleSumToDoubleDoubleSum((convert ( s7, int32) ?: s7)))] \n' +
              '[4] group [s6] [s7 = count()] spillSlots[s5] mergingExprs[sum(s5)] \n' +
              '[4] project [s6 = (s2 ?: null)] \n' +
              '[2] filter {shardFilter(s1, makeBsonObj(MakeObjSpec([date = Add(0)], Open), Nothing, false, (s2 ?: null)))} \n' +
              '[1] scan s3 s4 none none none none none none lowPriority [s2 = date] @"cc031e4a-d430-44ca-a2b1-8d9683406cab" true false '
          }
        },
        rejectedPlans: []
      },
      executionStats: {
        executionSuccess: true,
        nReturned: 4287,
        executionTimeMillis: 694,
        totalKeysExamined: 0,
        totalDocsExamined: 1541467,
        executionStages: {
          stage: 'project',
          planNodeId: 4,
          nReturned: 4287,
          executionTimeMillisEstimate: 689,
          opens: 1,
          closes: 1,
          saveState: 46,
          restoreState: 46,
          isEOF: 1,
          projections: { '9': 'newBsonObj("_id", s6, "count", s8) ' },
          inputStage: {
            stage: 'project',
            planNodeId: 4,
            nReturned: 4287,
            executionTimeMillisEstimate: 689,
            opens: 1,
            closes: 1,
            saveState: 46,
            restoreState: 46,
            isEOF: 1,
            projections: {
              '8': 'doubleDoublePartialSumFinalize(convertSimpleSumToDoubleDoubleSum((convert ( s7, int32) ?: s7))) '
            },
            inputStage: {
              stage: 'group',
              planNodeId: 4,
              nReturned: 4287,
              executionTimeMillisEstimate: 689,
              opens: 1,
              closes: 1,
              saveState: 46,
              restoreState: 46,
              isEOF: 1,
              groupBySlots: [ Long('6') ],
              expressions: { '7': 'count() ', initExprs: { '7': null } },
              mergingExprs: { '5': 'sum(s5) ' },
              usedDisk: false,
              spills: 0,
              spilledBytes: 0,
              spilledRecords: 0,
              spilledDataStorageSize: 0,
              inputStage: {
                stage: 'project',
                planNodeId: 4,
                nReturned: 1541467,
                executionTimeMillisEstimate: 589,
                opens: 1,
                closes: 1,
                saveState: 46,
                restoreState: 46,
                isEOF: 1,
                projections: { '6': '(s2 ?: null) ' },
                inputStage: {
                  stage: 'filter',
                  planNodeId: 2,
                  nReturned: 1541467,
                  executionTimeMillisEstimate: 543,
                  opens: 1,
                  closes: 1,
                  saveState: 46,
                  restoreState: 46,
                  isEOF: 1,
                  numTested: 1541467,
                  filter: 'shardFilter(s1, makeBsonObj(MakeObjSpec([date = Add(0)], Open), Nothing, false, (s2 ?: null))) ',
                  inputStage: {
                    stage: 'scan',
                    planNodeId: 1,
                    nReturned: 1541467,
                    executionTimeMillisEstimate: 297,
                    opens: 1,
                    closes: 1,
                    saveState: 46,
                    restoreState: 46,
                    isEOF: 1,
                    numReads: 1541467,
                    recordSlot: 3,
                    recordIdSlot: 4,
                    scanFieldNames: [ 'date' ],
                    scanFieldSlots: [ Long('2') ]
                  }
                }
              }
            }
          }
        }
      }
    },
    RS2: {
      host: 'mongodb-rs201:27027',
      explainVersion: '2',
      queryPlanner: {
        namespace: 'stocks.values',
        parsedQuery: {},
        indexFilterSet: false,
        queryHash: '96AB8260',
        planCacheShapeHash: '96AB8260',
        planCacheKey: '77433B40',
        optimizationTimeMillis: 1,
        optimizedPipeline: true,
        maxIndexedOrSolutionsReached: false,
        maxIndexedAndSolutionsReached: false,
        maxScansToExplodeReached: false,
        prunedSimilarIndexes: false,
        winningPlan: {
          isCached: false,
          queryPlan: {
            stage: 'GROUP',
            planNodeId: 4,
            inputStage: {
              stage: 'SHARDING_FILTER',
              planNodeId: 2,
              inputStage: {
                stage: 'COLLSCAN',
                planNodeId: 1,
                filter: {},
                direction: 'forward'
              }
            }
          },
          slotBasedPlan: {
            slots: '$$RESULT=s9 env: { s1 = ShardFilterer (shardFilterer) }',
            stages: '[4] project [s9 = newBsonObj("_id", s6, "count", s8)] \n' +
              '[4] project [s8 = doubleDoublePartialSumFinalize(convertSimpleSumToDoubleDoubleSum((convert ( s7, int32) ?: s7)))] \n' +
              '[4] group [s6] [s7 = count()] spillSlots[s5] mergingExprs[sum(s5)] \n' +
              '[4] project [s6 = (s2 ?: null)] \n' +
              '[2] filter {shardFilter(s1, makeBsonObj(MakeObjSpec([date = Add(0)], Open), Nothing, false, (s2 ?: null)))} \n' +
              '[1] scan s3 s4 none none none none none none lowPriority [s2 = date] @"cc031e4a-d430-44ca-a2b1-8d9683406cab" true false '
          }
        },
        rejectedPlans: []
      },
      executionStats: {
        executionSuccess: true,
        nReturned: 2003,
        executionTimeMillis: 1234,
        totalKeysExamined: 0,
        totalDocsExamined: 2766836,
        executionStages: {
          stage: 'project',
          planNodeId: 4,
          nReturned: 2003,
          executionTimeMillisEstimate: 1224,
          opens: 1,
          closes: 1,
          saveState: 79,
          restoreState: 79,
          isEOF: 1,
          projections: { '9': 'newBsonObj("_id", s6, "count", s8) ' },
          inputStage: {
            stage: 'project',
            planNodeId: 4,
            nReturned: 2003,
            executionTimeMillisEstimate: 1224,
            opens: 1,
            closes: 1,
            saveState: 79,
            restoreState: 79,
            isEOF: 1,
            projections: {
              '8': 'doubleDoublePartialSumFinalize(convertSimpleSumToDoubleDoubleSum((convert ( s7, int32) ?: s7))) '
            },
            inputStage: {
              stage: 'group',
              planNodeId: 4,
              nReturned: 2003,
              executionTimeMillisEstimate: 1224,
              opens: 1,
              closes: 1,
              saveState: 79,
              restoreState: 79,
              isEOF: 1,
              groupBySlots: [ Long('6') ],
              expressions: { '7': 'count() ', initExprs: { '7': null } },
              mergingExprs: { '5': 'sum(s5) ' },
              usedDisk: false,
              spills: 0,
              spilledBytes: 0,
              spilledRecords: 0,
              spilledDataStorageSize: 0,
              inputStage: {
                stage: 'project',
                planNodeId: 4,
                nReturned: 2766836,
                executionTimeMillisEstimate: 1021,
                opens: 1,
                closes: 1,
                saveState: 79,
                restoreState: 79,
                isEOF: 1,
                projections: { '6': '(s2 ?: null) ' },
                inputStage: {
                  stage: 'filter',
                  planNodeId: 2,
                  nReturned: 2766836,
                  executionTimeMillisEstimate: 987,
                  opens: 1,
                  closes: 1,
                  saveState: 79,
                  restoreState: 79,
                  isEOF: 1,
                  numTested: 2766836,
                  filter: 'shardFilter(s1, makeBsonObj(MakeObjSpec([date = Add(0)], Open), Nothing, false, (s2 ?: null))) ',
                  inputStage: {
                    stage: 'scan',
                    planNodeId: 1,
                    nReturned: 2766836,
                    executionTimeMillisEstimate: 697,
                    opens: 1,
                    closes: 1,
                    saveState: 79,
                    restoreState: 79,
                    isEOF: 1,
                    numReads: 2766836,
                    recordSlot: 3,
                    recordIdSlot: 4,
                    scanFieldNames: [ 'date' ],
                    scanFieldSlots: [ Long('2') ]
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  queryShapeHash: '8EB01BDF1A1033B0E907C75671F02EBA8D499328AFF7317D47D11D8E47E03130',
  command: {
    aggregate: 'values',
    pipeline: [
      { '$group': { _id: '$date', count: { '$sum': 1 } } },
      { '$out': 'dateAggregate1' }
    ],
    cursor: {}
  },
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761070718, i: 1 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761070716, i: 1 })
}
[direct: mongos] stocks>
```

Считаем количество записей по дате через mapReduces
```
[direct: mongos] stocks> var mapItem = function () {
...     emit(this.date, 1)
... };

[direct: mongos] stocks> var reduceFunction = function(key, values) {
...   return Array.sum(values);
... };

[direct: mongos] stocks> db.values.mapReduce(
   mapItem,
   reduceFunction,
   {
     out: { merge: "dateAggregate" }
   }
 );
{
  result: 'dateAggregate',
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761069463, i: 6290 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761069463, i: 6290 })
}
[direct: mongos] stocks> db.dateAggregate.find().limit(10)
[
  { _id: '1996-07-24', value: 679 },
  { _id: '1995-04-26', value: 531 },
  { _id: '1988-12-07', value: 108 },
  { _id: '1990-05-17', value: 240 },
  { _id: '1998-12-17', value: 881 },
  { _id: '1996-11-21', value: 706 },
  { _id: '2004-12-02', value: 1424 },
  { _id: '1995-12-11', value: 618 },
  { _id: '1987-07-30', value: 92 },
  { _id: '2006-07-18', value: 1594 }
]
[direct: mongos] stocks> db.dateAggregate.find({_id: "1988-08-24"})
[ { _id: '1988-08-24', value: 106 } ]
[direct: mongos] stocks> db.dateAggregate.find({_id: "1991-07-10"})
[ { _id: '1991-07-10', value: 251 } ]
[direct: mongos] stocks> 
```

Смотрим план выполнения
```
[direct: mongos] stocks> db.values.explain("executionStats").mapReduce(
...    mapItem,
...    reduceFunction,
...    {
...      out: { merge: "dateAggregate" }
...    }
...  );
{
  serverInfo: {
    host: 'ae92008ef076',
    port: 27000,
    version: '8.0.14',
    gitVersion: 'bbdb887c2ac94424af0ee8fcaad39203bdf98671'
  },
  serverParameters: {
    internalQueryFacetBufferSizeBytes: 104857600,
    internalQueryFacetMaxOutputDocSizeBytes: 104857600,
    internalLookupStageIntermediateDocumentMaxSizeBytes: 104857600,
    internalDocumentSourceGroupMaxMemoryBytes: 104857600,
    internalQueryMaxBlockingSortMemoryUsageBytes: 104857600,
    internalQueryProhibitBlockingMergeOnMongoS: 0,
    internalQueryMaxAddToSetBytes: 104857600,
    internalDocumentSourceSetWindowFieldsMaxMemoryBytes: 104857600,
    internalQueryFrameworkControl: 'trySbeRestricted',
    internalQueryPlannerIgnoreIndexWithCollationForRegex: 1
  },
  mergeType: 'specificShard',
  mergeShardId: 'RS2',
  splitPipeline: {
    shardsPart: [
      {
        '$project': {
          emits: {
            '$_internalJsEmit': {
              eval: 'function () {\n    emit(this.date, 1)\n}',
              this: '$$ROOT'
            }
          },
          _id: false
        }
      },
      { '$unwind': { path: '$emits' } },
      {
        '$group': {
          _id: '$emits.k',
          value: {
            '$_internalJsReduce': {
              data: '$emits',
              eval: 'function(key, values) {\n  return Array.sum(values);\n}'
            }
          }
        }
      }
    ],
    mergerPart: [
      {
        '$mergeCursors': {
          lsid: {
            id: UUID('137796e7-0657-4def-a1dc-f20f3b4e6c3d'),
            uid: Binary.createFromBase64('47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=', 0)
          },
          compareWholeSortKey: false,
          tailableMode: 'normal',
          nss: 'stocks.values',
          allowPartialResults: false,
          recordRemoteOpWaitTime: false,
          requestQueryStatsFromRemotes: false
        }
      },
      {
        '$group': {
          _id: '$$ROOT._id',
          value: {
            '$_internalJsReduce': {
              data: '$$ROOT.value',
              eval: 'function(key, values) {\n  return Array.sum(values);\n}'
            }
          },
          '$doingMerge': true
        }
      },
      {
        '$merge': {
          into: { db: 'stocks', coll: 'dateAggregate' },
          on: '_id',
          whenMatched: 'replace',
          whenNotMatched: 'insert'
        }
      }
    ]
  },
  shards: {
    RS1: {
      host: 'mongodb-rs102:28017',
      explainVersion: '1',
      stages: [
        {
          '$cursor': {
            queryPlanner: {
              namespace: 'stocks.values',
              parsedQuery: {},
              indexFilterSet: false,
              queryHash: '8F2383EE',
              planCacheShapeHash: '8F2383EE',
              planCacheKey: '7DF350EE',
              optimizationTimeMillis: 0,
              maxIndexedOrSolutionsReached: false,
              maxIndexedAndSolutionsReached: false,
              maxScansToExplodeReached: false,
              prunedSimilarIndexes: false,
              winningPlan: [Object],
              rejectedPlans: []
            },
            executionStats: {
              executionSuccess: true,
              nReturned: 1541467,
              executionTimeMillis: 4044,
              totalKeysExamined: 0,
              totalDocsExamined: 1541467,
              executionStages: [Object]
            }
          },
          nReturned: Long('1541467'),
          executionTimeMillisEstimate: Long('3838')
        },
        {
          '$unwind': { path: '$emits' },
          nReturned: Long('1541467'),
          executionTimeMillisEstimate: Long('3903')
        },
        {
          '$group': {
            _id: '$emits.k',
            value: { '$_internalJsReduce': [Object] }
          },
          maxAccumulatorMemoryUsageBytes: { value: Long('25177912') },
          totalOutputDataSizeBytes: Long('2100630'),
          usedDisk: false,
          spills: Long('0'),
          spilledDataStorageSize: Long('0'),
          numBytesSpilledEstimate: Long('0'),
          spilledRecords: Long('0'),
          nReturned: Long('4287'),
          executionTimeMillisEstimate: Long('4042')
        }
      ]
    },
    RS2: {
      host: 'mongodb-rs201:27027',
      explainVersion: '1',
      stages: [
        {
          '$cursor': {
            queryPlanner: {
              namespace: 'stocks.values',
              parsedQuery: {},
              indexFilterSet: false,
              queryHash: '8F2383EE',
              planCacheShapeHash: '8F2383EE',
              planCacheKey: '7DF350EE',
              optimizationTimeMillis: 0,
              maxIndexedOrSolutionsReached: false,
              maxIndexedAndSolutionsReached: false,
              maxScansToExplodeReached: false,
              prunedSimilarIndexes: false,
              winningPlan: [Object],
              rejectedPlans: []
            },
            executionStats: {
              executionSuccess: true,
              nReturned: 2766836,
              executionTimeMillis: 7312,
              totalKeysExamined: 0,
              totalDocsExamined: 2766836,
              executionStages: [Object]
            }
          },
          nReturned: Long('2766836'),
          executionTimeMillisEstimate: Long('6927')
        },
        {
          '$unwind': { path: '$emits' },
          nReturned: Long('2766836'),
          executionTimeMillisEstimate: Long('7012')
        },
        {
          '$group': {
            _id: '$emits.k',
            value: { '$_internalJsReduce': [Object] }
          },
          maxAccumulatorMemoryUsageBytes: { value: Long('44509736') },
          totalOutputDataSizeBytes: Long('981470'),
          usedDisk: false,
          spills: Long('0'),
          spilledDataStorageSize: Long('0'),
          numBytesSpilledEstimate: Long('0'),
          spilledRecords: Long('0'),
          nReturned: Long('2003'),
          executionTimeMillisEstimate: Long('7309')
        }
      ]
    }
  },
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761069771, i: 1 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761069766, i: 1 })
}
[direct: mongos] stocks>
```
через aggregate посчиталось быстрей 

5. Не забываем ВМ остановить/удалить
```
$ docker compose stop
WARN[0000] /lessons/mongodb/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Stopping 13/13
 ✔ Container rs-2-init       Stopped                                                                                                                        0.0s 
 ✔ Container cs-init         Stopped                                                                                                                        0.0s 
 ✔ Container rs-1-init       Stopped                                                                                                                        0.0s 
 ✔ Container mongodb-mongos  Stopped                                                                                                                        0.0s 
 ✔ Container mongodb-rs102   Stopped                                                                                                                       10.9s 
 ✔ Container mongodb-cs102   Stopped                                                                                                                       10.8s 
 ✔ Container mongodb-rs101   Stopped                                                                                                                       11.0s 
 ✔ Container mongodb-rs103   Stopped                                                                                                                       11.0s 
 ✔ Container mongodb-cs103   Stopped                                                                                                                       10.7s 
 ✔ Container mongodb-cs101   Stopped                                                                                                                       10.8s 
 ✔ Container mongodb-rs202   Stopped                                                                                                                       11.2s 
 ✔ Container mongodb-rs201   Stopped                                                                                                                       11.2s 
 ✔ Container mongodb-rs203   Stopped 
 ```