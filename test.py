import unittest
from main import Point
from main import Face


class TestPointFunc(unittest.TestCase):
  def setUp(self):
    self.point_int = Point(1, 1, 1)
    self.point_float = Point(1.2, 3.4, 5.9)
  def test_rotate(self):
    point1 = self.point_int
    point1.rotate_x(1)
    self.assertAlmostEqual(point1.x, 1, 6)
    self.assertAlmostEqual(point1.y, -0.301168678, 6)
    self.assertAlmostEqual(point1.z, 1.38177321, 6)

    point2 = self.point_float
    point2.rotate_x(2.2)
    self.assertAlmostEqual(point2.x, 1.2, 6)
    self.assertAlmostEqual(point2.y, -6.77103258, 6)
    self.assertAlmostEqual(point2.z, -0.72326881, 6)
  def test_length(self):
    point1 = self.point_int
    self.assertAlmostEqual(point1.length(), 1.73205080, 6)
    point2 = self.point_float
    self.assertAlmostEqual(point2.length(), 6.91447756, 6)
  def test_angle_cos(self):
    point1 = Point(3, 4, 5)
    self.assertAlmostEqual(point1.angle_cos(self.point_int), 0.97979589, 6)
    point2 = Point(3.1, 4.5, 5.7)
    self.assertAlmostEqual(point2.angle_cos(self.point_float), 0.96431911, 6)

class TestFaceFunc(unittest.TestCase):
  def setUp(self):
    v1 = Point(1, 2, 3)
    v2 = Point(-2, 3, 4)
    v3 = Point(5, -1, 5)
    self.face_int = Face([v1, v2, v3])

    v4 = Point(1.1, 2.2, 3.3)
    v5 = Point(3.5, 7.8, 0.0)
    v6 = Point(0.0, 1.2, 4.4)
    self.face_float = Face([v4, v5, v6])

  def test_rotate(self):
    face1 = self.face_int
    face1.rotate_x(1)
    ans1 = [1, -1.4438083426874098, 3.3038488872202123, -2, -1.7449770216271667, 4.685622177896248, 5, -4.747657229907622, 1.8600405445328023]
    for i in range(3):
      self.assertAlmostEqual(face1.ver[i].x, ans1[3 * i], 6)
      self.assertAlmostEqual(face1.ver[i].y, ans1[3 * i + 1], 6)
      self.assertAlmostEqual(face1.ver[i].z, ans1[3 * i + 2], 6)

    face2 = self.face_float
    face2.rotate_x(3.5)
    ans2 = [1.1, -0.9026200606640069, -3.8620301689767915, 3.5, -7.304362160868211, -2.736109175979035, 0.0, 0.4196981770853718, -4.541349297307049]
    for i in range(3):
      self.assertAlmostEqual(face2.ver[i].x, ans2[3 * i], 6)
      self.assertAlmostEqual(face2.ver[i].y, ans2[3 * i + 1], 6)
      self.assertAlmostEqual(face2.ver[i].z, ans2[3 * i + 2], 6)

  def test_normal(self):
    face1 = self.face_int
    normal = face1.normal()
    self.assertAlmostEqual(normal.x, 5, 6)
    self.assertAlmostEqual(normal.y, 10, 6)
    self.assertAlmostEqual(normal.z, 5, 6)

    face2 = self.face_float
    normal2 = face2.normal()
    self.assertAlmostEqual(normal2.x, 2.86000000, 6)
    self.assertAlmostEqual(normal2.y, 0.98999999, 6)
    self.assertAlmostEqual(normal2.z, 3.76000000, 6)
    
  def test_is_visible(self):
    face1 = self.face_int
    face2 = self.face_float
    view_point = Point(10, 10, 10)

    self.assertTrue(face1.isVisible(view_point))
    self.assertTrue(face2.isVisible(view_point))

if __name__ == '__main__':
  unittest.main()