import threading
import time
from .ProducerClass import Producer
from .ConsumerClass import Consumer
from .SharedBuffer import SharedBuffer
from .GlobalStats import GlobalStats


class StoreSimulation:
    def __init__(self, num_p, num_c, simulation_name):
        self.__shared_buffer = SharedBuffer(10)
        self.__special_flag = threading.Event()
        self.__producers = [Producer(self.__shared_buffer, i+1) for i in range(num_p)]
        self.__consumers = [Consumer(self.__shared_buffer, i+1, self.__special_flag) for i in range(num_c)]
        self.__global_stats = GlobalStats()
        self.__simulation_name = simulation_name
        self.__total_items_produced = 0

    # Run the store simulation
    def Run(self):
        start_time = time.time()

        # Start producer threads
        producer_threads = [threading.Thread(target=producer.produce) for producer in self.__producers]
        for thread in producer_threads:
            thread.start()

        # Start consumer threads
        consumer_threads = [threading.Thread(target=consumer.consume) for consumer in self.__consumers]
        for thread in consumer_threads:
            thread.start()

        # Wait for all producer threads to finish
        for thread in producer_threads:
            thread.join()

        # Set the special flag to indicate all sale records have been read
        self.__special_flag.set()

        # Wait for all consumer threads to finish
        for thread in consumer_threads:
            thread.join()

        end_time = time.time()
        total_time = end_time - start_time

        # Collect local statistics from all consumers
        for consumer in self.__consumers:
            local_stats = consumer.ReportLocalStats()
            self.__global_stats.update(*local_stats)
            self.__total_items_produced += local_stats[2]

        # Print global statistics
        self.__print_local_stats()
        self.__print_global_stats(total_time)
        
    # Return the global statistics and total items produced
    def GetStats(self):
        return self.__global_stats.GetGlobalStats(), self.__total_items_produced


     # Print the local statistics for each consumer
    def __print_local_stats(self):

        print(f"\nLocal Statistics for {self.__simulation_name}:")
        print("=" * 50)

        for consumer in self.__consumers:
            local_storewide_total, local_month_total, local_aggregate_total = consumer.ReportLocalStats()

            print(f"Consumer {consumer._Consumer__consumer_id} Local Statistics:")

            for store_id, total in local_storewide_total.items():
                print(f"Store {store_id} Storewide Total: {total:.2f}")

            print()

            for store_id, month_data in local_month_total.items():
                print(f"Store {store_id} Monthly Totals:")
                month_totals = [month_data.get(month, 0) for month in range(1, 13)]
                month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                month_stats = ", ".join(f"{month_names[i]}: {total:.2f}" for i, total in enumerate(month_totals))
                print(f"[{month_stats}]")
                print()

            print(f"Consumer {consumer._Consumer__consumer_id} Aggregate Total: {local_aggregate_total:.2f}")
            print()

    # Print the global statistics
    def __print_global_stats(self, total_time):
        global_storewide_total, global_month_total, global_aggregate_total = self.__global_stats.GetGlobalStats()

        print(f"\nGlobal Statistics for {self.__simulation_name}:")
        print("=" * 50)

        for store_id, total in global_storewide_total.items():
            print(f"Store {store_id} Storewide Total: {total:.2f}")

        print()

        for store_id, month_data in global_month_total.items():
            print(f"Store {store_id} Monthly Totals:")
            month_totals = [month_data.get(month, 0) for month in range(1, 13)]
            month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            month_stats = ", ".join(f"{month_names[i]}: {total:.2f}" for i, total in enumerate(month_totals))
            print(f"[{month_stats}]")
            print()

        print(f"Aggregate Total: {global_aggregate_total:.2f}")
        print(f"Total Simulation Time: {total_time:.2f} seconds")
        print("=" * 50)
