# Star-Delta (Y-Δ) Transformation

def star_to_delta(ra, rb, rc):
    factor = (ra * rb) + (rb * rc) + (rc * ra)

    r1 = factor / rc
    r2 = factor / ra
    r3 = factor / rb

    return round(r1, 2), round(r2, 2), round(r3, 2)

print(star_to_delta(10, 20, 30))
