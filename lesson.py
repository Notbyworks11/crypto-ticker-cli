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

gbp_amount = 250
amount_in_usd = gbp_to_usd(gbp_amount)
print(f"{pretty_gbp(gbp_amount)} is {pretty_usd(amount_in_usd)}")
