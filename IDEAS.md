## General
### Implement for Distributed Minio
- A stand-alone Minio server would go down if the server hosting the disks goes offline. In contrast, a distributed Minio setup with n disks will have your data safe as long as n/2 or more disks are online. You'll need a minimum of (n/2 + 1) Quorum disks to create new objects though.
- A Subutai environment can have multiple peers. Distributed Minio has a per tenant limit of minimum 2 and maximum 32 servers https://docs.minio.io/docs/distributed-minio-quickstart-guide

