from payload import Payload
from telecom import Downlink

# 1. Describe the payload
payload = Payload(
    swath_width_angle=1.47,   # deg
    pixel_size=0.05,         # arcmin
    bits_per_pixel=8,
    duty_cycle=0.0204,         # fraction of the orbit the instrument is on
    downlink_time=18,        # hours per day available for downlink
)

# 2. Describe the link
link = Downlink(
    f_downlink=8.4,              # GHz
    sc_tx_power=200,              # W
    gs_tx_power=1000,             # W
    sc_antenna_diameter=1,     # m
    gs_antenna_diameter=35,     # m
    turn_around_ratio=749 / 880,
    orbit_altitude=500,          # km
    elongation_angle=10,          # deg (only used for interplanetary missions)
    pointing_offset_angle=0.05,   # deg
    required_uplink_dr=1e5,     # bps
    payload=payload,
    required_bit_error_rate=1e-6,
    elevation_angle=10,          # deg (default)
)

# 3. Compute the link margin
MU_EARTH = 3.986004418e14        # m^3/s^2
R_EARTH = 6371.0                 # km

margin, status = link.calculate_link_margin(
    mode="downlink",             # "downlink" or "uplink"
    type="Mercury",          # "Earth Orbit", "Lunar Orbit", or anything else for interplanetary
    d_S=0.308*149597870.7,             # km, spacecraft/planet to Sun distance (interplanetary only)
    mu=MU_EARTH,
    body_radius=R_EARTH,
    eb_n0_threshold_dB= 2.5
)



print(f"Link margin: {margin:.2f} dB")
print(status)