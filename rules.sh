#!/bin/sh
python3 CNASN.py
python3 USASN.py
git add CNASN.list
git add USASN.list
git commit -m "Update ASN"
git push -u origin main
