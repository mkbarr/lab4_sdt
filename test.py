import unittest
from main import Point
from main import Face


class TestPointFunc(unittest.TestCase):
  def setUp(self):
    self.point = Point(1, 1, 1)
  def test_rotate(self):
    point1 = self.point
    point1.rotate_x(1)
    self.assertAlmostEqual(point1.x, 1, 6)
    self.assertAlmostEqual(point1.y, -0.30116867, 6)
    self.assertAlmostEqual(point1.z, 1.38177321, 6)
  def test_length(self):
    point1 = self.point
    self.assertAlmostEqual(point1.length(), 1.73205080, 6)
    point1 = Point(2, 3, 4)
    self.assertAlmostEqual(point1.length(), 5.38516480, 6)
    point1 = Point(-1, 0, -5)
    self.assertAlmostEqual(point1.length(), 5.09901951, 6)
  def test_angle_cos(self):
    point1 = Point(3, 4, 5)
    self.assertAlmostEqual(point1.angle_cos(self.point), 0.97979589, 6)
    point1 = Point(-1, 10, -1)
    self.assertAlmostEqual(point1.angle_cos(self.point), 0.45732956, 6)
    point1 = Point(2, -2, 2)
    self.assertAlmostEqual(point1.angle_cos(self.point), 0.33333333, 6)

class TestFaceFunc(unittest.TestCase):
  def setUp(self):
    v1 = Point(1, 2, 3)
    v2 = Point(-2, 3, 4)
    v3 = Point(5, -1, 5)
    self.face = Face([v1, v2, v3])
  def test_rotate(self):
    face1 = self.face
    face1.rotate_x(1)
    ans = [1, -1.4438083426874098, 3.3038488872202123, -2, -1.7449770216271667, 4.685622177896248, 5, -4.747657229907622, 1.8600405445328023]
    for i in range(3):
      self.assertAlmostEqual(face1.ver[i].x, ans[3 * i], 8)
      self.assertAlmostEqual(face1.ver[i].y, ans[3 * i + 1], 8)
      self.assertAlmostEqual(face1.ver[i].z, ans[3 * i + 2], 8)
  def test_normal(self):
    face1 = self.face
    face1.rotate_y(10)
    normal = face1.normal()
    self.assertAlmostEqual(normal.x, -6.915463199829112, 8)
    self.assertAlmostEqual(normal.y, 10.0, 8)
    self.assertAlmostEqual(normal.z, -1.4752520909354132, 8)
  def test_is_visible(self):
    face1 = self.face
    face1.rotate_y(10)
    view_point = Point(10, 10, 10)
    self.assertTrue(face1.isVisible(view_point))
    face1.rotate_x(1)
    self.assertTrue(face1.isVisible(view_point))
    face1.rotate_z(2)
    self.assertFalse(face1.isVisible(view_point))

if __name__ == '__main__':
  unittest.main()