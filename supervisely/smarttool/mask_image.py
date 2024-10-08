import globals as g


def get_mask_from_clicks(image_np, clicks_list):
    g.CONTROLLER.setImage(image_np)
    for click in clicks_list:
        g.CONTROLLER.addClick(click.coords[1], click.coords[0], click.is_positive)
    res_mask, polygon = g.CONTROLLER.finishObject()
    return res_mask
