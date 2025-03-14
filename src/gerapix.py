import os

from pypix.pix import Pix


pix_key_by_pix_id = {
    "TERREO": "batman@lhc.net.br",
    "1ANDAR": "batman@lhc.net.br",
    "CAMISETA": "batman@lhc.net.br",
    "TOSCONF": "tosconf@lhc.net.br",
}

# fmt: off
values_by_pix_id = {
    'TERREO': [None, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 15.0, 20.0, ],
    '1ANDAR': [None, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 15.0, 20.0, ],
    'CAMISETA': [None, 59.99, 69.99, 79.99, ],
    'TOSCONF': [None, 5.0, 6.0, 7.5, 10.0, 15.0, 20.0, 59.99, 69.99, 79.99, ],
}
# fmt: on


def generate_pix(pix_id, value):
    pix = Pix()

    if value is not None:
        pix.set_description(f"{pix_id}-{value:.2f}")
        pix.set_amount(value)
    else:
        pix.set_description(f"{pix_id}-VALORABERTO")

    pix.set_name_receiver("LHC")
    pix.set_city_receiver("CAMPINAS")
    pix.set_key(pix_key_by_pix_id[pix_id])
    pix.set_identification(pix_id)

    return pix


def main():
    for pix_id in values_by_pix_id:
        os.makedirs(f"../QRCODES/{pix_id}", exist_ok=True)

    for pix_id, values in values_by_pix_id.items():
        for value in values:
            pix = generate_pix(pix_id, value)

            if value is None:
                value_part = "VALORABERTO"
            else:
                value_part = f"{value:.2f}"

            pix.save_qrcode(
                f"../QRCODES/{pix_id}/{pix_id}-{value_part}.png",
                color="black",
                box_size=10,
                border=1,
            )


if __name__ == "__main__":
    main()
