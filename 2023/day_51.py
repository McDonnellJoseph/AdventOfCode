ipt, D = open("input.txt").read().split("\n\n"), {}
SEEDS = [int(i) for i in ipt.pop(0).split("seeds: ")[1].split(" ")]

for idx, line in enumerate(ipt):
    val = [int(i) for i in line.replace("\n", " ").split(" ") if i and i[0].isdigit()]
    while val:
        D[idx] = D.get(idx, []) + [[val.pop(0), val.pop(0), val.pop(0)]]

for n_iter, part in [(1, 1), (20, 2)]:
    seeds = SEEDS if part ==2 else sum( [[i,1] for i in SEEDS], [] )
    ALL_SEEDS = (j for i in range(len(seeds)//2) for j in range(seeds[2*i], seeds[2*i] + seeds[2*i+1], 2**n_iter))
    for iter in range(n_iter, 0, -1):
        MIN = (0, float("inf"))
        for seed in ALL_SEEDS:
            val = seed
            for _l in D.values():
                val += next( (a-b for a,b,c in _l + [(val, val, 1)] if b<=val<b+c))
            
            MIN = MIN if MIN[1] < val else (seed, val)
        ALL_SEEDS = (i for i in range(MIN[0] - 2**(iter)-1, MIN[0]+ 2**(iter)+1, 2**(iter-1)))
    print(f"the answer {part} is : ", MIN[1])
