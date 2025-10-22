import pandas as pd
def MyWork(input_data,column_names): 
  df = pd.DataFrame(input_data,columns=column_names)
  return df 

data = [[]] /* Insert your data, for example: [10,'Lee Cox','Computing Systems',87] */
cols = [] /* Enter the columns, for example 'Name' */
final_data = MyWork(data,cols) // Finalize the data within the function by enter the consts and print the final const //
/* print(final_data) */
