def count_unique_coordinates(coordinates):
    unique = []
    for coord in coordinates:
        if coord in coordinates and coord not in unique:
            unique.append(coord)
    return len(unique)