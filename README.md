
Multiples of A and B

Command to run: python Multiples.py <input_file> <output_file>

input.txt is provided.

Code is written to handle excess whitespace. Task description didn't specify how to handle duplicate lines in input file. Implementation ignores the duplicates and genarates single result line. 

Input file is read to a list of lists like [ [2,4,10] , [4,8,16] , ...] and if there are duplicate multiples they are removed. That might be the case if given intial numbers are factors of each other or they have a common factor.

After calculation results are then temporarely stored in dictionary like {'10': [2, 4, 6, 8], '16': [4, 8, 12]}

Dictionary is then sorted by length of results, formatted and printed on screen and written in the given output file.
