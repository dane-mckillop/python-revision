# Dividends are payments made by a corporation to its shareholders, usually in the form of cash or additional shares.
class DividendsPerShare:
    """
    Dividends Per Share (DPS) is a financial metric that indicates the amount of cash a company returns to its shareholders
    in the form of dividends for each share they own. It is calculated by dividing the total dividends paid by the number of
    outstanding shares.

    Formula: DPS = Total Dividends Paid / Number of Outstanding Shares
    """

    def __init__(self, total_dividends_paid: float, outstanding_shares: int):
        self.total_dividends_paid = total_dividends_paid
        self.outstanding_shares = outstanding_shares

    def calculate(self) -> float:
        if self.outstanding_shares == 0:
            raise ValueError("Number of outstanding shares cannot be zero.")
        if self.total_dividends_paid < 0:
            raise ValueError("Total dividends paid cannot be negative.")
        return self.total_dividends_paid / self.outstanding_shares