# West Point Scavenger Hunt

A kid-friendly (ages 5–14) walking scavenger hunt around West Point, from Eisenhower Hall to Trophy Point.

**Play it:** https://zacseidel.github.io/west-point-scavenger-hunt/

- **Short Route:** 8 stops, about 0.8 miles
- **Long Route:** 14 stops, about 1.7 miles, including the Cadet Chapel

Each stop has a rhyming clue, a QR code and links for Google Maps and Apple Maps walking directions, a kid activity, a challenge question, and fun facts. Phone-sized PDFs with clickable links are included for each route.

## Editing

All content lives in `hunt_data.py`. After editing, rebuild the page and PDFs:

```bash
python3 build.py https://zacseidel.github.io/west-point-scavenger-hunt/
```

Requires Python 3 with `reportlab`. Coordinates marked `CHECK` in `hunt_data.py` are estimates.
