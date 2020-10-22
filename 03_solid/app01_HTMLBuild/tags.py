class Img():
    """Destinada a criação de tags de imagens"""
    
    __slots__ = ['__src', '__alt']
    
    def __init__(self, src: str, alt: str = ''):
        self.__src: str = src
        self.__alt: str = alt
    
    @property
    def src(self):
        return self.__src
    
    @property
    def alt(self):
        return self.__alt
    
    def render(self) -> str:
        if self.__alt == '':
            return f'<img src="{self.src}" alt="{self.src}">'
        return f'<img src="{self.src}" alt="{self.alt}">'
        


class Link():
    """Destinada a criação de tags de links"""
    
    __slots__ = ['__href', '__title']
    
    def __init__(self, href: str, title: str = ''):
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


link = Link('teste', 'oloko')
print(link.render())