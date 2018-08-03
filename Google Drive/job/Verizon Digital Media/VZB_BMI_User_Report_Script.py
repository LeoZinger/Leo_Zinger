import os

import csv

import datetime

# Read the BMI user file name (exported from BMI) from command line.

filename = input('Enter the exported bmi_user input file name: ')

in_BMI_User_Report_users_f = open(filename)
in_BMI_User_Report_users_f
# in_BMI_User_Report_users_f = open('BMI User Export Jan 2016.xlsx.csv')

##in_BMI_User_Report_users_f = open('bm_user_RCM_Feb-2016.csv')

in_user_report_f = csv.reader(in_BMI_User_Report_users_f)

##rownum = 0


# Output file - BMI RCM File Conversion Requirement

##csv_out_f = open('BMI User RCM File.out.txt', 'w')

output_file_name_formatted = 'BMI_RCM_VZIDG_UserList_File_' + datetime.datetime.now().strftime(
    "%Y%m%d%H%M%S") + '.out.csv'

csv_out_f = open(output_file_name_formatted, 'w')

print("output_file_name_formatted: ", output_file_name_formatted)

# exit()


# First 3 lines of RCM file format requirement

# Record 1 - the date the file is created in the format of mmddyyyy

# Record 2 – Server Name | Source

# i.           Server Name is the server name of where the code is located.  Can be hard coded

# ii.          “Source” is hard coded

# Record 3 - Column headers for the data.  (hard coded)

# Login ID|Correlation ID|Status|First Name|Middle Name|Last Name|Resource-Role|Access


# Record 1 - the date the file is created in the format of mmddyyyy

# print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

first_line_Filedate = datetime.datetime.now().strftime("%m%d%Y") + "\n"

print(first_line_Filedate)

# print ("\n")


# Record 2 – Server Name | Source (“Source” is hard coded)

# second_line_serverNameSource = "terremark.bigmachines.com" + "|" + " SDP TFS Code Access" + "\n"

second_line_serverNameSource = "terremark.bigmachines.com" + "\n"

print(second_line_serverNameSource)

# print ("\n")


# Record 3 - Column headers for the data.  (hard coded)

# Login ID|Correlation ID|Status|First Name|Middle Name|Last Name|Resource-Role|Access

third_line_Columnheaders = "Login ID|Correlation ID|Status|First Name|Middle Name|Last Name|Resource-Role|Access" + "\n"

print(third_line_Columnheaders)

# print ("\n")


csv_out_f.write(first_line_Filedate)

csv_out_f.write(second_line_serverNameSource)

csv_out_f.write(third_line_Columnheaders)

for row in in_user_report_f:

    # print (row[5] + "\n")

    # Skip the column header line that is embedded in the BMI user export csv file bc the RCM column header has to be hardcoded in.

    # if (row[5] != "first_name") and (row[8] != "email") :

    # Skip empty lines:

    # if not row:

    # continue

    # Skip the column header line that is embedded in the BMI user export csv file bc the RCM column header has to be hardcoded in.

    # if (row[5] != "first_name") and (row[8] != "email") :

    if len(row) >= 2:

        if (row[2] != "") and (row[2] != "login"):

            # print (row[0] + row[2] + row[5] + "\n")

            # print (row)

            # print ("\n")

            # login (C 2), email (I 8), status (AU 46), first_name (F 5), last_name (G 6), group_list(BB 53), type (E 4)

            output_str = row[2] + "|" + row[8] + "|" + row[46] + "|" + row[5] + "|" + row[6] + "|" + row[53] + "|" + \
                         row[4] + "\n"

            print(output_str)

            # print ((row[0].split("(")).strip(")"))

            # print ()

            # We only extract the Active BMI users to put in RCM report, filtering out the inactive ones.

            if (row[46] == "Active"):
                # write to output file

                csv_out_f.write(output_str)

            # For Testing only - only process first 2 lines/rows of the input file, skip the rest for sake of quicker test.

            # Comment out for Production

            # rownum = rownum + 1

            # if rownum >= 5 :

            # break

in_BMI_User_Report_users_f.close()

csv_out_f.close()
