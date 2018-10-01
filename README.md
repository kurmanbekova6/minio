#  Subutai Minio Blueprint

Minio is an object storage server. It is compatible with Amazon S3 cloud storage service. It is best suited for storing unstructured data such as photos, videos, log files, backups and container / VM images. Size of an object can range from a few KBs to a maximum of 5TB.

## Server Access via SSH

The server and your data can be found in the folder /minio-data

To access the minio at console, ssh into the container. It is running as a service. You can check it by running

systemctl status minio.service 

## Deployment

This is a blue print which is published on Subutai Hub's Bazaar. You can also fork and deploy your own version.

https://github.com/subutai-blueprints/hackathon/wiki/Using-Subutai-Blueprints

## Overview

![Blueprint Overview](https://raw.githubusercontent.com/neilspink/minio/master/docs/Blueprint-Overview.jpeg)
