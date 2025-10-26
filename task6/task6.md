1. Развернуть 2 шарда по 2(3) реплики (не забываем про КС) + 1 Mongos

Запускаем ReplicaSet1, ReplicaSet2, ConfigSet1

RS1
```
$ docker exec -it mongodb-rs101 bash
[mongodb@26b8bdb4bcb2 /]$ mongosh --port 27017
Current Mongosh Log ID: 68fceb34cf729d3fd634de76
Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.2
Using MongoDB:          8.0.4-1
Using Mongosh:          2.3.2

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.

test>   rs.initiate({"_id" : "RS1", members : [{"_id" : 0, priority : 3, host : "mongodb-rs101:27017"},{"_id" : 1, host : "mongodb-rs102:28017"},{"_id" : 2, host : "mongodb-rs103:29017"}]});
{ ok: 1 }
RS1 [direct: secondary] test> rs.status()
{
  set: 'RS1',
  date: ISODate('2025-10-25T15:25:23.481Z'),
  myState: 1,
  term: Long('1'),
  syncSourceHost: '',
  syncSourceId: -1,
  heartbeatIntervalMillis: Long('2000'),
  majorityVoteCount: 2,
  writeMajorityCount: 2,
  votingMembersCount: 3,
  writableVotingMembersCount: 3,
  optimes: {
    lastCommittedOpTime: { ts: Timestamp({ t: 1761405911, i: 15 }), t: Long('1') },
    lastCommittedWallTime: ISODate('2025-10-25T15:25:11.428Z'),
    readConcernMajorityOpTime: { ts: Timestamp({ t: 1761405911, i: 15 }), t: Long('1') },
    appliedOpTime: { ts: Timestamp({ t: 1761405911, i: 15 }), t: Long('1') },
    durableOpTime: { ts: Timestamp({ t: 1761405911, i: 15 }), t: Long('1') },
    writtenOpTime: { ts: Timestamp({ t: 1761405911, i: 15 }), t: Long('1') },
    lastAppliedWallTime: ISODate('2025-10-25T15:25:11.428Z'),
    lastDurableWallTime: ISODate('2025-10-25T15:25:11.428Z'),
    lastWrittenWallTime: ISODate('2025-10-25T15:25:11.428Z')
  },
  lastStableRecoveryTimestamp: Timestamp({ t: 1761405901, i: 1 }),
  electionCandidateMetrics: {
    lastElectionReason: 'electionTimeout',
    lastElectionDate: ISODate('2025-10-25T15:25:11.318Z'),
    electionTerm: Long('1'),
    lastCommittedOpTimeAtElection: { ts: Timestamp({ t: 1761405901, i: 1 }), t: Long('-1') },
    lastSeenWrittenOpTimeAtElection: { ts: Timestamp({ t: 1761405901, i: 1 }), t: Long('-1') },
    lastSeenOpTimeAtElection: { ts: Timestamp({ t: 1761405901, i: 1 }), t: Long('-1') },
    numVotesNeeded: 2,
    priorityAtElection: 3,
    electionTimeoutMillis: Long('10000'),
    numCatchUpOps: Long('0'),
    newTermStartDate: ISODate('2025-10-25T15:25:11.365Z'),
    wMajorityWriteAvailabilityDate: ISODate('2025-10-25T15:25:11.837Z')
  },
  members: [
    {
      _id: 0,
      name: 'mongodb-rs101:27017',
      health: 1,
      state: 1,
      stateStr: 'PRIMARY',
      uptime: 241,
      optime: { ts: Timestamp({ t: 1761405911, i: 15 }), t: Long('1') },
      optimeDate: ISODate('2025-10-25T15:25:11.000Z'),
      optimeWritten: { ts: Timestamp({ t: 1761405911, i: 15 }), t: Long('1') },
      optimeWrittenDate: ISODate('2025-10-25T15:25:11.000Z'),
      lastAppliedWallTime: ISODate('2025-10-25T15:25:11.428Z'),
      lastDurableWallTime: ISODate('2025-10-25T15:25:11.428Z'),
      lastWrittenWallTime: ISODate('2025-10-25T15:25:11.428Z'),
      syncSourceHost: '',
      syncSourceId: -1,
      infoMessage: 'Could not find member to sync from',
      electionTime: Timestamp({ t: 1761405911, i: 1 }),
      electionDate: ISODate('2025-10-25T15:25:11.000Z'),
      configVersion: 1,
      configTerm: 1,
      self: true,
      lastHeartbeatMessage: ''
    },
    {
      _id: 1,
      name: 'mongodb-rs102:28017',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 22,
      optime: { ts: Timestamp({ t: 1761405911, i: 15 }), t: Long('1') },
      optimeDurable: { ts: Timestamp({ t: 1761405911, i: 15 }), t: Long('1') },
      optimeWritten: { ts: Timestamp({ t: 1761405911, i: 15 }), t: Long('1') },
      optimeDate: ISODate('2025-10-25T15:25:11.000Z'),
      optimeDurableDate: ISODate('2025-10-25T15:25:11.000Z'),
      optimeWrittenDate: ISODate('2025-10-25T15:25:11.000Z'),
      lastAppliedWallTime: ISODate('2025-10-25T15:25:11.428Z'),
      lastDurableWallTime: ISODate('2025-10-25T15:25:11.428Z'),
      lastWrittenWallTime: ISODate('2025-10-25T15:25:11.428Z'),
      lastHeartbeat: ISODate('2025-10-25T15:25:23.359Z'),
      lastHeartbeatRecv: ISODate('2025-10-25T15:25:22.357Z'),
      pingMs: Long('0'),
      lastHeartbeatMessage: '',
      syncSourceHost: 'mongodb-rs101:27017',
      syncSourceId: 0,
      infoMessage: '',
      configVersion: 1,
      configTerm: 1
    },
    {
      _id: 2,
      name: 'mongodb-rs103:29017',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 22,
      optime: { ts: Timestamp({ t: 1761405911, i: 15 }), t: Long('1') },
      optimeDurable: { ts: Timestamp({ t: 1761405911, i: 15 }), t: Long('1') },
      optimeWritten: { ts: Timestamp({ t: 1761405911, i: 15 }), t: Long('1') },
      optimeDate: ISODate('2025-10-25T15:25:11.000Z'),
      optimeDurableDate: ISODate('2025-10-25T15:25:11.000Z'),
      optimeWrittenDate: ISODate('2025-10-25T15:25:11.000Z'),
      lastAppliedWallTime: ISODate('2025-10-25T15:25:11.428Z'),
      lastDurableWallTime: ISODate('2025-10-25T15:25:11.428Z'),
      lastWrittenWallTime: ISODate('2025-10-25T15:25:11.428Z'),
      lastHeartbeat: ISODate('2025-10-25T15:25:23.359Z'),
      lastHeartbeatRecv: ISODate('2025-10-25T15:25:22.357Z'),
      pingMs: Long('0'),
      lastHeartbeatMessage: '',
      syncSourceHost: 'mongodb-rs101:27017',
      syncSourceId: 0,
      infoMessage: '',
      configVersion: 1,
      configTerm: 1
    }
  ],
  ok: 1
}
RS1 [direct: primary] test> 
``` 

