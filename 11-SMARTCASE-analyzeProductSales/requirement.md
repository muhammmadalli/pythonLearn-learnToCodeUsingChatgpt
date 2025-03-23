## YOU ARE 
A warehouse manager AT Mckenzie Megamart. 
### WHAT YOU DO
Keeps shelves stocked across all stores. Analysis a ton of data, 
#### Technical Task
i.e. weekly, each store sends you a spreadsheet with sales of all products; and you have to find if any product fluctuated from more than 10% of the average sales across all stores.   

## HOW TO DO IT
### 1\. 1ST PART
Read data from spreadsheets. 

> I have a directory named Sales with multiple excel files. Each file has two columns, the first is the name of product and has the header **Product** and the second is the number of that product sold and has the header **Sold**.

Now we want to incorporate units testing as we build the app. 

> Write a function that reads in that data for further analysis. 

We also want to add a constraint. 

> The data from each file needs to be separate. 

It is the complete prompt.

I have a directory named sales with multiple Excel files. Each file has two columns. The first is the name of a product and has the header Product, and the second is the number of that product sold and has the header Sold. Write a function that reads in that data for further analysis. The data from each file needs to be separate.

### 2\. Now we also want to test the function. 
> Design test cases and a program to unit test the read_sales_data function.

### 3\.
> Write a function that compares the number of products sold for products that appear in multiple files. Using the data returned by read_sales_data, it should:
> 1. Find the average sales for that product across the files it's in.
> 2. Find any files where the sales are more than 10% different than the average.
> 3. Return the product, the average, and the files where the sales vary by 10%.

### 4\. Provided the Spreadsheets to the Program
> I've put read_sales_data and compare_product_sales in a file named analyze_data.py. Write a program that uses the functions to highlight in yellow any product in one of the Excel files with sales differing by 10%.

