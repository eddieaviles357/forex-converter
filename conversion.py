from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError, DecimalFloatMismatchError
from datetime import datetime

c_rates = CurrencyRates()
c_codes = CurrencyCodes()


def try_conversion_and_set_rate(from_cur, to_cur, amnt):
    """ Converts one currency to another based 
        on todays date and returns a dict 
    """
    try:
        # convert to float
        amount = float(amnt)
        # check if currency symbols exist
        symbol_from = c_codes.get_symbol(from_cur)
        symbol_to = c_codes.get_symbol(to_cur)
        # if both currency don't exist let user know
        if (symbol_from == None) and (symbol_to == None):
            return {
                "conversion": "error",
                "message": f"{from_cur} and {to_cur} not valid"
            }
        # get todays date
        today_dt = datetime.now()
        # round amount to a float 2 decimals places
        norm_conversion = round(
            c_rates.convert(from_cur, to_cur, amount, today_dt), 2)
        conv = f"{symbol_to}{norm_conversion}"

        # user entered valid inputs convert currency
        return {"conversion": conv, "message": "success"}

    except RatesNotAvailableError as rate_not_avlb:
        if to_cur in str(rate_not_avlb):
            return {"conversion": "error", "message": f"{to_cur} not valid"}
        else:  # "Currency Rates Source Not Ready"
            return {"conversion": "error", "message": f"{from_cur} not valid"}

    except ValueError:
        return {
            "conversion": "error",
            "message": f"{amnt} is not a valid number"
        }

    except DecimalFloatMismatchError:
        return {
            "conversion": "error",
            "message": "Mismatch number Please check input"
        }
    except Exception:
        return {"conversion": "error", "message": "Something went wrong"}
