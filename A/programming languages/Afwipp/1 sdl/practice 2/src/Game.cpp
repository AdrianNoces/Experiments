#include "Game.hpp"
#include <iostream>
#include "SDL2/SDL.h"

Game::Game()
{}
Game::~Game()
{}

void Game::init(const char *tittle, int xpos, int ypos, int width, int height, bool fullscreen)
{
    
    int flags = 0;
    if(fullscreen)
    {
        flags = SDL_WINDOW_FULLSCREEN;
    }
    
    if(SDL_Init(SDL_INIT_EVERYTHING) == 0)
    {
        std::cout << "subsystems initialized!...." << std::endl;
        
        window = SDL_CreateWindow(tittle, xpos, ypos, width, height, flags);
        if(window)
        {
            std::cout << "window created" << std::endl;
        }
        renderer  = SDL_CreateRenderer(window, -1,0);
        if(renderer)
        {
            
            SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
            std::cout << "renderer created" << std::endl;
        }
        isRunning = true;
        
    } 
    else 
    {
        
        isRunning = false;
        
        
    }
      
    
}

void Game::handleEvents()
{
    
    SDL_Event event;
    SDL_PollEvent(&event);
    switch (event.type) 
    {
        
        case SDL_QUIT:
                    isRunning = false;
                    break;
        default:
                    break;
                    
    }
   
}

void Game::update()
{}

void Game::render()
{
    
    SDL_RenderClear(renderer);
    SDL_RenderPresent(renderer);
    
}

void Game::clean()
{
    
    SDL_DestroyWindow(window);
    SDL_DestroyRenderer(renderer);
    SDL_Quit();
    std::cout << "Game cleaned" << std::endl;
}