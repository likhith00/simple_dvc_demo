from os import read
import argparse
from get_data import read_params
import mlflow


def log_production_model(config_path):
    config = read_params(config_path=config_path)
    mlflow_config = config["mlflow_config"]
    print(mlflow_config)
    '''mlflow_name = mlflow_config["registered_model_name"]
    remote_server_uri = mlflow_config["remote_server_uri"]
    mlflow.set_registry_uri(remote_server_uri)
    runs = mlflow.search_runs()
    print(runs)'''
    




if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    log_production_model(parsed_args.config)



