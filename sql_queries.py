__author__ = 'Charlie'

# Place to put named sql queries

ALL_PRICES_QUERY = "SELECT * FROM route_prices"

FULLY_QUALIFIED_PRICE_QUERY = """
    SELECT
        FromIATA as FromIATA,
        ToIATA AS ToIATA,
        DepartureDate AS DepartureDate,
        ReturnDate AS ReturnDate,
        Price AS Price
    FROM
        route_prices
    WHERE
        FromIATA = :from_iata
        AND ToIATA = :to_iata
        AND DepartureDate = :departure_date
        AND ReturnDate = :return_date"""