RS2
```
$ docker exec -it mongodb-rs201 bash
[mongodb@e53a02088c0d /]$ mongosh --port 27027
Current Mongosh Log ID: 68fcec730964b1153334de76
Connecting to:          mongodb://127.0.0.1:27027/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.2
Using MongoDB:          8.0.4-1
Using Mongosh:          2.3.2

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.

test>     rs.initiate({"_id" : "RS2", members : [{"_id" : 0, priority : 3, host : "mongodb-rs201:27027"},{"_id" : 1, host : "mongodb-rs202:28027"},{"_id" : 2, host : "mongodb-rs203:29027"}]});
{ ok: 1 }
RS2 [direct: primary] test> rs.status()
{
  set: 'RS2',
  date: ISODate('2025-10-25T15:29:47.554Z'),
  myState: 1,
  term: Long('1'),
  syncSourceHost: '',
  syncSourceId: -1,
  heartbeatIntervalMillis: Long('2000'),
  majorityVoteCount: 2,
  writeMajorityCount: 2,
  votingMembersCount: 3,
  writableVotingMembersCount: 3,
  optimes: {
    lastCommittedOpTime: { ts: Timestamp({ t: 1761406181, i: 1 }), t: Long('1') },
    lastCommittedWallTime: ISODate('2025-10-25T15:29:41.975Z'),
    readConcernMajorityOpTime: { ts: Timestamp({ t: 1761406181, i: 1 }), t: Long('1') },
    appliedOpTime: { ts: Timestamp({ t: 1761406181, i: 1 }), t: Long('1') },
    durableOpTime: { ts: Timestamp({ t: 1761406181, i: 1 }), t: Long('1') },
    writtenOpTime: { ts: Timestamp({ t: 1761406181, i: 1 }), t: Long('1') },
    lastAppliedWallTime: ISODate('2025-10-25T15:29:41.975Z'),
    lastDurableWallTime: ISODate('2025-10-25T15:29:41.975Z'),
    lastWrittenWallTime: ISODate('2025-10-25T15:29:41.975Z')
  },
  lastStableRecoveryTimestamp: Timestamp({ t: 1761406140, i: 1 }),
  electionCandidateMetrics: {
    lastElectionReason: 'electionTimeout',
    lastElectionDate: ISODate('2025-10-25T15:29:11.914Z'),
    electionTerm: Long('1'),
    lastCommittedOpTimeAtElection: { ts: Timestamp({ t: 1761406140, i: 1 }), t: Long('-1') },
    lastSeenWrittenOpTimeAtElection: { ts: Timestamp({ t: 1761406140, i: 1 }), t: Long('-1') },
    lastSeenOpTimeAtElection: { ts: Timestamp({ t: 1761406140, i: 1 }), t: Long('-1') },
    numVotesNeeded: 2,
    priorityAtElection: 3,
    electionTimeoutMillis: Long('10000'),
    numCatchUpOps: Long('0'),
    newTermStartDate: ISODate('2025-10-25T15:29:11.951Z'),
    wMajorityWriteAvailabilityDate: ISODate('2025-10-25T15:29:12.435Z')
  },
  members: [
    {
      _id: 0,
      name: 'mongodb-rs201:27027',
      health: 1,
      state: 1,
      stateStr: 'PRIMARY',
      uptime: 166,
      optime: { ts: Timestamp({ t: 1761406181, i: 1 }), t: Long('1') },
      optimeDate: ISODate('2025-10-25T15:29:41.000Z'),
      optimeWritten: { ts: Timestamp({ t: 1761406181, i: 1 }), t: Long('1') },
      optimeWrittenDate: ISODate('2025-10-25T15:29:41.000Z'),
      lastAppliedWallTime: ISODate('2025-10-25T15:29:41.975Z'),
      lastDurableWallTime: ISODate('2025-10-25T15:29:41.975Z'),
      lastWrittenWallTime: ISODate('2025-10-25T15:29:41.975Z'),
      syncSourceHost: '',
      syncSourceId: -1,
      infoMessage: 'Could not find member to sync from',
      electionTime: Timestamp({ t: 1761406151, i: 1 }),
      electionDate: ISODate('2025-10-25T15:29:11.000Z'),
      configVersion: 1,
      configTerm: 1,
      self: true,
      lastHeartbeatMessage: ''
    },
    {
      _id: 1,
      name: 'mongodb-rs202:28027',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 46,
      optime: { ts: Timestamp({ t: 1761406181, i: 1 }), t: Long('1') },
      optimeDurable: { ts: Timestamp({ t: 1761406181, i: 1 }), t: Long('1') },
      optimeWritten: { ts: Timestamp({ t: 1761406181, i: 1 }), t: Long('1') },
      optimeDate: ISODate('2025-10-25T15:29:41.000Z'),
      optimeDurableDate: ISODate('2025-10-25T15:29:41.000Z'),
      optimeWrittenDate: ISODate('2025-10-25T15:29:41.000Z'),
      lastAppliedWallTime: ISODate('2025-10-25T15:29:41.975Z'),
      lastDurableWallTime: ISODate('2025-10-25T15:29:41.975Z'),
      lastWrittenWallTime: ISODate('2025-10-25T15:29:41.975Z'),
      lastHeartbeat: ISODate('2025-10-25T15:29:45.979Z'),
      lastHeartbeatRecv: ISODate('2025-10-25T15:29:46.980Z'),
      pingMs: Long('0'),
      lastHeartbeatMessage: '',
      syncSourceHost: 'mongodb-rs201:27027',
      syncSourceId: 0,
      infoMessage: '',
      configVersion: 1,
      configTerm: 1
    },
    {
      _id: 2,
      name: 'mongodb-rs203:29027',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 46,
      optime: { ts: Timestamp({ t: 1761406181, i: 1 }), t: Long('1') },
      optimeDurable: { ts: Timestamp({ t: 1761406181, i: 1 }), t: Long('1') },
      optimeWritten: { ts: Timestamp({ t: 1761406181, i: 1 }), t: Long('1') },
      optimeDate: ISODate('2025-10-25T15:29:41.000Z'),
      optimeDurableDate: ISODate('2025-10-25T15:29:41.000Z'),
      optimeWrittenDate: ISODate('2025-10-25T15:29:41.000Z'),
      lastAppliedWallTime: ISODate('2025-10-25T15:29:41.975Z'),
      lastDurableWallTime: ISODate('2025-10-25T15:29:41.975Z'),
      lastWrittenWallTime: ISODate('2025-10-25T15:29:41.975Z'),
      lastHeartbeat: ISODate('2025-10-25T15:29:45.979Z'),
      lastHeartbeatRecv: ISODate('2025-10-25T15:29:46.980Z'),
      pingMs: Long('0'),
      lastHeartbeatMessage: '',
      syncSourceHost: 'mongodb-rs201:27027',
      syncSourceId: 0,
      infoMessage: '',
      configVersion: 1,
      configTerm: 1
    }
  ],
  ok: 1
}
RS2 [direct: primary] test>
```

