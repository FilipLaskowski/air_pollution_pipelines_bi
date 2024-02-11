from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor

from datetime import datetime, timedelta
import requests


def response_check(response):
    try:
        response.raise_for_status()  # Sprawdź, czy odpowiedź jest w porządku
        data = response.json()
        print(data)
        if isinstance(data, list):
            return len(data) > 0
        else:
            return False
    except requests.exceptions.HTTPError as err:
        print(f"Błąd HTTP: {err}")
        return False
    except ValueError as err:
        print(f"Błąd dekodowania JSON: {err}")
        return False


default_args = {
    'owner' : 'airflow',
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retries' : 2,
    'retry_delay' : timedelta(minutes=5)
}

with DAG('fetch_data', start_date=datetime(2024, 2, 10), schedule_interval='@daily', default_args=default_args, catchup=False) as dag:

    is_api_available = HttpSensor(
        task_id='is_api_available',
        http_conn_id='fetch_data_gov',
        endpoint = '/pjp-api/rest/station/findAll',
        response_check = lambda response: response_check(response),
        poke_interval=2,
        timeout=20,
    )