def growingPlant(u, d, h):
    return max(1, (h + u - 2 * d - 1) // (u - d))
