import csv

with open('parcels.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

lengths = [int(r['length']) for r in rows]
widths = [int(r['width']) for r in rows]
heights = [int(r['height']) for r in rows]

volumes = [ll * ww * hh for ll, ww, hh in list(zip(lengths, widths, heights))]

print(volumes)
