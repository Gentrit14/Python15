from itertools import product
from operator import index

import numpy as np
import pandas as pd

import pandas as pd

# arr_2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(arr_2d)
#
# element = arr_2d[1,2]
# print(element)
#
# dimension = arr_2d.mint
# print(dimension)
#
# size = arr_2d.size
# print(size)


products = ["apples" , "oranges" , "watermelons" , "peaches"]

sales = [150, 200 , 350 , 90]

sales_series = pd.Series(sales , index=products)

total_sales = sales_series.sum()

best_selling_product = sales_series.idsmax()

print(f"Best selling products:", {best_selling_product})



