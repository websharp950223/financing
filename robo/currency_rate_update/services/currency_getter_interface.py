# -*- coding: utf-8 -*-
import logging

from datetime import datetime
from odoo import fields
from odoo.exceptions import except_orm

_logger = logging.getLogger(__name__)


class AbstractClassError(Exception):
    def __str__(self):
        return 'Abstract Class'

    def __repr__(self):
        return 'Abstract Class'


class AbstractMethodError(Exception):
    def __str__(self):
        return 'Abstract Method'

    def __repr__(self):
        return 'Abstract Method'


class UnknowClassError(Exception):
    def __str__(self):
        return 'Unknown Class'

    def __repr__(self):
        return 'Unknown Class'


class UnsuportedCurrencyError(Exception):
    def __init__(self, value):
        self.curr = value

    def __str__(self):
        return 'Unsupported currency %s' % self.curr

    def __repr__(self):
        return 'Unsupported currency %s' % self.curr


class Currency_getter_interface(object):
    "Abstract class of currency getter"

    log_info = " "

    supported_currency_array = [
        'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN',
        'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL',
        'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY',
        'COP', 'CRC', 'CUP', 'CVE', 'CYP', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD',
        'EEK', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP',
        'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG',
        'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD',
        'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD',
        'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD',
        'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MTL', 'MUR', 'MVR',
        'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD',
        'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON',
        'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP',
        'SLL', 'SOS', 'SPL', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS',
        'TMM', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX',
        'USD', 'UYU', 'UZS', 'VEB', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG',
        'XAU', 'XCD', 'XDR', 'XOF', 'XPD', 'XPF', 'XPT', 'YER', 'ZAR', 'ZMK',
        'ZWD'
    ]

    # Updated currency this arry will contain the final result
    updated_currency = {}

    def get_updated_currency(self, currency_array, main_currency,
                             max_delta_days):
        """Interface method that will retrieve the currency
           This function has to be reinplemented in child
        """
        raise AbstractMethodError

    def validate_cur(self, currency):
        """Validate if the currency to update is supported"""
        if currency not in self.supported_currency_array:
            raise UnsuportedCurrencyError(currency)

    def get_url(self, url):
        """Return a string of a get url query"""
        try:
            import urllib2
            opener = urllib2.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
            response = opener.open(url)
            rawfile = response.read()
            return rawfile
        except ImportError:
            raise except_orm(
                'Error !',
                'Unable to import urllib !'
            )
        except urllib2.HTTPError as e:
            raise except_orm(
                'Error !',
                '%s %s !' % (e.code, e.read())
            )
        except IOError:
            raise except_orm(
                'Error !',
                'Web Service does not exist !'
            )

    def check_rate_date(self, rate_date, max_delta_days):
        """Check date constrains. rate_date must be of datetime type"""
        days_delta = (datetime.today() - rate_date).days
        if days_delta > max_delta_days:
            raise Exception(
                'The rate timestamp %s is %d days away from today, '
                'which is over the limit (%d days). '
                'Rate not updated in OpenERP.' % (rate_date,
                                                  days_delta,
                                                  max_delta_days)
            )

        # We always have a warning when rate_date != today
        if rate_date.date() != datetime.today().date():
            rate_date_str = fields.Date.to_string(rate_date)
            msg = "The rate timestamp %s is not today's date %s" % \
                (rate_date_str, fields.Date.today())
            self.log_info = "\n WARNING : %s" % msg
            _logger.warning(msg)
