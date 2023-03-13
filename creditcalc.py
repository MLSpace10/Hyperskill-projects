import math
import argparse


def dif_pay(principal, interest, periods):
    i_ = interest/12/100
    month_ = 1
    count_ = 0
    while month_ <= periods:
        dif_ = principal/periods + i_*(principal - (principal*(month_ - 1)/periods))
        count_ += math.ceil(dif_)
        print(f'Month {month_}: payment is {math.ceil(dif_)}')
        month_ += 1
    over_pay = count_ - principal
    print(f'Overpayment = {math.ceil(over_pay)}')


def annuit_payment(principal, periods, interest):
    i_ = interest/12/100
    ann_ = principal * ((i_ * math.pow(1 + i_, periods)) / (math.pow(1 + i_, periods) - 1))
    over_pay = math.ceil(ann_) * periods - principal
    print(f'Your annuity payment = {math.ceil(ann_)}! \nOverpayment = {over_pay}')


def annu_principal(payment, periods, interest):
    i_ = interest/12/100
    princ_ = payment / ((i_ * math.pow(1+i_, periods))/(math.pow(1 + i_, periods) - 1))
    over_pay = math.fabs(math.floor(princ_) - payment * periods)
    print(f'Your loan principal = {math.floor(princ_)}! \nOverpayment = {math.ceil(over_pay)}')


def periods_pay(principal, payment, interest):
    i_ = interest/12.0/100.0
    months = math.ceil(math.log(payment / (payment - i_ * principal), 1 + i_))
    if months == 1:
        print('It will take 1 month to repay the loan!')
    elif months > 1:
        years_ = months // 12
        months1 = math.ceil(months % 12)
        if years_ == 1 and months1 == 1:
            print(f'It will take {years_} year and {months} month to repay the loan!')
        elif years_ == 0 and months1 == 1:
            print(f'It will {months1} month to repay the loan!')
        elif months1 == 0 and years_ == 1:
            print(f'It will take {years_} year to repay the loan!')
        elif years_ == 1:
            print(f'It will take {years_} year and {months1} months to repay the loan!')
        elif months1 == 1:
            print(f'It will take {years_} years and {months1} month to repay the loan!')
        elif years_ == 0:
            print(f'It will take {months1} months to repay the loan!')
        elif months1 == 0:
            print(f'It will take {years_} years to repay the loan!')
        else:
            print(f'It will take {years_} years and {months1} months to repay the loan!')
    over_pay = months * payment - principal
    print(f'Overpayment = {math.ceil( over_pay)}')


parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=float)
args = parser.parse_args()

if args.type is None:
    print('Incorrect parameters')
if args.type == 'diff':
    if args.payment is not None or args.periods is None or args.principal is None or args.interest is None:
        print('Incorrect parameters')
    else:
        if args.periods < 0 or args.principal < 0 or args.interest < 0:
            print('Incorrect parameters')
        dif_pay(args.principal, args.interest, args.periods)
if args.type == 'annuity':
    if args.periods is not None and args.principal is not None and args.interest is not None:
        if args.periods < 0 or args.principal < 0 or args.interest < 0:
            print('Incorrect parameters')
        else:
            annuit_payment(args.principal, args.periods, args.interest)
    else:
        print('Incorrect parameters')
    if args.payment is not None and args.principal is not None and args.interest is not None:
        if args.payment < 0 or args.principal < 0 or args.interest < 0:
            print('Incorrect parameters')
        else:
            periods_pay(args.principal, args.payment, args.interest)
    else:
        print('Incorrect parameters')
    if args.payment is not None and args.periods is not None and args.interest is not None:
        if args.payment < 0 or args.periods < 0 or args.interest < 0:
            print('Incorrect parameters')
        else:
            annu_principal(args.payment, args.periods, args.interest)
    else:
        print('Incorrect parameters')
