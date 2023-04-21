import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page, page_size):
        '''returns a tuple of size two containing a start index and an end
        index corresponding to the range of indexes to return in a list
        for those particular pagination parameters'''

        start_index = (page - 1) * page_size
        end_index = page * page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        ranges = self.index_range(page, page_size)
        results = []

        csv_file = open('Popular_Baby_Names.csv', 'r')
        line_count = 0
        line = csv_file.readline()
        while True:
            line = csv_file.readline()
            line_count += 1
            if (not (line) or line_count > ranges[1]):
                break
            if (line_count > ranges[0] and line_count <= ranges[1]):
                results.append(line.replace("\n", "").split(','))
        return results
