import csv


def main(args):
    with open('swisscrawl_confirmed_gsw_ids.txt') as fin:
        gsw_ids = set([line.strip('\n') for line in fin])
    with open(args.swisscrawl) as fin, open(args.output, 'w') as fout:
        reader = csv.reader(fin)
        writer = csv.writer(fout)
        header = next(reader)
        writer.writerow(['id'] + header + ['confirmation'])
        for i, row in enumerate(reader, start=1):
            if str(i) in gsw_ids:
                writer.writerow([i] + row + ['confirmed-GSW'])
            else:
                writer.writerow([i] + row + ['unconfirmed-GSW'])


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--swisscrawl', help='Path to swisscrawl-csv-file.')
    parser.add_argument('-o', '--output', help='Path to labelled swisscrawl file.')
    cmd_args = parser.parse_args()
    main(cmd_args)
