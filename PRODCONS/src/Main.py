# main.py
from SharedBuffer import SharedBuffer
from ProducerClass import ProducerClass
from ConsumerClass import ConsumerClass
from GlobalStats import GlobalStats
import threading

def main():
    # Create the SharedBuffer instance
    shared_buffer = SharedBuffer(capacity=10)

    # Create the global statistics objects
    storewide_total = GlobalStats()
    month_total = GlobalStats()
    aggregate_total = GlobalStats()

    # Create the Producer instances and start them as threads
    producers = [threading.Thread(target=ProducerClass(shared_buffer).run) for _ in range(2)]  # Assuming 2 producers

    # Create the Consumer instances and start them as threads
    consumers = [threading.Thread(target=ConsumerClass(shared_buffer, storewide_total, month_total, aggregate_total).consume) for _ in range(2)]  # Assuming 2 consumers

    # Start the producers and consumers
    for producer in producers:
        producer.start()
    for consumer in consumers:
        consumer.start()

    # Wait for the producers and consumers to finish
    for producer in producers:
        producer.join()
    for consumer in consumers:
        consumer.join()

    # Print the final global statistics
    print("Global Statistics:")
    print(f"Storewide Total: {storewide_total.storewide_total}")
    print(f"Month-wise Total: {month_total.month_total}")
    print(f"Aggregate Total: {aggregate_total.aggregate_total}")

if __name__ == "__main__":
    main()