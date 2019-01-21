def add_loan(name, amount, interest, minimum_payment):
    pass

def delete_loan():
    pass

def compound_interest(principal, rate, frequency, time):
    '''
    Returns the amount of interest accrued by the compound interest formula.

    :param principal: the principal investment amount (the initial deposit or loan amount)
    :type principal: float
    :param rate: the annual interest rate
    :type rate: float
    :param frequency: the number of times that interest is compounded per year
    :type frequency: int
    :param time: the number of years the money is invested or borrowed for
    :type time: int
    '''

    #TODO: Assert variable types

    #convert to decimal
    dec_rate = float(rate/100)
    
    return (principal*((1 + (dec_rate/frequency))**(frequency*time))) - principal

def simple_interest():
    pass

def calculate_remaining_payments():
    pass

def set_repayment_method():
    pass



