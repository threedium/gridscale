#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import (unicode_literals, print_function)

import random
import names
from time import time
from flask import (Blueprint, request, jsonify, make_response)
cust = Blueprint('cust', __name__)
from core.models import (Customers)
from core import db


@cust.before_app_first_request
def before_request():
    # create dummy customers
    cust_class=['Enduser', 'Reseller', 'ResellerHighVolume']
    vats_data=[10, 12, 16]
    customers = Customers.query.all()
    if not len(customers):
        start=int(time())
        init = 0
        while True:
            for x in range(1000):
                init += 1
                try:
                    if not init:
                        customer = Customers(
                            customer_id=101010101,
                            name=names.get_full_name(),
                            customer_class=random.choice(cust_class),
                            vat_percentage=random.choice(vats_data),
                            status="Active"
                            )
                    else:
                        customer = Customers(
                            # customer_id="NULL",
                            name=names.get_full_name(),
                            customer_class=random.choice(cust_class),
                            vat_percentage=random.choice(vats_data),
                            status="Active"
                            )
                    db.session.add(customer)
                    db.session.commit()
                except Exception as e:
                    break
            break
    return
    

@cust.route('/customers/delete', methods=['POST', 'GET'])
def delete_cust():
    customers = Customers.query.all()
    if len(customers) > 0:
        Customers.query.delete()
        db.session.commit()
    return jsonify({"data": True})


@cust.route('/customers', methods=['POST', 'GET'])
def customers():
    customers = Customers.query.all()
    if len(customers) > 0:
        custs = []
        for customer in customers:
            obj = {}
            obj['customer_id'] = customer.customer_id
            obj['customer_class'] = customer.customer_class
            custs.append(obj)
        response = jsonify(custs)
        response.status_code = 200
        return response
    return make_response(" ", 404)


@cust.route('/customers/<int:customerId>', methods=['POST', 'GET'])
def customerid(customerId):
    # Get Customer based on ID
    customer = Customers.query.filter(Customers.customer_id == customerId).first()

    if customer is None:
        return make_response("", 404)
    else:
        obj = {
            'customer_id': customer.customer_id,
            'name': customer.name,
            'customer_class': customer.customer_class,
            'vat_percentage': customer.vat_percentage,
            'status': customer.status
        }
        response = jsonify(obj)
        response.status_code = 200
        return response