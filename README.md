# MongoDB
This service is a wrapper around the official Python SDK for MongoDB.

### Usage

```coffee
# Storyscript
result = mongodb insert db: "test" coll: "my_coll" doc: {"foo": "bar"}
# Do something with result._id

# You can also specify the arguments sort and fields (projection) below.
result = mongodb find db: "test" coll: "my_coll" query: {}
result = mongodb find_one db: "test" coll: "my_coll" query: {}
```

### TODOs
This is a WIP in progress service, and as such, only a few APIs from the MongoDB SDK have
been exposed.

PRs are welcome.

The following APIs are yet to be implemented:
1. Update
2. Upsert
3. A string cursor implementation
4. Find - limit
5. And much more
