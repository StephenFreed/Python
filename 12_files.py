import os
import shutil
import csv
import json


dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
print(dir_path)

env_var = os.environ.get("HOME")
print(env_var)

path = "/Users"

# checks if file exists
print(os.path.exists(path))
# checks if file
print(os.path.isfile(path))
# checks if dir
print(os.path.isdir(path))
# returns list of all files in dir
print(os.listdir(path))
# join dir path and filename
print(os.path.join(dir_path, "some/file/path"))
# move file
# os.replace(excel_file_source, excel_file_dest)
# copy file
# shutil.copy(full_file_path, excel_dir)
# remove file
os.remove(path)

# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file’s creation and modification times)

# examples
repo_dir = "/Users/stephenfreed/Projects"
repo_files = os.listdir(repo_dir)
for file_name in repo_files:
    full_file_path = os.path.join(repo_dir, file_name)
    if os.path.isfile(full_file_path):
        excel_dir = "/Users/stephenfreed/Projects"
        shutil.copy(full_file_path, excel_dir)


processed_source = "/Users/stephenfreed/Projects"
with open(processed_source, "a") as fp:
    fp.write(f"file_name_to_parse\n")

old_way_file = open("old_way_file.txt", "r")
old_way_file.write("old_way_file.txt")
old_way_file.close()

try_way_file = open("try_file.txt", "r")
try:
    try_way_file.write("try_file.txt")
finally:
    try_way_file.close()

# context manager
with open("file.txt", "r") as new_file:
    new_file.write("hello")

with open('message.json') as message_json:
  message = json.load(message_json)
print(message['text'])

with open('how_many_lines.txt', 'a') as my_file:
    my_file.write('This is new')

with open('how_many_lines.txt', 'r') as my_file:
    lines_list = my_file.read()
print(lines_list)


test_dict = [[1,2,3],[4,5,6],[7,8,9]]
with open('csv_test.txt', 'w') as myfile:
    csv_writer = csv.writer(myfile)
    for elm in test_dict:
      csv_writer.writerow(elm)
