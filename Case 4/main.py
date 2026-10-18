from payload import Payload
from telecom import Downlink

# 1. Describe the payload
payload = Payload(
    swath_width_angle=0.229,   # deg
    pixel_size=0.05,         # arcmin
    bits_per_pixel=8,
    duty_cycle=0.024,         # fraction of the orbit the instrument is on
    downlink_time=12,        # hours per day available for downlink
)

# 2. Describe the link
link = Downlink(
    f_downlink=8.4,              # GHz
    sc_tx_power=100,              # W
    gs_tx_power=4000,             # W
    sc_antenna_diameter=3,     # m
    gs_antenna_diameter=35,     # m
    turn_around_ratio=749 / 880,
    orbit_altitude=300,          # km
    elongation_angle=150,          # deg (only used for interplanetary missions)
    pointing_offset_angle=0.05,   # deg
    required_uplink_dr=1e6,     # bps
    payload=payload,
    required_bit_error_rate=1e-6,
    elevation_angle=10,          # deg (default)
)

# 3. Compute the link margin
MU_EARTH = 3.986004418e14        # m^3/s^2
R_EARTH = 6371.0                 # km

MU_MARS = 4.28283744e13       # m^3/s^2
R_MARS = 3389.5                 # km

margin, status = link.calculate_link_margin(
    mode="uplink",             # "downlink" or "uplink"
    type="Mars",          # "Earth Orbit", "Lunar Orbit", or anything else for interplanetary
    d_S=1.524 * 149597870.7,             # km, spacecraft/planet to Sun distance (interplanetary only)
    mu=MU_MARS,
    body_radius=R_MARS,
    eb_n0_threshold_dB= 0.5
)



print(f"Link margin: {margin:.2f} dB")
print(status)