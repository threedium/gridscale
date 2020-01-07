#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import (unicode_literals, print_function)

import csv
import names
import json
import random
import requests
import threading
import urllib
from time import (time, strftime)

url = "http://localhost:8000"

def main(csvfile):

    with open(csvfile) as csv_reader:
        i = 0
        csv_data = csv.reader(csv_reader, delimiter=',')
        for row in csv_data:
            if i > 0:
                cust = requests.post(url + '/customers/' + str(row[1]))
                cust = json.loads(cust.text)
                prod = requests.post(url + '/products?name=' + row[2])
                prod = json.loads(prod.text)
                param = {}
                param['quantity'] = str(row[3])
                param['price_net'] = int(float(prod['price_net']))
                param['customer_class'] = cust['customer_class']
                param['vat_percentage'] = cust['vat_percentage']
                param = urllib.parse.urlencode(param)
                price = requests.post(url + '/prices', params=param)
                param = {}
                param['order_no'] = row[0]
                param['customer_id'] = cust['customer_id']
                param['product_id'] = prod['product_id']
                param['quantity'] = str(row[3])
                param['price_net'] = int(float(prod['price_net']))
                param['price_gross'] = price.text
                param = urllib.parse.urlencode(param)
                order = requests.post(url + '/orders/create', params=param)
            i += 1


if __name__ == '__main__':

    customers = requests.post(url + '/customers')
    customers = json.loads(customers.text)
    products = requests.post(url + '/products')
    products = json.loads(products.text)

    with open('orders.txt', mode='w') as csv_file:
        start = int(time())
        csv_write = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        headers = ["order_no", "customer_id", "product_name", "quantity"]
        csv_write.writerow(headers)
        for x in range(100000):
            customer = customers[random.randint(0,len(customers)-1)]
            product = products[random.randint(0,len(products)-1)]
            ordn = random.randint(506070809, 908070605)
            qtty = random.randint(1,100)
            csv_write.writerow([ordn,customer['customer_id'],product['name'], qtty])
        stop=int(time())
        dura=stop-start
        print('Time Taken',dura,'Seconds')

    # main('orders.txt')
    