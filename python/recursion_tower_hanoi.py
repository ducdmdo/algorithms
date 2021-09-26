def moveTower(height, startPole, destinationPole, middlePole):
    if height >=1:
        moveTower(height-1, startPole, middlePole,destinationPole)
        moveDisk(startPole, destinationPole)
        moveTower(height-1,middlePole,destinationPole,startPole)

def moveDisk(fromPole,toPole):
    print("moving disk from",fromPole,"to",toPole)

moveTower(3,"A","B","C")