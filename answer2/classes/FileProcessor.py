import os
import datetime
from typing import List, Optional, Tuple
from pydicom import examples
import csv
import statistics
from classes.LoggerObj import LoggerObj


class FileProcessor:
    def __init__(self, base_path: str, log_file: str):
        self.base_path = base_path
        self.logger = LoggerObj(log_file)

    def list_folder_contents(self, folder_name: str, details: bool = False) -> None:
        path = f'{self.base_path}/{folder_name}'
        dirs = os.listdir(path)

        print(f'Folder: {path}')
        print(f'Number of elements: {len(dirs)}')
        files = []
        folders = []

        try:
            for element in dirs:
                file_path = f'{path}/{element}'
                file_size = 'N/A'
                file_modified = 'N/A'

                if details:
                    file_size = self.getMB(os.path.getsize(file_path))
                    file_modified = self.getDate(os.path.getmtime(file_path))

                if os.path.isdir(file_path):
                    folders.append((element, f'Last Modified: {file_modified}'))
                else:
                    files.append((element, f'{file_size} MB', f'Last Modified: {file_modified}'))

            print('Files: ')
            for file in files:
                print(f'- {file}')

            print('Folders: ')
            for folder in folders:
                print(f'- {folder}')

        except Exception as ex:
            self.logger.log(f'{ex}')

    def read_csv(self, filename: str, report_path: Optional[str] = None, summary: bool = False) -> None:
        try:
            report = f'==== {datetime.datetime.now()} ===='
            report += '\nCSV Analysis: \n'

            file_path = f'{self.base_path}/{filename}'
            with open(f"{file_path}", "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                
                columns = []
                values = []
                idx = 0
                for row in reader:
                    if idx == 0:
                        columns = row
                    else:
                        values.append(row)

                    idx += 1
                
                report += f'Columns ({len(columns)}): {columns} \n'
                report += f'Rows: {len(values)} \n'
                
                numerics = []
                non_numerics = []
                first_value = values[0]

                idx_col = 0
                for column in first_value:
                    try:
                        int(column)
                        numerics.append(idx_col)
                    except: 
                        non_numerics.append(idx_col)

                    idx_col += 1
                
                report += 'Numerics Columns: \n'
                for header in numerics:
                    array = []
                    for value in values:
                        array.append(int(value[header]))

                    average = round(statistics.mean(array), 2)
                    deviation = round(statistics.stdev(array), 2)

                    report += f'- {columns[header]}: Average = {average}, Std Dev = {deviation} \n'
                
                if summary:
                    report += 'Non-Numeric Columns: \n'
                    for header in non_numerics:
                        report += f'- {columns[header]}: Unique Values = {len(values)} \n'
                
                if report_path is not None:
                    report_base_path = f'{self.base_path}/{report_path}'

                    if not os.path.exists(report_base_path):
                        os.mkdir(report_base_path)
                    
                    with open(f'{report_base_path}/report.txt', 'a') as archive:
                                report += f'Saved Summary report to {report_path}\n'
                                archive.write(report)

                print(report)
        except Exception as ex:
            self.logger.log(f'{ex}')

    def read_dicom(self, filename: str, tags: Optional[List[Tuple[int, int]]] = None, extract_image: bool = False) -> None:
        try:
            path_file = f'{self.base_path}/{filename}'
            ds = examples._get_path(path_file)
            print(ds)
        except Exception as ex:
            self.logger.log(f'{ex}')
    
    def __str__(self):
        return f'{self.base_path} {self.logger}'

    def getDate(self, time_ms: float):
        dt = datetime.datetime.fromtimestamp(time_ms, tz=datetime.timezone.utc)
        return dt

    def getMB(self, bytes: int):
        return round(bytes / 1028 / 1028, 1)
