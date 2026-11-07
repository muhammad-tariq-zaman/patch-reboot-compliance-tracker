"""Hosts patched but not yet rebooted.

Usage: python3 main.py hosts.csv
CSV columns: host,patched (yes/no),rebooted (yes/no).
COMPLIANT only when patched and rebooted; PATCHED, NO REBOOT is
the action list; NOT PATCHED is listed separately.
"""
import argparse, csv, sys

def track(rows):
    out = []
    for row in rows:
        patched = row["patched"].strip().lower() == "yes"
        rebooted = row["rebooted"].strip().lower() == "yes"
        if patched and rebooted:
            verdict = "COMPLIANT"
        elif patched:
            verdict = "PATCHED, NO REBOOT"
        else:
            verdict = "NOT PATCHED"
        out.append((row["host"], verdict))
    order = {"PATCHED, NO REBOOT": 0, "NOT PATCHED": 1, "COMPLIANT": 2}
    return sorted(out, key=lambda r: order[r[1]])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        result = track(list(csv.DictReader(f)))
    for host, verdict in result:
        print(f"{host}: {verdict}")
    print(f"{sum(1 for _, v in result if v != 'COMPLIANT')} host(s) not compliant.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