Config Set

```
$ docker exec -it mongodb-cs101 bash
[mongodb@69cdaf39fff1 /]$ mongosh --port 27037
Current Mongosh Log ID: 68fced80003c3292a534de76
Connecting to:          mongodb://127.0.0.1:27037/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.2
Using MongoDB:          8.0.4-1
Using Mongosh:          2.3.2

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.

test> rs.initiate({"_id" : "RScfg", members : [{"_id" : 0, priority : 3, host : "mongodb-cs101:27037"},{"_id" : 1, host : "mongodb-cs102:28037"},{"_id" : 2, host : "mongodb-cs103:29037"}]});
{ ok: 1 }
RScfg [direct: secondary] test> rs.status()
{
  set: 'RScfg',
  date: ISODate('2025-10-25T15:34:48.499Z'),
  myState: 1,
  term: Long('1'),
  syncSourceHost: '',
  syncSourceId: -1,
  configsvr: true,
  heartbeatIntervalMillis: Long('2000'),
  majorityVoteCount: 2,
  writeMajorityCount: 2,
  votingMembersCount: 3,
  writableVotingMembersCount: 3,
  optimes: {
    lastCommittedOpTime: { ts: Timestamp({ t: 1761406487, i: 1 }), t: Long('1') },
    lastCommittedWallTime: ISODate('2025-10-25T15:34:47.632Z'),
    readConcernMajorityOpTime: { ts: Timestamp({ t: 1761406487, i: 1 }), t: Long('1') },
    appliedOpTime: { ts: Timestamp({ t: 1761406487, i: 1 }), t: Long('1') },
    durableOpTime: { ts: Timestamp({ t: 1761406487, i: 1 }), t: Long('1') },
    writtenOpTime: { ts: Timestamp({ t: 1761406487, i: 1 }), t: Long('1') },
    lastAppliedWallTime: ISODate('2025-10-25T15:34:47.632Z'),
    lastDurableWallTime: ISODate('2025-10-25T15:34:47.632Z'),
    lastWrittenWallTime: ISODate('2025-10-25T15:34:47.632Z')
  },
  lastStableRecoveryTimestamp: Timestamp({ t: 1761406456, i: 1 }),
  electionCandidateMetrics: {
    lastElectionReason: 'electionTimeout',
    lastElectionDate: ISODate('2025-10-25T15:34:28.428Z'),
    electionTerm: Long('1'),
    lastCommittedOpTimeAtElection: { ts: Timestamp({ t: 1761406456, i: 1 }), t: Long('-1') },
    lastSeenWrittenOpTimeAtElection: { ts: Timestamp({ t: 1761406456, i: 1 }), t: Long('-1') },
    lastSeenOpTimeAtElection: { ts: Timestamp({ t: 1761406456, i: 1 }), t: Long('-1') },
    numVotesNeeded: 2,
    priorityAtElection: 3,
    electionTimeoutMillis: Long('10000'),
    numCatchUpOps: Long('0'),
    newTermStartDate: ISODate('2025-10-25T15:34:28.472Z'),
    wMajorityWriteAvailabilityDate: ISODate('2025-10-25T15:34:28.959Z')
  },
  members: [
    {
      _id: 0,
      name: 'mongodb-cs101:27037',
      health: 1,
      state: 1,
      stateStr: 'PRIMARY',
      uptime: 206,
      optime: { ts: Timestamp({ t: 1761406487, i: 1 }), t: Long('1') },
      optimeDate: ISODate('2025-10-25T15:34:47.000Z'),
      optimeWritten: { ts: Timestamp({ t: 1761406487, i: 1 }), t: Long('1') },
      optimeWrittenDate: ISODate('2025-10-25T15:34:47.000Z'),
      lastAppliedWallTime: ISODate('2025-10-25T15:34:47.632Z'),
      lastDurableWallTime: ISODate('2025-10-25T15:34:47.632Z'),
      lastWrittenWallTime: ISODate('2025-10-25T15:34:47.632Z'),
      syncSourceHost: '',
      syncSourceId: -1,
      infoMessage: 'Could not find member to sync from',
      electionTime: Timestamp({ t: 1761406468, i: 1 }),
      electionDate: ISODate('2025-10-25T15:34:28.000Z'),
      configVersion: 1,
      configTerm: 1,
      self: true,
      lastHeartbeatMessage: ''
    },
    {
      _id: 1,
      name: 'mongodb-cs102:28037',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 31,
      optime: { ts: Timestamp({ t: 1761406487, i: 1 }), t: Long('1') },
      optimeDurable: { ts: Timestamp({ t: 1761406487, i: 1 }), t: Long('1') },
      optimeWritten: { ts: Timestamp({ t: 1761406487, i: 1 }), t: Long('1') },
      optimeDate: ISODate('2025-10-25T15:34:47.000Z'),
      optimeDurableDate: ISODate('2025-10-25T15:34:47.000Z'),
      optimeWrittenDate: ISODate('2025-10-25T15:34:47.000Z'),
      lastAppliedWallTime: ISODate('2025-10-25T15:34:47.632Z'),
      lastDurableWallTime: ISODate('2025-10-25T15:34:47.632Z'),
      lastWrittenWallTime: ISODate('2025-10-25T15:34:47.632Z'),
      lastHeartbeat: ISODate('2025-10-25T15:34:48.463Z'),
      lastHeartbeatRecv: ISODate('2025-10-25T15:34:47.464Z'),
      pingMs: Long('0'),
      lastHeartbeatMessage: '',
      syncSourceHost: 'mongodb-cs101:27037',
      syncSourceId: 0,
      infoMessage: '',
      configVersion: 1,
      configTerm: 1
    },
    {
      _id: 2,
      name: 'mongodb-cs103:29037',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 31,
      optime: { ts: Timestamp({ t: 1761406487, i: 1 }), t: Long('1') },
      optimeDurable: { ts: Timestamp({ t: 1761406487, i: 1 }), t: Long('1') },
      optimeWritten: { ts: Timestamp({ t: 1761406487, i: 1 }), t: Long('1') },
      optimeDate: ISODate('2025-10-25T15:34:47.000Z'),
      optimeDurableDate: ISODate('2025-10-25T15:34:47.000Z'),
      optimeWrittenDate: ISODate('2025-10-25T15:34:47.000Z'),
      lastAppliedWallTime: ISODate('2025-10-25T15:34:47.632Z'),
      lastDurableWallTime: ISODate('2025-10-25T15:34:47.632Z'),
      lastWrittenWallTime: ISODate('2025-10-25T15:34:47.632Z'),
      lastHeartbeat: ISODate('2025-10-25T15:34:48.464Z'),
      lastHeartbeatRecv: ISODate('2025-10-25T15:34:47.466Z'),
      pingMs: Long('0'),
      lastHeartbeatMessage: '',
      syncSourceHost: 'mongodb-cs101:27037',
      syncSourceId: 0,
      infoMessage: '',
      configVersion: 1,
      configTerm: 1
    }
  ],
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761406487, i: 1 }),
    signature: {
      hash: Binary.createFromBase64('CQuk2CSrYh+yDUCfVXv8kvOT6AY=', 0),
      keyId: Long('7565183175022870551')
    }
  },
  operationTime: Timestamp({ t: 1761406487, i: 1 })
}
RScfg [direct: primary] test> 
```

