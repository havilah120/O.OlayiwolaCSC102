def pau():
 import pandas as pd
 name = input("Input your Name:\n")
 number = input("Input ypur Matric Number:\n")
 department = input("Input your Department:\n")
 level = input("Input your Level:\n")
 records = {
    'Student Name': name,
    'Matric.Number': number,
    'Department': department,
    'Level': level
    }
  
 df = pd.DataFrame(records)
 df.to_csv('PAUSIMS.csv')

