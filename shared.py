def is_click_on_pause_button(click_pos, pause_button_rect):
    return pause_button_rect.collidepoint(click_pos)
