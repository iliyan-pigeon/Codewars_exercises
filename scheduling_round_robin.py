def round_robin(jobs, time_slice, index):
    cc = 0
    while True:
        for i in range(len(jobs)):
            if jobs[index] <= time_slice and index == i:
                cc += jobs[index]
                return cc
            elif time_slice >= jobs[i]:
                cc += jobs[i]
                jobs[i] = 0
            elif time_slice < jobs[i]:
                jobs[i] -= time_slice
                cc += time_slice
