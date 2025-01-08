# pylint: disable=invalid-name
# pylint: enable=invalid-name
"""
Solution for task of Multiples of A and B.
"""
import argparse


class Multiples():

    """
    Class to calculate multiples smaller than given value.
    """

    def __init__(self):
        """
        Initialize object with command line arguments.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("input_file", help="Path to input file.")
        parser.add_argument("output_file", help="Path to output file.")
        self.args = parser.parse_args()

    def read_input_file(self):
        """
        Function to open and read file contents.
        
        Returns:
            list: Input values.
        """
        incoming_list_of_lists = []
        with open(self.args.input_file, "r", encoding="utf-8") as incoming:
            for line in incoming:
                if line != "\n":
                    incoming_list_of_lists.append(line.strip().split())
        return incoming_list_of_lists

    def multiply(self, incoming_values:list):
        """
        The multiplication as specified.
        
        Inputs:
            list: Values read from the input file.
        Returns:
            dict: Calculation results identified by the limiting third value.
        """
        outgoing_dict = {}
        for alist in incoming_values:
            multiplier = 1
            temp_list = []
            while True:
                result1 = int(alist[0]) * multiplier
                result2 = int(alist[1]) * multiplier
                if result1 < int(alist[2]):
                    temp_list.append(result1)
                if result2 < int(alist[2]):
                    temp_list.append(result2)
                multiplier += 1
                if result1 > int(alist[2]) and result2 > int(alist[2]):
                    break

            outgoing_dict.update({alist[2]:self.remove_duplicates_and_sort_results(temp_list)})

        return outgoing_dict

    def remove_duplicates_and_sort_results(self, results:list):
        """Making sure duplicate values are not in results
          and results are also sorted.

        Args:
            results (list): Unsorted results.
        Returns: 
            list: Sorted and single value results.
        """
        inorder = []
        for item in results:
            if item not in inorder:
                inorder.append(item)

        return sorted(inorder)

    def format_output(self, outgoing:dict):
        """
        Modify the string into a given format.

        Inputs:
            dict: Calculation results.
        Returns:
            str: Calculation result sorted and in printable form.
        """
        sorting_values = sorted(outgoing, key=lambda key: len(outgoing[key]))
        printable_file = ""
        for value in sorting_values:
            printable_line = f"{value}:"
            for item in outgoing[value]:
                printable_line += f"{item} "
            printable_file += printable_line + "\n"
        return printable_file

    def write_output_file(self, content:str):
        """
        Write results in outputfile.

        Inputs:
            str: Ready to print text.
        """
        with open(self.args.output_file,"w", encoding="utf-8") as outgoing:
            outgoing.write(content)

    def run(self):
        """
        Runner code to make the module work.
        """
        multiples_of_a_and_b = Multiples()
        file_content = multiples_of_a_and_b.read_input_file()
        results = multiples_of_a_and_b.multiply(file_content)
        ready_to_print = multiples_of_a_and_b.format_output(results)
        multiples_of_a_and_b.write_output_file(ready_to_print)
        print(ready_to_print)

if __name__ == "__main__":
    run_forest = Multiples()
    run_forest.run()
