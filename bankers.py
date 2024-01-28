def bankers_formula(p, resource, allocation, max_allo):
    process, need, n = [" "], [" "], [max_allo[i] - allocation[i] for i in range(len(p))]
    return_, available, finished = [" "], [(resource - sum(allocation))], [0] * len(p) 

    while True:
        np = None
        for i in range(len(p)):
            if n[i] <= available[-1] and finished[i] == 0:
                process.extend([f"P{i}", f"P{i} Ex"])
                need.extend([n[i], " "])
                return_.extend([" ", max_allo[i]])
                available.append(available[-1] - n[i])
                available.append(return_[-1] + available[-1])
                finished[i] = 1
                np = process[-1]
                break

        if np is None:
            break

    return process, need, return_, available, finished

def main():
    allocation, max_allo = [], []

    print("\n-----------------------------------")
    print("CPU SCHEDULING | Banker's Algorithm")
    print("-----------------------------------\n")

    n = int(input(f"Enter number of process: "))
    p = [f"P{i}" for i in range(n)]
    resource = int(input("Enter the number of resource: "))

    for i in range(n):
        allocation.append(int(input(f"\nAllocation of {p[i]}: ")))
        max_allo.append(int(input(f"Maximum allocation of {p[i]}: ")))

    process, need, return_, available, finished  = bankers_formula(p, resource, allocation, max_allo)

    print("+-------" * 4, end="+\n")
    print("| Prcss\t| Need\t| Retrn\t| Avail\t", end="|\n")
    print("+-------" * 4, end="+\n")
    for i in range(len(process)):
        print(f"| {process[i]}\t|   {need[i]}\t|   {return_[i]}\t|   {available[i]}\t", end="|\n")
    print("+-------" * 4, end="+\n")

    if len(p) == sum(finished):
        print("\n\nNo Deadlock. Safe sequence")
    else:
        print("\n\nThere's Deadlock. Unsafe state")
    print("--------------------------")


main()