# import module to write testcases for the code
import unittest
# import The OpenGL interface
import glm
# 6 x 3 matrix direction
DIRECTIONS = (glm.ivec3(1, 0, 0), 
            glm.ivec3(-1, 0, 0), 
            glm.ivec3(0, 1, 0), 
            glm.ivec3(0, -1, 0), 
            glm.ivec3(0, 0, 1), 
            glm.ivec3(0, 0, -1))
# direction vectors declarations
EAST = glm.ivec3(1, 0, 0)
WEST = glm.ivec3(-1, 0, 0)
UP = glm.ivec3(0, 1, 0)
DOWN = glm.ivec3(0, -1, 0)
SOUTH = glm.ivec3(0, 0, 1)
NORTH = glm.ivec3(0, 0, -1)
# Class Unittest
class MyCodeTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary test data or configurations

        # Initialize the DIRECTIONS matrix from OpenGL interface for testing
        self.DIRECTIONS = (glm.ivec3(1, 0, 0), 
            glm.ivec3(-1, 0, 0), 
            glm.ivec3(0, 1, 0), 
            glm.ivec3(0, -1, 0), 
            glm.ivec3(0, 0, 1), 
            glm.ivec3(0, 0, -1))
        # Initialize the individual directions variables from OpenGL interface for testing
        self.EAST = glm.ivec3(1, 0, 0)
        self.WEST = glm.ivec3(-1, 0, 0)
        self.UP = glm.ivec3(0, 1, 0)
        self.DOWN = glm.ivec3(0, -1, 0)
        self.SOUTH = glm.ivec3(0, 0, 1)
        self.NORTH = glm.ivec3(0, 0, -1)

    # test EAST variable 
    def test_EAST(self):
        self.assertIsInstance(self.EAST, glm.ivec3)
        self.assertEqual(len(self.EAST), 3)
        self.assertEqual([self.EAST.x, self.EAST.y, self.EAST.z], [1, 0, 0])
    # test WEST variable
    def test_WEST(self):
        self.assertIsInstance(self.WEST, glm.ivec3)
        self.assertEqual(len(self.WEST), 3)
        self.assertEqual([self.WEST.x, self.WEST.y, self.WEST.z], [-1, 0, 0])
    # test UP variable
    def test_UP(self):
        self.assertIsInstance(self.UP, glm.ivec3)
        self.assertEqual(len(self.UP), 3)
        self.assertEqual([self.UP.x, self.UP.y, self.UP.z], [0, 1, 0])
    # test DOWN variable
    def test_DOWN(self):
        self.assertIsInstance(self.DOWN, glm.ivec3)
        self.assertEqual(len(self.DOWN), 3)
        self.assertEqual([self.DOWN.x, self.DOWN.y, self.DOWN.z], [0, -1, 0])
    # test SOUTH variable
    def test_SOUTH(self):
        self.assertIsInstance(self.SOUTH, glm.ivec3)
        self.assertEqual(len(self.SOUTH), 3)
        self.assertEqual([self.SOUTH.x, self.SOUTH.y, self.SOUTH.z], [0, 0, 1])
    # test NORTH variable
    def test_NORTH(self):
        #self.assertIsInstance(self.NORTH, glm.ivec3)
        self.assertEqual(len(self.NORTH), 3)
        self.assertEqual([self.NORTH.x, self.NORTH.y, self.NORTH.z], [0, 0, -1])


    # test DIRECTIONS variable
    def test_DIRECTIONS(self):
        for coords in self.DIRECTIONS:
            self.assertEqual(len(coords), 3)
        self.assertEqual(self.DIRECTIONS[0], [1, 0, 0])
        self.assertEqual(self.DIRECTIONS[1], [-1, 0, 0])
        self.assertEqual(self.DIRECTIONS[2], [0, 1, 0])
        self.assertEqual(self.DIRECTIONS[3], [0, -1, 0])
        self.assertEqual(self.DIRECTIONS[4], [0, 0, 1])
        self.assertEqual(self.DIRECTIONS[5], [0, 0, -1])


        
if __name__ == '__main__':
    unittest.main()




