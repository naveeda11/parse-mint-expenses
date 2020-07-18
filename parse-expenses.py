import os
import argparse
import csv
''' Parse transactions from mint.com export. Exclude descriptions or categories
'''
ap = argparse.ArgumentParser()
ap.add_argument("fname")
args = ap.parse_args()

description_exclusions = ["YOU SOLD",
                          "YOU BOUGHT",
                          "INTEREST EARNED",
                          "CARDMEMBER SERV"]

category_exclusions = ["Investments",
                       "Trade Commissions", ]

dirname, fname = os.path.split(args.fname)
with open(args.fname) as f:
    with open('edited_' + fname, 'w', newline='') as fo:
        expenses_csv = csv.DictReader(f)
        for i, r in enumerate(expenses_csv):
            if i == 0:
                fieldnames = list(r.keys())
                writer = csv.DictWriter(fo, fieldnames=fieldnames)
            if r['Description'] and \
                not any(e in r['Category'] for e in category_exclusions) and \
                    not any(e in r['Description'] for e in description_exclusions):
                writer.writerow(r)
