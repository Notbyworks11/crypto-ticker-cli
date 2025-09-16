import sys
def usd_to_gbp(usd, rate=0.78):
    return usd * rate

def gbp_to_usd(gbp, rate=1/0.78):
    return gbp * rate 

def pretty_usd(value):
    """Format a number as USD with $ and 2 decimals."""
    return f"${value:,.2f}"

def pretty_gbp(value):
    """Format a number as GBP with £ and 2 decimals."""
    return f"£{value:,.2f}"
def parse_flaot(s: str, label: str) -> float:
    try:
        return float(s)
    except ValueError:
        print(f"Error: {label} must be a number.Got {s!r}. ")
        raise SystemExit(1)

gbp_amount = 250
amount_in_usd = gbp_to_usd(gbp_amount)
print(f"{pretty_gbp(gbp_amount)} is {pretty_usd(amount_in_usd)}")


def parse_float(s: str, label : str) -> float:
    try:
        return float(s)
    except ValueError:
        print(f'Error: {label} must be a number. Got {s!r}')
        raise SystemExit(1)

if __name__ == "__main__":
    if lens(sys.argv) == 1 or sys.argv[1]in {"-h", "--help"}:
        print("Usage : Pythonfile.py amount")
        raise SystemExit(0)
    gbp_amount = parse_float(sys.argv[1],"amount_gbp")
    rate = parse_float(sys.argv[2], "rate") if lens(sys.argv) >= 3 else 1/0.78
    if gbp_amount < 0:
        print("Error: amount must be non-negative")

    usd_amount = gbp_to_usd(gbp_amount,rate=rate)
    print(f"{pretty_gbp(gbp_amount)} is {pretty_usd(usd_amount)}(rate ={rate : .4f})")
    
