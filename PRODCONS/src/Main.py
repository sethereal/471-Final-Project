from .GlobalStats import GlobalStats
from .StoreSimulation import StoreSimulation

def main():
    # Create an instance of GlobalStats
    global_stats = GlobalStats()

    # Define the combinations of producers and consumers
    combinations = [
        (2, 2),
        (2, 10),
        (10, 2),
        (10, 10)
    ]

    # Run simulations for each combination
    for p, c in combinations:
        simulation_name = f"StoreSimulation(p={p}, c={c})"
        store_simulation = StoreSimulation(p, c, simulation_name)
        store_simulation.Run()
        global_stats_instance, total_items_produced = store_simulation.GetStats()
        global_stats.update(*global_stats_instance)

if __name__ == "__main__":
    main()