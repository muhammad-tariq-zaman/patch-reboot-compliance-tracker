# patch-reboot-compliance-tracker

Track patch compliance honestly: compliant only when patched AND rebooted, with patched-but-not-rebooted hosts listed first as the action list.

## How to run

```sh
python3 main.py hosts.csv
```

## Example output

```
PC-04: PATCHED, NO REBOOT
PC-11: COMPLIANT
1 host(s) not compliant.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
