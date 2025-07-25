from classes.FileProcessor import FileProcessor

# base = "C:/Users/asus/Downloads"
base = "E:/Personal - Luis/Projects/Pruebas Tecnicas/Imexhs/answer2"

fileproc = FileProcessor(f"{base}/data", f'{base}/logs')
fileproc.list_folder_contents(folder_name='', details=False)
print('')
fileproc.read_csv(filename='sample-02-csv.csv', report_path='./reports', summary=True)
print('')
fileproc.read_dicom('sample-02-dicom.dcm')