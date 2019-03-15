import quandl
quandl.ApiConfig.api_key = 'hKmkC9QzvdU8Y3sZ3182'

# get the table for daily stock prices and,
# filter the table for selected tickers, columns within a time range
# set paginate to True because Quandl limits tables API to 10,000 rows per call
company = str(input("Enter the name of the Company."))
fromm = input("Enter Date (From)[YYYY-MM-DD]")
to = input("Enter Date (TO)[YYYY-MM-DD]")
data = quandl.get_table('WIKI/PRICES', ticker = [company ], 
                        qopts = { 'columns': ['ticker', 'date', 'adj_close'] }, 
                        date = { 'gte': fromm, 'lte': to }, 
                        paginate=True)
new = data.set_index('date')

# use pandas pivot function to sort adj_close by tickers
clean_data = new.pivot(columns='ticker')

# check the head of the output
print(clean_data.head()) 