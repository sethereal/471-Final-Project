from .fifo import FIFO
from .lru import LRU
from .mru import MRU
from .optimal import Optimal

PAGE_SIZES = [512, 2048]
FRAME_NUMBERS = [4, 12]

def read_page_references(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]

def simulate_algorithm(algorithm_class, page_references, frames, page_size):
    if algorithm_class == Optimal:
        algorithm = algorithm_class(frames, page_references)
    else:
        algorithm = algorithm_class(frames)
    
    for current_index, page_number in enumerate(page_references):
        if algorithm_class is Optimal:
            algorithm.access_page(page_number, current_index)
        else:
            algorithm.access_page(page_number)

    page_faults = algorithm.get_page_faults()
    total_references = len(page_references)
    page_fault_percentage = (page_faults / total_references) * 100
    
    return page_fault_percentage

def main(data_file):
    page_references = read_page_references(data_file)
    with open('VMEMMAN/Report.md', 'w') as report:
        report.write("James Tieu\n")
        report.write("Spring 2024\n")
        report.write("CS471\n")
        for page_size in PAGE_SIZES:
            for frames in FRAME_NUMBERS:
                num_pages = len(set(page_reference // page_size for page_reference in page_references))

                simulation_header = (
                    f"\nSIMULATION: PAGE SIZE {page_size} WORDS AND {frames} FRAMES\n"
                    f"TOTAL # OF PAGES: {num_pages}\n"
                )
                print(simulation_header, end='')
                report.write(simulation_header)

                results = {}

                for algorithm_class, alg_name in [
                    (FIFO, 'FIFO'),
                    (LRU, 'LRU'),
                    (MRU, 'MRU'),
                    (Optimal, 'Optimal')
                ]:
                    fault_percentage = simulate_algorithm(algorithm_class, page_references, frames, page_size)
                    results[alg_name] = fault_percentage

                summary_header = "\nSUMMARY OF CURRENT RUN:\n"
                print(summary_header, end='')
                report.write(summary_header)

                for alg_name, fault_percentage in results.items():
                    summary_line = (
                        f"Page Size: {page_size}, Number of Pages: {num_pages}, "
                        f"Algorithm: {alg_name}, Page Fault Percentage: {fault_percentage:.2f}%\n"
                    )
                    print(summary_line, end='')
                    report.write(summary_line)

            
if __name__ == '__main__':
    data_file = 'VMEMMAN/data.txt'
    main(data_file)
