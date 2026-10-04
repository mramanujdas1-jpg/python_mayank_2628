# Basic file handling

# it creates a file and writes to it, then reads from it and prints the content.
# python provides the open() function to open a file, and the write() and read() methods to write to and read from the file.
# # open(filename, mode) - opens a file in the specified mode. The mode can be 'r' for reading, 'w' for writing, 'a' for appending, and 'x' for creating a new file.
# r-mode meaning - read mode, it is used to read the content of the file. It is the default mode. If the file does not exist, it will raise an error.
# w-mode meaning - write mode, it is used to write to the file. If the file does not exist, it will be created. If the file exists, its content will be overwritten.
# a-mode meaning - append mode, it is used to append content to the file. If the file does not exist, it will be created.
# x-mode meaning - exclusive creation mode, it is used to create a new file. If the file already exists, it will raise an error.
# r+-mode meaning - read and write mode, it is used to read from and write to the file. If the file does not exist, it will raise an error.

#example:
# open a file in read mode
# file=open("example.txt", "r")
# content=file.read()
# print(content)
# file.close() 
#file.close() is used to close the file after we are done with it. It is a good practice to close the file after we are done with it to free up system resources.

#write mode
#example:
# open a file in write mode
# file=open("example.txt", "w")
# file.write("Hello, this is an example of file handling in Python.")
# file.close()   
# print("File written successfully.")

#CSV FILE (comma separated values) - 
#it is a file format that is used to store tabular data in plain text. Each line of the file represents a row of the table, and each value in the row is separated by a comma. Python provides the csv module to read from and write to CSV files.
#it have two types of mode same as text file 
#reader and writer (csv.reader and csv.writer)ethods are used to read from and write to CSV files. The reader method returns an iterator that can be used to iterate over the rows of the CSV file, and the writer method returns a writer object that can be used to write rows to the CSV file. 
#when we write csv file we have to use import csv module and use the writer method to write to the file. The writerow() method is used to write a single row to the CSV file, and the writerows() method is used to write multiple rows to the CSV file.

#example:
# import csv
# # open a CSV file in read mode
# file=open("filehandling.csv", "r", newline="")
# reader=csv.reader(file)
# for row in reader:
#     print(row)

# file.close()


#example:
# import csv
# file= open(r"D:\python\xyz.csv", "r")
# reader=csv.reader(file)
# for row in reader:
#     print(row)

# import csv
# file = open(r"D:\python\write.csv", "w")
# writer = csv.writer(file)
# writer.writerow(["Name", "Age", "Gender"])

# print("CSV file written successfully.")


# file.close()
# file=(r"D:\python\file.txt","r")
# f=open(r"D:\python\file.txt","w")
# f.write("hello world")
# f.close()
# print("file written successfully")