from unittest import TestCase
from app import app
from flask import session
from conversion import try_conversion_and_set_rate


class FlaskTests(TestCase):

    def setUp(self):
        """ set up testing """
        self.client = app.test_client()
        app.config.update({
            "TESTING": True,
        })
        # must use trailing slash or will get a 308 error code
        self.URL = "http://127.0.0.1:5000/"

    def test_home(self):
        """ Test home page route """
        with self.client:
            resp = self.client.get(self.URL)  # hit home page route
            self.assertEqual(resp.status_code, 200)  # success
            html = resp.get_data(as_text=True)
            self.assertIn("<h1>Converter</h1>", html)

    def test_currency(self):
        """ Test currency route """
        with self.client:
            resp = self.client.post(f"{self.URL}currency",
                                    data={
                                        "convert-from": "USD",
                                        "convert-to": "MXN",
                                        "amount": "1"
                                    })
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn("<title> Exchanged </title>", html)

            # test redirect if client inputs are invalid
            resp = self.client.post(f"{self.URL}currency",
                                    data={
                                        "convert-from": "TES",
                                        "convert-to": "TES",
                                        "amount": "1"
                                    })
            self.assertEqual(resp.status_code, 302)  # redirect status code
            self.assertEqual(resp.location, "/")  # redirect to home

    def test_conversion(self):
        """ Test for try_conversion_and_set_rate function that handles currency routh """
        data_test = try_conversion_and_set_rate("USD", "MXN", "1")
        self.assertIn("message", data_test)
        self.assertIn("conversion", data_test)
        self.assertEqual("success", data_test["message"])
        self.assertIn("$", data_test["conversion"])

        # test with 2 invalid currencies
        data_test = try_conversion_and_set_rate("TES", "CAT", "1")
        self.assertIn("TES and CAT not valid", data_test["message"])
        self.assertEqual("error", data_test["conversion"])

        # test with 1st argument invalid currency
        data_test = try_conversion_and_set_rate("TES", "MXN", "1")
        self.assertIn("TES not valid", data_test["message"])
        self.assertEqual("error", data_test["conversion"])

        # test with 2nd argument invalid
        data_test = try_conversion_and_set_rate("USD", "CAT", "1")
        self.assertIn("CAT not valid", data_test["message"])
        self.assertEqual("error", data_test["conversion"])

        # test with invalid amount
        data_test = try_conversion_and_set_rate("USD", "CAT", "testing amount")
        self.assertIn("testing amount is not a valid number",
                      data_test["message"])
        self.assertEqual("error", data_test["conversion"])