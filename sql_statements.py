__author__ = 'Charlie'

# Place to put named sql queries

CREATE_PRICES_TABLE = """
    CREATE TABLE route_prices (
        FromIATA text,
        ToIATA TEXT,
        DepartureDate DATE,
        ReturnDate DATE,
        Price MONEY)"""

INSERT_PRICES_TABLE = """
    INSERT INTO route_prices (
        FromIATA,
        ToIATA,
        DepartureDate,
        ReturnDate,
        Price
        )
    VALUES (
        :FromIATA,
        :ToIATA,
        :DepartureDate,
        :ReturnDate,
        :Price
        )"""

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

