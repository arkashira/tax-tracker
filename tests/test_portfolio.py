from src.axentx_product.portfolio import Portfolio
from src.axentx_product.product import Product

def test_portfolio_creation():
    portfolio = Portfolio()
    assert portfolio.get_products() == []

def test_add_product_to_portfolio():
    portfolio = Portfolio()
    product = Product("Test Product", 10)
    portfolio.add_product(product)
    assert product in portfolio.get_products()

def test_add_duplicate_product_to_portfolio():
    portfolio = Portfolio()
    product = Product("Test Product", 10)
    portfolio.add_product(product)
    portfolio.add_product(product)
    assert len(portfolio.get_products()) == 1
