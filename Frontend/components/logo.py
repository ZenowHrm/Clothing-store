import reflex as rx

def Logo(fondo, isotipo) -> rx.Component:
    return rx.el.svg(
            rx.el.svg.rect(width="1000", height="1000", fill=fondo),
            rx.el.svg.path(
                d=(
                    "M 435 343 "
                    "L 245 343 "
                    "C 255 310, 275 270, 320 270 "
                    "L 710 270 "
                    "L 640 343 "
                    "L 510 343 "
                    "L 450 680 "
                    "L 400 580 "
                    "Z"
                ),
                fill=isotipo,
            ),
            rx.el.svg.path(
                d=(
                    "M 760 370 "
                    "L 695 370 "
                    "Q 680 370, 670 385 "
                    "L 465 680 "
                    "A 33 33 0 0 0 519 717 "
                    "L 760 370 "
                    "Z"
                ),
                fill=isotipo,
            ),
            xmlns="http://www.w3.org/2000/svg",
            view_box="0 0 1000 1000",
            width="100%",
            height="100%"
        )