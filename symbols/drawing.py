def draw_rect(ctx, rect):
    ctx.rectangle(
        rect.location[0], rect.location[1],
        rect.size[0], rect.size[1])
