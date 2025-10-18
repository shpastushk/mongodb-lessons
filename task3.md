1. Развернуть ВМ (Linux) с MongoDB (у вас ест ВМ в ВБ, лбой другой способ, в т.. докер)

```
$ docker compose up mongodb
```

```
$ docker exec -it mongodb bash
root@bc7ffdbe0ba8:/# mongosh --port 27017 -u "admin" -p "admin"
Current Mongosh Log ID: 68f37655acf32f9ff24f87fd
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

2. Создать коллекцию (~20 строк) с товарами и их характеристиками
```
test> db.products3.insertMany([
...     { "_id" : 1, "item" : "apples", "price" : 12, "description": "about apples" },
...     { "_id" : 2, "item" : "oranges", "price" : 20, "description": "about oranges" },
...     { "_id" : 3, "item" : "mangos", "price" : 30, "description": "about mangos" },
...     { "_id" : 4, "item" : "lemons", "price" : 10, "description": "about lemons" },
...     { "_id" : 5, "item" : "pineapples", "price" : 14, "description": "about pineapples" },
...     { "_id" : 6, "item" : "potatoes", "price" : 60, "description": "about potatoes" },
...     { "_id" : 7, "item" : "limes", "price" : 21, "description": "about limes" },
...     { "_id" : 8, "item" : "cucumbers", "price" : 45, "description": "about cucumbers" },
...     { "_id" : 9, "item" : "pecans", "price" : 33, "description": "about pecans" },
...     { "_id" : 10, "item" : "cookies", "price" : 31, "description": "about cookies" },
...     { "_id" : 11, "item" : "chocolate", "price" : 32, "description": "about chocolate" },
...     { "_id" : 12, "item" : "candies", "price" : 53, "description": "about candies" },
...     { "_id" : 13, "item" : "chicken", "price" : 63, "description": "about chicken" },
...     { "_id" : 14, "item" : "turkey", "price" : 83, "description": "about turkey" },
...     { "_id" : 15, "item" : "watermelon", "price" : 93, "description": "about watermelon" },
...     { "_id" : 16, "item" : "melon", "price" : 11, "description": "about melon" },
...     { "_id" : 17, "item" : "coca-cola", "price" : 88, "description": "about coca-cola" },
...     { "_id" : 18, "item" : "bread", "price" : 3, "description": "about bread" },
...     { "_id" : 19, "item" : "water", "price" : 100, "description": "about water" },
...     { "_id" : 20, "item" : "coffee", "price" : 200, "description": "about coffee" },
...  ])
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
    '9': 10,
    '10': 11,
    '11': 12,
    '12': 13,
    '13': 14,
    '14': 15,
    '15': 16,
    '16': 17,
    '17': 18,
    '18': 19,
    '19': 20
  }
}
test> 
```

3. Создать wildtext индекс, проверить работу и проанализировать план запроса

Создаем индекс
```
test> db.products3.createIndex( { "$**" : "text" }, { default_language: "none" } )
$**_text
test> db.products3.getIndexes();
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  {
    v: 2,
    key: { _fts: 'text', _ftsx: 1 },
    name: '$**_text',
    weights: { '$**': 1 },
    default_language: 'none',
    language_override: 'language',
    textIndexVersion: 3
  }
]
```

Ищем товары cо словом about

```
test> db.products3.find({$text: {$search: "about"}});
[
  { _id: 20, item: 'coffee', price: 200, description: 'about coffee' },
  { _id: 19, item: 'water', price: 100, description: 'about water' },
  { _id: 18, item: 'bread', price: 3, description: 'about bread' },
  { _id: 16, item: 'melon', price: 11, description: 'about melon' },
  {
    _id: 15,
    item: 'watermelon',
    price: 93,
    description: 'about watermelon'
  },
  { _id: 14, item: 'turkey', price: 83, description: 'about turkey' },
  { _id: 13, item: 'chicken', price: 63, description: 'about chicken' },
  { _id: 12, item: 'candies', price: 53, description: 'about candies' },
  {
    _id: 11,
    item: 'chocolate',
    price: 32,
    description: 'about chocolate'
  },
  { _id: 10, item: 'cookies', price: 31, description: 'about cookies' },
  { _id: 9, item: 'pecans', price: 33, description: 'about pecans' },
  {
    _id: 8,
    item: 'cucumbers',
    price: 45,
    description: 'about cucumbers'
  },
  { _id: 7, item: 'limes', price: 21, description: 'about limes' },
  {
    _id: 6,
    item: 'potatoes',
    price: 60,
    description: 'about potatoes'
  },
  {
    _id: 5,
    item: 'pineapples',
    price: 14,
    description: 'about pineapples'
  },
  { _id: 4, item: 'lemons', price: 10, description: 'about lemons' },
  { _id: 3, item: 'mangos', price: 30, description: 'about mangos' },
  { _id: 2, item: 'oranges', price: 20, description: 'about oranges' },
  { _id: 1, item: 'apples', price: 12, description: 'about apples' },
  {
    _id: 17,
    item: 'coca-cola',
    price: 88,
    description: 'about coca-cola'
  }
]
```

Смотрим план <br>
Индекс $**_text используется

```
test> db.products3.explain().find({$text: {$search: "about"}});
{
  explainVersion: '1',
  queryPlanner: {
    namespace: 'test.products3',
    parsedQuery: {
      '$text': {
        '$search': 'about',
        '$language': 'none',
        '$caseSensitive': false,
        '$diacriticSensitive': false
      }
    },
    indexFilterSet: false,
    queryHash: 'CF6F4CEE',
    planCacheShapeHash: 'CF6F4CEE',
    planCacheKey: '08852285',
    optimizationTimeMillis: 0,
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    prunedSimilarIndexes: false,
    winningPlan: {
      isCached: false,
      stage: 'TEXT_MATCH',
      indexPrefix: {},
      indexName: '$**_text',
      parsedTextQuery: {
        terms: [ 'about' ],
        negatedTerms: [],
        phrases: [],
        negatedPhrases: []
      },
      textIndexVersion: 3,
      inputStage: {
        stage: 'FETCH',
        inputStage: {
          stage: 'IXSCAN',
          keyPattern: { _fts: 'text', _ftsx: 1 },
          indexName: '$**_text',
          isMultiKey: true,
          isUnique: false,
          isSparse: false,
          isPartial: false,
          indexVersion: 2,
          direction: 'backward',
          indexBounds: {}
        }
      }
    },
    rejectedPlans: []
  },
  queryShapeHash: '600EE6DB3AA27E5BD210AF56406804990607F07820F93A814BD236A328CC4536',
  command: {
    find: 'products3',
    filter: { '$text': { '$search': 'about' } },
    '$db': 'test'
  },
  serverInfo: {
    host: 'bc7ffdbe0ba8',
    port: 27017,
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
  ok: 1
}
```

Ищем продукты со словом apples
```
test> db.products3.find({$text: {$search: "apples"}});
[ { _id: 1, item: 'apples', price: 12, description: 'about apples' } ]
```

План <br>
Индекс $**_text используется
```
test> db.products3.explain("executionStats").find({$text: {$search: "apples"}});
{
  explainVersion: '1',
  queryPlanner: {
    namespace: 'test.products3',
    parsedQuery: {
      '$text': {
        '$search': 'apples',
        '$language': 'none',
        '$caseSensitive': false,
        '$diacriticSensitive': false
      }
    },
    indexFilterSet: false,
    queryHash: 'CF6F4CEE',
    planCacheShapeHash: 'CF6F4CEE',
    planCacheKey: '08852285',
    optimizationTimeMillis: 0,
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    prunedSimilarIndexes: false,
    winningPlan: {
      isCached: false,
      stage: 'TEXT_MATCH',
      indexPrefix: {},
      indexName: '$**_text',
      parsedTextQuery: {
        terms: [ 'apples' ],
        negatedTerms: [],
        phrases: [],
        negatedPhrases: []
      },
      textIndexVersion: 3,
      inputStage: {
        stage: 'FETCH',
        inputStage: {
          stage: 'IXSCAN',
          keyPattern: { _fts: 'text', _ftsx: 1 },
          indexName: '$**_text',
          isMultiKey: true,
          isUnique: false,
          isSparse: false,
          isPartial: false,
          indexVersion: 2,
          direction: 'backward',
          indexBounds: {}
        }
      }
    },
    rejectedPlans: []
  },
  executionStats: {
    executionSuccess: true,
    nReturned: 1,
    executionTimeMillis: 0,
    totalKeysExamined: 1,
    totalDocsExamined: 1,
    executionStages: {
      isCached: false,
      stage: 'TEXT_MATCH',
      nReturned: 1,
      executionTimeMillisEstimate: 0,
      works: 2,
      advanced: 1,
      needTime: 0,
      needYield: 0,
      saveState: 0,
      restoreState: 0,
      isEOF: 1,
      indexPrefix: {},
      indexName: '$**_text',
      parsedTextQuery: {
        terms: [ 'apples' ],
        negatedTerms: [],
        phrases: [],
        negatedPhrases: []
      },
      textIndexVersion: 3,
      docsRejected: 0,
      inputStage: {
        stage: 'FETCH',
        nReturned: 1,
        executionTimeMillisEstimate: 0,
        works: 2,
        advanced: 1,
        needTime: 0,
        needYield: 0,
        saveState: 0,
        restoreState: 0,
        isEOF: 1,
        docsExamined: 1,
        alreadyHasObj: 0,
        inputStage: {
          stage: 'IXSCAN',
          nReturned: 1,
          executionTimeMillisEstimate: 0,
          works: 2,
          advanced: 1,
          needTime: 0,
          needYield: 0,
          saveState: 0,
          restoreState: 0,
          isEOF: 1,
          keyPattern: { _fts: 'text', _ftsx: 1 },
          indexName: '$**_text',
          isMultiKey: true,
          isUnique: false,
          isSparse: false,
          isPartial: false,
          indexVersion: 2,
          direction: 'backward',
          indexBounds: {},
          keysExamined: 1,
          seeks: 1,
          dupsTested: 1,
          dupsDropped: 0
        }
      }
    }
  },
  queryShapeHash: '600EE6DB3AA27E5BD210AF56406804990607F07820F93A814BD236A328CC4536',
  command: {
    find: 'products3',
    filter: { '$text': { '$search': 'apples' } },
    '$db': 'test'
  },
  serverInfo: {
    host: 'bc7ffdbe0ba8',
    port: 27017,
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
  ok: 1
}

```
4. Не забываем ВМ остановить/удалить
```
$ docker compose stop mongodb
WARN[0000] /lessons/mongodb/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Stopping 1/1
 ✔ Container mongodb  Stopped 
 ```
