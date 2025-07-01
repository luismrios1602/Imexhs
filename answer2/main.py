from classes.FileProcessor import FileProcessor

fileproc = FileProcessor("E:/Personal - Luis/Projects/Pruebas Tecnicas/Imexhs/answer2/data", './logs')
fileproc.list_folder_contents('', True)
print('')
fileproc.read_csv(filename='sample-01-csv.csv', report_path='./reports', summary=True)