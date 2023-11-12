#include <SFML/Graphics.hpp>
#include <time.h>

using namespace sf;

int main(int argc, char *argv[])
{
	RenderWindow window(VideoMode(750, 1250), "the chess");
	
	Texture t1;
	
	t1.loadFromFile("images/board.png");
	
	Sprite s(t1);
	
	while (window.isOpen())
	{
	    Event e;
	    
	    while (window.pollEvent(e))
	    {
	        if (e.type == Event::Closed)
	            window.close();
	    }
	    
	window.clear();
	
	window.draw(s);
	
	window.display();
	}
}