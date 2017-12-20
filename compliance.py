from subprocess import check_output

print "Compliance Checker!"

cmds = {} # commands dict
cmds["python"] = ["python", "2.7.8"]
cmds["pythonIncorrect"] = ["python", "2.7.9"]

incompliant = {} # incompliant dict

for key in cmds:
  cmd = cmds[key][0]
  expected = cmds[key][1]
  actual = check_output(cmd, shell=True)
  print "compliance check: " + cmd + " " + expected + " " + actual
  if expected not in actual:
    print expected + " not found in " + actual
    incompliant[key] = cmds[key] + [actual]

if len(incompliant.keys()) > 0:
  for key2 in incompliant:
    print "{0} : {1}".format(key2, incompliant[key2][2])


# run a command and return whether it contains
# expected version number
# def containsCorrectVersion(cmd, expected):
#   actual = check_output([cmd])
#   return expected in actual

