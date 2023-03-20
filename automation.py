from gps import Gps
from drive import Drive
from cmritPath import CmritField
from coordinates import Coordinates

class Automation:
    
    """
    This class will contain the code for automating the vehicle from one point to another
    Params: Start(Lat-Lng) and End(Lat-Lng)
    """
    def __init__(self, start_coordinates: Coordinates, end_coordinates: Coordinates):
        self.start_coordinates = start_coordinates
        self.end_coordinates = end_coordinates
        self.drive = Drive()

    
    def __check_if_destination_is_reached(self,current_coord, dest_coord):
        """
        Params: (current_corrd : Tuple, dest_coord: Tuple)
        Return : Boolean (True/False)
        Here we will check if the vehicle is in the range of the
        destination coordinate if yes then return true else return false.
        Using pythagorea's theorem to check whether the point is in range
        """
        range = 0.0005 # NOTE::Taken 5 (vague value for now) meters range, this is a value which will change during testing and calibration
        square_dist = (dest_coord[0] - current_coord[0]) ** 2 + (dest_coord[1] - current_coord[1]) ** 2
        return square_dist < range ** 2
    
    def __drive_vehicle(self,state):
        if state == 1:
            self.drive.forward()
        elif state == -1:
            self.drive.reverse()
        elif state == 0:
            self.drive.stop()



    def automate_linear(self):
        # Instatintiating the gps and drive classes here
        gps = Gps()
        path = CmritField().find_shortest_route(
            self.start_coordinates.point_name, 
            self.end_coordinates.point_name
            )

        # TODO:: Logic for moving the vehicle
        # Uncomment this while deploying on pi
        # current_coord = gps.get_gps_coordinates()
        state = 0 # stop now
        current_coord = gps.mock_gps_coordinates(state,self.start_coordinates.point_coordinate)
        while(not self.__check_if_destination_is_reached(current_coord, self.end_coordinates.point_coordinate)):
            # TODO:: Calling the functions to move the vehicle
            tmp_coord = current_coord
            if tmp_coord < self.end_coordinates.point_coordinate:
                state = 1
            elif tmp_coord == self.end_coordinates.point_coordinate:
                state = 0
            else:
                state = -1
            print(current_coord)
            current_coord = gps.mock_gps_coordinates(state,tmp_coord)
            self.__drive_vehicle(state)


