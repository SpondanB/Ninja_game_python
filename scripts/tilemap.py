class Tilemap:
    def __init__(self, game, tile_size = 16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tile = []
        
        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'varient': 1, 'pos': ((3 + i), 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'varient': 1, 'pos': (10, (5 + i))} 

    def render(self, surf):
        for tile in self.offgrid_tile:
            surf.blit(self.game.assets[tile['type']][tile['varient']], tile['pos'])
        
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(self.game.assets[tile['type']][tile['varient']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))