import test_module.test_coordinates as tc

# Instructions
# Start from basic_science -> ganesha_statue ------> basic_science


class TestTree:
    def __init__(self, gt, start_node, end_node):
        self.G = gt
        self.start_node = start_node
        self.end_node = end_node

        if (self.start_node == 'basic_science' and self.end_node == 'ganesha_statue') or (self.start_node == 'ganesha_statue' and self.end_node == 'basic_science'):
            self.G.add_tree(tc.tree1.point_coordinate, start_node, end_node)
            self.G.add_tree(tc.tree2.point_coordinate, start_node, end_node)
            self.G.add_tree(tc.tree3.point_coordinate, start_node, end_node)
            self.G.save_and_return()

        elif (self.start_node == 'ganesha_statue' and self.end_node == 'hostel_turn') or (self.start_node == 'hostel_turn' and self.end_node == 'ganesha_statue'):
            self.G.add_tree(tc.tree4.point_coordinate, start_node, end_node)
            self.G.add_tree(tc.tree5.point_coordinate, start_node, end_node)
            self.G.add_tree(tc.tree6.point_coordinate, start_node, end_node)
            self.G.save_and_return()

        elif (self.start_node == 'hostel_turn' and self.end_node == 'volley_ball_court') or (self.start_node == 'volley_ball_court' and self.end_node == 'hostel_turn'):
            self.G.add_tree(tc.tree7.point_coordinate, start_node, end_node)
            self.G.add_tree(tc.tree8.point_coordinate, start_node, end_node)
            self.G.add_tree(tc.tree9.point_coordinate, start_node, end_node)
            self.G.save_and_return()

        elif (self.start_node == 'volley_ball_court' and self.end_node == 'teacher_parking') or (self.start_node == 'teacher_parking' and self.end_node == 'volley_ball_court'):
            self.G.add_tree(tc.tree10.point_coordinate, start_node, end_node)
            self.G.add_tree(tc.tree11.point_coordinate, start_node, end_node)
            self.G.save_and_return()

        elif (self.start_node == 'teacher_parking' and self.end_node == 'basic_science') or (self.start_node == 'basic_science' and self.end_node == 'teacher_parking'):
            self.G.add_tree(tc.tree12.point_coordinate, start_node, end_node)
            self.G.add_tree(tc.tree13.point_coordinate, start_node, end_node)
            self.G.save_and_return()

        else:
            pass
