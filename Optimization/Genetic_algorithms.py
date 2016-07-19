import optimization
reload(optimization)
domain=[(0,9)]*(len(optimization.people)*2)
s=optimization.geneticoptimize(domain,optimization.schedulecost)
