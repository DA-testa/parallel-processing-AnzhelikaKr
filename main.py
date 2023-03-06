# python3

def parallel_processing(n, m, data):
    output = []
    paral=[0]*n
    #print(paral) 
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    t=0
    j=0
    while j<m:
        done=False
        while not done:
            try:
                i=paral.index(t)
            except: 
                # print("not in array", t,j)
                done = True
            if not done:
                paral[i]+=data[j]
                j+=1
                output.append([i,t])
                # print(i,t, paral[i])
            if j==m:
                # print("b")
                break
        t+=1

   

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n,m=map(int,input().split())   
    
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = [int(s) for s in input().split()]

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for i in result:
        print(i)
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
