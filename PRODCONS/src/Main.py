from GlobalStats import GlobalStats
from StoreSimulation import StoreSimulation


def main():
    # define global statistics
    global_stats = GlobalStats()

    # p1, c1
    store_simulation_1 = StoreSimulation(2, 2)

    # run simulations
    store_simulation_1.Run()

    # get local statistics
    global_stats_1, _ = store_simulation_1.GetStats()

    # tally local stats into global stats
    global_stats_1 = global_stats.update(global_stats_1[0], global_stats_1[1], global_stats_1[2])

    print("All consumers have finished computing their local statistics.")

    print("Global Statistics:")
    print(f"Store Total: {round(global_stats_1[0], 2)}")
    print(f"Month-wise Total: {round(global_stats_1[1], 2)}")
    print(f"Aggregate Total: {round(global_stats_1[2], 2)}")

if __name__ == "__main__":
    main()