# Extract and read data using pandas
# We use the read_csv() function to import a CSV file with the health data



# print(health_data)

# Data Cleaning

# There are some blank fields
# Average pulse of 9 000 is not possible
# 9 000 will be treated as non-numeric, because of the space separator
# One observation of max pulse is denoted as "AF", which does not make sense

# So, we must clean the data in order to perform the analysis.

if __name__=="__main__":
    import pandas as pd

    health_data = pd.read_csv("health_data.csv", header=0, sep=",")

    health_data = pd.DataFrame(data=health_data)

    print(health_data.dropna(inplace=True))
    print(health_data.info())
    print(health_data.describe())