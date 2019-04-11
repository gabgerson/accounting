# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(customer1_name, "paid {:.2f}, expected {:.2f}".format(
#         customer1_paid, customer1_expected))

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(customer2_name, "paid {:.2f}, expected {:.2f}".format(
#         customer2_paid, customer2_expected))

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(customer3_name, "paid {:.2f}, expected {:.2f}".format(
#         customer3_paid, customer3_expected))

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(customer4_name, "paid {:.2f}, expected {:.2f}".format(
#         customer4_paid, customer4_expected))

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(customer5_name, "paid {:.2f}, expected {:.2f}".format(
#         customer5_paid, customer5_expected))

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(customer6_name, "paid {:.2f}, expected {:.2f}".format(
#         customer6_paid, customer6_expected))




# def sales_reports(log_file):  # defining fucntion that takes log_file as it's argument
#     for line in log_file:     # iterating over data in log file
#         line = line.rstrip()  #deletes trailing characters in each line
#         day = line[0:3]       #sets day eqaul to first 3 chars of line
#         if day == "Mon":     # if the first 3 characters of the line are == "tue" or whatever day print that line
#             print(line)


# sales_reports(log_file)

# customer_orders = open("customer-orders.txt")

# melon_cost2 = 1.00

# def under_paid(customer_orders): #defining funtionn that takes file object
#     """A function that lists unpaid and/or overpaid customers"""

#     for line in customer_orders:  #parsing each line
#         line = line.split("|")   #turning lines in to lists that split on |
#         quantity = line[2]
#         quantity = int(quantity)      # making the index of quantity less confusing
#         paid = line[3]
#         paid = float(paid)           # var for index of paid
#         name = line[1]          # var for index of name
#         expected = float(quantity) * melon_cost2  # finding expected cost 

#         if paid < expected:     #printing underpaid customers
#             print(f"UNDERPAID {name} , expected {expected}, paid {paid}")
#         elif paid > expected:  #printing overpaid customers
#             print(f"OVERPAID {name} ,expected {expected}, paid {paid}")



# under_paid(customer_orders)







customer_orders = open("customer-orders.txt")

melon_cost2 = 1.00



def under_paid(customer_orders): #defining funtionn that takes file object
    """A function that lists unpaid and/or overpaid customers"""
    underpaid_ls = []
    overpaid_ls = []

    for line in customer_orders:  #parsing each line
        line = line.split("|")   #turning lines in to lists that split on |
        quantity = line[2]
        quantity = int(quantity)      # making the index of quantity less confusing
        paid = line[3]
        paid = float(paid)           # var for index of paid
        name = line[1]          # var for index of name
        expected = float(quantity) * melon_cost2  # finding expected cost 

      
        

        if paid < expected:     #printing underpaid customers
            underpaid_ls.append(' '.join(["underpaid", name + ",", "Expected", str(expected) + ",", "Paid", str(paid)]))
            # print(f"UNDERPAID {name} , expected {expected}, paid {paid}")

        elif paid > expected:  #printing overpaid customers
            overpaid_ls.append(' '.join(["overpaid", name + ",", "Expected", str(expected) + ",", "Paid", str(paid)]))
            # print(f"OVERPAID {name} ,expected {expected}, paid {paid}")
    # underpaid_ls = str()  
    print("UNDERPAID LIST")

    for x in underpaid_ls:

        print(x)

    print("OVERPAID LIST")
    for x in overpaid_ls:

        print(x)

    # print(f"UNDERPAID LIST \n {underpaid_ls}")
    # print(f"OVERPAID LIST \n {overpaid_ls}")




under_paid(customer_orders)