Создаем пользователей
```
$ docker exec -it mongodb-cs102 bash
root@0f2d58515e87:/# mongosh --port 28037
Current Mongosh Log ID: 68fcce359000e110fb4f87fd
Connecting to:          mongodb://127.0.0.1:28037/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.8
Using MongoDB:          8.0.14
Using Mongosh:          2.5.8

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.

------
   The server generated these startup warnings when booting
   2025-10-25T13:08:32.913+00:00: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
   2025-10-25T13:08:33.488+00:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
   2025-10-25T13:08:33.489+00:00: For customers running the current memory allocator, we suggest changing the contents of the following sysfsFile
   2025-10-25T13:08:33.489+00:00: We suggest setting the contents of sysfsFile to 0.
   2025-10-25T13:08:33.489+00:00: vm.max_map_count is too low
   2025-10-25T13:08:33.489+00:00: We suggest setting swappiness to 0 or 1, as swapping can cause performance problems.
------

RScfg [direct: primary] test> use admin
switched to db admin
RScfg [direct: primary] admin> db.createUser({user: "UserClusterAdmin",pwd: "password", roles: [ "clusterAdmin" ]})
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761398417, i: 5 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761398417, i: 5 })
}
RScfg [direct: primary] admin> db.createUser({user: "UserdbOwner",pwd: "root$123", roles: [ { role: "dbOwner", db: "*" } ]})
... 
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761398434, i: 2 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761398434, i: 2 })
}
RScfg [direct: primary] admin> db.createUser({user: "UserRoot",pwd: "root$123", roles: [ "root" ]})
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761398453, i: 2 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761398453, i: 2 })
}
RScfg [direct: primary] admin> 
```

Добавляем в контейнер --auth

```
  mongodb-cs103:
    image: mongo:latest
    container_name: mongodb-cs103
    ports:
      - "29037:29037"
    command: mongod --auth --configsvr --replSet RScfg --port 29037 --bind_ip_all
    volumes:
      - ./mongodb-configdata-103:/data/db
```

Не запускается
```
$ docker compose up mongodb-cs103
Attaching to mongodb-cs103
mongodb-cs103  | BadValue: security.keyFile is required when authorization is enabled with replica sets
mongodb-cs103  | try 'mongod --help' for more information
mongodb-cs103 exited with code 2
```

Генерируем ключи
```
$ openssl rand -base64 756 > ./keyfile
$ chmod 400 ./keyfile
```

Прокидываем в контейнер
```
  mongodb-cs103:
    image: mongo:latest
    container_name: mongodb-cs103
    ports:
      - "29037:29037"
    command: mongod --auth --configsvr --replSet RScfg --port 29037 --bind_ip_all --keyFile /etc/secrets/mongodb-keyfile
    volumes:
      - ./mongodb-configdata-103:/data/db
      - ./secrets:/etc/secrets:ro
```
Контейнеры перезапустились
```
$ docker ps
CONTAINER ID   IMAGE                    COMMAND                  CREATED              STATUS          PORTS                                             NAMES
d180dfc9abdb   percona/percona-server-mongodb:8.0-multi             "docker-entrypoint.s…"   About a minute ago   Up 59 seconds   0.0.0.0:28037->28037/tcp, [::]:28037->28037/tcp   mongodb-cs102
16dc4f418282   percona/percona-server-mongodb:8.0-multi             "docker-entrypoint.s…"   About a minute ago   Up 59 seconds   0.0.0.0:27037->27037/tcp, [::]:27037->27037/tcp   mongodb-cs101
a3d4202fc1ca   percona/percona-server-mongodb:8.0-multi             "docker-entrypoint.s…"   4 minutes ago        Up 59 seconds   0.0.0.0:29037->29037/tcp, [::]:29037->29037/tcp   mongodb-cs103
```

```
$ docker exec -it mongodb-cs102 bash
root@d180dfc9abdb:/# mongosh --port 28037 -u "UserClusterAdmin" -p password --authenticationDatabase "admin"
Current Mongosh Log ID: 68fcd24ffc8285120e4f87fd
Connecting to:          mongodb://<credentials>@127.0.0.1:28037/?directConnection=true&serverSelectionTimeoutMS=2000&authSource=admin&appName=mongosh+2.5.8
Using MongoDB:          8.0.14
Using Mongosh:          2.5.8

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

------
   The server generated these startup warnings when booting
   2025-10-25T13:33:39.174+00:00: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
   2025-10-25T13:33:39.852+00:00: For customers running the current memory allocator, we suggest changing the contents of the following sysfsFile
   2025-10-25T13:33:39.852+00:00: We suggest setting the contents of sysfsFile to 0.
   2025-10-25T13:33:39.852+00:00: vm.max_map_count is too low
   2025-10-25T13:33:39.852+00:00: We suggest setting swappiness to 0 or 1, as swapping can cause performance problems.
------

RScfg [direct: primary] test> 
```



