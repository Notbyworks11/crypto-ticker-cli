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
