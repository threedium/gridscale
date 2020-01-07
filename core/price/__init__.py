#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import (unicode_literals, print_function)

from flask import (Blueprint, request, jsonify, make_response)
price = Blueprint('price', __name__)


@price.route('/prices', methods=['POST', 'GET'])
def price_api():
    data = request.args.to_dict()
    if len(data) > 0 and 'price_net' in data and 'customer_class' in data and 'vat_percentage' in data:
        quantity = 1
        vat_percentage = 1 + (int(data['vat_percentage'])/100)
        rebate = 0.0
        price_net = int(data['price_net'])
        if 'quantity' in data and int(data['quantity']) > 1:
            quantity = int(data['quantity'])

        if data['customer_class'] == 'Reseller':
            rebate = 0.05
            if quantity == 10:
                rebate = 0.06
            elif quantity >= 50:
                rebate = 0.07
            price_net = price_net * (1 - rebate)

        elif data['customer_class'] == 'ResellerHighVolume':
            rebate = 0.07
            if quantity >= 10 and quantity <= 49:
                rebate = 0.08
            elif quantity >= 50:
                rebate = 0.09
            price_net = price_net * (1 - rebate)

        price_gross = float(price_net) * quantity * (vat_percentage)
        return make_response(str("{0:.2f}".format(price_gross)), 201)
    else:
        return make_response(" ", 404)
