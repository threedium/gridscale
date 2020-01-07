#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import (unicode_literals, print_function)

import csv
import names
import json
import random
import requests
import urllib
from time import (time, strftime)

url = "http://localhost:8000"

def main():
    customers = requests.post(url + '/customers')
    customers = json.loads(customers.text)
    # print('We check customers', len(customers))

    products = requests.post(url + '/products')
    products = json.loads(products.text)
    # print('We gather all products', len(products))

    # print('Randomize quantity between 1-100')
    # csv_write = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for cust in customers:
        quantity = random.randint(1,100)
        cust = requests.post(url + '/customers/' + str(cust['customer_id']))
        # print(json.loads(cust.text))
        product = products[random.randint(0,len(products)-1)]
        prod = requests.post(url + '/products?name=' + product['name'])
        if prod.status_code != 404:
            cust = json.loads(cust.text)
            prod = json.loads(prod.text)
            # print(prod[0])
            # {"quantity": "2", "price_net": "27", "customer_class": "Reseller", "vat_percentage": "12"}
            param = {}
            param['quantity'] = str(quantity)
            param['price_net'] = int(float(prod[0]['price_net']))
            param['customer_class'] = cust['customer_class']
            param['vat_percentage'] = cust['vat_percentage']
            param = urllib.parse.urlencode(param)
            price = requests.post(url + '/prices', params=param)
            # print('We call price API', json.loads(price.text))
            # price = price.text
            # csv_write.writerow([n,c,y])

            # print('API Order Log')
            param = {}
            param['order_no'] = random.randint(506070809, 908070605)
            param['customer_id'] = cust['customer_id']
            param['product_id'] = prod[0]['product_id']
            param['quantity'] = quantity
            param['price_net'] = int(float(prod[0]['price_net']))
            param['price_gross'] = price.text
            # print(param)
            param = urllib.parse.urlencode(param)
            order = requests.post(url + '/orders/create', params=param)
            # print('Status', order.status_code)
            # print('We call price API', json.loads(order.text))
    delet = requests.post(url + '/orders')
    print('Current Orders', delet.text)


if __name__ == '__main__':

    customers = requests.post(url + '/customers')
    customers = json.loads(customers.text)
    # custinit = customers[0]['customer_id']  # first ID
    products = requests.post(url + '/products')
    products = json.loads(products.text)

    with open('orders.txt', mode='w') as csv_file:
        start = int(time())
        csv_write = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        print('Create Headers')
        headers = ["order_no", "customer_id", "product_name", "quantity"]
        csv_write.writerow(headers)
        for x in range(100000):
            # customer = requests.post(url + '/customers/' + str(custinit))
            customer = customers[random.randint(0,len(customers)-1)]
            product = products[random.randint(0,len(products)-1)]
            ordn = random.randint(506070809, 908070605)
            # cusn = random.randint(123456789, 987654321)
            qtty = random.randint(1,100)
            csv_write.writerow([ordn,customer['customer_id'],product['name'], qtty])
            # custinit += 1
        stop=int(time())
        dura=stop-start
        print('Time Taken',dura,'Seconds')

    with open('orders.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        i = 0
        for row in csv_reader:
            if i == 0:
                print(f'Column names are {", ".join(row)}')
            i += 1
        print(f'Processed {i} lines.')
    # main()