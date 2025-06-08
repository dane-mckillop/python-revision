# A stock split increases the number of shares outstanding
# while reducing the price per share, keeping the total market value of the company unchanged.
class StockSplits:
    """
    Stock Splits adjust the number of shares outstanding and the price per share,
    keeping the total market value of the company unchanged.
    
    Formula: New Shares = Old Shares * Split Ratio
             New Price = Old Price / Split Ratio
    """

    def __init__(self, old_shares: int, old_price: float, split_ratio: float):
        if old_shares < 0:
            raise ValueError("Original shares cannot be negative.")
        if split_ratio <= 0:
            raise ValueError("Split ratio cannot be negative.")
        self.old_shares = old_shares
        self.old_price = old_price
        self.split_ratio = split_ratio

    def calculate_new_shares(self) -> int:
        return int(self.old_shares * self.split_ratio)

    def calculate_new_price(self) -> float:
        return self.old_price / self.split_ratio