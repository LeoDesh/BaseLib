from typing import Iterable,List,Any


class Table:
    def __init__(self,data_container:Iterable[List[Any]],header:List[str]):
        if not header:
            size = len(data_container[0])
            header = [f"Column{idx+1}" for idx in range(size)]
        self.header = header
        self.rows = data_container
        self.compare_header_with_row()
        self.shape = (len(self.rows),len(self.header))
        self.convert_rows_to_columns()
        
        #self.compute_column_types()
        #self.convert_column_types()
    def compare_header_with_row(self):
        if len(self.rows[0]) != len(self.header):
            raise ValueError(f"Header size {len(self.header)} does not match with elements in row ({len(self.rows[0])}")

    def convert_rows_to_columns(self):
        self.columns = [[row[i] for row in self.rows]  for i in range(self.shape[1])]

