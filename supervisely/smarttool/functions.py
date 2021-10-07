import numpy as np
import globals as g
import supervisely_lib as sly
from supervisely_lib.io.fs import silent_remove
from eiseg.inference.predictor import get_predictor
from eiseg.inference import clicker


def get_smart_bbox(crop):
    x1, y1 = crop[0]["x"], crop[0]["y"]
    x2, y2 = crop[1]["x"], crop[1]["y"]
    return x1, y1, x2, y2


def get_pos_neg_points_list_from_context(context):
    pos_points = context["positive"]
    neg_points = context["negative"]

    pos_points_list = []
    neg_points_list = []
    for coords in pos_points:
        pos_point = []
        for coord in coords:
            pos_point.append(coords[coord])
        pos_points_list.append(pos_point)

    for coords in neg_points:
        neg_point = []
        for coord in coords:
            neg_point.append(coords[coord])
        neg_points_list.append(neg_point)

    return pos_points_list, neg_points_list


def get_bitmap_from_points(pos_points, neg_points, image, crop_list):

    mask = np.zeros(image.shape[:2], dtype=np.uint8)

    my_predictor = get_predictor(g.model.model, **g.my_predictor_params)
    my_predictor.set_input_image(image)
    my_clicker = clicker.Clicker()
    for point in pos_points:
        click = clicker.Click(is_positive=True, coords=(point[1], point[0]))
        my_clicker.add_click(click)
    for point in neg_points:
        click = clicker.Click(is_positive=False, coords=(point[1], point[0]))
        my_clicker.add_click(click)
    pred = my_predictor.get_prediction(my_clicker)

    object_mask = pred > g.prob_thresh
    mask[object_mask] = 1

    x1, y1, x2, y2 = crop_list
    result_mask = np.zeros(image.shape[:2], dtype=np.uint8)
    result_mask[y1:y2, x1:x2] = mask[y1:y2, x1:x2]

    #import cv2
    #cv2.imwrite('test.png', result_mask*255)

    bool_mask = np.array(result_mask, dtype=bool)
    bitmap = sly.Bitmap(bool_mask)
    return bitmap


def unpack_bitmap(bitmap):
    bitmap_json = bitmap.to_json()["bitmap"]
    bitmap_origin = bitmap_json["origin"]
    bitmap_origin = {"y": bitmap_origin[1], "x": bitmap_origin[0]}

    bitmap_data = bitmap_json["data"]
    return bitmap_origin, bitmap_data


def get_image_by_hash(hash, save_path):
    if g.cache.get(hash) is None:
        g.api.image.download_paths_by_hashes([hash], [save_path])
        base_image = sly.image.read(save_path)
        g.cache.add(hash, base_image)
        silent_remove(save_path)
    else:
        base_image = g.cache.get(hash)
    if g.cache.count > g.cache_item_limit:
        g.cache.clear()
    return base_image