#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (unicode_literals, print_function)
from core import db


class Customers(db.Model):
    """This class represents the customers table."""
    __tablename__ = 'customers'

    customer_id = db.Column(db.BigInteger(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    customer_class = db.Column(db.Enum('Enduser', 'Reseller', 'ResellerHighVolume', name='Enduser'))
    vat_percentage = db.Column(db.Integer())
    status = db.Column(db.Enum('Active', 'Deleted', name='customer_status'))

    def __repr__(self):
        return "<Customers: {}>".format(
            self.customer_id,
            self.name,
            self.customer_class,
            self.vat_percentage,
            self.status
            )


class Products(db.Model):
    """This class represents the products table."""
    __tablename__ = 'products'

    product_id = db.Column(db.BigInteger(), primary_key=True)
    name = db.Column(db.String(255))
    price_net = db.Column(db.Float(10,2))
    status = db.Column(db.Enum('Active', 'Inactive', name='product_status'))

    def __repr__(self):
        return "<Products: {}>".format(
            self.product_id,
            self.name,
            self.price_net,
            self.status
            )


class Orders(db.Model):
    """This class represents the customers table."""
    __tablename__ = 'orders'

    order_id = db.Column(db.BigInteger(), primary_key=True)
    order_no = db.Column(db.Integer())
    customer_id = db.Column(db.Integer())
    product_id = db.Column(db.Integer())
    quantity = db.Column(db.Integer())
    price_net = db.Column(db.Float(10,2))
    price_gross = db.Column(db.Float(10,2))

    def __repr__(self):
        return "<Products: {}>".format(
            self.order_id,
            self.order_no,
            self.customer_id,
            self.product_id,
            self.quantity,
            self.price_net,
            self.price_gross
            )
