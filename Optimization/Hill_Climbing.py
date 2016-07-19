import optimization
reload(optimization)
domain=[(0,9)]*(len(optimization.people)*2)
s=optimization.hillclimb(domain,optimization.schedulecost)
print optimization.schedulecost(s)
