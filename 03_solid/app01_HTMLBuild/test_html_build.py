import unittest

from html_build import HTMLBuild

class HTMLBuildTest(unittest.TestCase):
    """Tests para 'HTMLBuild'"""
    
    def test_image_render(self) -> str:
        html = HTMLBuild()
        img = html.img('images/photo.jpg')
        
        self.assertEquals('<img src="images/photo.jpg">', img)


unittest.main()