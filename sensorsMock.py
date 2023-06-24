def CheckForCollision():
    #Here we read from sensor if there is an obstacle
    #The finction below should return the distace to the closest detected object
    #distance=ReadRadarSensor()
    distance=30
    Threshold=20 #[cm]
    if distance<Threshold:
        collision=True
    else:
        collision=False
    return collision