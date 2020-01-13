#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import (unicode_literals, print_function)

import time
from flask import (Blueprint, request, jsonify, make_response)
ordered = Blueprint('ordered', __name__)
from core import db
from core.models import (Orders)


@ordered.route('/orders/delete', methods=['POST', 'GET'])
def delete_orders():
    k = Orders.query.all()
    if len(k) > 0:
        Orders.query.delete()
        db.session.commit()
    return make_response(str(len(k)),200)


@ordered.route('/orders/create', methods=['POST', 'GET'])
def create_orders():
    status_code = 200
    data = request.args.to_dict()
    # k = Orders.query.all()
    # i = 2345678 + len(k)
    # print('Order', i)
    try:
        creord = Orders(
            # order_id=i,
            order_no=data['order_no'],
            customer_id=data['customer_id'],
            product_id=data['product_id'],
            quantity=data['quantity'],
            price_net=data['price_net'],
            price_gross=data['price_gross']
            )
        db.session.add(creord)
        db.session.commit()
    except Exception as e:
        status_code = 404

    return make_response(" ", status_code)


@ordered.route('/orders', methods=['POST', 'GET'])
def orders():
    orders = Orders.query.all()
    results = []

    if len(orders) > 0:
        for order in orders:
            obj = {
                "order_id": order.order_id,
                "order_no": order.order_no,
                "customer_id": order.customer_id,
                "product_id": order.product_id,
                "quantity": order.quantity,
                "price_net": str("{0:.2f}".format(order.price_net)),
                "price_gross": str("{0:.2f}".format(order.price_gross))
            }
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response
    else:
        return make_response(" ", 404)