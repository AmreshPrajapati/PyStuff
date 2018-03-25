if __name__ == '__main__':
    N = int(input())
    mylist = []
    for i in range(N):
        cmd = input().split()
        if(len(cmd)==3):
            eval("mylist.{0}({1}, {2})".format(cmd[0], cmd[1], cmd[2]))
        elif(len(cmd)==2):
            eval("mylist.{0}({1})".format(cmd[0], cmd[1]))
        elif(cmd[0]=='print'):
                print(mylist)
        elif(len(cmd)==1):
            eval("mylist.{0}()".format(cmd[0]))
