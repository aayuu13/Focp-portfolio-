import math
import time
import sys

print("Park Run Timer")
print("~~~~~~~~~~~~~~")
print("Lets Go!")
data=[]
time_records=[]
player_num=[]
time_taken=[]
runners=[]
total=0
#INITIALIZING VALUE---------------
fastest_time=0
slowest_time=0
fastest_runner=None
total_runners=0

#FUNCTION TO CONVERT TIME TO MIN,SEC
def convert(timeinsec):
    result = time.strftime("%M minutes and %S seconds", time.gmtime(timeinsec))
    return result

while True:
  line= input(">")
  if line == "END":
    break

  parts = line.split("::")
  if len(parts) != 2:
    print("Error in data stream. Ignorning. Carry on.")
    continue
  # Check for special characters in input
  if not parts[0].isnumeric() or not parts[1].isnumeric():
    print("Error in data stream input contains special characters. Ignoring.")
    continue

  try:
    runner_number = int(parts[0])
    timee = int(parts[1])
    data.append(parts)
  except ValueError:
    print("Error in data stream. Ignorning. Carry on.")
    continue
  total=total+timee
  if '::' in parts:
    data.append(runners.split("::"))

  #FOR FINDING THT BEST TIME RUNNER
  if fastest_time == 0 or timee < fastest_time:
    fastest_time = timee
    best_time_here_runner = runner_number 

#Created 2 different list for player number and tike taken to complete the set 
player_num = [i[0] for i in data] 
time_taken =[i[1] for i in data]  

#TOTAL NUMBER OF RUNNERS-------------------------------
total_runners=len(data)

#FOR AVERAGE--------------------------------------------
if total_runners==0:
  print("No data found. Nothing to do. What a pity.")
  sys.exit()
else:
  average_time=total/total_runners
for t in time_taken:
  time_taken=int(t)
  time_records.append(time_taken)

#FOR FASTEST & SLOWEST TIME---------------------------  
fastest_time=min(time_records)
slowest_time=max(time_records)

#Results----------------
print("Total Runners:",total_runners)

avg=convert(average_time)
print("Average time:",avg)

fastest_runner=convert(fastest_time)
print("Fastest Runner:",fastest_runner)

slowest_runner=convert(slowest_time)
print("Slowest Runner:",slowest_runner)
 
print("Fastest Runner #",best_time_here_runner) 