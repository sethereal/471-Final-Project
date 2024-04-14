import threading
import time
from SharedBuffer import SharedBuffer
from ProducerClass import Producer
from ConsumerClass import Consumer
from GlobalStats import GlobalStats

class StoreSimulation:
    def __init__(self, num_p, num_c) -> None:
        self.__shared_buffer = SharedBuffer(10)
        self.__producers = [Producer(self.__shared_buffer, i+1) for i in range(num_p)]  #
        self.__consumers = [Consumer(self.__shared_buffer, i+1) for i in range(num_c)]
        self.__global = GlobalStats()
        self.__elapsed_time = None
        
    
    def Run(self) -> None:
        self.start()

            # Start threads for existing producers
        producer_threads = [threading.Thread(target=producer.run) for producer in self.__producers]
        for thread in producer_threads:
            thread.start()

        # Start threads for existing consumers
        consumer_threads = [threading.Thread(target=consumer.consume) for consumer in self.__consumers]
        for i, thread in enumerate(consumer_threads):
            thread.start()
            print(f"Consumer {i+1} thread started")

        for consumer in self.__consumers:
            local_stats = consumer.ReportLocalStats()
            self.__global.update(*local_stats)


        for producer in producer_threads:
            producer.join()
            
        for thread in consumer_threads:  # Call join on thread, not Consumer
            thread.join()
                
        self.stop()
        print(f"Consumer {i+1} thread ended")
        self.GetStats()

    # starts the timer
    def start(self) -> None:
        self.__start_time = time.time()
      

    # ends the time and sets the elapsed time
    def stop(self) -> None:
        self.__end_time = time.time()
        self.__elapsed_time = self.__end_time - self.__start_time
       

    def PrintStats(self)-> None:
        
        self.CollectStatistics()
        
        # output the collected stats
        self.ReportGlobalStats()
   
    # this function returns the global stat tuples, and local stat tuples in one tuple
    # def GetStats(self):
    #     local_stats = self.CollectStatistics()
    #     global_stats = self.__global.GetGlobalStats()
    #     return global_stats, local_stats

    def GetStats(self):
        local_stats = self.CollectStatistics()
        
        # Update global stats
        storewide_total, month_total, aggregate_total = 0, 0, 0
        for consumer_stats in local_stats:
            storewide_total += consumer_stats[0]
            month_total += consumer_stats[1]
            aggregate_total += consumer_stats[2]
        
        global_stats = self.__global.update(storewide_total, month_total, aggregate_total)
        
        return global_stats, local_stats
    
    # This function collects statistics from all consumers
    def CollectStatistics(self)-> None:
        local_stats = []    
        counter = 1
        print("*" * 10)
        for consumer in self.__consumers:
            consumer : Consumer
            local_stats.append(consumer.ReportLocalStats())
            print(f"Consumer {counter} Local Stat: {local_stats[-1]}")  # Print the most recently added local stats
            counter += 1
        print("*" * 10)


        return local_stats

    # this function reports the global stats
    def ReportGlobalStats(self) -> tuple:
        storewide_total, month_total, aggregate_total = self.__global.update()
        return storewide_total, month_total, aggregate_total
