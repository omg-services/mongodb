# _MongoDB_ OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)

This service is a wrapper around the official Python SDK for MongoDB.

## Direct usage in [Storyscript](https://storyscript.io/):

```coffee
result = mongodb insert db: "test" coll: "my_coll" doc: {"foo": "bar"}
# Do something with result._id

# You can also specify the arguments sort and fields (projection) below.
result = mongodb find db: "test" coll: "my_coll" query: {}
result = mongodb find_one db: "test" coll: "my_coll" query: {}
```

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

### TODOs
This is a WIP service, and as such, only a few APIs from the MongoDB SDK have
been exposed.

PRs are welcome.

The following APIs are yet to be implemented:
1. Update
2. Upsert
3. A string cursor implementation
4. Find - limit
5. And much more

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### Find
```shell
$ omg run find -a db=<DATABASE> -a coll=<COLUMN> -a query=<QUERY> -a sort=<SORT> -a fields=<FIELDS> -e MONGODB_URI=<MONGODB_URI>
```
##### FindOne
```shell
$ omg run findOne -a db=<DATABASE> -a coll=<COLUMN> -a query=<QUERY> -a sort=<SORT> -a fields=<FIELDS> -e MONGODB_URI=<MONGODB_URI>
```
##### Insert
```shell
$ omg run find -a db=<DATABASE> -a coll=<COLUMN> -a doc=<DOC> -e MONGODB_URI=<MONGODB_URI>
```

**Note**: the OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/mongodb/blob/master/LICENSE).
