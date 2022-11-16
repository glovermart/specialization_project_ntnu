## Convert.fq to csv file ######################################################################################################################

# import sys

# def help():
#     print('Usage: {} <input_file> [output_file]'.format(sys.argv[0]))


# def convert_to_csv(in_file, out_file):
#     out_file.write(u'"sequence_identifier","read_sequence","quality"\n')
#     for line in in_file:
#         if not line.startswith('@'):
#             continue
#         sequence_identifier = line.strip()
#         read_sequence = next(in_file).strip()
#         next(in_file)
#         quality = next(in_file).strip()
#         out_file.write(u'"{}","{}","{}"\n'.format(sequence_identifier, read_sequence, quality))


# def main():
#     if len(sys.argv) < 2:
#         help()
#         sys.exit(1)
#     else:
#         in_file = sys.argv[1]
#         if len(sys.argv) >= 3:
#             # If we have it, take name of output from parameters
#             out_file = sys.argv[2]
#         else:
#             # else make it from input file name
#             out_file = '.'.join(in_file.split('.')[:-1]) + '.csv'

#         with open(in_file) as infd:
#             with open(out_file, 'w') as outfd:
#                 convert_to_csv(infd, outfd)


# if __name__ == '__main__':
#     main()

## Convert.fq to csv file #############################################################################################################################



### remove lines not needed in .txt file  ################################################################################################################


# import os

# with open("single.txt", "r") as input:
#     with open("single_cleaned.txt", "w") as output:
#         # iterate all lines from file
#         for line in input:
#             # if line starts with substring 'time' then don't write it in temp file
#             if not line.strip("\n").startswith('[M::'):
#                 output.write(line)

# # replace file with original name
# os.replace('temp.txt', 'sample3.txt')


### remove lines not needed in .txt file  ##########################################################################################################################

## convert from .txt to csv  ###########################################################################################################################################

# importing pandas library
# import pandas as pd
  
# # reading given csv file 
# # and creating dataframe
# exec = pd.read_csv("single.txt"
#                        ,header = None)
  
# # adding column headings
# exec.columns = ['execution_time']
  
# # store dataframe into csv file
# exec.to_csv('execution_time.csv', 
#                 index = None)

## convert from .txt to csv  #################################################################################################################################################

#### merge two files with differenr headers and combiine into one .csv file ######################################################################################################################
# import pandas as pd
# csv1 = pd.read_csv('single.csv')
# #csv1.head()
# csv2 = pd.read_csv('execution_time.csv')
# #csv2.head()
# merged = pd.concat([csv1,csv2], axis =1)
# merged.head()
#  merged.to_csv('sequence_execution_time.csv', 
#                  index = None)
#### merge two files with differenr headers and combiine into one .csv file ######################################################################################################################