Добавим пользователей на ReplicaSet1 и ReplicaSet2

Пример на ReplicaSet1
```
RS1 [direct: primary] test> use admin
switched to db admin
RS1 [direct: primary] admin> db.createUser({user: "UserDBAdmin",pwd: "root$123", roles: [ { role: "dbAdmin", db: "*" } ]})
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761408341, i: 4 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761408341, i: 4 })
}
RS1 [direct: primary] admin> db.createUser({user: "UserDBRoot",pwd: "root$123", roles: [ "root" ]})
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761408347, i: 1 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761408347, i: 1 })
}
RS1 [direct: primary] admin> 

```

ReplicaSet 2

```
RS2 [direct: primary] test> use admin
switched to db admin
RS2 [direct: primary] admin> db.createUser({user: "UserDBAdmin",pwd: "root$123", roles: [ { role: "dbAdmin", db: "*" } ]})
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761408517, i: 4 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761408517, i: 4 })
}
RS2 [direct: primary] admin> db.createUser({user: "UserDBRoot",pwd: "root$123", roles: [ "root" ]})
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761408523, i: 1 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1761408523, i: 1 })
}
RS2 [direct: primary] admin>  
```

Запускаем mongos
```
M6T223J26Q:mongodb korotkova.a34$ docker exec -it mongodb-mongos bash
[mongodb@c5c05b3df961 /]$ mongosh --port 27000 
Current Mongosh Log ID: 68fcf8964afb210e5b34de76
Connecting to:          mongodb://127.0.0.1:27000/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.2
Using MongoDB:          8.0.4-1
Using Mongosh:          2.3.2

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.

[direct: mongos] test> sh.addShard("RS1/mongodb-rs101:27017,mongodb-rs102:28017,mongodb-rs103:29017")
MongoServerError[Unauthorized]: Command addShard requires authentication
[direct: mongos] test> exit
[mongodb@c5c05b3df961 /]$ mongosh --port 27000 -u "UserRoot" -p root\$123 --authenticationDatabase "admin"
Current Mongosh Log ID: 68fcf8cc29075dc5ca34de76
Connecting to:          mongodb://<credentials>@127.0.0.1:27000/?directConnection=true&serverSelectionTimeoutMS=2000&authSource=admin&appName=mongosh+2.3.2
Using MongoDB:          8.0.4-1
Using Mongosh:          2.3.2

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

------
   The server generated these startup warnings when booting
   2025-10-25T16:19:05.950+00:00: This server is bound to localhost. Remote systems will be unable to connect to this server. Start the server with --bind_ip <address> to specify which IP addresses it should serve responses from, or with --bind_ip_all to bind to all interfaces. If this behavior is desired, start the server with --bind_ip 127.0.0.1 to disable this warning
------

[direct: mongos] test> sh.addShard("RS1/mongodb-rs101:27017,mongodb-rs102:28017,mongodb-rs103:29017")
{
  shardAdded: 'RS1',
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761409235, i: 20 }),
    signature: {
      hash: Binary.createFromBase64('gJubRdOkTqhNkXpLZgWk03KwIo0=', 0),
      keyId: Long('7565186495032590359')
    }
  },
  operationTime: Timestamp({ t: 1761409235, i: 20 })
}
[direct: mongos] test> sh.addShard("RS2/mongodb-rs201:27027,mongodb-rs202:28027,mongodb-rs203:29027")
{
  shardAdded: 'RS2',
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761409244, i: 24 }),
    signature: {
      hash: Binary.createFromBase64('HVzxNbxWbyn9yz78T0x2x6o4SaE=', 0),
      keyId: Long('7565186495032590359')
    }
  },
  operationTime: Timestamp({ t: 1761409244, i: 18 })
}
[direct: mongos] test> sh.status()
shardingVersion
{ _id: 1, clusterId: ObjectId('68fcf109f8d4136511b6cff1') }
---
shards
[
  {
    _id: 'RS1',
    host: 'RS1/mongodb-rs101:27017,mongodb-rs102:28017,mongodb-rs103:29017',
    state: 1,
    topologyTime: Timestamp({ t: 1761409235, i: 10 }),
    replSetConfigVersion: Long('-1')
  },
  {
    _id: 'RS2',
    host: 'RS2/mongodb-rs201:27027,mongodb-rs202:28027,mongodb-rs203:29027',
    state: 1,
    topologyTime: Timestamp({ t: 1761409244, i: 9 }),
    replSetConfigVersion: Long('-1')
  }
]
---
active mongoses
[ { '8.0.4-1': 1 } ]
---
autosplit
{ 'Currently enabled': 'yes' }
---
balancer
{
  'Currently enabled': 'yes',
  'Currently running': 'no',
  'Failed balancer rounds in last 5 attempts': 0,
  'Migration Results for the last 24 hours': 'No recent migrations'
}
---
databases
[
  {
    database: { _id: 'config', primary: 'config', partitioned: true },
    collections: {}
  }
]
[direct: mongos] test> rs.secondaryOk(true)
DeprecationWarning: .setSecondaryOk() is deprecated. Use .setReadPref("primaryPreferred") instead
Setting read preference from "primary" to "primaryPreferred"
[direct: mongos] test> 
```

Загружаем данные
```
[mongodb@c5c05b3df961 /]$ mongorestore --port 27000 -u "UserRoot" -p root\$123 --authenticationDatabase "admin" /data/stocks/values.bson
2025-10-25T16:23:20.061+0000    WARNING: On some systems, a password provided directly using --password may be visible to system status programs such as `ps` that may be invoked by other users. Consider omitting the password to provide it via stdin, or using the --config option to specify a configuration file with the password.
2025-10-25T16:23:20.070+0000    checking for collection data in /data/stocks/values.bson
2025-10-25T16:23:20.122+0000    restoring stocks.values from /data/stocks/values.bson
2025-10-25T16:23:23.070+0000    [###.....................]  stocks.values  93.5MB/715MB  (13.1%)
2025-10-25T16:23:26.072+0000    [####....................]  stocks.values  149MB/715MB  (20.8%)
2025-10-25T16:23:29.069+0000    [#######.................]  stocks.values  216MB/715MB  (30.2%)
2025-10-25T16:23:32.067+0000    [#########...............]  stocks.values  278MB/715MB  (38.8%)
2025-10-25T16:23:35.067+0000    [###########.............]  stocks.values  349MB/715MB  (48.7%)
2025-10-25T16:23:38.068+0000    [#############...........]  stocks.values  408MB/715MB  (57.1%)
2025-10-25T16:23:41.066+0000    [################........]  stocks.values  480MB/715MB  (67.1%)
2025-10-25T16:23:44.079+0000    [#################.......]  stocks.values  527MB/715MB  (73.7%)
2025-10-25T16:23:47.067+0000    [###################.....]  stocks.values  580MB/715MB  (81.2%)
2025-10-25T16:23:50.073+0000    [#####################...]  stocks.values  645MB/715MB  (90.2%)
2025-10-25T16:23:53.066+0000    [########################]  stocks.values  715MB/715MB  (100.0%)
2025-10-25T16:23:53.067+0000    finished restoring stocks.values (4308303 documents, 0 failures)
2025-10-25T16:23:53.068+0000    4308303 document(s) restored successfully. 0 document(s) failed to restore.
```

