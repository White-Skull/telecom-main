from payload import Payload
from telecom import Downlink

# 1. Describe the payload
payload = Payload(
    swath_width_angle=5.72,   # deg
    pixel_size=0.07,         # arcmin
    bits_per_pixel=8,
    duty_cycle=0.025,         # fraction of the orbit the instrument is on
    downlink_time=1,        # hours per day available for downlink
)

# 2. Describe the link
link = Downlink(
    f_downlink=2.4,              # GHz
    sc_tx_power=60,              # W
    gs_tx_power=1000,             # W
    sc_antenna_diameter=0.75,     # m
    gs_antenna_diameter=18.3,     # m
    turn_around_ratio=221 / 240,
    orbit_altitude=50,          # km
    elongation_angle=0,          # deg (only used for interplanetary missions)
    pointing_offset_angle=0.02,   # deg
    required_uplink_dr=1e8,     # bps
    payload=payload,
    required_bit_error_rate=1e-6,
    elevation_angle=10,          # deg (default)
)

# 3. Compute the link margin
MU_EARTH = 3.986004418e14        # m^3/s^2
R_EARTH = 6371.0                 # km

MU_MOON = 4.9048695e12   # m^3/s^2
R_MOON = 1737.4          # km

margin, status = link.calculate_link_margin(
    mode="uplink",             # "downlink" or "uplink"
    type="Lunar Orbit",          # "Earth Orbit", "Lunar Orbit", or anything else for interplanetary
    d_S=149597870.7,             # km, spacecraft/planet to Sun distance (interplanetary only)
    mu=MU_MOON,
    body_radius=R_MOON,
    eb_n0_threshold_dB= 2.6
)



print(f"Link margin: {margin:.2f} dB")
print(status)