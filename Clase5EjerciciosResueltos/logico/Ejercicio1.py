import pandas as pd

archivo = pd.ExcelFile('ArchivoExcel.xlsx')
print(archivo.sheet_names)