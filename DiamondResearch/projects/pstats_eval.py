import pstats

p = pstats.Stats(
    "/Users/vishwanathwimalasena/Documents/RandomElectricFieldSimulations/spectrum_new.pstat"
)

p.strip_dirs()
p.sort_stats(pstats.SortKey.TIME)
p.print_stats(
    0.5,
)