Смотрим что загрузили и запускаем шардирование
```
[direct: mongos] test> use stocks
switched to db stocks
[direct: mongos] stocks>  db.values.find().limit(1)
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
[direct: mongos] stocks>  db.values.find().count()
4308303
[direct: mongos] stocks> db.values.createIndex({date: 1})
date_1
[direct: mongos] stocks> sh.enableSharding("stocks")
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761480766, i: 3 }),
    signature: {
      hash: Binary.createFromBase64('cbi8a9Y27mB2RjgF2YPIzjAEF0U=', 0),
      keyId: Long('7565186495032590359')
    }
  },
  operationTime: Timestamp({ t: 1761480766, i: 3 })
}
[direct: mongos] stocks> sh.shardCollection("stocks.values",{ date: 1 })
{
  collectionsharded: 'stocks.values',
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761480775, i: 42 }),
    signature: {
      hash: Binary.createFromBase64('eJBuQbGr6Ogt6eyBNnUOJOzs008=', 0),
      keyId: Long('7565186495032590359')
    }
  },
  operationTime: Timestamp({ t: 1761480775, i: 41 })
}
[direct: mongos] stocks> sh.status()
shardingVersion
{ _id: 1, clusterId: ObjectId('68fcf109f8d4136511b6cff1') }
---
shards
[
  {
    _id: 'RS1',
    host: 'RS1/mongodb-rs101:27017,mongodb-rs102:28017,mongodb-rs103:29017',
    state: 1,
    topologyTime: Timestamp({ t: 1761409235, i: 10 }),
    replSetConfigVersion: Long('1')
  },
  {
    _id: 'RS2',
    host: 'RS2/mongodb-rs201:27027,mongodb-rs202:28027,mongodb-rs203:29027',
    state: 1,
    topologyTime: Timestamp({ t: 1761409244, i: 9 }),
    replSetConfigVersion: Long('1')
  }
]
---
active mongoses
[ { '8.0.4-1': 1 } ]
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
databases
[
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
        uuid: UUID('a0775af9-40c6-464d-b240-679735692ae2'),
        timestamp: Timestamp({ t: 1761409400, i: 2 }),
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
[direct: mongos] stocks> 
```


Добавим пользователей для pbm - пример на RS1
```
$ docker exec -it mongodb-rs101 bash
[mongodb@f90c5b455ff8 /]$ mongosh --port 27017 -u "UserDBRoot" -p root\$123 --authenticationDatabase "admin"
Current Mongosh Log ID: 68fcfa7f80d0ff78f334de76
Connecting to:          mongodb://<credentials>@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&authSource=admin&appName=mongosh+2.3.2
Using MongoDB:          8.0.4-1
Using Mongosh:          2.3.2

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.

------
   The server generated these startup warnings when booting
   2025-10-25T16:12:38.014+00:00: For customers running the current memory allocator, we suggest changing the contents of the following sysfsFile
   2025-10-25T16:12:38.014+00:00: We suggest setting the contents of sysfsFile to 0.
   2025-10-25T16:12:38.014+00:00: vm.max_map_count is too low
   2025-10-25T16:12:38.014+00:00: We suggest setting swappiness to 0 or 1, as swapping can cause performance problems.
------

RS1 [direct: primary] test> use admin
switched to db admin
RS1 [direct: primary] admin> db.getSiblingDB("admin").createRole({ "role": "pbmAnyAction",
...       "privileges": [
...          { "resource": { "anyResource": true },
...            "actions": [ "anyAction" ]
...          }
...       ],
...       "roles": []
...    });
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761409681, i: 3 }),
    signature: {
      hash: Binary.createFromBase64('E8c3xEMNpoYJ3wK15sGxkTvdQ+I=', 0),
      keyId: Long('7565186495032590359')
    }
  },
  operationTime: Timestamp({ t: 1761409681, i: 3 })
}
RS1 [direct: primary] admin> db.getSiblingDB("admin").createUser({user: "pbmuser",
n", "role" : "restore" },
...        "pwd": "secretpwd",
...        "roles" : [
...           { "db" : "admin", "role" : "readWrite", "collection": "" },
...           { "db" : "admin", "role" : "backup" },
...           { "db" : "admin", "role" : "clusterMonitor" },
...           { "db" : "admin", "role" : "restore" },
...           { "db" : "admin", "role" : "pbmAnyAction" }
...        ]
...     });
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761409690, i: 1 }),
    signature: {
      hash: Binary.createFromBase64('xM/XxPZ6kU9+2JcvwXJdq5meR2g=', 0),
      keyId: Long('7565186495032590359')
    }
  },
  operationTime: Timestamp({ t: 1761409690, i: 1 })
}
RS1 [direct: primary] admin> 
```

2. Протестировать создание бэкапов через PBM

Устанавлмваем pbm в контейнеры
```
$ docker exec -it -u root mongodb-rs102 bash
[root@3eb5caa3edc2 /]# percona-release enable pbm release
* Enabling the Percona Backup MongoDB repository
<*> All done!
[root@3eb5caa3edc2 /]# yum install percona-backup-mongodb
...
Installed:
  percona-backup-mongodb-2.11.0-1.el8.aarch64                                                                                                                                                                         

Complete!
```

Создадим файл конфига в контейнерах
```
$ docker exec -it -u root mongodb-rs101  bash
[root@f90c5b455ff8 /]# cat > temp.cfg << EOF 
> storage:
>   type: filesystem
>   filesystem:
>     path: /data/backups
> EOF
[root@f90c5b455ff8 /]# cat temp.cfg | tee -a /data/pbm_config.yaml
storage:
  type: filesystem
  filesystem:
    path: /data/backups
[root@f90c5b455ff8 /]# cat /data/pbm_config.yaml
storage:
  type: filesystem
  filesystem:
    path: /data/backups
```

Запускаем агентов для бэкапа

