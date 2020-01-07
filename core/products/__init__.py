#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import (unicode_literals, print_function)

import os
import random
import string
from flask import (Blueprint, request, jsonify, make_response)
prod = Blueprint('prod', __name__)
from core import db
from core.models import (Products)


def create_products():
    # create products from flat file
    response = False
    if os.path.isfile('prods.txt'):
        prods = Products.query.all()
        if len(prods) > 0:
            response = True
        else:
            init = 231415161
            with open('prods.txt') as f:
                content=f.readlines()
            content = [x.strip() for x in content]
            for k in content:
                prd = {}
                init += 1
                prd['product_id'] = init
                prd['price_net'] = float(random.randint(1,50))
                prd['name'] = k.replace(" ", "_")
                prd['status'] = 'Active'
                if len(k) > 0:
                    try:
                        add_prd = Products(
                            product_id=init,
                            name=k.replace(" ", "_"),
                            price_net=random.randint(1,50),
                            status="Active"
                            )
                        db.session.add(add_prd)
                        db.session.commit()
                    except Exception as e:
                        return False

    return response


@prod.route('/products', methods=['POST', 'GET'])
def products():
    data = request.args.to_dict()
    create_products()
    if len(data) > 0:
        # filter data (name or status)
        product = None
        if 'name' in data:
            product = Products.query.filter(Products.name == data['name']).first()
        elif 'status' in data:
            product = Products.query.filter(Products.status == data['status']).first()

        if product is None:
            return make_response(" ", 404)
        else:
            obj = {
                'product_id': product.product_id,
                'name': product.name,
                'price_net': "{0:.2f}".format(product.price_net),
                'status': product.status
            }
            response = jsonify(obj)
            response.status_code = 200
            return response
    else:
        # return Products Obj
        products = Products.query.all()
        if len(products) > 0:
            results = []
            for product in products:
                obj = {
                    'product_id': product.product_id,
                    'name': product.name,
                    'price_net': "{0:.2f}".format(product.price_net),
                    'status': product.status
                }
                results.append(obj)

            response = jsonify(results)
            response.status_code = 200
            return response
