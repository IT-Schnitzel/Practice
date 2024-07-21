def stat(s):
    lis = s.split(", ")
    min = 100000
    max = 0
    summa = 0
    numb = 0
    for elem in lis:
      elem1 = str(elem)
      elem = elem1.split("|")
      sumelem = 3600*int(elem[0]) + 60*int(elem[1]) + int(elem[2])
      if (sumelem > max):
        max = sumelem
      if (sumelem < min):
        min = sumelem
      summa += sumelem
      numb += 1
    range1 = max - min
    range = ""
    if (range1 / 3600 < 10):
      range += "0" + str(range1//3600) + "|"
    else:
      range += str(range1//3600) + "|"
    range1 = range1%3600
    if (range1 / 60 < 10):
      range += "0" + str(range1//60) + "|"
    else:
      range += str(range1//60) + "|"
    range1 = range1 % 60
    if (range1 < 10):
      range += "0" + str(range1)
    else:
      range += str(range1)


    range1 = round(summa / numb)
    range2 = ""
    if (range1 / 3600 < 10):
      range2 += "0" + str(range1//3600) + "|"
    else:
      range2 += str(range1//3600) + "|"
    range1 = range1%3600
    if (range1 / 60 < 10):
      range2 += "0" + str(range1//60) + "|"
    else:
      range2 += str(range1//60) + "|"
    range1 = range1 % 60
    if (range1 < 10):
      range2 += "0" + str(range1)
    else:
      range2 += str(range1)
    s = "Range: " + range + " " + "Average: " + range2
    return s
