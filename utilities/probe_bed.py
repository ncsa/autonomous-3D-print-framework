def probe_cell_region(lulzbot, bed_temp, x_start, y_start,
                      prnt_shape_x, prnt_shape_y):
    """
    Heat the bed to experiment temperature and probe the print footprint before printing.
    Returns True if the bed was heated as part of this step.
    """
    bed_heated = False
    if bed_temp is not None:
        lulzbot.move(f"M190 R{bed_temp}\n")
        lulzbot.move("M400\n")
        bed_heated = True
    # y_start is cell top-left (back); print extends toward front (-Y).
    lulzbot.setPosMode("absolute")
    lulzbot.move(
        f"G29 L{x_start} R{x_start + prnt_shape_x} "
        f"F{y_start - prnt_shape_y} B{y_start}\n"
    )
    lulzbot.move("M400\n")
    return bed_heated
