import re
def balance(book):
  tasks = book.splitlines()
  s = ''''''
  start_b = float(str(re.findall(r'\d*\.\d+|\d+', tasks[0])[0]))
  sum = 0
  num = 0
  #print("Original Balance: " + str('{:.2f}'.format(start_b)))
  s += str("Original Balance: " + str('{:.2f}'.format(start_b)) + "\n")
  i = -1
  for task in tasks:
    i+=1
    tas = re.findall(r'\d*\.\d+|\d+', task)
    task = task.replace("_", " ")
    task = task.replace("!", "")
    task = task.replace("=", "")
    task = task.replace(":", "")
    task = task.replace(";", "")
    task = task.replace("?", "")
    task = task.replace("{", "")
    task = task.replace("}", "")
    task = task.replace(",", "")
    if (i != 0):
      task = task.replace(str(tas[1]), '{:.2f}'.format(float(tas[1])))
      sum += float(str((tas[1])))
      num += 1
      start_b -= float(str((tas[1])))
      #print(task + " Balance " + str('{:.2f}'.format(start_b,2)))
      s += str(task + " Balance " + str('{:.2f}'.format(start_b,2))+ "\n")
      #print("Total expense  " + str('{:.2f}'.format(sum,2)))
  s+= str("Total expense  " + str('{:.2f}'.format(sum,2))+ "\n")
  #print("Average expense  " + str('{:.2f}'.format(sum/num,2)))
  s += str("Average expense  " + str('{:.2f}'.format(sum/num,2)))
  #print(s)
  #print()
  return s