```
pbm-agent --mongodb-uri "mongodb://pbmuser:secretpwd@mongodb-rs101:27017/?authSource=admin&replicaSet=RS1"  > /data/agent.101.27017.log 2>&1 &
 pbm-agent --mongodb-uri "mongodb://pbmuser:secretpwd@mongodb-rs102:28017/?authSource=admin&replicaSet=RS1"  > /data/agent.102.28017.log 2>&1 &
pbm-agent --mongodb-uri "mongodb://pbmuser:secretpwd@mongodb-rs103:29017/?authSource=admin&replicaSet=RS1"  > /data/agent.103.29017.log 2>&1 &

pbm-agent --mongodb-uri "mongodb://pbmuser:secretpwd@mongodb-rs201:27027/?authSource=admin&replicaSet=RS2"  > /data/pbm/agent.201.27027.log 2>&1 &
pbm-agent --mongodb-uri "mongodb://pbmuser:secretpwd@mongodb-rs202:28027/?authSource=admin&replicaSet=RS2"  > /data/agent.202.28027.log 2>&1 &
pbm-agent --mongodb-uri "mongodb://pbmuser:secretpwd@mongodb-rs203:29027/?authSource=admin&replicaSet=RS2"  > /data/agent.202.29027.log 2>&1 &

pbm-agent --mongodb-uri "mongodb://pbmuser:secretpwd@mongodb-cs101:27037/?authSource=admin&replicaSet=RScfg"  > /data/pbm/agent.101.27037.log 2>&1 &
pbm-agent --mongodb-uri "mongodb://pbmuser:secretpwd@mongodb-cs102:28037/?authSource=admin&replicaSet=RScfg"  > /data/pbm/agent.102.28037.log 2>&1 &
pbm-agent --mongodb-uri "mongodb://pbmuser:secretpwd@mongodb-cs103:29037/?authSource=admin&replicaSet=RScfg"  > /data/pbm/agent.103.29037.log 2>&1 &
```

Применим конфиг
```
$ docker exec -it -u root mongodb-cs101  bash
[root@8c213972809d /]# pbm config --file /data/pbm_config.yaml --mongodb-uri "mongodb://pbmuser:secretpwd@mongodb-cs101:27037/?authSource=admin&replicaSet=RScfg"
storage:
  type: filesystem
  filesystem:
    path: /data/backups
```



```
$ docker exec -it -u root -e PBM_MONGODB_URI="mongodb://pbmuser:secretpwd@mongodb-cs101:27037/?authSource=admin&replicaSet=RScfg" mongodb-cs101  bash
[root@718efd8e43c7 /]# ls /data/backups
[root@718efd8e43c7 /]# pbm status
Cluster:
========
RScfg:
  - mongodb-cs101:27037 [P]: pbm-agent [v2.11.0] OK
  - mongodb-cs102:28037 [S]: pbm-agent [v2.11.0] OK
  - mongodb-cs103:29037 [S]: pbm-agent [v2.11.0] OK
RS1:
  - mongodb-rs101:27017 [P]: pbm-agent [v2.11.0] OK
  - mongodb-rs102:28017 [S]: pbm-agent [v2.11.0] OK
  - mongodb-rs103:29017 [S]: pbm-agent [v2.11.0] OK
RS2:
  - mongodb-rs201:27027 [P]: pbm-agent [v2.11.0] OK
  - mongodb-rs202:28027 [S]: pbm-agent [v2.11.0] OK
  - mongodb-rs203:29027 [S]: pbm-agent [v2.11.0] OK


PITR incremental backup:
========================
Status [OFF]

Currently running:
==================
(none)

Backups:
========
FS  /data/backups
  (none)
[root@718efd8e43c7 /]# pbm backup
Starting backup '2025-10-25T20:16:20Z'....Backup '2025-10-25T20:16:20Z' to remote store '/data/backups'
```

Так не работает
Попробуем с s3 хранилищем
```
[root@f90c5b455ff8 /]# pbm config --set storage.s3.endpointUrl=http://host.docker.internal:9000
[storage.s3.endpointUrl=http://host.docker.internal:9000]
[root@f90c5b455ff8 /]# pbm config --set storage.s3.bucket=backup                    
[storage.s3.bucket=backup]
[root@f90c5b455ff8 /]# pbm config --set storage.s3.credentials.access-key-id=admin
[storage.s3.credentials.access-key-id=admin]
[root@f90c5b455ff8 /]# pbm config --set storage.s3.credentials.secret-access-key=password
[storage.s3.credentials.secret-access-key=password]
[root@f90c5b455ff8 /]# pbm config --set storage.s3.region=us-east-1
[storage.s3.region=us-east-1]
[root@f90c5b455ff8 /]# pbm config
storage:
  type: s3
  s3:
    region: us-east-1
    endpointUrl: hhttp://host.docker.internal:9000
    bucket: backup
    credentials:
      access-key-id: '***'
      secret-access-key: '***'
    insecureSkipTLSVerify: false
pitr:
  enabled: false
  compression: s2
backup:
  oplogSpanMin: 0
  compression: s2
restore: {}
```

Запускаем backup
```
[root@718efd8e43c7 /]# pbm config --force-resync
Storage resync started
[root@718efd8e43c7 /]# pbm status
Cluster:
========
RS2:
  - mongodb-rs201:27027 [P]: pbm-agent [v2.11.0] OK
  - mongodb-rs202:28027 [S]: pbm-agent [v2.11.0] OK
  - mongodb-rs203:29027 [S]: pbm-agent [v2.11.0] OK
RS1:
  - mongodb-rs101:27017 [P]: pbm-agent [v2.11.0] OK
  - mongodb-rs102:28017 [S]: pbm-agent [v2.11.0] OK
  - mongodb-rs103:29017 [S]: pbm-agent [v2.11.0] OK
RScfg:
  - mongodb-cs101:27037 [P]: pbm-agent [v2.11.0] OK
  - mongodb-cs102:28037 [S]: pbm-agent [v2.11.0] OK
  - mongodb-cs103:29037 [S]: pbm-agent [v2.11.0] OK


PITR incremental backup:
========================
Status [OFF]

Currently running:
==================
(none)

Backups:
========
S3 us-east-1 http://host.docker.internal:9000/backup
  Snapshots:
    2025-10-26T06:16:50Z 155.75MB <logical> success [restore_to_time: 2025-10-26T06:16:54]
[root@718efd8e43c7 /]# pbm backup
Starting backup '2025-10-26T12:15:27Z'....Backup '2025-10-26T12:15:27Z' to remote store 'http://host.docker.internal:9000/backup'
[root@718efd8e43c7 /]# pbm status
Cluster:
========
RScfg:
  - mongodb-cs101:27037 [P]: pbm-agent [v2.11.0] OK
  - mongodb-cs102:28037 [S]: pbm-agent [v2.11.0] OK
  - mongodb-cs103:29037 [S]: pbm-agent [v2.11.0] OK
RS1:
  - mongodb-rs101:27017 [P]: pbm-agent [v2.11.0] OK
  - mongodb-rs102:28017 [S]: pbm-agent [v2.11.0] OK
  - mongodb-rs103:29017 [S]: pbm-agent [v2.11.0] OK
RS2:
  - mongodb-rs201:27027 [P]: pbm-agent [v2.11.0] OK
  - mongodb-rs202:28027 [S]: pbm-agent [v2.11.0] OK
  - mongodb-rs203:29027 [S]: pbm-agent [v2.11.0] OK


PITR incremental backup:
========================
Status [OFF]

Currently running:
==================
(none)

Backups:
========
S3 us-east-1 http://host.docker.internal:9000/backup
  Snapshots:
    2025-10-26T12:15:27Z 207.55MB <logical> success [restore_to_time: 2025-10-26T12:15:30]
    2025-10-26T06:16:50Z 155.75MB <logical> success [restore_to_time: 2025-10-26T06:16:54]
[root@718efd8e43c7 /]# 
```

