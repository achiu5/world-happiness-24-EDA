import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
import tabula

#happy_df = pd.read_csv("")

pdf_path = 'https://files.worldhappiness.report/WHR24_Ch02.pdf?_gl=1*6t3037*_gcl_au*NDUwNTU2MTUzLjE3NTk3MDQ3Njg.'
pages_to_read = '22-24'

df_list = tabula.read_pdf(pdf_path, pages = pages_to_read, lattice = True)

# If the library finds one table on that page, it will be the first item in the list.
if df_list:
    my_table = df_list[0]
    my_table.to_excel('output_from_page_3.xlsx', index=False)
    print("Successfully extracted the table from the specified page.")
else:
    print("No tables were found on that page.")