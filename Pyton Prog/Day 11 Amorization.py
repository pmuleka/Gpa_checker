""" Day 11 print Amortization schedule starter from day ^
    from: Day6 print pmt Schedule formatted print.py
    Prisca Muleka 04/22/2024
    - added print of down payment and amount financed,
    Day 11 midifications:
      - remove Hard code down payment (10% of purchase price)
      - replace with amount financed
      - input term in years (current loan 23 months)
      - input APR replacing 12% hard coded
      - replace payment from hard coded 5% of amount financed.
      - new fixed payment calculated with method pmt-Pmt (amtFin,apr,term)
      - put into try/except to catch input errors.
      - Add totals to fonal report post process
      Prisca Muleka
"""
def Pmt(amtFin,apr,years):
    term = years*12     #monthly compound assumed
    rate = apr/12/100
    payment = amtFin*(rate*(rate+1.0)**term)/((1+rate)**term -1)  # calculate pmt
    print("Calculated payment = ", payment)  # diagnostic print.
    return payment   # return unrounded amount
#  input parameters
try:
    amtFin=float(input("Enter amount financed:"))
    apr =  float(input("Enter APR of loan:    "))
    years =float(input("Enter term in years:  "))
    pmt = Pmt(amtFin,apr,years)  # call method to calculate fixed Payment
    BalRem = amtFin
    totInt = 0   #  initialize accumulators
    totPmt = 0
    print("Month  Starting  Balance Interest to Pay  Principal  to Pay", \
          "Payment Ending Balance")   # Print to  heading
    month = 1  # Initialize month for loan
    while BalRem >= 0.01:  # terminate when paid off
                       # Note comparison BalRem >= 0 causes infinite loop
        StartBal = BalRem
        Interest = StartBal * 0.12/12   # monthly interest hard code 12%
        Principal = pmt - Interest  # what remains will pay down
        BalRem = StartBal - Principal
    # final fixed payment will leave a negative result adjust to reduce payment
        if BalRem < 0:
            pmt = pmt + BalRem
            BalRem = 0.00
            Principal = StartBal
#     print formatted line  reference P75 of text
        print("%2d%14.2f%15.2f%17.2f%17.2f%17.2f" % \
            (month,StartBal,Interest,Principal,pmt,BalRem))
        month+=1
        totInt += Interest
        totPmt += pmt
    print(f"Total Payments = {totPmt:12.2f}")
    print(f"Total Interest = {totInt:12.2f}")
except ValueError:
    print("Input values must be floating point numeric.")
print("**End Program**")


            


    
