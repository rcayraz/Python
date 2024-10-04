from data_io import Data_IO
data=Data_IO()
data_source=data.read_file_excel('/workspaces/Python/projects/sales/data/Online_Retail.xlsx')
curated_data=data.curated_data(data_source)
data.export_df_parquet(curated_data,'/workspaces/Python/projects/sales/data/curated/curated_online_retail.parquet')

