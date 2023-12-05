import csv
import os
import time

from fastapi import HTTPException
from fastapi.responses import StreamingResponse
from src.config.config import get_settings

SETTINGS = get_settings()

class CSVItem():
    def __init__(self, csv_file_name: str, input_text: str, prediction_type: str, prediction: str, datetime: str, execution_time: str, models: str):
        self.csv_file_name = csv_file_name
        self.input_text = input_text
        self.prediction_type = prediction_type
        self.prediction = prediction
        self.datetime = datetime
        self.execution_time = execution_time
        self.models = models

    def to_list(self):
        return [
            self.csv_file_name,
            self.input_text,
            self.prediction_type,
            self.prediction,
            self.datetime,
            self.execution_time,
            self.models
        ]


class CSVService():
    def __init__(self):
        self.csv_path = SETTINGS.csv_path
        self.csv_headers = ["csv_file_name", "input_text", "prediction_type", "prediction", "datetime", "execution_time", "models"]

        folders = self.csv_path.split("/")[:-1]

        # create folders if not exists
        for i in range(1, len(folders) + 1):
            folder = "/".join(folders[:i])
            if not os.path.exists(folder):
                os.mkdir(folder)

        # create csv file if not exists
        if not os.path.exists(self.csv_path):
            with open(self.csv_path, "a") as f:
                f.write(",".join(self.csv_headers) + "\n")
        

    def write_csv(self, data: CSVItem):
        with open(self.csv_path, "a", newline="") as f:
            writer = csv.writer(f, delimiter="|")
            writer.writerow(data.to_list())

    def read_csv(self) -> list:
        with open(self.csv_path, "r") as f:
            reader = csv.reader(f, delimiter="|")
            data = list(reader)
        return data
    
    def get_csv_file(self) -> StreamingResponse:
        if not os.path.exists(self.csv_path):
            raise HTTPException(status_code=404, detail="CSV file not found")
        
        with open(self.csv_path, mode="r", encoding="utf-8") as file:
            csv_data = file.read()

        response = StreamingResponse(iter([csv_data]), media_type="text/csv")

        response.headers["Content-Disposition"] = f'attachment; filename="report-{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}.csv"'
        
        return response