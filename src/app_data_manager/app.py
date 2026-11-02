import os
import sys
from pathlib import Path

from data_manager import DataManager  # type: ignore
from utils import read_config  # type: ignore

# Add project root and app_ui directory to path
project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))
os.chdir(project_root)


if __name__ == "__main__":
    config = read_config(os.path.join(project_root, "conf", "base", "parameters.yml"))
    data_manager = DataManager(config["data_manager"])
    # data_manager.init_raw_db_table()
    # last_n_points = data_manager.get_last_n_points(10, config["data_manager"]["raw_data_table_name"])
    # print("Last 10 points in raw_data table:", last_n_points)
    # inference_data = pd.read_parquet(
    #   os.path.join(project_root, "data", "01_raw", "df_prod.parquet")
    # )
    # data_manager.insert_data_to_db(inference_data, table_name="raw_data")
    # last_n_points = data_manager.get_last_n_points(10, config["data_manager"]["raw_data_table_name"])
    # print("Last 10 points in raw_data table after insertion:", last_n_points)
    # data_manager.init_predictions_db_table()
    # data_manager.init_errors_db_table()
    # data_manager.init_anomalies_db_table()

    # data = data_manager.get_data_since_timestamp(
    #    start_timestamp="2010-01-20 00:00:00",
    #    table_name="raw_data"
    #    )
    # predictions = data_manager.get_last_n_points(
    #     n=10,
    #     table_name="predictions"
    # )
    # print("predictions: ", predictions)
    # errors = data_manager.get_last_n_points(
    #     n=10,
    #     table_name="errors"
    # )
    # print("errors: ", errors)
    # anomalies = data_manager.get_last_n_points(
    #     n=10,
    #     table_name="anomalies"
    # )
    # print("anomalies: ", anomalies)
    # print(data)
    # data_manager.init_retraining_trigger_db_table()
    # print("retraining trigger table initialized")
    # triggers = data_manager.get_last_n_points(
    #     n=10,
    #     table_name="retraining_trigger"
    # )
    # print("triggers: ", triggers)
