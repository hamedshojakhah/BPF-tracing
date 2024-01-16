import os
import csv


log_path = 'log.txt'
delta_dir = 'delta'


if not os.path.exists(delta_dir):
   os.mkdir(delta_dir)




def calculate_average(filepath):
   with open(filepath, 'r') as csvfile:
       reader = csv.reader(csvfile)
       first_column = []
       for row in reader:
           first_column.append(float(row[0]))


   average = sum(first_column) / len(first_column)
   return average




def write_average(filepath, average):
   with open(filepath, 'a') as csvfile:
       csvwriter = csv.writer(csvfile)
       csvwriter.writerow([average])




def read_file_line_by_line(file_path):
   with open(file_path, 'r') as file:
       for line in file:
           yield line.strip()






lines = read_file_line_by_line(log_path)
first_line = next(lines)
layer, timestamp, skb_buff = first_line.split()
for line in lines:
   next_layer, next_timestamp, next_skb_buff = line.split()
   if next_skb_buff == skb_buff:
       if next_layer > layer:
           with open(f"{delta_dir}/{layer}-{next_layer}.csv", "a") as target_file:
               target_file.write(f"{int(next_timestamp) - int(timestamp)}, {skb_buff}\n")
   layer, timestamp, skb_buff = next_layer, next_timestamp, next_skb_buff




for filename in os.listdir(delta_dir):
   filepath = os.path.join(delta_dir, filename)
   average = calculate_average(filepath)
   write_average(filepath, average)