Восстановление из бэкапа
```
[direct: mongos] stocks> sh.stopBalancer()
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1761481151, i: 4 }),
    signature: {
      hash: Binary.createFromBase64('iobYEipQbmy1dZanFIaHMPMU/wI=', 0),
      keyId: Long('7565186495032590359')
    }
  },
  operationTime: Timestamp({ t: 1761481151, i: 4 })
}
[direct: mongos] stocks> show databases
admin     1.86 MiB
config    3.04 MiB
stocks  468.08 MiB
[direct: mongos] stocks> db.dropDatabase()
{ ok: 1, dropped: 'stocks' }


[root@718efd8e43c7 /]# pbm list
Backup snapshots:
  2025-10-26T06:16:50Z <logical> [restore_to_time: 2025-10-26T06:16:54]
  2025-10-26T12:15:27Z <logical> [restore_to_time: 2025-10-26T12:15:30]

PITR <off>:


[root@718efd8e43c7 /]# pbm restore 2025-10-26T12:15:27Z
Starting restore 2025-10-26T12:21:47.686472545Z from '2025-10-26T12:15:27Z'.....Restore of the snapshot from '2025-10-26T12:15:27Z' has started
[root@718efd8e43c7 /]# pbm status
Cluster:
========
RS2:
  - mongodb-rs201:27027 [P]: pbm-agent [v2.11.0] OK
  - mongodb-rs202:28027 [S]: pbm-agent [v2.11.0] OK
  - mongodb-rs203:29027 [S]: pbm-agent [v2.11.0] OK
RScfg:
  - mongodb-cs101:27037 [P]: pbm-agent [v2.11.0] OK
  - mongodb-cs102:28037 [S]: pbm-agent [v2.11.0] OK
  - mongodb-cs103:29037 [S]: pbm-agent [v2.11.0] OK
RS1:
  - mongodb-rs101:27017 [P]: pbm-agent [v2.11.0] OK
  - mongodb-rs102:28017 [S]: pbm-agent [v2.11.0] OK
  - mongodb-rs103:29017 [S]: pbm-agent [v2.11.0] OK


PITR incremental backup:
========================
Status [OFF]

Currently running:
==================
Snapshot restore "2025-10-26T12:15:27Z", started at 2025-10-26T12:21:48Z. Status: snapshot restore. [op id: 68fe125b854c92f9d0af3219]

Backups:
========
S3 us-east-1 http://host.docker.internal:9000/backup
  Snapshots:
    2025-10-26T12:15:27Z 207.55MB <logical> success [restore_to_time: 2025-10-26T12:15:30]
    2025-10-26T06:16:50Z 155.75MB <logical> success [restore_to_time: 2025-10-26T06:16:54]


```

Восстановление прошло успешно
```
[direct: mongos] stocks> use stocks
already on db stocks
[direct: mongos] stocks> sh.status()
shardingVersion
{ _id: 1, clusterId: ObjectId('68fcf109f8d4136511b6cff1') }
---
shards
[
  {
    _id: 'RS1',
    host: 'RS1/mongodb-rs101:27017,mongodb-rs102:28017,mongodb-rs103:29017',
    state: 1,
    topologyTime: Timestamp({ t: 1761409235, i: 10 }),
    replSetConfigVersion: Long('1')
  },
  {
    _id: 'RS2',
    host: 'RS2/mongodb-rs201:27027,mongodb-rs202:28027,mongodb-rs203:29027',
    state: 1,
    topologyTime: Timestamp({ t: 1761409244, i: 9 }),
    replSetConfigVersion: Long('1')
  }
]
---
active mongoses
[ { '8.0.4-1': 1 } ]
---
autosplit
{ 'Currently enabled': 'yes' }
---
balancer
{
  'Currently enabled': 'no',
  'Currently running': 'no',
  'Failed balancer rounds in last 5 attempts': 0,
  'Migration Results for the last 24 hours': { '2': 'Success' }
}
---
databases
[
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
        uuid: UUID('a0775af9-40c6-464d-b240-679735692ae2'),
        timestamp: Timestamp({ t: 1761409400, i: 2 }),
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
[direct: mongos] stocks
```
3. Не забываем ВМ остановит/удалить

```
$ docker compose stop
WARN[0000] /lessons/mongodb/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Stopping 14/14
 ✔ Container minio           Stopped                                                                                                          0.4s 
 ✔ Container rs-1-init       Stopped                                                                                                          0.0s 
 ✔ Container rs-2-init       Stopped                                                                                                          0.0s 
 ✔ Container cs-init         Stopped                                                                                                          0.0s 
 ✔ Container mongodb-mongos  Stopped                                                                                                         11.2s 
 ✔ Container mongodb-cs102   Stopped                                                                                                         11.3s 
 ✔ Container mongodb-cs103   Stopped                                                                                                         11.3s 
 ✔ Container mongodb-cs101   Stopped                                                                                                         11.5s 
 ✔ Container mongodb-rs201   Stopped                                                                                                         11.6s 
 ✔ Container mongodb-rs202   Stopped                                                                                                         11.8s 
 ✔ Container mongodb-rs203   Stopped                                                                                                         11.8s 
 ✔ Container mongodb-rs103   Stopped                                                                                                         11.9s 
 ✔ Container mongodb-rs101   Stopped                                                                                                         11.5s 
 ✔ Container mongodb-rs102   Stopped                                                                                                         11.7s 
```
