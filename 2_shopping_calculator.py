def calculate_total(price, tax_rate=0.20, discount=0, ):
    subtotal = price - discount
    tax = subtotal * tax_rate
    total = subtotal + tax 
    #(tip)
    total=total*1.12 
    return total

# Test cases
#print(f"£{calculate_total(100):.2f}")
#print(f"£{calculate_total(100, 0.1):.2f}")
#print(f"£{calculate_total(100, 0.08, 10):.2f}")


def Final_Grade (Homework,Test):
    total=Homework+Test
    HWpercent=(Homework/total)*100
    TPercent=(Test/total)*100
    return TPercent

print(Final_Grade(5,7))