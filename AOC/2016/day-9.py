import re
with open("day-9.in") as d:
  data = d.read()

counter = 0
index = 0
d = data

while True:
    commands = d[index:].split("(")


    if len(commands) <= 1:
        print("PART I", len(d))
        break


    if "x" in list(commands[1]):
      cmd_1 = int(commands[1].split(")")[0].split("x")[0])
      cmd_2 = int(commands[1].split(")")[0].split("x")[1])
      pattern = commands[1].split(")")[1][0:cmd_1]*cmd_2


      if pattern == "":
        location = 0
        for index_,loc in enumerate(d[index:]):
            if loc == "(":
                location = index_
                break

        pattern = d[index+location+len(f"({cmd_1}x{cmd_2})"):index+location+len(f"({cmd_1}x{cmd_2})")+cmd_1]*cmd_2
        replaced = d[index+location:index+location+len(f"({cmd_1}x{cmd_2})")+len(d[index+location+len(f"({cmd_1}x{cmd_2})"):index+location+len(f"({cmd_1}x{cmd_2})")+cmd_1])]
        d = d.replace(replaced, pattern)
        index += len(pattern)+1


      else:
        location = 0
        for index_, loc in enumerate(d[index:]):
            if loc == "(":
                location = index_
                break

        replaced_ = d[index+location:index+location+int(len(pattern)/cmd_2)+len(f"({cmd_1}x{cmd_2})")]
        d = d.replace(replaced_, pattern)
        index += len(pattern) + 1

