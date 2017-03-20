def return_continue_break(type):
    if(not type in ["return", "continue", "break"]):
        print '"type" should be "return, continue, break".'
        return
    for j in range(0, 10):
        for i in range(0, 10):
            print "j_i: %d_%d" %(j, i)
            if(i > 3):
               if(type == "return"):
                   return
               elif(type == "continue"):
                   continue
               else:
                   break
            print "executed!"

if __name__ == '__main__':
    return_continue_break("break")
    return_continue_break("continue")
    return_continue_break("return")
