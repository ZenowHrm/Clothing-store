import reflex as rx

class CarouselState(rx.State):
    current_index: int = 0
    
    images: list[str] = [
        "/gallery/1.png",
        "/gallery/2.png",
        "/gallery/3.png",
        "/gallery/4.png",
        "/gallery/5.png",
    ]

    def next_slide(self):
        self.current_index = (self.current_index + 1) % len(self.images)

    def prev_slide(self):
        self.current_index = (self.current_index - 1) % len(self.images)

    def set_slide(self, index: int):
        self.current_index = index