FROM python:3.8

COPY requirements.txt ./

ARG AIRFLOW_HOME=/opt/airflow

ENV AIRFLOW_HOME=${AIRFLOW_HOME}

RUN pip install --no-cache-dir -r requirements.txt

COPY start_airflow_scheduler.sh .

RUN chmod +x start_airflow_scheduler.sh

CMD ["./start_airflow_scheduler.sh"]