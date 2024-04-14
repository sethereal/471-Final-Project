# GlobalStats.py

class GlobalStats:
    def __init__(self):
        self.__storewide_total = 0 
        self.__month_total = 0
        self.__aggregate_total = 0
    

    # Update the statistics in a thread-safe manner
    def update(self, storewide_total, month_total, aggregate_total):
        self.__storewide_total += storewide_total
        self.__month_total += month_total
        self.__aggregate_total += aggregate_total
        return self.GetGlobalStats()
        
    
    def GetGlobalStats(self):
        return(self.__storewide_total, self.__month_total, self.__aggregate_total)
    
 