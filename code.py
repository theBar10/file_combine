import os
import glob
import pandas as pd
import datetime 

print("starting...")
print("current directory:")
print(os.getcwd())
# Returns the current local date 
current_time = datetime.datetime.now()
year = current_time.year
month = current_time.month
day = current_time.day

current_time = str("{}_{}_{}".format(year, month, day))

os.chdir(r"C:\Users\tbarten\Desktop\Projects\Cost_Productivity\PyRun")
print("grabbing data from directory:")
print(os.getcwd())
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
os.chdir(r"C:\Users\tbarten\Desktop\Projects\Cost_Productivity\PyRun\Master File")
print("saving master file in directory:")
print(os.getcwd())
combined_csv.to_csv( "master_csv.csv", index=False, encoding='utf-8-sig')
combined_csv.to_csv( "archive_master_csv_{}.csv".format(current_time), index=False, encoding='utf-8-sig')

print("finished at {}".format(current_time))
