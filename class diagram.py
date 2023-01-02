+----------------+       +------------+
|  Game          |-------|  Room      |
+----------------+       +------------+
| - player: Player|       | - name: str   |
| - current_room: Room |  | - image: str  |
+----------------+       | - north: Room |
| + go_north()      |   | - south: Room |
| + go_south()      |   | - east: Room  |
| + go_east()       |   | - west: Room  |
| + go_west()       |   +------------+
| + update_display(): void  |
+----------------+

+----------------+
|  Player        |
+----------------+
| - inventory: List[str]|
| - current_room: Room |
+----------------+