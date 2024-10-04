import pandas as pd
import numpy as np

class Data_IO():
    
    def read_file_excel(self, path):
        try:
            data = pd.read_excel(path)
            print(f"File successfully read from {path}")
            return data
        except FileNotFoundError:
            print(f"File not found: {path}")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
        return None

    def curated_data(self,df):
        missing_data=df.isnull().sum()
        df['Description'].fillna('Not Description', inplace=True)
        df.dropna(subset=['CustomerID'], inplace=True)
        missing_data = df.isnull().sum()
        print("Missing data after curation:")
        print(missing_data)
        return df
    def parsing_data(self,data,file_config):
        try:
            with open(file_config, 'r') as f:
            config = json.load(f)
            
            for column, dtype in config.items():
            if column in data.columns:
                data[column] = data[column].astype(dtype)
            else:
                print(f"Column {column} not found in data")
            
            print("Data parsing completed based on config")
            return data
        except FileNotFoundError:
            print(f"Config file not found: {file_config}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from config file: {file_config}")
        except Exception as e:
            print(f"An error occurred while parsing the data: {e}")
        return None

    def export_df_parquet(self, df, path):
        try:
            df.to_parquet(path, index=False)
            print(f"DataFrame successfully exported to {path}")
        except Exception as e:
            print(f"An error occurred while exporting the DataFrame: {e}")



        
