#!/usr/bin/env bash

function usage() {
    printf "submit_job.sh <python script file>\n"
}

if [ -z $1 ]; then
    usage
    exit 1
fi

spark-submit --driver-class-path /opt/bitnami/spark/jars/postgresql.jar --jars /opt/bitnami/spark/jars/postgresql.jar $1
