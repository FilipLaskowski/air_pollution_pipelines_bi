#!/usr/bin/env bash

cd $AIRFLOW_HOME

airflow db init

airflow users create -e "admin@airflow.com" -f "airflow" -l "airflow" -p "airflow" -r "Admin" -u "airflow"

airflow webserver -p 8080