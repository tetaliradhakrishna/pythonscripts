import sched, time
s = sched.scheduler(time.time, time.sleep)

def ass(x):
  if x == 1:
    print("ass matched.") 
    return True

def do_something(sc): 
    print("Doing stuff...")
    var_stu = ass(2)
    print(var_stu)
    if var_stu:
      print("hey ass")
    else:
      # do your stuff
      print("calling Else ")
      s.enter(10, 1, do_something, (sc,))

s.enter(10, 1, do_something, (s,))
s.run()



