class Link():
    """Destinada a criação de tags de links"""
    
    __slots__ = ['__href', '__title']
    
    def __init__(self, href: str = '', title: str = ''):
        self.__href: str = href
        self.__title: str = title
    
    @property
    def href(self):
        return self.__href
    
    @property
    def title(self):
        return self.__title
    
    def render(self) -> str:
        if self.__title == '':
            return f'<a href="{self.href}" title="{self.href}">'
        return f'<a href="{self.href}" title="{self.title}">'
class HTMLBuild(object):
    
    def __getattribute__(self, name, **kwargs):
        return eval(name.title())().render()


html = HTMLBuild()
print(html.link)